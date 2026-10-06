# Learning When to Commit from Partial Speech for End-to-End Simultaneous Speech Translation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-06  
**来源：** rss  

## 项目描述
arXiv:2610.02612v1 Announce Type: new Abstract: Simultaneous speech translation must emit useful target text before the source is complete while preserving every committed token. We adapt a full-utterance speech language model using prefix supervision derived from its own complete- and partial-waveform translations, requiring neither transcripts nor human translations. We compare single-turn forced-prefix and multi-turn append-only decoding, use a confidence threshold to control the inference-time quality--latency trade-off, and vary the density of training prefixes with a separate synthesis margin. On FLEURS and CoVoST2 in three language directions, prefix training improves quality--latency frontiers over the unadapted model, and confidence provides the broadest consistently competitive operating range. Multi-turn decoding is generally stronger at low latency; under multi-turn training, commit-calibration error falls by 63--68% overall and 68--80% at early prefixes, whereas single-turn training provides only modest overall calibration gains and no early-prefix improvement. A small synthesis margin sometimes extends the frontier to lower latency, particularly on shorter utterances, while a larger margin degrades translation quality and calibration. Prefix adaptation therefore improves simultaneous speech translation, especially under multi-turn append-only decoding, while synthesis density introduces a non-monotonic quality--latency trade-off.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.02612
