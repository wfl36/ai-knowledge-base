# Steering Instruction Hierarchies at Inference Time

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-30  
**来源：** rss  

## 项目描述
arXiv:2607.26228v1 Announce Type: new Abstract: Instruction hierarchies are a core safety assumption of language model deployment: higher priority inputs, such as system prompts, should override conflicting lower priority inputs from users or tools. Yet frontier LLMs often violate this hierarchy. We introduce V-Steer, a training-free inference time method that restores privileged influence by editing cached value vectors at prompt positions. Using direct logit attribution on the first next token prediction, V-Steer identifies heads where lower priority spans dominate privileged ones, then boosts privileged spans and suppresses conflicting lower priority spans through in-place multiplicative edits to cached V tensors. Since the method acts only on cached values, it remains compatible with fused attention backends and adds only a one time prefill overhead. Across models from 7B to 70B, this attribution guided intervention raises primary constraint accuracy from under 18% up to 92% on controlled role conflict benchmarks, and on broader instruction hierarchy evaluations substantially outperforms prompt only baselines while matching or exceeding SoTA training based methods on 3 of 4 scales of LLMs, with negligible decoding-speed overhead. The code is available at https://github.com/cindy2000sh/v-steer.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.26228
