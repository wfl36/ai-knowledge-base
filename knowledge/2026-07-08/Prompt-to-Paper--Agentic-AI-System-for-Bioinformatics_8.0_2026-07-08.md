# Prompt-to-Paper: Agentic AI System for Bioinformatics

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, 多智能体, RAG, 科学研究, 生物信息学, 论文  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05456v1 Announce Type: new Abstract: While recent advances in large language models have enabled end-to-end automated manuscript generation, existing systems suffer from three critical deficiencies: (i) generated claims are not deterministically grounded in verifiable literature, (ii) experimental results are frequently fabricated rather than executed, and (iii) there exists no standardized, multi-dimensional framework to assess whether AI-generated manuscripts meet the quality and rigor required for real-world publication. We present Prompt-to-Paper, a multi-agent framework that directly addresses this evaluation gap through three integrated innovations. First, a deterministic retrieval-augmented generation pipeline with section-aware relevance scoring and snowball citation expansion grounds every claim in a verifiable corpus of 60--100 papers. Second, an autonomous coding agent executes real computational biology experiments replacing synthetic outputs with genuine numerical results. Third, an eight-dimensional automated quality scorer, benchmarked with approximate reference statistics from published papers and augmented with explicit hallucination penalties, provides standardized, reproducible quality assessments. The quality-driven improvement loop uses a context-rich reviser that routes each iteration to one of three researcher actions and fires a deep research cycle every ten iterations to re-run experiments and re-manuscript from stronger outputs. We validate the system on five bioinformatics case studies; all five cases compiled submission-formatted PDFs with zero out-of-range citations. The improvement loop raises manuscript quality by an average of +17.96 points on a 0--100 scale (maximum +26.04. As partial external checks, a human reviewer scored the five manuscripts at an average of 7.0 out of 10. Complete manuscripts are produced at approximately 0.31 USD per paper.

## 综合总结
本文提出了Prompt-to-Paper，一个用于生物信息学的多智能体AI系统，旨在解决现有AI生成论文中声明不可验证、实验数据伪造和缺乏质量评估的痛点。系统集成了确定性RAG管道、自主执行真实实验的编码Agent以及带幻觉惩罚的八维自动评分器，并通过质量驱动的迭代闭环不断优化手稿。在5个生物信息学案例验证中，系统成功生成了零越界引用的提交级PDF，质量平均提升17.96分，人类评审均分达7.0/10，且单篇成本仅0.31美元，为AI辅助科研提供了一种高保真、可验证的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究针对AI自动生成学术论文的三大核心痛点（声明不可验证、实验数据伪造、缺乏标准化评估）提出了系统性的多智能体解决方案。技术创新显著：1) 引入带有章节感知和滚雪球引用扩展的确定性RAG管道，确保声明有据可依；2) 采用自主编码Agent执行真实计算实验，从根本上杜绝数据捏造；3) 构建了带有幻觉惩罚机制的八维自动质量评分器，并结合质量驱动的迭代循环（每10次迭代触发深度研究重跑），形成闭环优化。整体架构严谨，论证逻辑清晰，技术深度较高。

### 实用性 (评分: 8.0/10)
系统在生物信息学领域展现了极高的可落地性。通过自主编码Agent执行真实实验并生成可提交格式的PDF，直接对接了科研人员的核心需求。极低的生成成本（约0.31美元/篇）和经过验证的质量提升效果（平均提升17.96分，人类评审7.0/10）使其具备显著的实践指导价值。不过，其高度依赖可执行代码的实验验证模式，在泛化到非计算型实验学科时可能需要较多适配。

### 社区活跃度 (评分: 7.5/10)
AI自动生成学术论文是当前学术界与工业界共同关注的极具争议和时效性的前沿话题。该研究直击AI学术写作的伦理与质量痛点，来源为arXiv预印本，具备一定的学术可信度。尽管AI代写论文在社区中存在伦理争议，但其提出的'可验证性'和'反幻觉'机制为AI辅助科研提供了更负责任的范式，预计将在AI4Science和学术评估社区引发较高关注和讨论。

## 项目链接
https://arxiv.org/abs/2607.05456
