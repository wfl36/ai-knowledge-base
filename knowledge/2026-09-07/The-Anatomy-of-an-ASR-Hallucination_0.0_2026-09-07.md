# The Anatomy of an ASR Hallucination

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-07  
**来源：** rss  

## 项目描述
arXiv:2609.04404v1 Announce Type: new Abstract: ASR systems sometimes produce fluent text that is unrelated to the speech they receive. We view these hallucinations as one possible consequence of a broader grounding failure, in which the transcript is no longer adequately guided by the audio. To understand where this failure becomes possible, we study two independently trained Conformer-Large recognizers - one CTC and one RNN-T - under environmental degradation and speaker-background shift. In both models, the final encoder stage emerges as a critical boundary: bypassing the final block causes divergence on nearly every utterance, whereas bypassing middle blocks has little effect. At this same stage, the representations become more compact, text becomes readable by the trained decoder, and grapheme information becomes explicit. Importantly, the intervention produces garbled or repetitive output rather than fluent fabrication. Our result therefore identifies a mechanistic precondition for hallucination - the failure to produce adequately grounded output - not the complete origin of naturally occurring hallucinations. Together, the results reveal a consistent terminal-stage dependency for grounded recognition across two decoder families and multiple distribution shifts.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.04404
