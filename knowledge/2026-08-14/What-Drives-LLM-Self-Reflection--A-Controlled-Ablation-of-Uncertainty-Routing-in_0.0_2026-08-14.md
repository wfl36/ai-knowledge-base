# What Drives LLM Self-Reflection? A Controlled Ablation of Uncertainty Routing in Armed Conflict Forecasting

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-14  
**来源：** rss  

## 项目描述
arXiv:2608.12322v1 Announce Type: new Abstract: Self-reflection is widely assumed to improve LLM reasoning, yet which component drives the gain remains poorly understood. We present a controlled six-condition ablation isolating four components of LLM self-reflection: evidence exposure, diagnostic scaffolding, taxonomy vocabulary, and action routing. Two precise null results converge on a single mechanism. First, structured diagnostic questions add no measurable value over unstructured reflection ($\text{F1} = 0.296$ vs $0.297$, $p = 1.000$, 95\% CI $[-0.041, +0.040]$). Second, presenting the full uncertainty taxonomy while collapsing the action space to a single generic action also adds no value ($\Delta\text{F1} = +0.008$, overlapping 95\% CIs), ruling out taxonomy vocabulary as the mechanism. Typed action routing provides consistent directional gains ($\text{F1} = 0.379$ vs $0.296$); the conservative estimate controlling for taxonomy vocabulary is $\Delta\text{F1} = +0.075$, and the overall gain over the single-shot baseline is significant by bootstrap CI ($\Delta\text{F1} = +0.101$, 95\% CI $[+0.020, +0.185]$). The vocabulary-routing decomposition replicates on GPT-4o: taxonomy vocabulary adds no significant value over generic reflection ($p = 0.773$), while action routing provides significant gains ($p = 0.025$), confirming the mechanism holds across backbones. Gains concentrate on structurally novel conflicts: in Myanmar ($\text{F1}: 0.000 \rightarrow 0.353$) and Ukraine ($0.167 \rightarrow 0.500$), the vocabulary-only condition recovers no more than generic reflection while action routing breaks the degenerate prior. These findings identify typed action routing -- not diagnostic scaffolding or taxonomy vocabulary -- as a promising design principle for metacognitive LLM forecasting agents, while motivating larger-scale evaluation across conflict typologies.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.12322
