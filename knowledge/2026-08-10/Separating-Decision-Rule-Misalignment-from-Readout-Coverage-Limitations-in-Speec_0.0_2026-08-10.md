# Separating Decision-Rule Misalignment from Readout-Coverage Limitations in Speech Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-10  
**来源：** rss  

## 项目描述
arXiv:2608.06409v1 Announce Type: new Abstract: Speech language models are increasingly evaluated on paralinguistic tasks by the accuracy of prompted answers, but answer accuracy combines failures at different stages of the audio-to-answer computation. We introduce a generation-aligned diagnostic ladder that compares the emitted answer, the option logits, an affine readout of those logits, and a linear readout of the hidden state at the same answer token. Successive differences separate endpoint, decision-rule, and readout-coverage gaps. Across five systems and two emotion corpora, state decoding exceeds generation by 27.8 accuracy points on average, and both the decision-rule and readout-coverage gaps are positive in all ten conditions. A label-free logit correction improves generated accuracy in every condition, showing that part of the decision-rule gap is actionable. In rank-matched comparisons, emotion information outside the native readout generalizes to held-out speakers and survives controls for measured acoustic descriptors, but replacing the selected readout-external directions usually has little effect on emitted answers. These results distinguish information availability from behavioral use and localize performance losses across the decision rule and the state-to-answer readout.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.06409
