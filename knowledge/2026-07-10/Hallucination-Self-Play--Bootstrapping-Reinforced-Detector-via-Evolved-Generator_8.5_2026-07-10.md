# Hallucination Self-Play: Bootstrapping Reinforced Detector via Evolved Generator

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 幻觉检测, 自我博弈, 强化学习, RLAIF, 论文  
**更新日期：** 2026-07-10  
**来源：** rss  

## 项目描述
arXiv:2607.07993v1 Announce Type: new Abstract: Identifying faithfulness hallucinations in LLM-generated outputs remains challenging due to the scarcity of high-quality annotated data. Recent work relies on advanced LLMs to synthesize training data, including rationales, labels, and hallucinated claims. However, these methods treat the generator as a static component, limiting iterative improvement of the detector. To address this limitation, we introduce Hallucination Self-Play (HSP), a novel framework that enables the detector to bootstrap with an evolved generator. HSP involves two roles initialized from the same base model, a detector that assesses the faithfulness of model outputs, and a generator that produces increasingly hard-to-detect hallucinated responses. Specifically, the detector is first fine-tuned on human-labeled data and then employed as a reward model to train the generator via reinforcement learning from AI feedback (RLAIF). In turn, the evolved generator synthesizes hallucination data to further optimize the detector through rule-based reinforcement learning. Experiments on RAGTruth benchmark and two model families demonstrate that the proposed framework can progressively enhance a small LLM to match or even outperform advanced LLMs without external supervision. Our code is available at https://anonymous.4open.science/r/Hallucination-Self-Play-50B5 .

## 综合总结
本文提出幻觉自我博弈框架（HSP），通过检测器与生成器的对抗博弈实现相互促进。检测器作为奖励模型指导生成器产生更隐蔽的幻觉数据，进化后的生成器再反哺检测器优化。实验表明，该闭环框架能使小模型在无外部监督下逐步增强，最终在RAGTruth基准上匹配甚至超越高级大模型的幻觉检测性能，为低成本、高精度的幻觉检测提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出了一种新颖的幻觉自我博弈（HSP）框架，将幻觉检测转化为检测器与生成器的对抗博弈过程。检测器作为奖励模型通过RLAIF训练生成器产生更难检测的幻觉，而进化后的生成器合成数据通过强化学习反哺检测器优化，形成闭环迭代。该方法巧妙借鉴了GAN的思想并应用于大模型幻觉检测，技术路径创新性强，闭环设计精巧且论证严谨。

### 实用性 (评分: 8.5/10)
该框架使小参数模型能够通过自我迭代达到甚至超越高级大模型的幻觉检测能力，无需昂贵的人工标注或依赖外部更强模型的监督。这极大降低了企业部署高精度幻觉检测系统的算力和数据成本，在RAG等高幻觉风险场景中具有极高的落地价值和适用性。

### 社区活跃度 (评分: 8.0/10)
幻觉检测是当前大模型可信度与落地应用的核心痛点。该论文结合了Self-play与RLAIF两大前沿热点，在RAGTruth基准上验证了有效性，且开源了代码。其提出的'小模型超越大模型'的范式对学术界和工业界均具有较强吸引力，具备较高的关注潜力和社区影响力。

## 项目链接
https://arxiv.org/abs/2607.07993
