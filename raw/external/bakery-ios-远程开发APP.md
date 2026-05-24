---
title: "Superlinear Academy community"
source: "https://www.superlinear.academy/c/share-your-projects/ios-claudecode-codex-app"
author:
published:
created: 2026-04-16
description: "Superlinear Academy community home page"
tags:
  - "clippings"
---
**我为什么做了 Bakery**

看见市场上已经有不少的 iOS App支持在手机上写 App，但是很少看到有能在手机上直接做测试，体验App的功能。

## 我真正想要的

根据自己的开发习惯，我想让Claude 写代码、编译、然后App 出现在我手机上，可以实时预览，以及操作

然后我做了Bakery APP，就像面包店一样，你自己做蛋糕，面包，又可以亲自感受。

## 它有什么不同

Bakery 把 iOS 模拟器画面直接串流到你的 iPhone 上。你可以在手机上实时验证你的 App

你在手机上点一个按钮——模拟器响应了。你滑动——它滚动了。你打字——键盘弹出来了。

实际上就把手机当成了一个控制器，尽量减少和在MAC端的开发体验差异

## 完整的开发循环，在你手机上

\> 「做一个带打卡日历的习惯追踪器。」

看着 Claude 逐个文件编写，实时 diff 滚动。看它编译、启动。App 出现在你屏幕上。点一点，找到问题。

\> 「让打卡圆环在完成时加个动画。」

看它改。再点一下。

最后结合 Asc CLI,让他自动发不App到 AppStore 也变得没有太多成本了

以前只能在Mac端实现的功能，现在可以在手机端完成了，反馈循环也有了，就可以在任何地方写App了

## 为什么实时预览对 iOS 这么重要

iOS App 是空间性的。手势、转场、触觉反馈、滚动物理效果——这些东西你从代码 diff 里看不出来。

你得拿在手里。那 1 像素的偏移、滚动手感不对、按钮太小拇指点不到——这些只有在真实屏幕上才能发现。

## 如何安装两分钟搞定

1\. 打开Bakery Server, 自动安装asc CLI、Claude 服务

2\. 用iPhone扫一下二维码

3\. 开始聊, 就这么简单

## 最后

纯聊天的客户端有它的价值。但对 iOS 开发来说，「build succeeded」只是故事的一半。另一半是拿起手机，感受 App 在你手中运行。

Bakery 补上了这一半。

欢迎大家体检

TestFlight 内测地址： [https://testflight.apple.com/join/cPVeBSjg](https://testflight.apple.com/join/cPVeBSjg)

Bakery Server 下载地址：

目前版本在XCode 26.4 测试验证

是否支持户外使用呢? 如果是局域网的话, 让 claude 直接安装到手机上体验即可.

ios和windows可以吗

试试 slock.ai