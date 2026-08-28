import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseAX, makeCapture, summarize, inferRelationships, hash } from '../scripts/ax.mjs';
import { proposeRoutes, sync, renderDocument, verifyRendered, saveCapture, readCapture, verifyExisting } from '../scripts/sync.mjs';

const project = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const work = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../.work/tests');
const cycle = '2026.09.01-2026.11.30';
const copy = value => structuredClone(value);
const json = value => JSON.stringify(value, null, 2) + '\n';

function fixture({ offset = 0, extraNode = false, missingCell = false } = {}) {
  let index = offset + 4;
  const lines = ['Window: "效率提升", App: 无边记.', '\t1 分离组', '\t\t2 滚动区', '\t\t\t3 布局区域'];
  function node(value) {
    lines.push(`\t\t\t\t${index++} 布局项目 (selectable) Description: ${value}, 文本框, Secondary Actions: 编辑文本`);
    index += 3; // IDs need not be consecutive.
    lines.push(`\t\t\t\t\t${index++} 文本输入区 (settable) Value: ${value}, Secondary Actions: 显示格式选项`);
  }
  node('12 week year');
  node('我的15年aspiration\nphysically\n睡够睡饱\n2 保留数字开头的原文\n一行包含 Value: 字样');
  node(`12 Week Goal (${cycle})\n一个结果✅\nCommitment\n保护时间`);
  node('Goal 1: 项目目标\nTactic 1: 阅读\nLead Indicators\n作品数量');
  node('无关分支');
  if (extraNode) node('新出现的待分类节点');
  lines.push(`\t\t\t\t${index++} 布局项目 (selectable) Secondary Actions: 显示格式选项, Description: 连接线, 从12 week year, 文本框的中间连接至我的15年aspiration physically 睡够睡饱的顶部, 曲线`);
  lines.push(`\t\t\t\t${index++} 布局项目 (selectable) Description: 连接线, 从我的15年aspiration physically 睡够睡饱的中间连接至12 Week Goal (${cycle}) 一个结果✅的顶部, 曲线, Secondary Actions: 显示格式选项`);
  lines.push(`\t\t\t\t${index++} 布局项目 (selectable) Description: 连接线, 从12 Week Goal (${cycle}) 一个结果✅的中间连接至Goal 1: 项目目标 Tactic 1: 阅读的左侧, 曲线, Secondary Actions: 显示格式选项`);
  lines.push(`\t\t\t\t${index++} 布局项目 (selectable) Description: 表格, Secondary Actions: 显示格式选项`);
  const rows = [['Goal 1 指标', 'W1', 'W2'], ['本周到期 Tactics 数', '2', ''], ['文本测试', '空单元格', 'a|b\\c\n下一行<&>']];
  rows.forEach((row, r) => row.forEach((value, c) => {
    if (missingCell && r === 1 && c === 1) return;
    lines.push(`\t\t\t\t\t${index++} 单元格 Description: 第${r + 1}行，第${c + 1}列, Help: 选择, Value: ${value || '空单元格'}, ID: row ${r + 1}, column ${c + 1}, Secondary Actions: 显示格式选项`);
    if (value) { index += 3; lines.push(`\t\t\t\t\t\t${index++} 文本输入区 Value: ${value}, Secondary Actions: 显示格式选项`); }
  }));
  return lines.join('\n');
}

