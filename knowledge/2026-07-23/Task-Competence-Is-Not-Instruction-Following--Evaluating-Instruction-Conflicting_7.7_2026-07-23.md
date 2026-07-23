# Task Competence Is Not Instruction Following: Evaluating Instruction-Conflicting Behavior in Small Language Models

**评分：** 7.7  
**状态：** 正常  
**标签：** 小模型, 指令遵循, 模型评估, 对齐, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19608v1 Announce Type: new Abstract: Instruction tuning is meant to make language models follow user requests, yet it is unclear whether small models comply when an instruction conflicts with their usual task behavior. We study this across three tasks - multiple-choice question answering (MCQA), sentiment classification, and mathematical question answering - by pairing a standard instruction with a conflicting non-standard one (select an incorrect option, output the opposite sentiment, or return twice the answer). This cross-task design allows us to test whether resistance to conflicting instructions is tied to specific task characteristics or reflects a broader behavioral tendency. As all predictions are scored against the original ground truth, a model that ignores the non-standard instruction still appears accurate. Using standard accuracy, non-standard accuracy, and an Instruction-Following Failure Rate (IFFR), we evaluate instruction-tuned Qwen models across sizes. Both standard accuracy and instruction following generally improve with scale, although the pattern is not consistent across all tasks and datasets. Small models stay competent yet routinely ignore the non-standard instruction, while larger models show a clear gap between the two settings. These findings suggest that gains in task capability do not automatically provide reliable control over model behavior. Task competence and instruction following are therefore distinct abilities, and reporting only standard accuracy hides instruction-following failures.

## 综合总结
本文针对小语言模型在指令冲突下的行为进行了深入研究，指出任务能力与指令遵循是两种解耦的能力。实验表明，小模型在保持任务准确率的同时经常忽略非标准指令，而仅报告标准准确率会掩盖其指令遵循的失败。该研究为小模型的评估和可控性提供了新的视角和评测方法。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了“任务能力不等于指令遵循”的核心洞见，通过在MCQA、情感分类和数学问答三个任务上设计冲突指令实验，引入指令遵循失败率（IFFR）指标，严谨地论证了小模型虽然能保持任务准确率，但普遍存在忽略冲突指令的现象，而大模型则表现出任务能力与指令遵循的分离。研究设计巧妙，揭示了标准评估指标的盲区，具有较高的理论深度和新颖性。

### 实用性 (评分: 7.5/10)
研究对AI从业者的模型评估和选型具有直接指导意义。它提醒开发者在评估小模型时，不能仅依赖标准准确率，必须单独考察其指令遵循与可控性。提出的IFFR指标和冲突指令测试方法可直接应用于现有的评测体系中，以更全面地衡量小模型的真实可用性及安全性。

### 社区活跃度 (评分: 7.0/10)
论文聚焦于小模型的可控性与对齐问题，这是当前大模型社区高度关注的热点，时效性强。作为arXiv上的新论文，其观点对现有大模型评估范式提出了有力挑战，具有较高的讨论价值。但实验主要基于Qwen系列模型，结论的跨架构普适性有待社区进一步验证。

## 项目链接
https://arxiv.org/abs/2607.19608
