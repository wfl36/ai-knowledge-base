# TimeOmni-o1: Bidirectionally Coupling Time Series Foundation Models and LLMs for Multimodal Reasoning and Forecasting

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-12  
**来源：** rss  

## 项目描述
arXiv:2611.12902v1 Announce Type: new Abstract: Time series from real-world systems are often accompanied by text, such as a report on an event that affects them. Two common tasks on these series are understanding, e.g., answering questions about a series, and forecasting its future values. Both tasks require reasoning over the series and the text together. Moreover, understanding outputs text while forecasting outputs a time series, so serving both requires a model that reads and generates both modalities. Large language models (LLMs) read time series as digit tokens and handle long series poorly. Time series foundation models (TSFMs) forecast well from large-scale pretraining but typically neither read nor generate text. Time series language models add a time series modality to the LLM but forecast on the LLM side, leaving the TSFM's pretrained forecasting ability unused. We present TimeOmni-o1, which couples a pretrained TSFM and an LLM bidirectionally. In one direction, the TSFM encodes the series in compressed form for the LLM, which reasons over it together with the text. In the other, the LLM's reasoning is fed back into the TSFM, which produces the forecast conditioned on it. One model architecture thus reads and generates both series and text, reasons in text, and draws on the TSFM's pretrained forecasting ability. To train it, we build MMTR, a multimodal time series reasoning dataset with annotated reasoning traces, covering both tasks across 12 domains with 500k+ samples. On MMTR, TimeOmni-o1 outperforms existing models on both understanding and forecasting across most domains, as well as the LLM and the TSFM inside it when used individually. The gains carry over to three open benchmarks, where it outperforms the dedicated time series models.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.12902
