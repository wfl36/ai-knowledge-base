# RECAP: Training Long-horizon LLM Agents with Context Compaction

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-26  
**来源：** rss  

## 项目描述
arXiv:2611.31258v1 Announce Type: new Abstract: Context compaction enables large language model agents to tackle long-horizon tasks within limited context budgets by replacing interaction histories with compressed summaries. However, learning effective compaction jointly with the agent policy remains challenging, as summaries affect task success over many subsequent interactions. We introduce RECAP, a reinforcement learning (RL) framework based on the principle that a summary should preserve the behavior induced by the original interaction history. We formalize this principle with a behavior distortion objective that measures the divergence between the agent's subsequent behavior under compressed and original contexts. We show that the gradient of the distortion objective decomposes into two complementary learning signals: distortion-based reward for summary generation and self-distillation for subsequent actions. Experiments on Qwen3.5-4B show that RECAP consistently outperforms the task-reward-only RL baselines on both environments, leading to an absolute improvement of 4.6% and 4.3% on BrowseComp-plus and SWE-bench Verified, respectively. Ablations further highlight the value of jointly supervising summary generation and post-compaction behavior for RECAP.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.31258
