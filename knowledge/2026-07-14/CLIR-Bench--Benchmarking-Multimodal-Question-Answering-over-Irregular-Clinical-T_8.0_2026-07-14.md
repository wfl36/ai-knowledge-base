# CLIR-Bench: Benchmarking Multimodal Question Answering over Irregular Clinical Time Series

**评分：** 8.0  
**状态：** 正常  
**标签：** 医疗AI, 时间序列, 多模态, 问答系统, 基准测试, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09880v1 Announce Type: new Abstract: Clinical time series are central to patient monitoring, risk assessment, and clinical decision support. However, they are often sparse, irregularly sampled, and asynchronous, making it difficult for models to identify the temporal evidence required for clinical Question Answering (QA). Existing benchmarks primarily focus on regularly sampled time-series QA or medical QA over static data, and therefore rarely assess whether models can faithfully ground their answers in irregular temporal observations. To fill this gap, we introduce CLIR-Bench, a benchmark for irregular clinical time series QA constructed from de-identified ICU records through a principled four-stage pipeline. CLIR-Bench contains 6,600 QA instances spanning 11 clinical variables, organized into four capability dimensions and 11 tasks. Each question is linked to explicit temporal evidence and task-specific answer derivation rules, enabling evaluation of both answer accuracy and evidence use. Experiments show that existing generalist models struggle to retrieve and reason over sparse clinical evidence, highlighting the need for stronger irregular time-series reasoning methods. Our code and data are available at https://huggingface.co/datasets/winall/CLIR-Bench.

## 综合总结
本文提出CLIR-Bench，首个针对不规则临床时间序列多模态问答的基准。该基准基于ICU记录构建，包含6600个QA实例，通过关联明确的时间证据与推导规则，实现对模型答案准确性与证据使用能力的双重评估。实验表明现有通用模型在此类任务上表现挣扎，凸显了研发更强不规则时序推理方法的迫切需求。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
填补了不规则临床时间序列QA的基准空白，构建流程严谨（四阶段流水线），设计了细粒度的能力维度（4维度11任务），并创新性地引入了基于明确时间证据和推导规则的评估机制，深刻揭示了现有通用模型在稀疏/异步临床时间序列推理上的缺陷。

### 实用性 (评分: 7.5/10)
开源了代码与数据集，为医疗AI和时间序列推理研究者提供了标准化的评估工具。虽然直接面向临床落地的应用门槛较高（涉及医疗数据合规等），但对相关模型的研发、评估和迭代具有极高的指导价值。

### 社区活跃度 (评分: 8.0/10)
针对医疗AI领域长期存在的不规则时间序列处理痛点，话题时效性强；arXiv预印本发布，数据集托管于HuggingFace，具备良好的开源社区属性和学术可信度，有望成为该细分领域的重要评测标准。

## 项目链接
https://arxiv.org/abs/2607.09880
