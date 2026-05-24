# Clawhouse 项目设想

来源：与 Codex 的对话中直接提供
时间：2026-04-12 录入
类型：个人写作 / 混合产品设想

## 核心问题

无法同时在移动端访问不同设备上的 agent，并且有足够清晰友好的 interface。

## 用户和背景

我手头有很多设备，例如实验室台式机、宿舍的游戏本、MacBook air、腾讯云的 vps。这几个每个都可以跑 coding agent，我用 GitHub 或者 iCloud 等服务同步项目的静态文件，然后在不同设备上进行工作。问题是，我有时从工作中走开，还没来得及同步，用手机用平板的时候想做些什么，我没办法立即连上原来那台设备去工作，我得回到原来那台设备的位置，或者我就只能记下来，晚点再弄，要么就得用远程桌面。

我当然可以每个电脑都部署一个龙虾，但是龙虾只能对接聊天软件，聊天软件编程就变成了黑盒，不知道龙虾背后到底做了什么，只能知道龙虾反馈给你的内容。有时候这些反馈还是虚假的。

## 核心洞察

1. 静态上下文很容易同步，但是 agent session 的运行时上下文很难同步。
2. 现在的 agent 已经能很顺利地写好前端页面。
3. 每个 agent 不仅仅是它的模型 + 上下文，还包含了它所处的硬件设备的能力。
4. 用户脑子里有很多隐性知识：每个设备的硬件能力，每个设备上安装了什么 coding agents，当下每个设备上的 agent 都在运行什么任务，每个设备上项目文件处在什么状态，到底有没有被同步。

## 现成的解决方案

- `tmux`：一台电脑，终端
- 聊天软件：多台电脑（多只龙虾），聊天框
- Claude code ui + pinggy：有 interface，支持连接 CC、Cursor、Codex 三个 agent，可以聊天看文件。pinggy 创建一个 tunnel，类似 Cloudflare。
- conduit code：连接 opencode，图形化的 chat 界面、文件浏览和 git。但是不能连接 cc、codex。

## OKR

### O1：统一入口

让手机/平板能访问任意设备上的 Agent。

1. KR1：能添加并显示多个 agent 的卡片
2. KR2：在手机浏览器正常渲染，100% 可用
3. KR3：能跟添加的 Agent 正常对话

### O2：解决黑盒

Agent 动态生成 UI，披露运行时上下文。

1. KR1：`System Status` app 显示设备 CPU / 内存 / uptime / agent 状态
2. KR2：Agent 能动态渲染“此刻最重要的信息”，如测试流、`git status`
3. KR3：每个项目有专属 Dashboard，Agent 根据项目状态动态生成 HTML
4. KR4：Launcher 能展示项目级别的 Dashboard，而非设备级别
5. KR5：用户在 Launcher 能看到 Agent 正在做什么任务

### O3：网络可达

让散落在各处的 Agent 可访问。

1. KR1：支持 Tailscale IP 访问 Agent Server
2. KR2：提供一键安装脚本，包含 Tailscale + Agent Server
3. KR3：Agent 关闭或重启后，Launcher 能检测并更新状态
