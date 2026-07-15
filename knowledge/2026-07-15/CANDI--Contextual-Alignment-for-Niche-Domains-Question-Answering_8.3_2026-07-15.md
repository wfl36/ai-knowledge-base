# CANDI: Contextual Alignment for Niche Domains Question Answering

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 领域评测, 神经符号, 上下文对齐, 推理, 论文, 数据集/基准  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.11891v1 Announce Type: new Abstract: The deployment of large language models (LLMs) in specialized domains like medical diagnostics and financial advisory necessitates evaluating capabilities beyond general knowledge. Traditional question-answering benchmarks often fail to capture the nuanced contextual grounding, user awareness, and domain understanding these fields require. To address this, we introduce CANDI-QA (Contextual Alignment for Niche Domains Question Answering), a novel dataset evaluating LLMs on delivering accurate, context-sensitive, and user-aligned answers in specialized settings. CANDI-QA features expert-curated question-answer pairs structured into two categories: (1) Information Assistance Questions, which are direct, factual queries requiring precise extraction, and (2) Applied Inference Questions, which are multi-hop reasoning tasks needing situational inference to generate actionable insights. We evaluate over ten diverse language models, from compact open-source to state-of-the-art proprietary systems. As a robust baseline, we present MTSS-Net, a lightweight neuro-symbolic framework combining neural retrieval with rule-based reasoning. Our findings highlight the profound challenges of achieving contextual alignment in niche domains, revealing the limitations of current LLMs without enhanced contextual or symbolic integration. Ultimately, CANDI-QA serves as a critical benchmark for advancing research in context-aware language models, stimulating the development of robust, trustworthy AI for high-stakes domains.

## 综合总结
本文针对大语言模型在医疗、金融等专业领域缺乏上下文对齐能力的问题，提出了CANDI-QA评测基准，包含事实提取与多跳情境推理两类专家级问答。研究评估了十余种主流LLM，并提出了一种结合神经检索与规则推理的轻量级神经符号框架MTSS-Net作为基线。实验揭示了当前LLM在专业领域上下文理解上的显著局限，强调了引入符号集成与上下文增强的必要性，为高风险领域的可信AI发展提供了关键基准与实用方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文针对LLM在专业领域缺乏上下文对齐和用户意识的问题，提出了CANDI-QA基准，将问题细分为事实提取与多跳情境推理，结构清晰且切中痛点。同时提出的MTSS-Net基线模型，巧妙结合了神经检索与规则推理（神经符号系统），为解决大模型在专业领域的幻觉和推理偏差提供了严谨的技术路径，研究深度与论证逻辑扎实。

### 实用性 (评分: 8.5/10)
对医疗、金融等高壁垒行业的AI从业者具有极高的参考价值。CANDI-QA数据集可直接用于垂直领域大模型的评测与微调；MTSS-Net作为一种轻量级神经符号框架，可无缝集成至现有RAG或领域QA系统中，提升系统在复杂情境下的推理可靠性与可解释性，落地指导性强。

### 社区活跃度 (评分: 8.5/10)
发布时间为2026年7月，时效性极强，紧扣当前大模型向垂直领域深水区落地的行业热点。作者团队包含Amit Sheth等知名学者，学术权威性高。针对医疗和金融等高风险高关注领域的评测基准，极易引发学术界与工业界的广泛讨论与跟进。

## 项目链接
https://arxiv.org/abs/2607.11891
