import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { hash, inferRelationships, summarize } from './ax.mjs';
export { parseAX, summarize, makeCapture, inferRelationships } from './ax.mjs';

const PROJECT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const CYCLE = /^\d{4}\.\d{2}\.\d{2}-\d{4}\.\d{2}\.\d{2}$/;
const json = value => JSON.stringify(value, null, 2) + '\n';
const sorted = values => [...values].sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
const firstLine = text => text.split('\n')[0];
const exists = async file => fs.access(file).then(() => true, e => { if (e.code === 'ENOENT') return false; throw e; });

async function rootPath(root) {
  const result = path.resolve(root);
  if (result !== PROJECT && !result.startsWith(PROJECT + path.sep)) throw new Error('根目录必须位于本项目内。');
  if (await fs.realpath(result) !== result) throw new Error('根目录不能经由符号链接。');
  await fs.access(path.join(result, 'AGENTS.md'));
  return result;
}

async function safePath(root, relative) {
  if (typeof relative !== 'string' || path.isAbsolute(relative) || relative.includes('\\') || relative.split('/').some(p => !p || p === '.' || p === '..')) throw new Error(`不安全路径：${relative}`);
  let current = root;
  for (const part of relative.split('/')) {
    current = path.join(current, part);
    try { if ((await fs.lstat(current)).isSymbolicLink()) throw new Error(`拒绝符号链接：${relative}`); }
    catch (e) { if (e.code !== 'ENOENT') throw e; }
  }
  return current;
}

function validScope(scope) {
  if (scope === '长期-Vision' || scope === '12-Week-Year-方法论') return true;
  if (!CYCLE.test(scope)) return false;
  return scope.split('-').every(s => {
    const iso = s.replaceAll('.', '-');
    const date = new Date(iso + 'T00:00:00Z');
    return !Number.isNaN(date.valueOf()) && date.toISOString().slice(0, 10) === iso;
  }) && scope.slice(0, 10) <= scope.slice(11);
}

