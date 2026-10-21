# MedPAO-Assist: Edge-Deployable, Modality-Aware Agentic AI for Radiology Report Structuring

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-21  
**来源：** rss  

## 项目描述
arXiv:2610.26913v1 Announce Type: new Abstract: The adoption of Large Language Models for radiology report structuring has been largely dominated by either proprietary cloud-based models or large open models requiring high-end GPUs for deployment, which is a critical bottleneck for clinical adoption in radiology workflows that demand data privacy and offline operation. To address this, we present MedPAO-Assist, an edge-deployable agentic framework that generates structured radiology reports directly from radiologist dictation and voice commands, requiring only $\approx3.3$ GB peak RAM and achieving an average end-to-end latency of $\approx31$ seconds on a standard laptop CPU through an asynchronous, multi-threaded execution pipeline. The system currently supports four major imaging modalities -- Chest X-ray, Chest CT, Abdomen CT, and Brain MRI. To our knowledge, it is among the earliest agentic systems to run its entire pipeline with a Small Language Model (SLM) in the 0.6B-parameter range. This multi-agent architecture, built around an Extract-Ground-Generate paradigm, performs concept extraction, SNOMED-CT grounding, and structured report generation, followed by a speech-driven human-in-the-loop correction phase, together forming a fully "no-touch" reporting workflow that requires no keyboard input, external API calls, or internet connectivity. We evaluate each pipeline stage individually -- concept extraction, ontology grounding, and concept categorization and report hardware profiling results demonstrating the system's feasibility for real-time, CPU-only clinical deployment.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.26913
