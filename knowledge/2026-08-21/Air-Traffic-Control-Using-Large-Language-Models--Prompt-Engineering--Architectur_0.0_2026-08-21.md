# Air Traffic Control Using Large Language Models: Prompt Engineering, Architecture, and Evaluation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-21  
**来源：** rss  

## 项目描述
arXiv:2608.19299v1 Announce Type: new Abstract: Air traffic control (ATC) communication is a safety-critical dialogue that remains largely human-driven even as other parts of air traffic management have been semi-automated. In this article, we experimentally evaluate whether large language models (LLMs) can generate operationally realistic ATC transmissions. An experimental general-aviation flight flying over the San Francisco "Bay Tour" route is hand-transcribed and used as ground truth (P0). Through a pilot-in-the-loop process we design five prompt structures (P1-P5) of increasing constraint and embed them in a stateful multi-turn pipeline, where the model plays ATC to a fixed pilot transcript while conditioning on the accumulating dialogue history. Across nine open- and closed-source LLMs we vary the prompt, the presence of a worked transcript from a different experimental flight as an in-context example, and whether the model conditions on its own prior replies or on injected ground-truth history. Turns are scored with lexical, structural, and semantic similarity metrics and by an LLM-as-judge (GPT-5.5) validated against human expert annotation. Supplying a worked example improves similarity, but tightening the prompt does not: the lightest prompts perform best and the most heavily scripted one collapses as its own errors accumulate through the dialogue, which injecting correct history repairs. These results outline a concrete path and its current limits toward LLM-assisted ATC.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.19299
