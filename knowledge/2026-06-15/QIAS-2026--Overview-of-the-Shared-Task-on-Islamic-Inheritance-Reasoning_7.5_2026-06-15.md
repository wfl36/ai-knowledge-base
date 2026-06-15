# QIAS 2026: Overview of the Shared Task on Islamic Inheritance Reasoning

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 推理, 法律AI, 阿拉伯语NLP, 评测, 论文  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13756v1 Announce Type: new Abstract: This paper presents a comprehensive overview of the QIAS 2026 shared task, organized as part of the OSACT7 Workshop and co-located with LREC 2026. The shared task was designed to evaluate the ability of large language models to perform complex reasoning in the religious and legal domain of Islamic inheritance. Unlike conventional question-answering benchmarks, QIAS 2026 focuses on end-to-end reasoning from natural language cases, requiring systems to perform the full inheritance calculation process, from identifying the eligible heirs to assigning the correct share to each beneficiary. To support this evaluation, the task was based on the MAWARITH benchmark, a dataset of $12{,}500$ Arabic inheritance cases annotated with intermediate reasoning steps and final answers. System submissions were evaluated using MIR-E, a multi-step metric that measures performance across the main stages of inheritance reasoning. A total of $16$ teams participated in the shared task, investigating a range of approaches, including prompting-based methods, retrieval-augmented generation, and fine-tuning strategies. The results show that Islamic inheritance remains a highly challenging benchmark for current language models, especially in stages that require precise legal interpretation and structured numerical reasoning. This overview summarizes the task design, dataset, evaluation framework, participating systems, and main results.

## 综合总结
本文概述了QIAS 2026共享任务，旨在评估大模型在伊斯兰继承法领域的端到端复杂推理能力。基于12500个阿拉伯语案例的MAWARITH基准和多步评估指标MIR-E，16支团队测试了提示工程、RAG和微调等策略。结果显示，当前LLM在涉及精确法律解释和数值计算的继承推理上仍面临巨大挑战。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
针对大模型在宗教与法律领域（伊斯兰继承法）的复杂推理能力进行了系统性评测。构建了包含12500个阿拉伯语案例的MAWARITH基准及多步评估指标MIR-E，揭示了当前LLM在精确法律解释与结构化数值推理上的显著局限性，评测框架设计严谨，具有较好的方法学参考价值。

### 实用性 (评分: 6.5/10)
对从事法律AI、阿拉伯语NLP及复杂推理系统的开发者具有较高参考价值，提供的数据集与评估指标可直接复用；但由于领域高度垂直（宗教法+阿拉伯语），对通用AI从业者的落地指导意义相对有限。

### 社区活跃度 (评分: 8.5/10)
作为LREC 2026及OSACT7 Workshop的共享任务概述，来源权威且时效性强。16支团队的广泛参与为该领域提供了多样化的基线结果，增强了结论的可信度与社区影响力，凸显了LLM在专业领域推理的当前边界。

## 项目链接
https://arxiv.org/abs/2606.13756
