# Bakery：iOS 端远程开发 APP

> 来源：Superlinear Academy 社区分享
> 作者：社区成员

## 产品定位

Bakery 把 iPhone 变成 Mac 上运行的 Claude Code 的**远程控制器**。

**官方描述**：

> Bakery app turns your iPhone into a remote control for Claude Code running on your Mac. Chat with Claude, watch it write and edit code in real time, and preview the result in a live iOS Simulator stream — all from your phone, on the couch, on the train, or next to your Mac when you don't feel like sitting at the keyboard.

**核心价值**：
1. iPhone → Claude Code（Mac）的远程控制
2. 实时看到 Claude 写代码、改代码
3. iOS 模拟器画面实时串流到手机预览
4. 场景：沙发上、火车上、不想坐键盘前

## 解决的问题

### 问题 1：iOS App 的空间性体验

iOS App 是空间性的——手势、转场、触觉反馈、滚动物理效果。这些东西从代码 diff 里看不出来，只有拿在手里才能发现：1 像素偏移、滚动手感不对、按钮太小拇指点不到。

**"build succeeded" 只是故事的一半，另一半是拿起手机感受 App 在你手中运行。**

### 问题 2：离开桌面后如何继续使用 Claude Code

传统方式：只能坐在 Mac 前、用键盘和终端。

Bakery 方式：沙发上、火车上、任何地方都能继续和 Claude Code 工作。

## 产品机制

| 功能 | 说明 |
|------|------|
| **远程控制 Claude Code** | iPhone 作为控制器，Mac 上运行 Claude Code |
| **实时代码可见性** | 看到 Claude 写代码、改代码的实时 diff |
| **iOS 模拟器串流** | 模拟器画面实时推送到 iPhone，直接触摸交互 |
| **完整开发闭环** | 聊天 → 写代码 → 编译 → 预览 → 测试 → 继续改 |

## 与 clawhouse 的核心重叠

**Bakery 也强调访问连续性**——让用户离开 Mac 后，能在 iPhone 上继续控制那台 Mac 上运行的 Claude Code。

这与 clawhouse 的核心目标高度一致：

> 无论身在何处，都能访问"我的 agent"。

### Bakery 已经 address 什么

| clawhouse 痛点 | Bakery 是否 address |
|---------------|---------------------|
| 移动端接回原 agent 工作 | **✅ 已 address** — iPhone 控制 Mac 上的 Claude Code |
| 实时代码可见性 | **✅ 已 address** — 实时看到 Claude 写/改代码 |
| 运行时现场可见性 | **✅ 已 address** — iOS 模拟器画面实时串流 |
| 对话历史同步 | **❓ 未知** — 描述未明确 |
| 不锁定用户到特定设备 | **⚠️ 单向锁定** — iPhone → Mac，而非任意设备互连 |

### Bakery 与 clawhouse 的差异

| 维度 | Bakery | clawhouse |
|------|--------|-----------|
| **方向** | iPhone → Mac（单向） | 任意设备互连（双向） |
| **场景** | iOS 开发 | 通用 coding agent |
| **agent 支持** | Claude Code | Codex / pi / Claude Code 等 |
| **可见性重点** | iOS 模拟器 + 代码 diff | 对话历史 + repo 状态 + 任务进度 |
| **是否开源** | ❌ 未开源 | 设想开源 |

## 安装方式

1. 打开 Bakery Server，自动安装 asc CLI、Claude 服务
2. 用 iPhone 扫二维码
3. 开始聊

## 相关链接

- TestFlight 内测：https://testflight.apple.com/join/cPVeBSjg
- 当前验证版本：XCode 26.4

## 与知识库其他主题的关联

- [Clawhouse：多设备 Agent 工作台](clawhouse-多设备-agent-工作台.md)：**高度重叠**——都解决离开原设备后如何继续使用 agent
- [Agent 复利工作模式](agent%20复利工作模式.md)：完整开发循环体现 agent 协作的复利价值
- [Claude Code：较厚的 agentic coding harness](claude-code-harness.md)：Bakery 作为 Claude Code 的移动端远程控制器

## 解决的问题

市场上已有不少 iOS App 支持在手机上写代码，但很少有能在手机上直接测试和体验 App 的功能。

iOS App 是空间性的：
- 手势
- 转场
- 触觉反馈
- 滚动物理效果

这些东西从代码 diff 里看不出来，只有拿在手里才能发现：1 像素偏移、滚动手感不对、按钮太小拇指点不到。

## 产品机制

Bakery 把 iOS 模拟器画面直接串流到 iPhone：
- 手机变成控制器
- 点击 → 模拟器响应
- 滑动 → 滚动
- 打字 → 键盘弹出

尽量减少和 Mac 端开发体验的差异。

## 完整开发循环

在手机上实现完整闭环：

1. 告诉 Claude 需求（"做一个带打卡日历的习惯追踪器"）
2. 看着 Claude 逐个文件编写，实时 diff 滚动
3. 看它编译、启动
4. App 出现在屏幕上
5. 点一点发现问题
6. 继续修改（"让打卡圆环在完成时加个动画"）
7. 结合 Asc CLI 自动发布到 AppStore

## 安装方式

1. 打开 Bakery Server，自动安装 asc CLI、Claude 服务
2. 用 iPhone 扫二维码
3. 开始聊

## 与其他工具的关系

- **Claude Code / Codex**：Bakery 作为前端，连接这些 coding agent
- **Asc CLI**：自动发布到 AppStore
- **iOS 模拟器**：串流到手机屏幕

## 相关链接

- TestFlight 内测：https://testflight.apple.com/join/cPVeBSjg
- 当前验证版本：XCode 26.4

## 与知识库其他主题的关联

- [Clawhouse：多设备 Agent 工作台](clawhouse-多设备-agent-工作台.md)：同样关注多设备场景下的 agent 访问与连续性
- [Agent 复利工作模式](agent%20复利工作模式.md)：完整开发循环体现 agent 协作的复利价值