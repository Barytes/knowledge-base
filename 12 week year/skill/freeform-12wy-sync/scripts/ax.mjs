// Pure transformations only. UI operations belong to computer-use in node_repl.
import { createHash } from 'node:crypto';

export const hash = value => createHash('sha256').update(value).digest('hex');
const flat = text => text.replace(/\s+/g, ' ').trim();
const title = text => text.split('\n')[0];

function field(record, name, suffixes = []) {
  const marker = `${name}: `;
  const pos = record.body.indexOf(marker);
  if (pos < 0) return null;
  let value = record.body.slice(pos + marker.length);
  for (const suffix of suffixes) {
    const end = value.lastIndexOf(suffix);
    if (end >= 0) value = value.slice(0, end);
  }
  return value.replace(/\n+$/, '');
}

export function parseAX(text) {
  const window = text.match(/^Window: "([^"]+)", App: (.+)\.$/m);
  if (!window || /^(Added|Removed|Changed|新增|移除):/m.test(text)) {
    throw new Error('需要 disableDiff:true 的完整画板状态，不能解析界面差量。');
  }
  const records = [];
  for (const line of text.split('\n')) {
    const m = line.match(/^(\t+)(\d+) (.+)$/);
    if (m) records.push({ depth: m[1].length, index: Number(m[2]), body: m[3] });
    else if (records.length && !line.startsWith('The focused UI element')) {
      records.at(-1).body += '\n' + line;
    }
  }
  const layouts = records.filter(r => r.body.startsWith('布局项目'));
  if (!layouts.length) throw new Error('没有画板项目；可能仍在菜单、导出窗口或读取失败。');
  const depth = Math.min(...layouts.map(r => r.depth));
  const nodes = [], tables = [], connectors = [];
  for (let i = 0; i < records.length; i++) {
    const parent = records[i];
    if (parent.depth !== depth || !parent.body.startsWith('布局项目')) continue;
    const children = [];
    for (let j = i + 1; j < records.length && records[j].depth > depth; j++) children.push(records[j]);
    const description = field(parent, 'Description', [', Secondary Actions:']);
    if (description?.startsWith('连接线,')) {
      connectors.push({ key: `edge-${parent.index}`, ax_index: parent.index, description });
    } else if (description === '表格') {
      const cells = children.filter(r => r.body.startsWith('单元格')).map(r => {
        const m = r.body.match(/Description: 第(\d+)行，第(\d+)列/);
        if (!m) throw new Error('无法识别表格行列。');
        const next = children[children.indexOf(r) + 1];
        const child = next?.depth === r.depth + 1 && next.body.startsWith('文本输入区') ? next : null;
        const value = child ? field(child, 'Value', [', Secondary Actions:']) : field(r, 'Value', [', Secondary Actions:', ', ID: row']);
        if (value === null) throw new Error('表格单元格缺少 Value。');
        return { r: Number(m[1]), c: Number(m[2]), value: !child && value === '空单元格' ? '' : value };
      });
      if (!cells.length) throw new Error('表格没有可读取单元格。');
      const height = Math.max(...cells.map(c => c.r)), width = Math.max(...cells.map(c => c.c));
      if (height * width > 100000) throw new Error('表格尺寸异常。');
      const rows = Array.from({ length: height }, () => Array(width));
      for (const cell of cells) {
        if (rows[cell.r - 1][cell.c - 1] !== undefined) throw new Error('表格出现重复坐标。');
        rows[cell.r - 1][cell.c - 1] = cell.value;
      }
      if (cells.length !== height * width) throw new Error('表格存在未读取的单元格，不能用空值补齐。');
      tables.push({ key: `table-${parent.index}`, ax_index: parent.index, rows });
    } else {
      const input = children.find(r => r.body.startsWith('文本输入区') && r.depth === depth + 1);
      if (!input) throw new Error(`项目 ${parent.index} 不是已支持的文本、连接线或表格；先人工检查。`);
      const value = field(input, 'Value', [', Secondary Actions:']);
      if (value === null) throw new Error('文本节点缺少 Value。');
      nodes.push({ key: `node-${parent.index}`, ax_index: input.index, text: value });
    }
  }
  const inventory = { board: window[1], nodes, tables, connectors };
  inventory.fingerprint = hash(JSON.stringify({
    board: inventory.board,
    nodes: nodes.map(n => n.text).sort(),
    tables: tables.map(t => JSON.stringify(t.rows)).sort(),
    connectors: connectors.map(c => c.description).sort(),
  }));
  return inventory;
}

export function summarize(inventory) {
  return {
    board: inventory.board, fingerprint: inventory.fingerprint,
    nodes: inventory.nodes.map(n => ({ key: n.key, title: title(n.text), lines: n.text.split('\n').length })),
    tables: inventory.tables.map(t => ({ key: t.key, title: t.rows[0][0], rows: t.rows.length, columns: t.rows[0].length })),
    connectors: inventory.connectors.length,
  };
}

