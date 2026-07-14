# Index SLM Technical Report

**评分：** 8.2  
**状态：** 正常  
**标签：** 小模型, 大模型, 角色扮演, RAG, 技术报告, 开源项目  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09885v1 Announce Type: new Abstract: We present Index-1.9B, a series of open small language models developed at Bilibili. The series comprises four models: Index-1.9B-Base, a foundation model with 1.9 billion non-embedding parameters pre-trained on 2.8 trillion predominantly Chinese and English tokens; Index-1.9B-Pure, a control variant trained with an identical recipe but with all instruction-like data strictly filtered from the corpus; Index-1.9B-Chat, aligned from the base model with supervised fine-tuning and direct preference optimization; and Index-1.9B-Character, which augments the chat model with retrieval-augmented generation for few-shot role-playing customization. Pre-training employs a Warmup-Stable-Decay learning-rate schedule in which the concentration of curated data is raised substantially during the decay phase, together with a Norm-Head output layer that stabilizes training under large learning rates. On a suite of standard benchmarks covering examination, reasoning, mathematics, and code, Index-1.9B-Base attains an average score of 64.92, competitive with or exceeding open models of several times its size. We further report controlled studies on model depth, learning-rate magnitude and scheduling, the interaction between learning-rate decay and data quality, and the effect of including instruction data during pre-training, and we document an unexplained surge in benchmark performance midway through the constant-learning-rate phase. All models, together with evaluation code, are released at https://github.com/bilibili/Index-1.9B.

## 综合总结
B站开源了Index-1.9B小语言模型系列，包含基座、纯净控制、对话及RAG增强角色扮演四个版本。该报告不仅展示了媲美更大参数模型的性能，还深入探讨了学习率调度与数据质量的交互、预训练中指令数据的影响等，并报告了训练中的异常性能激增现象，兼具工程实践与学术参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
报告不仅提出了Norm-Head输出层和W-S-D学习率调度配合数据浓度调整的工程创新，还通过严格的控制变量模型深入研究了预训练中指令数据的影响、LR衰减与数据质量的交互，并如实报告了训练中期的异常性能激增现象，展现了较高的研究深度与严谨性。

### 实用性 (评分: 8.5/10)
1.9B参数规模非常适合端侧和移动端部署；开源了从基座到对话、再到结合RAG的少样本角色扮演定制模型，直接对应虚拟角色交互等实际业务场景，对从业者具有极高的落地参考价值。

### 社区活跃度 (评分: 8.0/10)
由B站团队发布并完全开源，来源权威且可信度高；小语言模型(SLM)与角色扮演是当前AI社区的热点方向，该报告的发布具有很好的时效性和社区影响力。

## 项目链接
https://arxiv.org/abs/2607.09885
