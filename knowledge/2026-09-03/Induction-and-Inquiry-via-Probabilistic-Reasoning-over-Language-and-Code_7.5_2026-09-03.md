# Induction and Inquiry via Probabilistic Reasoning over Language and Code

**评分：** 7.5  
**状态：** 正常  
**标签：** 认知科学, 贝叶斯推理, 大模型, 符号推理, 归纳学习, 论文, LLM推理  
**更新日期：** 2026-09-03  
**来源：** rss  

## 项目描述
arXiv:2609.01815v1 Announce Type: new Abstract: How humans grow and maintain abstract knowledge from the sparse, streaming noisy data of experience is a longstanding challenge in cognitive science. Any computational account must satisfy at least three desiderata: It must be (1) data-efficient and compute-efficient, (2) capture gradations of uncertainty to support intelligent inquiry and information gathering, and (3) be flexible enough to mentally represent the endless range of concepts people can learn and think about. Here we introduce a computational model that captures these three properties, by encoding symbolic knowledge as mental programs that combine natural language with source code, and sequentially inferring mental programs using LLM-guided Bayesian learning algorithms. Across a range of behavioral studies this model successfully reproduces quantitative signatures of human inductive learning and active inquiry, such as anchoring, garden-pathing, and other effects. In contrast, pure LLMs and classic Bayesian models either fail at the underlying task, or do not reproduce human behavior, or succeed only at exorbitant computational cost. These results suggest that one way humans continually grow their knowledge is by mentally representing many hypotheses spanning language-like and program-like representations, then revising those hypotheses to approximate Bayesian updates, while a bottom-up neural mechanism (an LLM) makes inference both tractable and learnable.

## 综合总结
本文提出一种融合自然语言与源代码的'心智程序'表示，通过LLM引导的贝叶斯学习算法模拟人类归纳推理与主动探究行为。模型成功复现锚定效应、花园路径效应等人类认知特征，在数据效率、不确定性表征和概念灵活性三个维度上优于纯LLM和经典贝叶斯模型。该工作为认知科学与AI的交叉提供了新视角，但工程落地门槛较高，且发布时间存在异常。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了一种将符号知识编码为融合自然语言与源代码的'心智程序'，并用LLM引导的贝叶斯学习算法进行序列推断的计算模型。该方法在三个维度上具有新颖性：(1)将LLM作为底层推理机制与贝叶斯框架结合，实现近似贝叶斯更新；(2)混合语言-代码表示兼顾灵活性与可计算性；(3)成功复现人类归纳学习的多种量化特征（锚定效应、花园路径效应等）。论证较为严谨，与纯LLM和经典贝叶斯模型的对比实验增强了说服力，但创新更多体现在框架整合而非单一技术突破。

### 实用性 (评分: 6.5/10)
对认知科学研究者和构建人类对齐AI系统的从业者具有参考价值，为LLM与符号推理的融合提供了新范式。但实际工程落地较远——需要定制化LLM推理、贝叶斯后验近似等复杂流程，计算成本可能较高。适用场景集中于认知建模与行为实验模拟，对通用NLP/ML工程师的直接指导意义有限。

### 社区活跃度 (评分: 7.5/10)
作者团队来自MIT（Tenenbaum、Ellis等认知科学与AI交叉领域的知名学者），来源权威性高。话题处于'LLM+符号推理''AI认知建模'的热门交叉点，时效性强。但arXiv ID为2609.01815，发布时间标注为2026年9月，疑似预印本编号异常或为测试数据，需谨慎对待其真实性和影响力。话题本身在cognitive science + LLM社区有较高关注度。

## 项目链接
https://arxiv.org/abs/2609.01815
