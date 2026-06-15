# Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces

**评分：** 8.2  
**状态：** 正常  
**标签：** Web Agent, 安全性, 评估基准, 多模态, 红队测试  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13686v1 Announce Type: new Abstract: As autonomous web agents are increasingly deployed to perform real-world tasks, ensuring their safety has become a critical concern. In this work, we study web agent behavior under realistic deceptive interfaces in the e-commerce domain. We introduce WebDecept, a lightweight and configurable plugin framework that enables controlled injection of deceptive interface patterns into existing web environments. Using WebDecept, we instantiate seven deceptive patterns commonly observed on the open web, including targeted advertisements, domain redirection, and shopping manipulation. By injecting these patterns into the frontend during task execution, we perform controlled evaluation of multiple multimodal web agents. Our results show that current web agents are highly susceptible to multiple classes of deceptive interfaces, and that prompt-based constraints are often insufficient to mitigate these failures. We further analyze how the design choices of deceptive patterns influence the success of such manipulations. These findings highlight safety challenges that should be addressed as web agents are scaled toward real-world deployment.

## 综合总结
本文提出了WebDecept框架，用于评估多模态Web Agent在电商欺骗性界面下的安全性。通过注入7种常见欺骗模式，研究发现当前Web Agent极易受到操纵，且基于提示词的防御机制效果有限，揭示了Web Agent在真实部署中面临的严重安全挑战。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出了WebDecept框架，系统性地构建了7种电商欺骗界面模式（如定向广告、域名重定向、购物操纵等），揭示了当前多模态Web Agent对欺骗界面的高度脆弱性，并论证了简单的提示词约束无法有效防御，研究方法严谨且具有前瞻性。

### 实用性 (评分: 8.5/10)
WebDecept作为轻量级可配置的插件框架，可无缝集成到现有Web环境中进行安全评估，为Web Agent开发者提供了实用的红队测试工具，对提升Agent在真实电商场景下的鲁棒性和安全对齐具有直接的工程指导价值。

### 社区活跃度 (评分: 8.0/10)
随着Web Agent逐渐走向真实世界部署，其安全性成为社区关注焦点。本文聚焦电商场景下的欺骗界面问题，切中当前Agent落地的核心痛点，话题时效性强，易引发工业界与学术界的广泛讨论。

## 项目链接
https://arxiv.org/abs/2606.13686
