# A Hybrid Hierarchical 1D-CNN-BiLSTM Framework for Extractive Summarization of Biomedical and Clinical Text

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-15  
**来源：** rss  

## 项目描述
arXiv:2609.13481v1 Announce Type: new Abstract: Large language models have made abstractive summarization remarkably fluent, but generated summaries can hallucinate facts, posing serious risks in biomedical and clinical domains. We address this by removing generation from the pipeline and framing summarization as extractive sentence selection. Our Hybrid Hierarchical CNN-LSTM Summarizer uses stacked multi-kernel convolutions to compose sentence-level embeddings into richer inter-sentence representations, followed by a bidirectional LSTM to model long-range dependencies across the document. A lightweight scoring head assigns per-sentence importance scores and is trained end-to-end with binary cross-entropy against oracle extractive labels. At inference, a dynamic mean-plus-standard-deviation threshold with a top-3 fallback selects sentences directly from the source and chronologically reorders them into the final summary. Since every output sentence is copied from the input, the model avoids generation-induced factual drift. On PubMed, our architecture outperforms isolated CNN and LSTM baselines, while ablations show that wider convolutional receptive fields improve sentence scoring. On MIMIC-CXR and MIMIC-IV BHC, the model performs well on unstructured narratives but defaults toward positional baselines on highly templated reports. These results suggest that structural constraints can provide a reliable path toward factually grounded summarization systems that are trustworthy by design rather than by correction.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.13481