function sampleCapture() {
  const inventory = parseAX(fixture());
  const routes = [
    { key: inventory.nodes[1].key, kind: 'node', scope: '长期-Vision', id: 'vision', document: '长期-Vision/愿景.md' },
    { key: inventory.nodes[2].key, kind: 'node', scope: cycle, id: 'goals', document: `${cycle}/Goal.md` },
    { key: inventory.nodes[3].key, kind: 'node', scope: cycle, id: 'plan', document: `${cycle}/Plan.md` },
    { key: inventory.tables[0].key, kind: 'table', scope: cycle, id: 'score', document: `${cycle}/Scorecard.md` },
  ];
  const review = { complete: true, visual_checked: true, evidence: '合成测试夹具，非真实画板读取证明。', anchors: [{ key: inventory.nodes[0].key, id: '12-week-year' }], excluded: [{ key: inventory.nodes[4].key, reason: '测试用无关分支' }] };
  return { inventory, routes, review, capture: makeCapture(inventory, parseAX(fixture({ offset: 200 })), routes.map(r => ({ ...r, key: r.key.replace(/\d+$/, n => Number(n) + 200) })), { ...review, anchors: review.anchors.map(r => ({ ...r, key: r.key.replace(/\d+$/, n => Number(n) + 200) })), excluded: review.excluded.map(r => ({ ...r, key: r.key.replace(/\d+$/, n => Number(n) + 200) })) }) };
}

async function seed(t, { legacy = true } = {}) {
  await fs.mkdir(work, { recursive: true });
  const root = await fs.mkdtemp(path.join(work, 'case-'));
  t.after(() => fs.rm(root, { recursive: true, force: true }));
  await fs.writeFile(path.join(root, 'AGENTS.md'), '# 测试目录规则\n');
  await fs.writeFile(path.join(root, 'README.md'), '# 手工入口\n');
  const { capture } = sampleCapture();
  const files = [], snapshots = [], node_to_markdown = {};
  for (const input of capture.snapshots) {
    const snapshot = copy(input);
    Object.assign(node_to_markdown, Object.fromEntries(snapshot.nodes.map(n => [n.id, snapshot.documents[n.id]])));
    const contents = new Map(Object.values(snapshot.documents).map(rel => [rel, renderDocument(snapshot, rel)]));
    if (legacy) delete snapshot.documents;
    const rel = `${snapshot.scope}/source/current.json`;
    contents.set(rel, json(snapshot));
    for (const [name, content] of contents) {
      await fs.mkdir(path.dirname(path.join(root, name)), { recursive: true });
      await fs.writeFile(path.join(root, name), content);
      files.push({ path: name, sha256: hash(content) });
    }
    snapshots.push({ path: rel, sha256: hash(contents.get(rel)) });
  }
  files.push({ path: 'README.md', sha256: hash('# 手工入口\n') });
  await fs.writeFile(path.join(root, 'sync.json'), json({ schema_version: 1, files, snapshots, node_to_markdown }));
  return { root, capture };
}

async function fileState(root) {
  const result = {};
  async function walk(dir) {
    for (const e of await fs.readdir(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory()) await walk(p);
      else if (e.isFile()) result[path.relative(root, p)] = hash(await fs.readFile(p));
    }
  }
  await walk(root);
  return result;
}

test('AX preserves multiline text, numbered lines, literal empty-cell text, and table coordinates', () => {
  const inv = parseAX(fixture());
  assert.equal(inv.nodes.length, 5);
  assert.match(inv.nodes[1].text, /\n2 保留数字开头的原文\n一行包含 Value: 字样$/);
  assert.equal(inv.tables[0].rows[1][2], '');
  assert.equal(inv.tables[0].rows[2][1], '空单元格');
  assert.equal(inv.tables[0].rows[2][2], 'a|b\\c\n下一行<&>');
  assert.equal(inv.fingerprint, parseAX(fixture({ offset: 100 })).fingerprint);
  assert.equal(inferRelationships(inv, sampleCapture().routes, sampleCapture().review.anchors).relationships.length, 3);
  assert.ok(JSON.stringify(summarize(inv)).length < fixture().length / 2);
});

test('AX rejects incomplete cells, partial states, and unsupported shapes', () => {
  assert.throws(() => parseAX(fixture({ missingCell: true })), /未读取/);
  assert.throws(() => parseAX('No changes.'), /完整/);
  assert.throws(() => parseAX(fixture() + '\n\t\t\t\t999 布局项目 Description: 图片'), /不支持|已支持/);
});

