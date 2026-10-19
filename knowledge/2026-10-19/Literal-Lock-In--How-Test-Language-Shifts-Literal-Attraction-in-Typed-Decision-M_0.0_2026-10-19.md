# Literal Lock-In: How Test Language Shifts Literal Attraction in Typed Decision Models on Bengali Idioms

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-19  
**来源：** rss  

## 项目描述
arXiv:2610.22526v1 Announce Type: new Abstract: Decision models, non-generative scorers that report a probability over caller-supplied options and emit no text, are increasingly deployed as routers, classifiers and guardrails. Because they generate nothing, rationales and chain-of-thought do not apply. We audit three: an encoder scorer, a decoder scorer and a closed API, entirely through interventions on their input, using expert-annotated Bengali idioms carrying a gold figurative and a gold literal gloss. Dropping an idiom's own literal gloss into the option list draws every arm toward it, taking 65% to 96% of each arm's remaining Bengali errors. A model-by-language matrix over one shared item set shows how far this depends on the test language: every arm is 1.9 to 6.4 times more captured in Bengali than in English on the same paired entries, the commercial model's apparent resistance is a property of its test language, and capability does not order the failure. Calibration degrades in all three arms, and on the open arms confidence inverts, so gating on it is worse than gating at random. On a semantics-free option list, where accuracy is at chance, the best-calibrated arm still reports mean confidence 0.82. Code and data: https://github.com/sakhadib/literal-lock-in.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.22526
