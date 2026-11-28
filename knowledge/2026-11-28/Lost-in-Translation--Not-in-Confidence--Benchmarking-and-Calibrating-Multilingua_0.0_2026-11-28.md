# Lost in Translation, Not in Confidence: Benchmarking and Calibrating Multilingual Decision Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-28  
**来源：** rss  

## 项目描述
arXiv:2611.33307v1 Announce Type: new Abstract: Decision models are language models fine-tuned to return a probability for each option of a typed query, which routers and guardrails threshold directly. They are built on multilingual bases but ranked almost entirely in English. We evaluate 25 top-ranked open-weight decision models on 17 tasks in 14 languages, comparing each language with English on parallel items. Every model loses accuracy in every language, from about 2 points in high-resource languages to 8 in Tamil, while confidence falls only half as much: a threshold set for 95\% accuracy in English yields 90% in Tamil. The size of the loss is set by the language and the base model rather than by leaderboard rank. In 81 controlled fine-tuning runs, task skill learned in English transfers to other languages and a few thousand target-language items narrow large losses, but neither more data nor full-parameter tuning closes them. Finally, the same test items are answered more accurately in all 23 benchmark--language pairs we compare when an LLM rather than a person translated them, so LLM-translated test sets understate the gap.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.33307