export function inferRelationships(inventory, routes, anchors = []) {
  const refs = [...routes.filter(r => r.kind === 'node'), ...anchors].map(r => {
    const node = inventory.nodes.find(n => n.key === r.key);
    if (!node) throw new Error(`找不到当前节点 ${r.key}`);
    return { ...r, text: node.text };
  });
  const pick = fragment => {
    if (!fragment) return null;
    const value = flat(fragment);
    const exact = refs.filter(r => value.startsWith(flat(r.text)));
    if (exact.length === 1) return exact[0].id;
    const byTitle = refs.filter(r => value.startsWith(flat(title(r.text))));
    return byTitle.length === 1 ? byTitle[0].id : null;
  };
  const relationships = [], unresolved = [];
  for (const connector of inventory.connectors) {
    const desc = connector.description.replace(/^连接线, /, '');
    const parts = desc.startsWith('从') ? desc.slice(1).split('连接至') : [];
    const from = pick(parts[0]);
    const to = pick(parts[1] || (desc.startsWith('连接') ? desc.slice(2) : ''));
    const touchesBody = routes.some(r => r.kind === 'node' && (r.id === from || r.id === to));
    if (from && to && touchesBody) relationships.push({ key: connector.key, from, to, verification: 'accessibility-connector' });
    else if (touchesBody) unresolved.push({ key: connector.key, from, to, description: connector.description });
  }
  return { relationships, unresolved };
}

export function makeCapture(first, latest, routes, review) {
  if (first.fingerprint !== latest.fingerprint) throw new Error('两次完整读取不一致；重新读取并核对，不能覆盖。');
  if (review?.complete !== true || review?.visual_checked !== true || !review?.evidence?.trim()) {
    throw new Error('必须记录人工/模型的画板范围与视觉核对，不能把稳定读取当成完整性证明。');
  }
  const anchors = review.anchors || [];
  const excluded = review.excluded || [];
  if (excluded.some(e => !e.reason?.trim())) throw new Error('排除节点必须给出原因。');
  const actualKeys = [...latest.nodes, ...latest.tables].map(n => n.key);
  const accounted = [...routes, ...anchors, ...excluded].map(n => n.key);
  if (new Set(accounted).size !== accounted.length || accounted.length !== actualKeys.length || actualKeys.some(k => !accounted.includes(k))) {
    throw new Error('每个当前文本/表格必须且只能归类为同步、锚点或有理由排除；禁止静默遗漏。');
  }
  if (new Set([...routes, ...anchors].map(r => r.id)).size !== routes.length + anchors.length) throw new Error('本次路由 ID 必须唯一。');
  const inferred = inferRelationships(latest, routes, anchors);
  const manual = review.relationships || [];
  const skipped = review.excluded_connectors || [];
  if (manual.some(e => !e.evidence?.trim()) || skipped.some(e => !e.reason?.trim())) throw new Error('手动关系和排除连接线必须有核对证据。');
  for (const edge of inferred.unresolved) {
    if (!manual.some(e => e.key === edge.key) && !skipped.some(e => e.key === edge.key)) throw new Error(`连接线 ${edge.key} 的端点未确认。`);
  }
  const relationships = [...inferred.relationships.filter(e => !manual.some(m => m.key === e.key) && !skipped.some(m => m.key === e.key)), ...manual];
  const snapshots = [];
  for (const scope of [...new Set(routes.map(r => r.scope))]) {
    const scoped = routes.filter(r => r.scope === scope);
    const nodes = scoped.filter(r => r.kind === 'node').map(r => ({ id: r.id, text: latest.nodes.find(n => n.key === r.key).text }));
    const tables = scoped.filter(r => r.kind === 'table').map(r => ({ id: r.id, rows: latest.tables.find(t => t.key === r.key).rows }));
    const edges = relationships.filter(e => scoped.some(r => r.id === e.to) || (!routes.some(r => r.id === e.to) && scoped.some(r => r.id === e.from))).map(e => {
      const connector = latest.connectors.find(c => c.key === e.key);
      if (!connector || ![...routes, ...anchors].some(r => r.id === e.from) || ![...routes, ...anchors].some(r => r.id === e.to)) throw new Error('关系引用了不存在的节点或连接线。');
      return { from: e.from, to: e.to, verification: e.verification || 'visual-connector', ...(e.evidence ? { evidence: e.evidence } : {}), source_description: connector.description };
    });
    snapshots.push({ schema_version: 1, scope, source: { app: 'com.apple.freeform', board: latest.board, branch: '12 week year' }, nodes, tables, relationships: edges, documents: Object.fromEntries(scoped.map(r => [r.id, r.document])) });
  }
  return { schema_version: 1, board: latest.board, captured_at: new Date().toISOString(), review: { ...review, inventory_fingerprint: latest.fingerprint, full_state_reads: 2 }, snapshots };
}
