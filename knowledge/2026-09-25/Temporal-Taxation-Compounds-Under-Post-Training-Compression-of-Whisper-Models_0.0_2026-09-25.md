# Temporal Taxation Compounds Under Post-Training Compression of Whisper Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-25  
**来源：** rss  

## 项目描述
arXiv:2609.28739v1 Announce Type: new Abstract: Automatic speech recognition models are audited for demographic fairness at full precision, yet the models that ship to production have been quantized, pruned, and distilled. We ask whether post-training weight compression, which alters model weights rather than the audio signal or its feature representation, redistributes error burden across demographic groups. Across the Whisper family on Fair-Speech, Common Voice 25, and AfriSpeech-200, 50% Wanda pruning of Whisper-large-v3 sharply widens the Black/AA-vs-Asian temporal-taxation differential on Fair-Speech: the absolute word-error-rate gap between the worst- and best-served groups more than doubles; at an assumed cost of five seconds of correction effort per transcription error this is a rise from 30 to 64 seconds of correction time per minute of speech. This +111% relative increase is invariant to the assumed per-error cost, survives an audio-quality control, and is only partly mitigated by beam-search decoding, which still leaves an +86% increase. At edge model size, INT4 HQQ quantization compounds catastrophic transcript loops on West African accents by factors of five to seven. Distillation, by contrast, narrows demographic gaps in 21 of 27 evaluated settings (teacher-student pair, precision, and dataset), with the exceptions concentrated on a single model pair. We cast the temporal-taxation construct of Choi and Choi (2025) as a quantitative metric, and show that single-snapshot fairness audits on full-precision models do not capture the deployment-time burden that compression places on already-marginalized speakers.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.28739
