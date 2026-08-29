# Can a Model Catch Its Own Hallucinations for Free?: Label-Free Doubt Signals Hold Their Own Against a Labelled Dataset for Abstention

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-29  
**来源：** rss  

## 项目描述
arXiv:2608.26121v1 Announce Type: new Abstract: Large language models state false facts as fluently as true ones, yet a model often "knows" internally when it is on shaky ground: the probability it assigns to its own answer tends to dip on the facts it gets wrong. The usual way to act on this, teaching a model to abstain rather than guess, requires a labelled dataset of right and wrong answers. We ask whether the model's own confidence, which is free and needs no labels, can do that job instead. We fine-tune each model (with LoRA) to answer when its frozen confidence is high and to say "I'm not sure" when it is low, using the signal alone and no correctness labels. Across six open-weights models (1B-8B, two families) on short-form factual question answering, with correctness adjudicated by an independent judge model, this label-free recipe holds its own against label-supervised abstention-tuning: at matched coverage we find no statistically detectable difference between the two. A control that drills hard examples instead of abstaining does not help, indicating the gain comes from calibration, not rote memorization. The signal's one blind spot is confidently wrong facts, which it cannot flag. A model's own doubt is thus a near-free substitute for a labelled dataset when teaching it when to abstain. Code and artifacts are available on request.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.26121
