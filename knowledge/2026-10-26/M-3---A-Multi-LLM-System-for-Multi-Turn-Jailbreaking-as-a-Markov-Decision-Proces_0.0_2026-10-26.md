# $M^3$: A Multi-LLM System for Multi-Turn Jailbreaking as a Markov Decision Process

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-26  
**来源：** rss  

## 项目描述
arXiv:2610.31937v1 Announce Type: new Abstract: Modern Large Language Models (LLMs) remain vulnerable to carefully orchestrated multi-turn interactions that progressively bypass safety mechanisms. However, many existing red-teaming approaches rely on heuristics or impose strong assumptions that limit their applicability in fully black box settings. We address this gap by introducing $M^3$, an automated red-teaming framework that formalizes multi-turn jailbreaking as a finite-horizon Markov Decision Process (MDP). In $M^3$, an attacker LLM interacts with a target LLM while operating over a compact internal state produced by a state LLM. Across two benchmarks and six target models, $M^3$ consistently outperforms state-of-the-art multi-turn red-teaming methods in Attack Success Rates (ASR), achieving improvements of up to 53% in ASR@5. Even with lightweight attacker, $M^3$ attains gains up to 26% in ASR@1 and 34% in ASR@5, compared to baselines that use higher capacity attackers. Beyond improved effectiveness, $M^3$ exhibits steeper risk escalation over conversational turns and achieves more consistent performance across risk categories (up to 4.82 improvement in Gini index) without relying on predefined risk taxonomy, providing a scalable and principled framework for multi-turn red-teaming and safety evaluation.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.31937
