# LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining

**评分：** 8.2  
**状态：** 正常  
**标签：** 论辩挖掘, 结构化预测, 约束解码, 多智能体, 小模型, 论文, 比赛报告, 工程实践  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20430v1 Announce Type: new Abstract: We present LLM-INSTRUCT, the winning system for the UZH Shared Task at ArgMining 2026 on paragraph-level argument mining in UN and UNESCO resolutions. The task requires paragraph-type classification, prediction of a subset of 141 official tags, and directed relation prediction under a strict JSON schema setting using only open-weight models up to 8B parameters. We frame the task as constrained structured prediction. The system first narrows the candidate tag space with metadata-aware dense retrieval, then applies constrained decoding with per-dimension caps, escalates only uncertain cases to a three-agent debate branch, and finally validates the output schema. On the official leaderboard, LLM-INSTRUCT ranked 1st overall, with 1st in F1 and 5th in LLM-as-a-Judge. During development, our configuration search further improved Task 1b Micro-F1 from 35.83% to 40.08% while keeping the internal Task 2 score at 4.421. The main lesson is simple: reducing the decision space before generation improves both accuracy and submission robustness. Our code and supporting scripts are publicly available at: https://github.com/LLM-Instruct-at-UZH-Shared-Task-2026/Method

## 综合总结
本文介绍了在ArgMining 2026共享任务中夺冠的系统LLM-INSTRUCT，该系统在8B参数开源模型的限制下，通过元数据感知的密集检索缩小候选标签空间，结合带维度上限的约束解码、针对不确定案例的三智能体辩论以及输出Schema验证，实现了高质量的段落级论辩挖掘。该方法证明了在受限生成任务中，生成前减少决策空间能显著提升小模型的准确性与鲁棒性，对复杂结构化输出任务具有极高的工程参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
该工作将段落级论辩挖掘任务建模为约束结构化预测问题，巧妙组合了元数据感知的密集检索、带维度上限的约束解码、选择性三智能体辩论以及Schema验证四个模块。虽然各单一技术并非原创性突破，但在8B参数开源模型的严格限制下，通过'先缩小决策空间再生成'的思路显著提升了复杂结构化输出的准确性与鲁棒性，论证严谨且工程组合创新性强。

### 实用性 (评分: 8.5/10)
对受限于算力需使用小模型（8B以下）进行复杂结构化输出、多标签分类或关系抽取的从业者具有极高的参考价值。其'检索缩减候选空间->约束解码->不确定性升级辩论->格式校验'的流水线设计可直接迁移至其他受限生成场景，且代码已开源，落地指导性极强。

### 社区活跃度 (评分: 8.0/10)
本文是ArgMining 2026国际共享任务的冠军系统报告，具备极高的时效性和比赛成绩背书的权威性。arXiv预印本发布于2026年7月，反映了当前AI社区在小模型复杂推理与结构化输出方面的前沿探索动态。

## 项目链接
https://arxiv.org/abs/2607.20430
