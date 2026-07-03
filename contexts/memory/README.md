# Context Memory

这个目录是本仓库的轻量 context-infrastructure 层。

它不是维护好的 wiki，也不是 `life-record/`。它的作用是保存低置信度、可积累的协作观察，等信号重复后再通过 `wiki/self/` 或 `wiki/frameworks/` 晋升。

## 使用方式

- 新的偏好、烦躁点、失败样本，先写进 `OBSERVATIONS.md`。
- 不要从单次情绪直接生成公理。
- 多次重复的 observation 才能变成 pattern。
- 只有稳定、可复用、能约束未来行为的 pattern，才考虑写进 `wiki/self/`。

## 和 maintained wiki 的关系

- `contexts/memory/` 保存工作中的信号。
- `wiki/self/` 保存已经整理过的个人判断模式。
- `wiki/frameworks/` 保存可复用判断框架。
- `wiki/topics/` 保存主题知识和具体分析。

## 最小记录格式

```markdown
### YYYY-MM-DD | 标题

- 场景：
- 触发：
- 观察：
- 伤害：
- 下次规则：
- 置信度：
```
