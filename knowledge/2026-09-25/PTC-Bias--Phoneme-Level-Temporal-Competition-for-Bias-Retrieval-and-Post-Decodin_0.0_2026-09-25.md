# PTC-Bias: Phoneme-Level Temporal Competition for Bias Retrieval and Post-Decoding Correction in Speech LLMs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-25  
**来源：** rss  

## 项目描述
arXiv:2609.28727v1 Announce Type: new Abstract: Contextual biasing improves rare-word recognition in speech large language models (SpeechLLMs), but efficiently exploiting large bias lists remains challenging. We propose PTC-Bias, a two-stage framework based on phoneme-level temporal competition. At the prefill stage, PTC Retrieval performs frame-synchronous phoneme decoding and temporal competition among candidate pronunciations, producing a compact bias-word shortlist and corresponding speech intervals. After SpeechLLM decoding, PTC Correction conducts a second local competition between the retrieved candidates and mismatched transcript spans within these intervals. Selective correction reduces near-homophone and word-segmentation errors while preserving correct transcriptions. Both stages share the same phoneme posteriors and require no additional SpeechLLM forward pass. Experiments on LibriSpeech show consistent gains across two SpeechLLMs and bias lists of up to 2000 words. With Prompt-SLAM-ASR-7B and 2000 bias words, PTC-Bias reduces B-WER by 23.4%/23.9% relative to CTC-Filter on test-clean/test-other, while keeping U-WER nearly unchanged.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.28727
