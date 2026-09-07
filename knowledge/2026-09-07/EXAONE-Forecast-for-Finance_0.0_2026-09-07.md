# EXAONE Forecast for Finance

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-07  
**来源：** rss  

## 项目描述
arXiv:2609.04239v1 Announce Type: new Abstract: This technical report presents EXAONE Forecast for Finance (EXAONE Finance), a financial time series (TS) foundation model (TSFM) tailored to financial forecasting. Recent TSFMs achieve strong zero-shot performance through large-scale pretraining. However, they are primarily developed for general-domain TS and largely rely on self-attention backbones whose computational cost grows quadratically with sequence length and variate count. Moreover, they assume fully observed inputs and are pretrained on corpora that fail to capture the unique dynamics of financial markets. These limitations hinder their applicability to finance, where long, many-channel, intermittently observed panels are common. To address these challenges, EXAONE Finance adopts an attention-free architecture, replacing self-attention with two simple yet effective linear-time operators: 1) a causal 1D convolution for temporal mixing and 2) a group-aware pooling multi-layer perceptron (MLP) for variate mixing. Furthermore, a masked context augmentation exposes the model to contiguous missing spans during training, improving robustness to the missingness pervasive in financial markets. EXAONE Finance is pretrained on a large-scale financial corpus covering not only equities but also foreign exchange, commodities, crypto-assets, fixed income, and macroeconomic indicators. On FinVerse, a financial forecasting benchmark covering diverse asset classes, EXAONE Finance attains state-of-the-art performance, ranking first across all three evaluation tiers---point-forecast accuracy, cross-sectional asset ranking, and portfolio profitability.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.04239
