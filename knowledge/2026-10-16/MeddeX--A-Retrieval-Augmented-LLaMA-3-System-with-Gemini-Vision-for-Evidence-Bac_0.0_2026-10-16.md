# MeddeX: A Retrieval-Augmented LLaMA-3 System with Gemini Vision for Evidence-Backed Medical Report Analysis

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-16  
**来源：** rss  

## 项目描述
arXiv:2610.20632v1 Announce Type: new Abstract: Modern healthcare generates increasingly complex medical reports that challenge clinical professionals in terms of time and interpretive burden. Manual review processes are slow, error-prone, and difficult to scale. This paper presents MeddeX, a Medical Report Analyzer that combines a QLoRA fine-tuned LLaMA-3 (8B) model with Retrieval-Augmented Gen eration (RAG) and a multimodal Gemini Vision layer to deliver accurate, concise, and evidence-backed summaries of medical documents. The system handles text-native PDFs, scanned image based PDFs, and direct radiological images through an intelligent hybrid extraction pipeline that includes a novel garbage-text detection mechanism for corrupted and UTF-16-encoded doc uments. Beyond single-report Q&A, MeddeX introduces report scoped retrieval for precise contextual grounding, an automated longitudinal report comparison engine, and a self-healing backfill pipeline that lazily processes legacy documents on demand. A FastAPI backend, Supabase vector store, and Next.js fron tend complete the end-to-end architecture. Evaluation against the base LLaMA3-Med42-8B model demonstrates consistent improvements across ROUGE-1 (+9.2%), ROUGE-2 (+10.0%), ROUGE-L (+11.8%), BLEU (+71.4%), and BERTScore (+0.8%), validating the benefit of domain-specific fine-tuning. MeddeX represents a practical and robust step toward AI-assisted clinical decision support.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.20632
