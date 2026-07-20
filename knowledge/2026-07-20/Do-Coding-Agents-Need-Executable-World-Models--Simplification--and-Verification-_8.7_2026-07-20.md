# Do Coding Agents Need Executable World Models, Simplification, and Verification to Solve ARC-AGI-3?

**评分：** 8.7  
**状态：** 正常  
**标签：** 推理, Agent, ARC-AGI, 世界模型, 代码生成, 论文, 消融实验  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15439v1 Announce Type: new Abstract: Our previous ARC-AGI-3 agent bundled executable world modeling, scheduled simplification, and exact replay verification, leaving unclear which idea accounted for its performance. We address this attribution question with four nested Codex-based agents: a textual baseline; a flexible-interface executable world model without replay verification; the same executable model with scheduled simplification; and a fixed-interface verification treatment that retains simplification and requires exact reproduction of recorded observations. The main study evaluates all four agents with gpt-5.4 and gpt-5.5 at high and xhigh reasoning effort on the public ARC-AGI-3 games. Exploratory follow-ups evaluate the textual and verification variants with gpt-5.6-sol at xhigh and max. The most robust result is that every agent variant improves with a stronger model and with greater reasoning effort. Within each model-effort setting, differences among variants are smaller than anticipated, while the effects of individual components vary across settings. Requiring a persistent executable deliverable is not universally beneficial: the textual variant outperforms the flexible-interface executable variant in both gpt-5.5 settings. Simplification improves performance in three of the four model-effort settings, with the weakest setting as the only exception. The complete verification treatment ranks first in all four settings, although it uses substantially more resources. In the gpt-5.6-sol follow-up, the verification variant fully solves every public game at both reasoning efforts, achieves about 99% RHAE, and uses fewer than half the total actions of the human baseline. Because the model postdates these games and held-out performance remains untested, this result should be interpreted as saturation of the public set only.

## 综合总结
本文对ARC-AGI-3智能体的三个核心组件（可执行世界模型、简化、验证）进行了消融研究。实验表明，更强的模型和推理努力是性能提升的最稳健因素；可执行世界模型并非总是必要；简化策略在强模型下有效；验证机制虽资源消耗大但表现最佳。结合gpt-5.6-sol的验证变体完全解决了公开集（99% RHAE），但作者审慎指出这仅代表公开集饱和，需警惕数据泄露风险，保留集表现仍待验证。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文针对ARC-AGI-3智能体中的可执行世界模型、计划性简化和精确重放验证三个核心组件进行了严谨的消融实验。研究设计精巧，通过四个嵌套变体和多种前沿模型（gpt-5.4/5.5/5.6-sol）及不同推理努力程度的组合测试，揭示了反直觉的结论：可执行世界模型并非普遍有益（文本基线在部分设置下更优），简化策略在强模型下才凸显作用，而验证机制虽成本高昂但效果最稳健。这深刻揭示了模型基础能力与外部增强组件之间的复杂交互关系，论证严谨，洞见深刻。

### 实用性 (评分: 7.5/10)
对构建复杂推理和编码智能体的从业者具有较高参考价值。验证机制和简化策略的设计可以直接指导当前Agent架构的工程实践，特别是验证机制对提升任务完成确定性的显著作用。然而，验证机制带来的高昂资源消耗，以及部分组件效果高度依赖极强基础模型（如gpt-5.6-sol）的前提，限制了其在算力有限或使用普通模型场景下的直接落地适用性。

### 社区活跃度 (评分: 9.5/10)
ARC-AGI-3是AGI推理领域的核心基准，本文使用最新前沿模型（gpt-5.6-sol）在公开集上实现了完全解决（99% RHAE），具有极高的时效性和话题度。作者对结果保持了极度审慎的态度，明确指出模型晚于数据集发布可能存在的数据泄露风险，且未测试保留集，这种严谨性反而增强了研究的可信度。该成果必将引发社区对ARC基准现状及模型泛化能力的广泛讨论。

## 项目链接
https://arxiv.org/abs/2607.15439