function validateSnapshot(snapshot) {
  if (!validScope(snapshot.scope) || !Array.isArray(snapshot.nodes) || !Array.isArray(snapshot.tables || [])) throw new Error('快照 scope 或正文结构无效。');
  const ids = new Set();
  for (const item of [...snapshot.nodes, ...(snapshot.tables || [])]) {
    if (!/^[a-z0-9][a-z0-9-]*$/.test(item.id) || ids.has(item.id)) throw new Error('节点/表格 ID 无效或重复。');
    ids.add(item.id);
    if ('text' in item) {
      if (typeof item.text !== 'string' || !item.text.trim()) throw new Error('正文节点为空。');
      const goalDate = firstLine(item.text).match(/^12 Week Goal.*?(\d{4}\.\d{2}\.\d{2}-\d{4}\.\d{2}\.\d{2})/i);
      if (goalDate && goalDate[1] !== snapshot.scope) throw new Error('Goal 中的周期与保存目录不一致。');
    } else {
      if (!Array.isArray(item.rows) || !item.rows.length || !item.rows[0].length || item.rows.some(row => !Array.isArray(row) || row.length !== item.rows[0].length || row.some(v => typeof v !== 'string'))) throw new Error('表格不是完整的字符串矩阵。');
    }
    const document = snapshot.documents?.[item.id];
    if (typeof document !== 'string' || !document.startsWith(snapshot.scope + '/') || !document.endsWith('.md') || /\/(source|history)\//.test(document)) throw new Error(`正文目标文件无效：${item.id}`);
  }
  if (!ids.size) throw new Error('拒绝空快照。');
  for (const relation of snapshot.relationships || []) {
    if (typeof relation.from !== 'string' || typeof relation.to !== 'string' || !relation.verification) throw new Error('连接关系缺少端点或证据类型。');
  }
}

function semantic(snapshot) {
  return {
    scope: snapshot.scope, source: { app: snapshot.source.app, board: snapshot.source.board, branch: snapshot.source.branch },
    nodes: sorted(snapshot.nodes.map(({ id, text }) => ({ id, text }))),
    tables: sorted((snapshot.tables || []).map(({ id, rows }) => ({ id, rows }))),
    relationships: sorted((snapshot.relationships || []).map(r => ({ from: r.from, to: r.to, verification: r.verification.includes('visual') ? 'visual' : 'ax' }))),
  };
}

function withDocuments(snapshot, manifest) {
  return { ...snapshot, documents: Object.fromEntries([
    ...snapshot.nodes.map(n => [n.id, snapshot.documents?.[n.id] || manifest.node_to_markdown?.[n.id]]),
    ...(snapshot.tables || []).map(t => [t.id, snapshot.documents?.[t.id] || `${snapshot.scope}/Scorecard.md`]),
  ]) };
}

async function loadState(root) {
  const manifestPath = await safePath(root, 'sync.json');
  const raw = await exists(manifestPath) ? await fs.readFile(manifestPath, 'utf8') : null;
  const manifest = raw ? JSON.parse(raw) : { files: [], snapshots: [] };
  const expected = new Map((manifest.files || []).map(f => [f.path, f.sha256]));
  for (const s of manifest.snapshots || []) expected.set(s.path, s.sha256);
  return { manifest, raw, expected };
}

async function managedPaths(root, manifest) {
  const owned = new Set();
  for (const entry of manifest.snapshots || []) {
    const snapshot = withDocuments(JSON.parse(await fs.readFile(await safePath(root, entry.path), 'utf8')), manifest);
    owned.add(entry.path);
    for (const rel of Object.values(snapshot.documents)) owned.add(rel);
  }
  return owned;
}

export async function proposeRoutes(root, inventory, { cycle } = {}) {
  root = await rootPath(root);
  const { manifest } = await loadState(root);
  const paths = (manifest.snapshots || []).map(s => s.path);
  const cycles = paths.map(p => p.split('/')[0]).filter(s => CYCLE.test(s));
  if (!cycle && cycles.length > 1) throw new Error('存在多个周期，请明确指定本次 cycle。');
  cycle ||= cycles[0];
  const routes = [], unmatched = [], changed = [], used = new Set();
  for (const rel of paths) {
    const scope = rel.split('/')[0];
    if (CYCLE.test(scope) && scope !== cycle) continue;
    const snapshot = withDocuments(JSON.parse(await fs.readFile(await safePath(root, rel), 'utf8')), manifest);
    for (const item of [...snapshot.nodes, ...(snapshot.tables || [])]) {
      const kind = 'text' in item ? 'node' : 'table';
      const candidates = kind === 'node' ? inventory.nodes : inventory.tables;
      const exact = candidates.filter(n => kind === 'node' ? n.text === item.text : JSON.stringify(n.rows) === JSON.stringify(item.rows));
      const named = candidates.filter(n => kind === 'node' ? firstLine(n.text) === firstLine(item.text) : n.rows[0][0] === item.rows[0][0]);
      const matches = exact.length ? exact : named;
      if (matches.length !== 1 || used.has(matches[0].key)) {
        unmatched.push({ scope, id: item.id, title: kind === 'node' ? firstLine(item.text) : item.rows[0][0], reason: matches.length > 1 ? 'duplicate-title-or-content' : 'missing-or-renamed' });
      } else {
        used.add(matches[0].key);
        routes.push({ key: matches[0].key, kind, scope, id: item.id, document: snapshot.documents[item.id] });
        if (!exact.length) changed.push({ key: matches[0].key, kind, scope, id: item.id });
      }
    }
  }
  const roots = inventory.nodes.filter(n => n.text.trim().toLowerCase() === '12 week year');
  const anchors = roots.length === 1 ? [{ key: roots[0].key, id: '12-week-year' }] : [];
  for (const a of anchors) used.add(a.key);
  return { routes, anchors, changed, unmatched_existing: unmatched, unassigned: [...summarize(inventory).nodes, ...summarize(inventory).tables].filter(n => !used.has(n.key)), ...inferRelationships(inventory, routes, anchors) };
}

const escapeText = text => text.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
const cellText = text => escapeText(text).replaceAll('\\', '&#92;').replaceAll('|', '&#124;').replaceAll('\n', '<br>').replace(/^ +| +$/g, spaces => '&#32;'.repeat(spaces.length));
const headings = new Set(['Lead Indicators', 'Lag Indicators', 'External', 'Internal', 'Commitment', 'physically', 'spiritually', 'mentally', 'relationally', 'financially', 'professionally', 'personally']);

export function renderDocument(snapshot, document) {
  const link = path.posix.relative(path.posix.dirname(document), `${snapshot.scope}/source/current.json`);
  const out = [`# ${escapeText(path.posix.basename(document, '.md'))}`, '', `> 无边记「${escapeText(snapshot.source.board)}」的单向镜像；措辞、编号、日期、✅ 和空值以来源为准。`, `> [原文与连接关系](${link})`, ''];
  for (const node of snapshot.nodes.filter(n => snapshot.documents[n.id] === document)) {
    const lines = node.text.split('\n');
    out.push(`## ${escapeText(lines[0])}`, '');
    for (const line of lines.slice(1)) {
      if (!line.trim()) out.push('');
      else if (headings.has(line)) out.push('', `### ${line}`, '');
      else out.push('- ' + escapeText(line).replace(/([\\`*_\[\]])/g, '\\$1').trimEnd());
    }
    out.push('');
  }
  for (const table of (snapshot.tables || []).filter(t => snapshot.documents[t.id] === document)) {
    out.push(`## ${escapeText(table.rows[0][0])}`, '', '| ' + table.rows[0].map(cellText).join(' | ') + ' |', '| ' + table.rows[0].map(() => '---').join(' | ') + ' |', ...table.rows.slice(1).map(row => '| ' + row.map(cellText).join(' | ') + ' |'), '');
  }
  const localNodes = snapshot.nodes.filter(n => snapshot.documents[n.id] === document);
  const edges = (snapshot.relationships || []).filter(e => localNodes.some(n => n.id === e.from || n.id === e.to));
  if (edges.length) {
    const label = id => firstLine(snapshot.nodes.find(n => n.id === id)?.text || id);
    out.push('## 画板连接关系', '', '以下仅记录连线；视觉核对不等于已确认软件内部连接锚点。', '');
    for (const edge of edges) out.push(`- ${escapeText(label(edge.from))} → ${escapeText(label(edge.to))}（${edge.verification.includes('visual') ? '视觉核对' : '辅助功能端点'}）`);
    out.push('');
  }
  return out.join('\n').replace(/\n{3,}/g, '\n\n').trimEnd() + '\n';
}

export function verifyRendered(snapshot, document, markdown) {
  const decode = text => text.replaceAll('<br>', '\n').replaceAll('&#124;', '|').replaceAll('&#92;', '\\').replaceAll('&#32;', ' ').replaceAll('&lt;', '<').replaceAll('&gt;', '>').replaceAll('&amp;', '&');
  const lines = markdown.split('\n').map(line => decode(line.replace(/^(?:#{1,6} |[-] )/, '').replace(/\\([\\`*_\[\]])/g, '$1')).trimEnd());
  for (const node of snapshot.nodes.filter(n => snapshot.documents[n.id] === document)) {
    for (const line of node.text.split('\n').filter(l => l.trim())) {
      if (!lines.includes(line.trimEnd())) throw new Error(`生成文档漏失或改写原文：${node.id}`);
    }
  }
  const actual = [];
  let current = [], skippedSeparator = false;
  for (const line of [...markdown.split('\n'), '']) {
    if (line.startsWith('| ')) {
      const cells = line.split('|').slice(1, -1).map(value => decode(value.trim()));
      if (current.length === 1 && !skippedSeparator) {
        if (!cells.every(value => value === '---')) throw new Error('Markdown 表格缺少表头分隔行。');
        skippedSeparator = true;
      } else current.push(cells);
    } else if (current.length) { actual.push(current); current = []; skippedSeparator = false; }
  }
  const expected = (snapshot.tables || []).filter(t => snapshot.documents[t.id] === document).map(t => t.rows);
  if (JSON.stringify(actual) !== JSON.stringify(expected)) throw new Error(`生成表格与原始单元格不一致：${document}`);
}

function validateCapture(capture, apply) {
  if (capture.schema_version !== 1 || !Array.isArray(capture.snapshots) || !capture.snapshots.length || capture.review?.complete !== true || capture.review?.visual_checked !== true || capture.review?.full_state_reads < 2 || !capture.review?.inventory_fingerprint || !capture.review?.evidence?.trim()) throw new Error('输入不是经过范围、稳定性和视觉核对的捕获包。');
  const age = Date.now() - Date.parse(capture.captured_at);
  if (!Number.isFinite(age) || (apply && (age > 30 * 60 * 1000 || age < -60000))) throw new Error('捕获包已过期或时间无效；重新读取源画板再 apply。');
  const scopes = new Set();
  for (const snapshot of capture.snapshots) {
    validateSnapshot(snapshot);
    if (snapshot.source?.app !== 'com.apple.freeform' || snapshot.source?.board !== capture.board || snapshot.source?.branch !== '12 week year') throw new Error('来源身份不匹配。');
    if (scopes.has(snapshot.scope)) throw new Error('重复 scope。');
    scopes.add(snapshot.scope);
  }
  if ([...scopes].filter(s => CYCLE.test(s)).length > 1) throw new Error('一次同步只处理一个周期；长期 Vision 可同时处理。');
}

export async function planSync(root, capture, { apply = false } = {}) {
  root = await rootPath(root);
  validateCapture(capture, apply);
  const state = await loadState(root);
  const writes = new Map(), expectedBytes = new Map([['sync.json', state.raw]]), changes = [];
  for (const snapshot of capture.snapshots) {
    const sourcePath = `${snapshot.scope}/source/current.json`;
    const absolute = await safePath(root, sourcePath);
    const before = await exists(absolute) ? await fs.readFile(absolute, 'utf8') : null;
    const previous = before ? withDocuments(JSON.parse(before), state.manifest) : null;
    if (previous && (previous.source?.app !== snapshot.source.app || previous.source?.board !== snapshot.source.board || previous.source?.branch !== snapshot.source.branch)) throw new Error('来源画板身份改变；需要明确迁移，不能自动重新绑定。');
    const owned = new Set([sourcePath, ...Object.values(snapshot.documents), ...Object.values(previous?.documents || {})]);
    for (const rel of owned) {
      const file = await safePath(root, rel);
      const bytes = await exists(file) ? await fs.readFile(file, 'utf8') : null;
      expectedBytes.set(rel, bytes);
      const recordedHash = state.expected.get(rel);
      if ((bytes !== null && (!recordedHash || hash(bytes) !== recordedHash)) || (recordedHash && bytes === null)) throw new Error(`本地修改、缺失或未纳管文件冲突：${rel}`);
    }
    if (previous) {
      for (const old of [...previous.nodes, ...(previous.tables || [])]) {
        const next = [...snapshot.nodes, ...(snapshot.tables || [])].find(n => n.id === old.id);
        if (!next) throw new Error(`节点/表格消失：${old.id}；V1 不自动删除，先检查读取完整性。`);
        if (snapshot.documents[old.id] !== previous.documents[old.id]) throw new Error(`既有文件路由改变：${old.id}；文件迁移需单独处理。`);
        if (old.rows && (next.rows.length < old.rows.length || next.rows[0].length < old.rows[0].length)) throw new Error(`表格缩小：${old.id}；不能推定为真实删除。`);
      }
      for (const edge of previous.relationships || []) {
        if (!(snapshot.relationships || []).some(e => e.from === edge.from && e.to === edge.to)) throw new Error(`连接关系消失：${edge.from} → ${edge.to}；先核对画板。`);
      }
      if (JSON.stringify(semantic(previous)) === JSON.stringify(semantic(snapshot))) continue;
    }
    const changedIds = [...snapshot.nodes, ...(snapshot.tables || [])].filter(n => {
      const old = [...(previous?.nodes || []), ...(previous?.tables || [])].find(o => o.id === n.id);
      return !old || (n.text !== undefined ? n.text !== old.text : JSON.stringify(n.rows) !== JSON.stringify(old.rows));
    }).map(n => n.id);
    const oldEdges = semantic(previous || { ...snapshot, nodes: [], tables: [], relationships: [] }).relationships;
    const newEdges = semantic(snapshot).relationships;
    const topologyChanged = JSON.stringify(oldEdges) !== JSON.stringify(newEdges);
    const differentEdges = [...oldEdges.filter(e => !newEdges.some(n => JSON.stringify(n) === JSON.stringify(e))), ...newEdges.filter(e => !oldEdges.some(n => JSON.stringify(n) === JSON.stringify(e)))];
    const affected = [...changedIds, ...differentEdges.flatMap(e => [e.from, e.to])];
    const documents = new Set(affected.map(id => snapshot.documents[id]).filter(Boolean));
    for (const rel of documents) {
      const content = renderDocument(snapshot, rel);
      verifyRendered(snapshot, rel, content);
      if (content !== expectedBytes.get(rel)) writes.set(rel, content);
    }
    writes.set(sourcePath, json({ ...snapshot, snapshot_created_at: new Date().toISOString(), capture_review: capture.review }));
    changes.push({ scope: snapshot.scope, changed_ids: changedIds, relationships_changed: topologyChanged });
  }
  return { root, state, writes, expectedBytes, changes, status: writes.size ? 'changes' : 'no-op' };
}

async function currentBytes(root, rel) {
  const file = await safePath(root, rel);
  return await exists(file) ? fs.readFile(file, 'utf8') : null;
}

export async function sync(root, capture, { apply = false, beforeCommit } = {}) {
  const plan = await planSync(root, capture, { apply });
  const report = { status: plan.status, applied: false, changes: plan.changes, files: [...plan.writes.keys()] };
  if (!apply || !plan.writes.size) return report;
  root = plan.root;
  const writes = plan.writes;
  const now = new Date().toISOString();
  const owned = await managedPaths(root, plan.state.manifest);
  const manifestFiles = new Map((plan.state.manifest.files || []).filter(f => owned.has(f.path)).map(f => [f.path, f]));
  for (const [rel, content] of writes) manifestFiles.set(rel, { path: rel, sha256: hash(content), bytes: Buffer.byteLength(content) });
  const snapshots = new Map((plan.state.manifest.snapshots || []).map(s => [s.path, s]));
  for (const snapshot of capture.snapshots) {
    const rel = `${snapshot.scope}/source/current.json`;
    if (writes.has(rel)) snapshots.set(rel, { path: rel, sha256: hash(writes.get(rel)), content_sha256: hash(JSON.stringify(semantic(snapshot))) });
  }
  writes.set('sync.json', json({ schema_version: 2, synced_at: now, source: { app: 'com.apple.freeform', board: capture.board, branch: '12 week year' }, direction: 'Freeform -> local', automatic_sync: false, visual_pdf_exported: false, node_to_markdown: plan.state.manifest.node_to_markdown || {}, snapshots: [...snapshots.values()], files: [...manifestFiles.values()], latest_sync: { changes: plan.changes, capture_review: capture.review, scope: capture.snapshots.map(s => s.scope), text_nodes: capture.snapshots.reduce((n, s) => n + s.nodes.length, 0), table_cells: capture.snapshots.reduce((n, s) => n + (s.tables || []).reduce((m, t) => m + t.rows.length * t.rows[0].length, 0), 0) } }));
  const transaction = now.replaceAll(/[:.]/g, '-') + '-' + Math.random().toString(16).slice(2, 10);
  const base = `skill/freeform-12wy-sync/.work/transactions/${transaction}`;
  const staging = await safePath(root, base);
  const lock = await safePath(root, '.freeform-sync-lock');
  await fs.mkdir(lock); // Exclusive; an existing lock requires investigation, never force removal.
  const committed = [];
  let keepStaging = false;
  try {
    await fs.mkdir(staging, { recursive: true });
    for (const [rel, expected] of plan.expectedBytes) if (await currentBytes(root, rel) !== expected) throw new Error(`计划后文件发生变化：${rel}`);
    let i = 0;
    for (const [rel, content] of writes) {
      await fs.writeFile(path.join(staging, `${i++}.new`), content, { flag: 'wx' });
      const old = plan.expectedBytes.get(rel) ?? null;
      if (old !== null) {
        const scope = rel.split('/')[0];
        const archiveRel = rel === 'sync.json' ? `skill/freeform-12wy-sync/.work/history/${transaction}/sync.json` : `${scope}/source/history/${transaction}/${rel.slice(scope.length + 1)}`;
        const archive = await safePath(root, archiveRel);
        await fs.mkdir(path.dirname(archive), { recursive: true });
        await fs.writeFile(archive, old, { flag: 'wx' });
      }
    }
    await fs.writeFile(path.join(staging, 'transaction.json'), json({ status: 'prepared', files: [...writes.keys()], transaction }));
    i = 0;
    for (const [rel, content] of writes) {
      if (beforeCommit) await beforeCommit(i, rel);
      if (await currentBytes(root, rel) !== (plan.expectedBytes.get(rel) ?? null)) throw new Error(`提交前文件发生变化：${rel}`);
      const file = await safePath(root, rel);
      await fs.mkdir(path.dirname(file), { recursive: true });
      await fs.rename(path.join(staging, `${i++}.new`), file);
      committed.push(rel);
      if (await fs.readFile(file, 'utf8') !== content) throw new Error(`写后校验失败：${rel}`);
    }
  } catch (error) {
    for (const rel of committed.reverse()) {
      try {
        if (await currentBytes(root, rel) !== writes.get(rel)) { keepStaging = true; continue; }
        const before = plan.expectedBytes.get(rel);
        const file = await safePath(root, rel);
        if (before === null || before === undefined) await fs.unlink(file);
        else await fs.writeFile(file, before);
      } catch { keepStaging = true; }
    }
    if (keepStaging) throw new Error(`回滚遇到并发修改，保留事务目录 ${base}；${error.message}`);
    throw error;
  } finally {
    if (!keepStaging) {
      await fs.rm(staging, { recursive: true, force: true });
      await fs.rmdir(lock);
    }
  }
  return { ...report, status: 'updated', applied: true, files: [...writes.keys()], transaction };
}

export async function saveCapture(root, name, capture) {
  root = await rootPath(root);
  validateCapture(capture, false);
  if (!/^[a-zA-Z0-9-]+$/.test(name)) throw new Error('捕获名称只能包含字母、数字和连字符。');
  const descriptor = `skill/freeform-12wy-sync/.work/captures/${name}.json`;
  const files = capture.snapshots.map(snapshot => ({ path: `${snapshot.scope}/source/incoming-${name}.json`, content: json(snapshot) }));
  // Preflight every path before writing; Vision payloads never enter a cycle directory.
  for (const rel of [descriptor, ...files.map(f => f.path)]) if (await exists(await safePath(root, rel))) throw new Error(`捕获文件已存在：${rel}`);
  for (const file of files) {
    const dest = await safePath(root, file.path);
    await fs.mkdir(path.dirname(dest), { recursive: true });
    await fs.writeFile(dest, file.content, { flag: 'wx' });
  }
  const { snapshots, ...metadata } = capture;
  const dest = await safePath(root, descriptor);
  await fs.mkdir(path.dirname(dest), { recursive: true });
  await fs.writeFile(dest, json({ ...metadata, snapshot_files: files.map(f => ({ path: f.path, sha256: hash(f.content) })) }), { flag: 'wx' });
  return descriptor;
}

export async function readCapture(root, relative) {
  root = await rootPath(root);
  const descriptor = JSON.parse(await fs.readFile(await safePath(root, relative), 'utf8'));
  if (!Array.isArray(descriptor.snapshot_files) || !descriptor.snapshot_files.length) throw new Error('需要 saveCapture 生成的分目录捕获清单。');
  const snapshots = [];
  for (const entry of descriptor.snapshot_files) {
    const bytes = await fs.readFile(await safePath(root, entry.path), 'utf8');
    if (hash(bytes) !== entry.sha256) throw new Error(`捕获快照被修改：${entry.path}`);
    const snapshot = JSON.parse(bytes);
    if (!entry.path.startsWith(snapshot.scope + '/source/incoming-')) throw new Error('捕获快照存放位置与 scope 不匹配。');
    snapshots.push(snapshot);
  }
  return { ...descriptor, snapshots };
}

export async function verifyExisting(root) {
  root = await rootPath(root);
  const state = await loadState(root);
  let files = 0, nodes = 0, cells = 0;
  for (const entry of state.manifest.snapshots || []) {
    const snapshot = withDocuments(JSON.parse(await fs.readFile(await safePath(root, entry.path), 'utf8')), state.manifest);
    validateSnapshot(snapshot);
    for (const rel of new Set([entry.path, ...Object.values(snapshot.documents)])) {
      const bytes = await currentBytes(root, rel);
      if (bytes === null || !state.expected.get(rel) || hash(bytes) !== state.expected.get(rel)) throw new Error(`镜像文件不符合清单：${rel}`);
      files++;
    }
    nodes += snapshot.nodes.length;
    cells += (snapshot.tables || []).reduce((sum, t) => sum + t.rows.length * t.rows[0].length, 0);
  }
  if (!files) throw new Error('没有可验证的已有镜像。');
  return { status: 'verified-existing', files, nodes, cells, source_completeness_verified: false };
}

if (typeof process !== 'undefined' && process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url) {
  try {
    const [command, ...args] = process.argv.slice(2);
    const flags = {};
    for (let i = 0; i < args.length; i += 2) {
      if (!['--root', '--input'].includes(args[i]) || !args[i + 1] || flags[args[i]]) throw new Error('仅支持 --root 路径 和 --input 捕获文件。');
      flags[args[i]] = args[i + 1];
    }
    const root = flags['--root'] || process.cwd();
    if (command === 'verify-existing') console.log(json(await verifyExisting(root)));
    else if (['plan', 'apply'].includes(command) && flags['--input']) {
      const input = path.resolve(flags['--input']);
      const allowed = await rootPath(root);
      if (!input.startsWith(allowed + path.sep)) throw new Error('输入捕获包也必须在本项目目录内。');
      await safePath(allowed, path.relative(allowed, input));
      const capture = await readCapture(allowed, path.relative(allowed, input));
      console.log(json(await sync(root, capture, { apply: command === 'apply' })));
    } else throw new Error('用法：node sync.mjs verify-existing|plan|apply --root 项目目录 [--input 捕获文件]');
  } catch (error) { console.error(json({ status: 'blocked', error: error.message })); process.exitCode = 1; }
}
