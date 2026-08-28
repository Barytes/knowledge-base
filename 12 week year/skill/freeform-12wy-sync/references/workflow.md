# 运行参考

## 1. 只通过 computer-use 读取 UI

以下代码在 `node_repl` 中运行。`root` 使用本项目实际绝对路径；若调用方当前目录不在项目根目录，先确认，不向其他目录写入。

```js
var root = '/Users/beiyanliu/Desktop/knowledge base/12 week year';
var { sky } = await import('@oai/sky');
var { pathToFileURL } = await import('node:url');
var ff = await import(pathToFileURL(root + '/skill/freeform-12wy-sync/scripts/sync.mjs').href);
var stateA = await sky.get_app_state({app:'com.apple.freeform', disableDiff:true});
var a = ff.parseAX(stateA.text);
nodeRepl.write(JSON.stringify(ff.summarize(a)));
```

如果仍在菜单、尚未显示全分支或解析器报不支持的对象，先按 computer-use 指南查看必要 UI 状态/截图并完成导航，再重新取得 `stateA`。不能把上述一次读取当成完整性确认。

```js
var stateB = await sky.get_app_state({app:'com.apple.freeform', disableDiff:true});
var b = ff.parseAX(stateB.text);
var proposal = await ff.proposeRoutes(root, b, {cycle:'2026.09.01-2026.11.30'});
nodeRepl.write(JSON.stringify(proposal));
```

周期参数是本次输入，不应永久写死。每次使用 `proposal` 中的新 `key`；它只是当前读取中的定位标识。持久 `id` 和文档位置沿用已有快照，不能用当前 AX 编号生成持久 ID。

`proposal.routes` 中每项含：`key`、`kind`（node/table）、`scope`、`id`、`document`。已有节点先按完整正文、再按唯一标题匹配。重复内容、重复标题和改标题都可能需要人工消歧。新增项没有自动路由；正文文件必须在其 scope 下。

## 2. 明确范围和关系

完成视觉检查后再填写 review。以下是字段结构，不是可以原样宣称完成的检查记录：

```js
var routes = proposal.routes; // 核对后增补/修正；不能跳过 unmatched_existing。
var review = {
  complete: true,             // 仅在确认分支、孤立节点和表格覆盖后填写
  visual_checked: true,       // 仅在本次确实查看画面后填写
  evidence: '写明本次如何核对范围、表格边界及连线。',
  anchors: proposal.anchors,
  excluded: [                // 必须逐项解释 proposal.unassigned 的归属
    // {key:'node-当前编号', reason:'不是 12 Week Year 分支的内容'}
  ],
  relationships: [           // 仅填写当前已视觉核对的模糊连线
    // {key:'edge-当前编号', from:'语义ID', to:'语义ID',
    //  verification:'visual-connector', evidence:'具体画面依据；锚点是否可确认'}
  ],
  excluded_connectors: []     // {key, reason}；旧关系消失仍会被写入保护拦住
};
var packet = ff.makeCapture(a, b, routes, review);
nodeRepl.write(JSON.stringify(await ff.sync(root, packet)));
```

不应不经检查把全部 `unassigned` 自动排除。两次给定输入哈希一致不证明它们来自两次真实读取；调用者必须实际执行两次 `get_app_state` 并诚实填写证据。

默认在内存中完成捕获、预览和写入，可避免产生额外捕获文件：

```js
nodeRepl.write(JSON.stringify(await ff.sync(root, packet, {apply:true})));
nodeRepl.write(JSON.stringify(await ff.verifyExisting(root)));
```

## 3. 需要跨会话保留捕获包时

```js
var input = await ff.saveCapture(root, '20260827-140000', packet);
nodeRepl.write(input);
```

`saveCapture` 将每份正文分别保存在 `scope/source/incoming-名称.json`；`skill/freeform-12wy-sync/.work/captures/名称.json` 仅存检查元数据、文件路径和哈希。名称必须唯一，不覆盖已有捕获文件。

后续可在项目根目录运行：

```sh
node skill/freeform-12wy-sync/scripts/sync.mjs plan --input skill/freeform-12wy-sync/.work/captures/20260827-140000.json
node skill/freeform-12wy-sync/scripts/sync.mjs apply --input skill/freeform-12wy-sync/.work/captures/20260827-140000.json
```

`plan` 允许离线回放。`apply` 拒绝超过 30 分钟的捕获包；应重新读取，而不是改时间戳。CLI 的输入清单和其引用的快照都必须在项目内，且不允许符号链接。

## 4. 兼容、更新及恢复

- 支持本项目既有 v1 `source/current.json` 与 `sync.json`。旧快照的正文路由从 `node_to_markdown` 读取，旧表格使用该周期的 `Scorecard.md`。新快照将 `documents` 路由直接放在 scope 内。
- 无变化时不重排旧 Markdown，不重写 source JSON，不改变同步时间。哈希比较不受捕获时间、AX 编号、节点顺序影响；空字符串与字符串 `0` 始终不同。
- 只管理节点/表格对应的镜像文档和原文快照，不因项目 `AGENTS.md`、README 或初次同步说明变化而拒绝同步，也不重写这些管理文档。新增文档需要在项目入口补链接时，由代理另作最小更新并明确报告。
- 有变化时只生成受影响文档。新排版保留全部正文，链接到原文并列出相关连线；不把原书方法论混进周期计划，不翻译或优化用户措辞。
- 更新前归档旧镜像至所属 `scope/source/history/事务ID/`。旧同步清单保存在此 skill 的 `.work/history/事务ID/`。
- 文件先暂存，再逐个替换，最后替换清单。普通提交错误会恢复已经替换的文件；这不是跨文件的操作系统原子事务。
- 进程崩溃或并发修改可能留下 `.freeform-sync-lock` 和 `.work/transactions/事务ID/`。停止后续同步，检查事务清单和各 scope 的 history，确认后人工恢复。禁止盲目删除锁或用强制覆盖绕过冲突。
- V1 只支持当前中文 macOS Freeform 暴露的文本、连接线和表格。图片、附件、特殊形状、格式变化或辅助功能未暴露的内容会停止或需要人工检查，不承诺任意画板都能自动处理。

## 5. 校验范围

`verify-existing` 核对已纳管镜像文件的哈希和快照结构，返回节点、单元格数量；它明确返回 `source_completeness_verified:false`。测试使用合成画板，覆盖解析、空值、无变化、增量、冲突、路径保护和失败恢复，不在夹具中复制个人愿景。
