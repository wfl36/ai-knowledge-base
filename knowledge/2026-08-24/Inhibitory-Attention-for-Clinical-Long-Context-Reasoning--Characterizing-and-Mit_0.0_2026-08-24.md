# Inhibitory Attention for Clinical Long-Context Reasoning: Characterizing and Mitigating Lost-in-the-Middle Effects in EHR Processing

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-24  
**来源：** rss  

## 项目描述
arXiv:2608.20348v1 Announce Type: new Abstract: Electronic health records now routinely exceed 100,000 tokens per patient. Yet large language models exhibit the lost-in-the-middle (LitM) effect: information near the center of a long context is retrieved less reliably than information near the edges. In clinical use this is not benign: the single most consequential fact in a note can sit at its center. We term this the clinical lost-in-the-middle (CLitM) problem, give its first systematic characterization using MedAlign, and compare context-selection strategies as remedies. Across 2,196 instruction-response pairs and six language models, we observe a 21.9 percentage-point gap between peak accuracy (59.5%, 95% CI [46.3, 71.0], 20-30% decile) and trough accuracy (37.6% [23.2, 52.5] at 70-80%); 67.8% of reference answers fall between the 10th and 90th percentiles of the EHR timeline, inside the CLitM trough. We introduce Query-Conditioned Clinical Suppression (QCCS), a lightweight query-conditioned selection gate, and evaluate it against BM25, BM25 with section-header filtering, dense retrieval, and cross-encoder reranking (N=83 held-out instructions). With Qwen2.5-7B-Instruct (16k context), QCCS outperforms all five comparators under LLM-as-judge scoring: for middle-position instructions QCCS reaches 16.7% versus BM25 3.3%, cross-encoder 0.0%, dense 0.0%, and full context 6.7%; overall QCCS reaches 25.3% versus at most 3.6% for retrieval-only comparators. This advantage is not explained by retrieval recall: at k=20, BM25 retrieves the gold evidence sentence in 98.8% of instructions (QCCS 34.9%), yet retrieval arms stay at most 2.6% accurate even when they retrieve it, whereas QCCS reaches 25.0% even when it does not. In this proof-of-concept evaluation, query-aligned context selection predicts EHR instruction-following accuracy better than gold-sentence retrieval recall.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.20348
