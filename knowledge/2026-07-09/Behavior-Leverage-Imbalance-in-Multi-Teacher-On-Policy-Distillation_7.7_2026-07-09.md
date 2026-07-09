# Behavior Leverage Imbalance in Multi-Teacher On-Policy Distillation

**评分：** 7.7  
**状态：** 正常  
**标签：** 大模型, Agent, 知识蒸馏, 工具调用, 论文  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.07050v1 Announce Type: new Abstract: Agentic language models must learn when to call tools, when to consume tool responses, and when to answer directly. This makes multi-teacher on-policy distillation a natural training strategy: one teacher can specialize in tool calls, another in direct responses, and the student can learn from both on its own generated distribution. We show that this strategy can induce a behavior shift that is invisible from aggregate losses alone. In a two-teacher tool-use setting, vanilla generalized knowledge distillation improves tool-call recall but also moves the model toward over-calling, where it calls tools on examples that should be answered directly. Aggregate explanations are insufficient: tool-call samples do not receive more token exposure, and full-sequence per-token divergence is not larger for the tool-call teacher. We instead analyze behavior leverage imbalance: local token-level signals at mode- entry and structural positions, such as and function names, can have disproportionate control over the global generation mode. We propose Soft Clamp, a per-token divergence calibration method that dynamically compresses extreme token-level Jensen-Shannon divergence while preserving nonzero gradients. On APIGen-MT, Soft Clamp reduces over-calling from 13.7% to 9.0% relative to vanilla GKD while matching its decision accuracy. In a BFCL multi-turn diagnostic, it also lowers tool-call loops and repeated calls among GKD variants. These results suggest that multi-teacher OPD should monitor where teacher signals act, not only how large they are in aggregate.

## 综合总结
本文揭示了Agentic语言模型在多教师在线策略蒸馏中存在的'行为杠杆失衡'现象，即局部token级别的信号会对全局生成模式产生不成比例的控制，导致模型过度调用工具。作者提出了一种名为Soft Clamp的逐token散度校准方法，动态压缩极端Jensen-Shannon散度。实验表明，该方法在保持决策准确率的同时，显著降低了工具过度调用率，并减少了多轮对话中的工具调用循环和重复调用，为多教师蒸馏训练提供了重要的实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文针对多教师在线策略蒸馏（Multi-Teacher On-Policy Distillation）在Agentic语言模型训练中产生的'行为杠杆失衡'（Behavior Leverage Imbalance）现象进行了深入剖析。作者敏锐地指出，传统的基于聚合损失的分析无法解释模型过度调用工具的行为偏移，并从局部token级别（如模式入口和结构位置）揭示了信号的不成比例控制。提出的Soft Clamp方法通过动态压缩极端token级别的Jensen-Shannon散度并保留非零梯度，在理论分析和算法设计上均展现了较高的新颖性与严谨性。

### 实用性 (评分: 7.5/10)
该研究对从事Agent大模型训练、工具调用优化及知识蒸馏的工程师具有极高的实践指导价值。提出的Soft Clamp方法可直接应用于多教师蒸馏流程中，有效缓解工具过度调用和循环调用等实际痛点，且在APIGen-MT和BFCL等基准上验证了其有效性。方法具有较好的通用性，可落地性强，为多教师蒸馏训练提供了具体的调参和监控方向。

### 社区活跃度 (评分: 7.0/10)
随着Agent和工具调用成为大模型领域的热点，多教师蒸馏策略的可靠性备受关注。本文发表于arXiv（2026年），话题时效性极强，直击当前Agent训练中工具过度调用的痛点。虽然作者团队相对年轻，但研究问题切中业界核心痛点，实验基准（APIGen-MT, BFCL）具有代表性，对社区在多教师蒸馏范式下的认知有较好的启发和影响力。

## 项目链接
https://arxiv.org/abs/2607.07050
