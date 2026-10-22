# How Far Can the Gemma 4 Speech Encoder Go Without Changing Its Weights? Saudi and Gulf Arabic Speech Recognition with a Frozen and an Adapter-Augmented Encoder

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-22  
**来源：** rss  

## 项目描述
arXiv:2610.28673v1 Announce Type: new Abstract: We study the 305M-parameter audio encoder shared by Gemma 4 and EmbeddingGemma 2 (identical except for its final projection) for Saudi and Gulf Arabic speech recognition, without changing any of its weights. A frozen system trains only a 22.6M-parameter CTC reader over a mix of encoder layers; an adapted system adds 3.1M low-rank adapter parameters, a 41.5M-parameter hybrid CTC/attention reader and joint decoding with a sub-word language model. Against Cohere Transcribe Arabic (2.07B parameters), re-run on identical audio, the frozen system trails in word error rate (WER) but is statistically indistinguishable in character error rate (CER) on five of six human-labelled conditions, while running 3.4 times faster on CPU with greedy decoding. The adapted system is statistically indistinguishable in WER on a public Saudi customer-service call (19.20% against 19.27%) and on clean Emirati speech, is significantly better on telephone-coded Emirati speech, has a significantly lower CER on all six conditions of these sets, and beats a 0.6B recogniser fine-tuned on SADA in WER on all six; it still trails Cohere in WER on long-form Saudi speech. On a blind, human-corrected public call-centre sample it ranks 4 of 15 systems, behind three commercial APIs (significantly only one) and ahead of the other self-hostable systems by point estimate. An optimised joint decoder runs it at 139 times real time on one GPU. We also show that references made by correcting machine drafts favour the drafting system. Code and public-set results are released.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.28673
