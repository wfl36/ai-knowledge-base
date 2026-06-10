# Using Probabilistic Programs to Train Inductive Reasoning in Large Language Models

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 推理, 归纳推理, 不确定性校准, 概率程序, 论文  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.09856v1 Announce Type: new Abstract: Post-training Large Language Models (LLMs) for reasoning typically focuses on deductive tasks such as mathematics and coding where correctness is verifiable. Yet, many real-world reasoning problems are inductive: agents must infer uncertain beliefs from sparse, ambiguous observations. There are challenges to using standard fine-tuning methods for inductive reasoning, including difficulties in curating large-scale, high-quality labeled datasets and in handling targets that are inherently distributional. In this work, we introduce a novel approach, called Program-based Posterior Training (PPT), to address these limitations: we use an LLM to generate diverse open-world scenarios as probabilistic programs, run probabilistic inference to produce distributional target responses to queries, and then fine-tune on these probabilistic soft labels. Using this approach, we fine-tune LLMs on 10,000 programmatically generated scenarios and evaluate on held-out motifs, human-labeled judgments, and external benchmarks. Overall, PPT substantially improves estimation accuracy on held-out inductive tasks, increases alignment with human judgments, and transfers to external benchmarks for estimation and calibration. Additionally, the gains in raw calibration are not subsumed by post-hoc temperature scaling, showing that the models have more deeply internalized uncertainty compared to output rescaling. Together, these results suggest that probabilistic-program-mediated fine-tuning is a promising approach for post-training LLMs to reliably perform approximate inductive inference.

## 综合总结
本文针对大语言模型在不确定环境下归纳推理能力不足的问题，提出了一种新颖的基于程序的后验训练（PPT）方法。该方法利用LLM生成开放世界场景的概率程序，通过概率推理生成分布式的软标签进行微调，从而避免了高质量归纳数据集的标注难题。实验表明，PPT不仅显著提升了模型在未知归纳任务上的估计准确性和与人类判断的一致性，还能泛化至外部基准，且其不确定性校准能力的提升源于模型内部表征的改变，而非简单的事后温度调整。该研究为LLM的后训练提供了一条内化不确定性的新路径。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文切中了大语言模型重演绎推理而轻归纳推理的痛点，创新性地提出了基于程序的后验训练（PPT）方法。该方法利用LLM生成开放世界场景的概率程序，通过概率推理生成分布式的软标签进行微调，巧妙避开了归纳推理数据集难以构建和目标本质分布化的挑战。论证严谨，不仅验证了在保留任务上的准确性提升，还通过与温度缩放的对比，有力证明了模型深层内化了不确定性而非表面校准，研究深度与洞见极高。

### 实用性 (评分: 7.5/10)
PPT方法提供了一套自动生成归纳推理训练数据和软标签的完整Pipeline，大幅降低了人工标注成本，对需要处理不确定推理的AI从业者（如医疗诊断、金融预测、智能体决策等场景）具有极高的参考价值。不过，概率推理的计算成本较高，且需要设计或引导生成合适的概率程序，在通用大规模工程落地时可能面临效率与工程复杂度的挑战。

### 社区活跃度 (评分: 9.0/10)
大模型的归纳推理与不确定性校准是当前AI社区高度关注的核心议题，时效性极强。作者阵容包含Brenden M. Lake和Thomas L. Griffiths等认知科学与计算建模领域的顶尖学者，赋予了该研究极高的权威性与可信度。该工作将认知科学中的概率程序思想引入LLM后训练，极易引发学术界和工业界的广泛关注与后续跟进。

## 项目链接
https://arxiv.org/abs/2606.09856
