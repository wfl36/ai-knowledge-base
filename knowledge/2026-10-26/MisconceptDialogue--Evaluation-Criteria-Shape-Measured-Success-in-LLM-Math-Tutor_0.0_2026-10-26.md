# MisconceptDialogue: Evaluation Criteria Shape Measured Success in LLM Math Tutoring

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-26  
**来源：** rss  

## 项目描述
arXiv:2610.31679v1 Announce Type: new Abstract: Large language models are increasingly used as math tutors, raising two questions: can a single LLM detect a student's error, diagnose the underlying misconception, and remediate it through multi-turn dialogue - and can we trust the numbers that report how well it does? We address both with MISCONCEPTDIALOGUE, a fully automated framework that runs the full pipeline on five open-weight LLM tutors (7B-14B) interacting with LLM-simulated students over 5,000+ dialogues - a deliberately simulated protocol (paired conditions, a wrong-diagnosis control unsafe with real learners, scale) whose results do not establish real-student learning. On measurement, our headline finding is uncomfortable for the field: benchmark-style exact-match scoring common in standard math NLP - a lower-bound stress test - reports 42.1% measured Remediation Success Rate on identical dialogues where a human-calibrated LLM-as-judge reports 81.3%, a 39.2 percentage-point spread larger than the combined effects of tutor model, teaching strategy, and supplied diagnostic information. This is not a single-judge artifact: four independent LLM judges and 200 human annotations converge to within a few points (kappa up to 0.91). On capability, the verdict is equally striking: the score barely changes whether we tell the tutor the student's actual misconception or a deliberately swapped one - under the tested diagnosis-presentation format, these tutors show little evidence of reliably conditioning on the diagnostic information they are handed. For LLM tutoring evaluation to mature, multi-criterion scoring with multi-judge convergence and human anchoring should become standard practice - and the measurement question deserves as much scrutiny as the capability question it claims to answer.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.31679
