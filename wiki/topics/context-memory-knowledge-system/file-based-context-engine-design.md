# 长期 file-based context engine 设计

## 摘要

长期 `file-based context engine` 的核心不是把 memory 存成文件，也不是把 RAG 换成 `grep`。它真正要设计的是：哪些长期上下文应该以人和 agent 都能检查、修改、引用、diff 的文件形式存在，并在任务开始前被路由成当前模型真正需要的工作面。

所以它的产品定义可以写成：

> 用文件系统承载可复利的上下文资产，用轻量运行时负责路由、压缩、隔离、写回和验证。

这里的重点有两个。第一，文件是长期状态，不是 prompt 的替代品。第二，context engine 是调度层，不是知识库本身。文件层要稳定、可审计；运行时要薄、可观察；智能判断应更多沉淀在 skills、框架页、runbook 和写回规则里。

## 一、先确定默认工作面

设计这种系统时，第一问不是目录怎么分，而是未来高价值工作默认站在哪一层发生。

如果每次任务都重新读 raw transcript、聊天记录、网页全文或历史工具输出，系统只是有归档，没有复利。真正应该成为默认工作面的，通常是更高密度的中间层：

- 主题知识页
- 用户判断模式
- 项目 context pack
- 可复用 workflow / skill
- 失败案例与验证清单
- 任务状态 compaction

原始材料仍然重要，但它应主要承担证据、校准和纠错功能，而不是日常任务的默认起点。

## 二、文件层应该分生命周期

一个长期 context engine 至少需要按生命周期分层，而不是把所有 markdown 都放进同一个 memory 目录。

`raw/` 保存不可变证据。它解决的是可回查和可追责。

`wiki/` 或 `knowledge/` 保存被维护的综合知识。它解决的是未来不必从原始材料重新理解。

`self/` 或 `profile/` 保存稳定个人判断。它解决的是 agent 不要每次重新猜用户的偏好、边界和表达方式。

`skills/` 保存可复用流程。它解决的是“怎么做”不靠每次临场发挥。

`sessions/` 或 `runs/` 保存任务轨迹、工具使用、context packet、失败路径和最终结果。它解决的是回放、debug 和经验提炼。

`scratch/` 保存短期探索。它默认不进入长期层，除非经过明确写回。

这几层的关键差异不是名字，而是写入门槛不同。越接近长期默认工作面，写入门槛越高，越需要 provenance、验证和人工可检查性。

## 三、读路径要像文件系统，不要只像搜索框

file-based 的优势在于 agent 可以先定位结构，再深读内容。合理读路径应接近：

```text
route task -> list candidate dirs -> read index/summary -> inspect relevant pages -> deep read evidence if needed -> assemble context packet
```

这比直接做向量相似度检索更适合长期系统，因为它保留了目录、页面、上下游关系和维护语义。

向量、全文搜索和 rerank 仍然有用，但它们应该服务文件式探索，而不是替代文件式工作面。搜索负责发现候选，目录和页面负责解释候选为什么可信。

## 四、写路径要有门禁

长期系统最危险的不是“没记住”，而是把错误、临时、未验证、越权的信息写进长期层。

写入应分成三个动作：

```text
capture -> propose writeback -> promote
```

`capture` 记录本次任务发生了什么，可以比较宽松。

`propose writeback` 把可能复用的内容变成候选更新，例如一条观察、一段失败案例、一个 skill 改动、一页 wiki 补充。

`promote` 才进入长期默认工作面。它需要说明来源、适用范围、置信度、过期条件和回滚方式。

对个人偏好和判断模式尤其要慢。一次对话只能支持 observation，不能直接升级成 axiom。

## 五、运行时保持薄，智能沉淀到文件

更稳的架构是：

```text
thin runtime
  - 任务分类
  - 权限与命名空间
  - token 预算
  - 文件读写
  - trace / replay

fat files
  - framework
  - skill
  - index
  - runbook
  - eval cases
  - writeback policy
```

运行时不应该变成一个黑盒 God agent。它只需要负责把正确文件在正确时机加载出来，并记录自己做了什么。真正的判断流程尽量写成可读文件，让人能审、agent 能读、版本控制能 diff。

## 六、最小可行版本

一个可用的 MVP 不需要先做完整平台。可以从一个本地目录和几条命令开始：

```text
context/
  AGENTS.md
  index.md
  raw/
  wiki/
  self/
  skills/
  sessions/
  evals/
```

最小能力是：

- `ingest`：把新材料进入 raw，并生成或更新 wiki。
- `query`：先读 index / framework，再按需读 wiki / raw。
- `compact`：把长任务压成可接力的任务状态。
- `writeback`：把高复用结果提议进入 wiki / self / skills。
- `eval`：用固定任务检查上下文机制是否真的改善结果。

如果只做一个功能，优先做 `query + writeback` 闭环。因为它最直接决定系统是否会复利。

## 七、评价标准

长期 file-based context engine 不应只用“搜得准不准”评价。更关键的是：

- 未来任务是否更少回到 raw
- agent 是否先站在正确的中间层上工作
- 写入是否可追溯、可撤销、可纠错
- 人是否愿意回到这些文件继续编辑和引用
- 上下文是否更干净，而不是更满
- 失败后能否回放：读了什么、没读什么、为什么写回

一句话说，它的 north star 不是 memory recall，而是默认工作面质量。

## 与现有页面的关系

这页把 [Context Engine：上下文编排层](context-engine.md) 具体化到 file-based 形态。它也继承 [信息复利系统设计](information-compounding-systems-design.md) 的核心判断：长期系统的价值不在于多存信息，而在于把未来反复使用的信号提前提炼成默认工作面。

[volcengine/openviking 仓库地图](volcengine-openviking-repo-map.md) 提供了更工程化的参照：`viking://`、L0/L1/L2、session commit 和文件式工具面说明，file-based context 可以从黑盒检索接口升级成可浏览、可定位、可回写的 context runtime。

## 相关页面

- [Context Engine：上下文编排层](context-engine.md)
- [信息复利系统设计](information-compounding-systems-design.md)
- [本地知识库模式](local-knowledge-base-patterns.md)
- [知识库运行模型](knowledge-base-operating-model.md)
- [volcengine/openviking 仓库地图](volcengine-openviking-repo-map.md)
- [coding agent 的上下文压缩工作流](../agent-harness-runtime/coding%20agent%20的上下文压缩工作流.md)
