# 12 Week Year

本目录用于维护长期 Vision、12 Week Year 方法论，以及彼此独立的 12 Week 执行周期。

本项目独立于知识库维护规范；所有文件变更和同步产物只能发生在本目录及其子目录内。

## 目录

- [12 Week Year 方法论](12-Week-Year-方法论/12-week-plan与记分法.md)：原有的原书与 Field Guide 方法论整理，本次未改动。
- [长期 Vision](长期-Vision/README.md)：两份 15 年 aspiration 与 3 year vision。
- [2026.09.01–2026.11.30](2026.09.01-2026.11.30/README.md)：首个周期的目标、计划、障碍应对、方向探索、Week 1 和 Scorecard。
- [项目 Skills](skill/README.md)：服务于本项目的可复用流程，每个 skill 单独一个子目录。

新增周期时，在根目录创建一个以完整起止日期命名的目录：YYYY.MM.DD-YYYY.MM.DD/。

## 无边记同步

2026-08-27 已将无边记「效率提升」画板中 12 week year 分支的 20 个正文节点及两张记分表单向同步到本目录。无边记是原文来源；本地 Markdown 是便于阅读和检索的镜像。

原文与连接关系快照分别保存在长期 Vision 和对应周期的 source/current.json。同步不会写回无边记，也未设置后台或定时同步。

[同步范围、保留差异与验证记录](同步记录.md) · [同步清单及 SHA-256](sync.json)

后续同步可使用 [freeform-12wy-sync](skill/freeform-12wy-sync/SKILL.md)。项目 `AGENTS.md` 已加入对应任务入口；该 skill 存放在本目录，不安装到全局。脚本支持只读预览、无变化跳过、原文与空值保留、本地冲突检查和更新前归档；仍需要通过 computer-use 实际读取并确认画板范围。
