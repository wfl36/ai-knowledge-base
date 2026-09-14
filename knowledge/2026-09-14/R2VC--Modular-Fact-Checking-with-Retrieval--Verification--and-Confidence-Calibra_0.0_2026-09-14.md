# R2VC: Modular Fact-Checking with Retrieval, Verification, and Confidence Calibration

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-14  
**来源：** rss  

## 项目描述
arXiv:2609.11955v1 Announce Type: new Abstract: Large language models are increasingly used for automated fact checking, but end-to-end prompting often entangles evidence retrieval, reasoning, and uncertainty estimation, making failures difficult to diagnose and confidence difficult to trust. We present R2VC, a modular retrieve, reason, verify, calibrate architecture for evidence-grounded fact checking with citations and abstention. R2VC combines hybrid sparse+dense retrieval over Wikipedia, a supervised fine-tuned and DPO-aligned generator that produces diverse structured verdict candidates, an external NLI cross-encoder for evidence-based candidate selection, and a lightweight sequence-level calibrator for confidence estimation and selective abstention. On FEVER, an 8B backbone with R2VC achieves 13.74% higher accuracy than baseline. Ablation studies show that verifier-based candidate selection and confidence calibration are the largest contributors to performance. Removing candidate selection drops FEVER accuracy to 76.24%, while removing calibration nearly doubles the Brier score to 0.161. A manual analysis of 250 errors further shows that retrieval failures, especially wrong-entity evidence, remain the dominant bottleneck. Together, these results show that modular fact-checking pipelines can substantially improve both predictive accuracy and confidence reliability in open-domain verification.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.11955