test('capture requires fresh keys, explicit coverage and stable full reads', () => {
  const { inventory, routes, review } = sampleCapture();
  assert.throws(() => makeCapture(inventory, parseAX(fixture({ extraNode: true })), routes, review), /不一致/);
  assert.throws(() => makeCapture(inventory, inventory, routes, { ...review, complete: false }), /范围|视觉/);
  assert.throws(() => makeCapture(inventory, inventory, routes, { ...review, excluded: [] }), /遗漏/);
  assert.equal(makeCapture(inventory, inventory, routes, review).snapshots.length, 2);
});

test('unresolved connectors require explicit evidence rather than invented endpoints', () => {
  const text = fixture().replace('从我的15年aspiration physically 睡够睡饱的中间连接至', '连接');
  const inv = parseAX(text), { routes, review } = sampleCapture();
  const inferred = inferRelationships(inv, routes, review.anchors);
  assert.equal(inferred.unresolved.length, 1);
  assert.throws(() => makeCapture(inv, inv, routes, review), /端点未确认/);
  const capture = makeCapture(inv, inv, routes, { ...review, relationships: [{ key: inferred.unresolved[0].key, from: 'vision', to: 'goals', verification: 'visual-connector', evidence: '仅用于测试的视觉核对记录' }] });
  assert.equal(capture.snapshots[1].relationships.find(e => e.from === 'vision' && e.to === 'goals').verification, 'visual-connector');
});

test('legacy snapshot routes are reused without persistent AX IDs; duplicate titles block matching', async t => {
  const { root } = await seed(t);
  const proposal = await proposeRoutes(root, parseAX(fixture({ offset: 1000 })));
  assert.equal(proposal.routes.length, 4);
  assert.deepEqual(proposal.unmatched_existing, []);
  const inv = parseAX(fixture());
  inv.nodes.push({ ...inv.nodes[1], key: 'node-99999' });
  assert.equal((await proposeRoutes(root, inv)).unmatched_existing[0].reason, 'duplicate-title-or-content');
});

test('unchanged apply is a true no-op, including original JSON timestamps and file mtimes', async t => {
  const { root, capture } = await seed(t);
  const before = await fileState(root);
  const mtime = (await fs.stat(path.join(root, 'sync.json'))).mtimeMs;
  const report = await sync(root, capture, { apply: true });
  assert.equal(report.status, 'no-op');
  assert.equal(report.applied, false);
  assert.deepEqual(await fileState(root), before);
  assert.equal((await fs.stat(path.join(root, 'sync.json'))).mtimeMs, mtime);
});

test('single-node updates change only its document and snapshot, archive old versions, then become no-op', async t => {
  const { root, capture } = await seed(t);
  const planBefore = await fs.readFile(path.join(root, cycle, 'Plan.md'), 'utf8');
  const goalBefore = await fs.readFile(path.join(root, cycle, 'Goal.md'), 'utf8');
  capture.snapshots[1].nodes[0].text += '\n新增加的目标标准';
  const preview = await sync(root, capture);
  assert.equal(preview.applied, false);
  assert.ok(preview.files.includes(`${cycle}/Goal.md`));
  assert.ok(!preview.files.includes(`${cycle}/Plan.md`));
  const report = await sync(root, capture, { apply: true });
  assert.equal(report.status, 'updated');
  assert.equal(await fs.readFile(path.join(root, cycle, 'Plan.md'), 'utf8'), planBefore);
  assert.equal(await fs.readFile(path.join(root, cycle, 'source/history', report.transaction, 'Goal.md'), 'utf8'), goalBefore);
  assert.equal((await sync(root, capture, { apply: true })).status, 'no-op');
  assert.equal((await verifyExisting(root)).nodes, 3);
});

