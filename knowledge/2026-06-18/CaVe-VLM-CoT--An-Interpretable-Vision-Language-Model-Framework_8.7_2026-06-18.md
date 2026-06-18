# CaVe-VLM-CoT: An Interpretable Vision-Language Model Framework

**评分：** 8.7  
**状态：** 正常  
**标签：** 多模态, VLM, RAG, Agent, 推理, 评估体系, 论文  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18385v1 Announce Type: new Abstract: Vision-Language Models (VLMs) remain prone to hallucinations, producing fluent but visually unfaithful outputs. Existing chain-of-thought and retrieval-augmented methods only partially address this, as they neither enforce step-level citation grounding nor route verification failures back to retrieval for correction. We present CaVe-VLM-CoT, a modular reflection-based agentic-RAG framework that enforces evidence-grounded reasoning through a five-stage closed-loop pipeline: Extractor, Retriever, Solver, Citation Injector, and Verifier, in which detected ungrounded claims trigger structured feedback to the Extractor for targeted re-retrieval. Since no existing framework jointly measures retrieval quality, step-wise citation faithfulness, and cross-modal grounding, we propose a suite of 23 component-wise metrics across all stages, anchored by CaVeScore, a composite metric weighting accuracy, citation precision and recall, attribution, and evidence grounding. Without any architectural or prompt modifications, CaVe-VLM-CoT achieves 87.1\% accuracy and 56.6\% CaVeScore on ScienceQA , and 55.2\% accuracy and 35.7\% CaVeScore on MMMU (30 subjects).

## 综合总结
本文提出CaVe-VLM-CoT框架，通过五阶段闭环流水线（提取、检索、求解、引用注入、验证）将基于反思的Agentic-RAG引入视觉语言模型，有效解决幻觉问题。验证失败时触发结构化反馈进行定向重检索，同时提出包含23个组件指标的评估套件及复合指标CaVeScore，全面衡量检索质量与引用忠实度。在ScienceQA和MMMU基准上，无需架构修改即取得优异表现，为构建高可信、可解释的VLM提供了新范式与评估标准。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了CaVe-VLM-CoT框架，创新性地将基于反思的Agentic-RAG与五阶段闭环流水线结合，解决了VLM中幻觉问题及现有CoT/RAG方法缺乏步骤级引用和验证反馈的痛点。同时提出了包含23个组件指标的评估体系及复合指标CaVeScore，在评估检索质量、引用忠实度和跨模态对齐方面填补了空白，技术深度与严谨性较高。

### 实用性 (评分: 8.8/10)
对解决VLM实际应用中的幻觉问题具有极高的参考价值。其模块化、闭环的Agentic-RAG设计可直接指导开发者构建高可靠性的多模态问答系统，且无需修改底层模型架构或提示词。提出的CaVeScore指标体系为工业界评估和优化VLM的生成可信度提供了可落地的量化工具。

### 社区活跃度 (评分: 8.7/10)
选题极具时效性，直击当前VLM领域的核心痛点（幻觉与不可解释性）。结合了Agentic RAG与多模态推理两大热门方向，在权威基准ScienceQA和MMMU上取得了显著效果，来源可信度高，对多模态RAG和评估体系的发展具有重要影响力。

## 项目链接
https://arxiv.org/abs/2606.18385
