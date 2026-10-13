# Beyond Binary Verifiable Rewards: Behavioral Self-Rewarding for SWE Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-13  
**来源：** rss  

## 项目描述
arXiv:2610.12598v1 Announce Type: new Abstract: Reinforcement learning with verifiable rewards (RLVR) provides reliable supervision for software engineering agents through executable tests, but binary rewards fail to distinguish trajectories with substantially different debugging quality. We investigate whether the current policy can judge its own trajectories and use these judgments to improve task performance without a separately trained reward model. To this end, we introduce Behavioral Self-Rewarding (BSR), a reward-refinement method that reuses the policy to compare observable debugging behavior among trajectories from the same task with the same verifier outcome. BSR aggregates pairwise preferences into task-local scores and converts them into bounded auxiliary rewards, introducing reward contrast while preserving the verifier-defined pass/fail ordering. This provides additional supervision from already-collected trajectories without requiring new environment interactions. Experiments on SWE-bench Verified and SWE-bench-Live show consistent improvements across the evaluated Qwen3-14B and Qwen3-32B configurations, supporting using the policy's own comparative judgments as a complementary learning signal for training software engineering agents.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.12598
