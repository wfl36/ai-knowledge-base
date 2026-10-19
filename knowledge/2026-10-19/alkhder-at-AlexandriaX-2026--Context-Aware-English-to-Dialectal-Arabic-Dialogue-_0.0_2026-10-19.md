# alkhder at AlexandriaX-2026: Context-Aware English-to-Dialectal Arabic Dialogue Translation with QLoRA-Fine-Tuned NileChat-3B

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-19  
**来源：** rss  

## 项目描述
arXiv:2610.22525v1 Announce Type: new Abstract: This paper describes team Alkhder's submission to Subtask 1 of the AlexandriaX-2026 shared task, which asks systems to translate English dialogue turns into thirteen Arabic dialects. We fine-tune NileChat-3B-Base with QLoRA on the Alexandria parallel dialogue corpus, training one set of adapter weights for all dialects. Each turn is translated conditioned on the target country and dialect, the domain, the participant roles, the speaker-addressee gender direction, and the preceding dialogue context. At inference, conversations are translated autoregressively and the model is fed its own previous outputs back as context without using any gold target-side test information. Under the constrained track, using only Alexandria data, it trains in about one hour and translates the private test set in under two hours. The system reaches a country-macro-averaged spBLEU of 20.36 and chrF++ of 36.64 on both tracks.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.22525
