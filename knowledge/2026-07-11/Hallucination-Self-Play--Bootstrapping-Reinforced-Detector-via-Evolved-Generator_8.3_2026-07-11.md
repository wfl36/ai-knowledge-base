# Hallucination Self-Play: Bootstrapping Reinforced Detector via Evolved Generator

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 幻觉检测, 强化学习, RLAIF, 自博弈, 论文  
**更新日期：** 2026-07-11  
**来源：** rss  

## 项目描述
arXiv:2607.07993v1 Announce Type: new Abstract: Identifying faithfulness hallucinations in LLM-generated outputs remains challenging due to the scarcity of high-quality annotated data. Recent work relies on advanced LLMs to synthesize training data, including rationales, labels, and hallucinated claims. However, these methods treat the generator as a static component, limiting iterative improvement of the detector. To address this limitation, we introduce Hallucination Self-Play (HSP), a novel framework that enables the detector to bootstrap with an evolved generator. HSP involves two roles initialized from the same base model, a detector that assesses the faithfulness of model outputs, and a generator that produces increasingly hard-to-detect hallucinated responses. Specifically, the detector is first fine-tuned on human-labeled data and then employed as a reward model to train the generator via reinforcement learning from AI feedback (RLAIF). In turn, the evolved generator synthesizes hallucination data to further optimize the detector through rule-based reinforcement learning. Experiments on RAGTruth benchmark and two model families demonstrate that the proposed framework can progressively enhance a small LLM to match or even outperform advanced LLMs without external supervision. Our code is available at https://anonymous.4open.science/r/Hallucination-Self-Play-50B5 .

## 综合总结
本文提出了一种新颖的幻觉自博弈框架（HSP），通过同源初始化的检测器和生成器进行对抗进化。检测器作为奖励模型通过RLAIF训练生成器产生更难检测的幻觉，进化后的生成器再合成数据通过强化学习优化检测器。实验表明，该闭环机制能使小模型在无外部监督下达到甚至超越高级模型的幻觉检测性能，为低成本构建高保真度检测器提供了突破性方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了幻觉自博弈框架（HSP），创新性地将对抗博弈思想引入幻觉检测，通过同源模型初始化检测器与生成器，利用RLAIF和基于规则的RL实现两者的闭环协同进化，摆脱了对静态高级模型的数据依赖，技术深度与论证严谨性较高。

### 实用性 (评分: 8.0/10)
为解决高质量幻觉标注数据稀缺问题提供了可落地的自动化方案，使小模型能在无外部监督下达到甚至超越高级模型的检测能力，大幅降低了对昂贵闭源模型API的依赖，对RAG及LLM输出可信度评估的工程实践具有极高参考价值。

### 社区活跃度 (评分: 8.5/10)
幻觉检测是当前大模型领域的核心痛点，该研究结合了自博弈与RLAIF等前沿热点，时效性极强；在RAGTruth基准上的表现证明了其有效性，对社区在低成本构建高质量检测器方面具有重要影响力和较高的可信度。

## 项目链接
https://arxiv.org/abs/2607.07993