test('table updates preserve blank versus zero, escaped cells, and added rows', async t => {
  const { root, capture } = await seed(t);
  const table = capture.snapshots[1].tables[0];
  table.rows[1][2] = '0';
  table.rows.push(['新增行', '', '  首尾空格  ']);
  table.rows.push(['---', '---', '---']);
  await sync(root, capture, { apply: true });
  const saved = JSON.parse(await fs.readFile(path.join(root, cycle, 'source/current.json')));
  assert.equal(saved.tables[0].rows[1][2], '0');
  assert.equal(saved.tables[0].rows[3][1], '');
  const md = await fs.readFile(path.join(root, cycle, 'Scorecard.md'), 'utf8');
  assert.match(md, /a&#124;b&#92;c<br>下一行&lt;&amp;&gt;/);
});

test('independent render verification detects changed text and cells', () => {
  const snapshot = sampleCapture().capture.snapshots[1];
  const doc = `${cycle}/Goal.md`;
  const output = renderDocument(snapshot, doc);
  assert.doesNotThrow(() => verifyRendered(snapshot, doc, output));
  assert.throws(() => verifyRendered(snapshot, doc, output.replace('一个结果✅', '错误改写')), /原文/);
  const tableDoc = `${cycle}/Scorecard.md`;
  assert.throws(() => verifyRendered(snapshot, tableDoc, renderDocument(snapshot, tableDoc).replace('| 2 |', '| 3 |')), /单元格/);
});

test('new nodes are added without adopting unrelated local files', async t => {
  const { root, capture } = await seed(t);
  capture.snapshots[1].nodes.push({ id: 'new-item', text: '新节点\n新内容' });
  capture.snapshots[1].documents['new-item'] = `${cycle}/New.md`;
  capture.snapshots[1].relationships.push({ from: 'goals', to: 'new-item', verification: 'accessibility-connector' });
  await fs.writeFile(path.join(root, cycle, 'New.md'), '已有未纳管文件');
  await assert.rejects(() => sync(root, capture, { apply: true }), /冲突/);
  await fs.unlink(path.join(root, cycle, 'New.md'));
  const preview = await sync(root, capture);
  assert.ok(preview.files.includes(`${cycle}/Goal.md`));
  assert.ok(!preview.files.includes(`${cycle}/Scorecard.md`));
  assert.ok(!preview.files.includes(`${cycle}/Plan.md`));
  await sync(root, capture, { apply: true });
  assert.match(await fs.readFile(path.join(root, cycle, 'New.md'), 'utf8'), /新内容/);
});

test('a different source board cannot silently rebind an existing mirror', async t => {
  const { root, capture } = await seed(t);
  capture.board = '另一张画板';
  for (const snapshot of capture.snapshots) snapshot.source.board = capture.board;
  await assert.rejects(() => sync(root, capture, { apply: true }), /来源画板/);
});

for (const [name, mutate] of [
  ['missing node', c => c.snapshots[1].nodes.pop()],
  ['missing table', c => { c.snapshots[1].tables = []; }],
  ['shrinking table', c => c.snapshots[1].tables[0].rows.pop()],
  ['missing connection', c => c.snapshots[1].relationships.pop()],
  ['changed route', c => { c.snapshots[1].documents.goals = `${cycle}/Other.md`; }],
]) test(`${name} stops before any file changes`, async t => {
  const { root, capture } = await seed(t);
  const before = await fileState(root);
  mutate(capture);
  await assert.rejects(() => sync(root, capture, { apply: true }));
  assert.deepEqual(await fileState(root), before);
});

test('manual mirror changes block; project policy and navigation changes do not', async t => {
  const { root, capture } = await seed(t);
  await fs.appendFile(path.join(root, 'README.md'), '\n新增 skill 入口\n');
  await fs.appendFile(path.join(root, 'AGENTS.md'), '\n新增项目规则\n');
  assert.equal((await sync(root, capture, { apply: true })).status, 'no-op');
  const goal = path.join(root, cycle, 'Goal.md');
  await fs.appendFile(goal, '\n用户手工修改\n');
  const before = await fileState(root);
  await assert.rejects(() => sync(root, capture, { apply: true }), /冲突/);
  assert.deepEqual(await fileState(root), before);
});

test('path traversal, symlinks, and outside-project roots are refused', async t => {
  const { root, capture } = await seed(t);
  const bad = copy(capture);
  bad.snapshots[1].documents.goals = `${cycle}/../escape.md`;
  await assert.rejects(() => sync(root, bad, { apply: true }), /路径/);
  await assert.rejects(() => sync('/private/tmp', capture), /本项目/);
  const goal = path.join(root, cycle, 'Goal.md');
  await fs.unlink(goal);
  await fs.symlink(path.join(root, 'README.md'), goal);
  await assert.rejects(() => sync(root, capture, { apply: true }), /符号链接/);
});

test('stale capture and existing lock refuse apply', async t => {
  const { root, capture } = await seed(t);
  const old = copy(capture); old.captured_at = '2000-01-01T00:00:00Z';
  await assert.rejects(() => sync(root, old, { apply: true }), /过期/);
  capture.snapshots[1].nodes[0].text += '\n修改';
  await fs.mkdir(path.join(root, '.freeform-sync-lock'));
  await assert.rejects(() => sync(root, capture, { apply: true }), /EEXIST/);
});

test('failed multi-file commit rolls back original files', async t => {
  const { root, capture } = await seed(t);
  const before = await fileState(root);
  capture.snapshots[1].nodes[0].text += '\n修改';
  await assert.rejects(() => sync(root, capture, { apply: true, beforeCommit: async index => { if (index === 1) throw new Error('injected failure'); } }), /injected failure/);
  for (const [rel, digest] of Object.entries(before)) assert.equal(hash(await fs.readFile(path.join(root, rel))), digest, rel);
  assert.equal((await verifyExisting(root)).status, 'verified-existing');
});

test('rollback preserves a concurrent user edit and keeps the recovery lock', async t => {
  const { root, capture } = await seed(t);
  const goal = path.join(root, cycle, 'Goal.md');
  capture.snapshots[1].nodes[0].text += '\n修改';
  await assert.rejects(() => sync(root, capture, { apply: true, beforeCommit: async index => {
    if (index === 1) { await fs.writeFile(goal, '并发用户修改'); throw new Error('interrupted'); }
  } }), /回滚遇到/);
  assert.equal(await fs.readFile(goal, 'utf8'), '并发用户修改');
  assert.ok((await fs.stat(path.join(root, '.freeform-sync-lock'))).isDirectory());
});

test('capture persistence keeps Vision out of cycle payloads and rejects tampering', async t => {
  const { root, capture } = await seed(t);
  const rel = await saveCapture(root, 'sample', capture);
  const descriptor = JSON.parse(await fs.readFile(path.join(root, rel)));
  assert.equal(descriptor.snapshots, undefined);
  const incoming = JSON.parse(await fs.readFile(path.join(root, cycle, 'source/incoming-sample.json')));
  assert.equal(incoming.scope, cycle);
  assert.ok(!incoming.nodes.some(n => n.id === 'vision'));
  assert.deepEqual((await readCapture(root, rel)).snapshots, capture.snapshots);
  await fs.appendFile(path.join(root, cycle, 'source/incoming-sample.json'), ' ');
  await assert.rejects(() => readCapture(root, rel), /修改/);
});

test('existing project snapshots pass read-only compatibility checks without regenerating files', async () => {
  const before = await fs.readFile(path.join(project, 'sync.json'), 'utf8');
  const report = await verifyExisting(project);
  assert.ok(report.nodes > 0 && report.cells > 0);
  assert.equal(await fs.readFile(path.join(project, 'sync.json'), 'utf8'), before);
});
