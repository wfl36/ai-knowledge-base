# Beyond the Sycophancy Score: How Task, Model, and Pressure Shape LLM Yielding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-08  
**来源：** rss  

## 项目描述
arXiv:2610.08840v1 Announce Type: new Abstract: Large language models (LLMs) often abandon a correct answer, or endorse a user's position, once the user pushes back. This behavior, called sycophancy, is usually reported as a single rate per model, which says little about when it happens or how a user can avoid it. We study the conditions that produce it with 103,939 graded replies from ten configurations: eight LLMs with reasoning disabled, and two of them again with maximum reasoning, all facing the same 200 items, 13 pressure conditions, and four-turn conversations, with every reply labeled by two independent LLM judges. We find that the dominant factors are how costly it is for the model to verify the user's claim, and whether a trained guardrail covers it. Removing this task factor from a logistic model costs 0.485 of McFadden $R^2$, against 0.139 for model family and 0.009 for pressure tactic. Anchored facts are almost never conceded (1.3%), while adoption on logic puzzles rises with the number of clues needed to refute the pushed answer. Personal choices are endorsed in 77.0% of conversations. Most concessions on hard items come from models that cannot reliably solve them; models that can solve them rarely give the answer up. For both models tested, maximum reasoning removes these concessions completely: adoption on deep puzzles falls from 19.2% and 12.5% to 0%. Fallacious or emotional framing adds nothing beyond plain repetition. Three human annotators agree with the judges' consensus on 118/120 calibration items. These results give practical rules for reliable use: simplify hard-to-verify problems and reason deeply, state the question rather than one's preferred answer, ask for evidence on open questions, and choose models by their measured guardrail profile.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.08840
