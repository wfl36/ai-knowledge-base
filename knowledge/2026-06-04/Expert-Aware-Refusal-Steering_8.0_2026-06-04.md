# Expert-Aware Refusal Steering

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 安全对齐, MoE, 越狱, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04160v1 Announce Type: new Abstract: Safety alignment in instruction-tuned large language models (LLMs) depends on a model's ability to reliably refuse to respond to harmful or disallowed requests. Recent work has shown that a steering vector can be applied to a dense LLM during inference to effectively suppress refusal behavior, inducing response to harmful requests. We extend this refusal steering method to three open-source Mixture-of-Experts (MoE) LLMs and find that steering performance is uninhibited by the complex routing patterns inherent to the MoE architecture. We then propose two expert-aware refusal steering methods that leverage refusal-specific expert routing patterns and expert-specific steering directions to suppress normal refusal behavior. We find that refusal behavior can be effectively steered based on the output of a single expert. Our results show that refusal signals captured by steering methods differ from expert routing behavior, suggesting a substantial role for attention in MoE refusal behavior.

## 综合总结
本文研究了指令微调大语言模型在MoE架构下的安全对齐问题，将传统的拒绝转向方法扩展至开源MoE模型。作者提出了两种专家感知的拒绝转向方法，发现MoE的复杂路由模式并未阻碍转向效果，且拒绝行为可通过单一专家的输出被有效控制。研究进一步揭示，转向方法捕获的拒绝信号与专家路由行为存在差异，注意力机制在MoE拒绝行为中扮演关键角色。该研究为MoE模型的安全评估与红蓝对抗提供了新视角。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文将传统的拒绝转向方法从稠密大模型扩展至混合专家架构，技术深度扎实。提出两种专家感知的拒绝转向方法，并发现MoE的复杂路由模式并未阻碍转向效果，且单一专家的输出即可有效控制拒绝行为。研究进一步揭示了转向方法捕获的拒绝信号与专家路由行为存在差异，指出注意力机制在MoE拒绝行为中的关键作用，具有较好的理论洞见。

### 实用性 (评分: 7.5/10)
对大模型安全对齐与红蓝对抗从业者具有较高参考价值。研究揭示了MoE模型在安全防御上的潜在脆弱性（单一专家即可被利用诱导越狱），为后续设计针对MoE架构的安全对齐策略和防御机制提供了明确的指导方向，但在防御侧的直接落地仍需进一步转化。

### 社区活跃度 (评分: 8.0/10)
MoE架构是当前大模型发展的重要趋势，安全对齐亦是社区核心议题，话题时效性极强。文章来源于arXiv，学术可信度良好。虽然发布时间显示为未来（可能为数据异常），但探讨的问题切中当前大模型安全研究热点，对社区有积极的影响力。

## 项目链接
https://arxiv.org/abs/2606.04160
