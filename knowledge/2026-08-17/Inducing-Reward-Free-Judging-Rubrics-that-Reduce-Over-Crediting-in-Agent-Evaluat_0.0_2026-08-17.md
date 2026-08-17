# Inducing Reward-Free Judging Rubrics that Reduce Over-Crediting in Agent Evaluation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-17  
**来源：** rss  

## 项目描述
arXiv:2608.13564v1 Announce Type: new Abstract: Evaluating language-model agents at scale increasingly relies on a second language model as an automatic judge, because the gold signal, an executable environment reward, is expensive, slow, or unavailable at deployment time. Such a judge is a reward-free proxy whose value depends on whether it can be trusted, yet existing judges either hand-write the scoring rubric, as in G-Eval, or fine-tune the judge's weights, and both tend to credit fluent but unsuccessful trajectories as successes. We instead induce the text of an agent-judging rubric from a small set of ground-truth-labeled trajectories, grounding it in true outcomes. We present RubricForge, which evolves a judge rubric by reflective evolution against labeled trajectories to maximize agreement with the environment reward, freezes it, and applies it to held-out trajectories in one model call with no environment access. The optimized artifact is human-readable text, so every verdict is attributable to named criteria. Using one frozen 7B model as both agent and judge, on tau-bench (173 labeled trajectories drawn from 220 rollouts) and WebShop (160), the principal gain is faithfulness rather than raw agreement. The edge over a generic G-Eval judge is not statistically significant (McNemar p = 0.248), and absolute-score calibration marginally favors the generic judge (|err| difference -0.048, p = 2x10^-4). Yet RubricForge over-credits failed trajectories roughly half as often (0.115 vs. 0.173 false-pass rate on tau-bench, with three over-credit catches and zero reversals) and ranks graded WebShop outcomes more faithfully (Spearman 0.410 vs. 0.370). For a reward-free evaluator the false-pass rate, not aggregate agreement, is the deployment-relevant quantity, since a false pass ships a broken agent whereas a false fail merely costs a retry.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.13564
