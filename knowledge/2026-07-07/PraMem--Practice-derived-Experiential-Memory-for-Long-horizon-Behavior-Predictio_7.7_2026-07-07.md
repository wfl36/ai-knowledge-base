# PraMem: Practice-derived Experiential Memory for Long-horizon Behavior Prediction

**评分：** 7.7  
**状态：** 正常  
**标签：** 大模型, 行为预测, 经验记忆, 长上下文, 范式转换, 论文  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02881v1 Announce Type: new Abstract: Long-horizon behavior prediction aims to infer a user's next action based on a lengthy historical sequence, playing a crucial role in artificial intelligence field. The rise of large language models (LLMs) offers a promising direction for sequential behavior prediction, yet LLMs struggle with latent behavioral pattern induction and model-intrinsic cognitive biases when tackling long-horizon behavior prediction. Prior memory management methods follow a context-compression paradigm that attempts to address this task by alleviating the historical sequence burden, yet fail to resolve the core challenges. In this paper, we advocate a paradigm shift that reframes the lengthy historical sequence from a burden into a valuable resource to be exploited, and accordingly propose PraMem, which conducts beforehand practice over the lengthy historical sequence to build an experiential memory, thereby serving as the assisted input for accurate long-horizon behavior prediction. Extensive experiments across diverse tasks demonstrate that PraMem achieves superior performance than prior methods, and more in-depth analyses provide valuable insights into the mechanism and evolution of the experiential memory. Code: https://github.com/icip-cas/PraMem.

## 综合总结
本文针对LLM在长视野行为预测中难以归纳潜在模式及存在认知偏差的问题，提出了一种从‘上下文压缩’到‘经验利用’的范式转换。作者提出PraMem框架，将长历史序列视为资源而非负担，通过预先实践构建经验记忆以辅助预测。实验证明PraMem性能优越，且开源了代码，为长序列行为预测及LLM长上下文处理提供了极具启发性和可落地的新思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文在技术深度与新颖性上表现出色。针对大语言模型（LLM）在长视野行为预测中面临的潜在行为模式归纳困难和模型内在认知偏差问题，作者敏锐地指出传统的上下文压缩范式仅能减轻历史序列负担，未能触及核心挑战。据此，提出了一种范式转换：将冗长的历史序列从‘负担’重新定义为‘可利用的资源’，并创新性地提出PraMem框架。该框架通过对长历史序列进行预先‘实践’来构建经验记忆，以此作为辅助输入提升预测准确性。论证逻辑严密，实验充分，且对经验记忆的机制与演化进行了深入分析，展现了扎实的研究深度。

### 实用性 (评分: 7.5/10)
对从业者的实际参考价值较高。PraMem将历史序列转化为经验记忆的思路，不仅适用于长视野行为预测，也为解决LLM长上下文处理和认知偏差问题提供了可落地的工程实践方向。其开源代码（https://github.com/icip-cas/PraMem）进一步降低了复现与应用门槛，可直接指导推荐系统、用户行为分析等领域的算法优化与系统设计，适用范围广泛。

### 社区活跃度 (评分: 7.0/10)
话题具有较好的时效性与学术权威性。长视野行为预测及LLM的长上下文处理是当前AI领域的热点与痛点。作者团队来自中科院软件所等机构，具备较强的学术公信力。论文发布于arXiv（2026年，时间节点具有前瞻性），虽然目前可能处于预印本阶段，但其提出的范式转换和开源代码有望在推荐系统、智能体等社区产生积极的影响力与讨论。

## 项目链接
https://arxiv.org/abs/2607.02881
