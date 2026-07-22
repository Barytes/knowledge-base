# 全双工语音 Agent：机制与改造边界

## 核心结论

全双工原本是通信概念：双方可以在同一时间发送和接收信息。放到语音 Agent 中，需要区分传输层和对话层。

传输层可以真正全双工。客户端在播放模型语音时，麦克风仍持续上传用户音频，服务端也持续下发音频和事件。对话层通常不是“两条语义流同时独立推理”，而是支持 `barge-in`：系统在模型说话时继续监听，一旦检测到用户开口，就取消当前回复、停止播放、截断尚未播放的内容，再基于新的会话状态继续。

因此，GPT Realtime 的全双工体验主要由持续双向连接、流式音频、VAD、可取消生成、播放截断和会话状态同步共同实现。它不是一个只靠 prompt 或模型参数就能打开的能力。

## GPT Realtime 如何实现

OpenAI Realtime API 维持一个有状态的长连接会话。浏览器和移动端通常通过 WebRTC 同时传送输入音频和接收输出音频；服务端媒体管线也可以使用 WebSocket。模型直接处理实时音频并流式生成音频，减少了传统 `STT -> text agent -> TTS` 串联路径中的等待和语音信息损失。

用户插话时，VAD 会产生 `input_audio_buffer.speech_started` 一类事件。开启 VAD 后，服务端会取消正在进行的模型回复。WebRTC 和 SIP 连接由服务端管理输出缓冲区，可以自动删除还没播放的音频；WebSocket 连接由客户端负责停止播放、记录已经播放到的位置，再发送 `conversation.item.truncate`，保证模型之后记住的是用户真正听到的内容，而不是原本准备说完的整段回复。

这说明体验的关键不只是低延迟，而是“声音、播放位置和会话记忆保持一致”。如果只停止扬声器，却没有截断会话历史，模型会误以为用户已经听完它实际没有听到的内容。

## 普通 Agent 能否改成全双工

可以，但改造对象主要是 runtime，不是 Agent 的业务逻辑。工具、handoff、guardrail、领域提示和状态机通常可以复用；需要替换或新增的是持续音频会话、异步事件循环、流式输出、取消与截断协议、回声消除、播放缓冲和插话后的状态恢复。OpenAI 的 `RealtimeAgent` / `RealtimeSession` 就是把这些媒体和会话职责放进 session 层，同时允许继续挂接普通 Agent 的工具与业务逻辑。

最小改法是保留原来的文本 Agent，在外面串接流式 STT 和 TTS，并在检测到插话时停止 TTS、取消当前 Agent run。这样能获得“可打断”的语音交互，但自然度和延迟通常不如原生 speech-to-speech，转写文本也会丢失语调、节奏和非语言信息。

更完整的改法是让 Realtime 模型负责实时对话，把原 Agent 降为工具或后端工作流。这样更接近自然全双工，但工具调用和副作用必须单独治理：用户插话可以取消语音生成，却不能默认撤销已经提交的付款、发信或数据库写入。听说循环、控制事件和有副作用的执行需要分成不同的 runtime 契约。

普通文本 Agent 也能获得类似的“全双工”交互：在 Agent 运行时继续接收用户 steering，把新输入送入控制队列，并在安全点选择继续、取消或重启当前工作。其本质同样是并发输入、可取消执行和一致状态，而不是让单次阻塞式模型调用凭空同时处理两轮对话。

## 选择建议

如果重点是自然对话、低首音延迟、用户随时插话和语音线索，应优先采用原生 Realtime speech-to-speech。若重点是可审计转写、确定性流程、审批或复用现有文本 Agent，链式语音管线通常更合适。所谓“把普通 Agent 改成全双工”，本质上是在选择新的交互 runtime；是否更换核心 Agent，要看原有业务逻辑是否需要实时音频本身。

若要先排除语音变量，验证全双工交互本身，可从[文字全双工 Agent 的最小 MVP](../ai-product-product-definition/文字全双工Agent的最小MVP.md)开始。

## 本地判断依据

- [AI 系统产品判断框架](../../frameworks/AI系统产品判断框架.md)：系统能力应按 runtime 中真实承担的责任判断，不能只看模型标签。
- [Harness 架构判断框架](../../frameworks/Harness架构判断框架.md)：取消、状态同步、工具副作用和恢复属于 harness / runtime 契约，而不是 prompt 补丁。

## 外部一手资料

- [OpenAI：Realtime and audio](https://developers.openai.com/api/docs/guides/realtime)
- [OpenAI：Realtime conversations](https://developers.openai.com/api/docs/guides/realtime-conversations)
- [OpenAI：Voice agents](https://developers.openai.com/api/docs/guides/voice-agents)
- [OpenAI：Realtime API with WebRTC](https://developers.openai.com/api/docs/guides/realtime-webrtc)
