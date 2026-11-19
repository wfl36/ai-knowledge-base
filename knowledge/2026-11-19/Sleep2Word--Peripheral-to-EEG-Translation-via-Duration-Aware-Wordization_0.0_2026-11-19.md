# Sleep2Word: Peripheral-to-EEG Translation via Duration-Aware Wordization

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-19  
**来源：** rss  

## 项目描述
arXiv:2611.21643v1 Announce Type: new Abstract: Estimating full-night electroencephalography (EEG) spectrograms from peripheral measurements could extend EEG-informed sleep analysis to recordings acquired without EEG. This task requires compact representations of signals with different temporal structures. We introduce Sleep2Word, a framework for translating respiration, electrocardiography (ECG), or photoplethysmography (PPG) into EEG spectrograms through duration-aware physiological words. Building on context-dependent chunking, Sleep2Word groups physiological embeddings into variable-duration chunks and jointly quantizes their content and duration into modality-specific wordbooks. A block-autoregressive translator then predicts target EEG word identities and occurrence-specific duration refinements within fixed-duration blocks. This design accommodates independent source and target wordbooks, limits temporal drift, and shortens the autoregressive decoding path. Trained on over 20K PSG cases across 9 datasets, Sleep2Word consistently outperforms existing spectrogram generation baselines in EEG spectrogram reconstruction, sleep staging, arousal detection, and survival prediction. Compressing full night sequences by up to 69.7%, the learned words yield a favorable accuracy-compute trade-off. Sleep event analysis further shows that the learned words capture physiologically plausible associations across modalities, suggesting their potential for interpretable cross-modal analysis.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.21643
