# Li$^{2}$SAO: Lifting Light Singl-Rollout Asynchronous RL Optimization via Group-Relative Actor-Critic Bootstrapping

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-03  
**来源：** rss  

## 项目描述
arXiv:2610.40726v1 Announce Type: new Abstract: Asynchronous reinforcement learning (RL) is becoming a mainstream paradigm for post-training large language models (LLMs), as it improves training efficiency by updating the model as rollouts arrive. Recent work argues that group-wise sampling in GRPO does not naturally fit asynchronous RL training because rollout lengths follow a long-tailed distribution, and proposes Single-rollout Asynchronous Optimization (SAO) to improve stability and off-policy behavior, especially on agentic tasks. However, SAO relies on a closed-source value model obtained from scaling value pretraining. In this paper, we analyze GRPO and LiSAO, our lightweight reproduction of SAO without the pretrained value model, on single-turn reasoning and multi-turn agentic tasks. We find that GRPO outperforms LiSAO on reasoning tasks, while the reverse holds on agentic tasks. Since the value model of LiSAO is not yet well trained , LiSAO lags behind GRPO substantially in early training steps. To address this issue, we propose Li$^{2}$SAO, which Lifts Light Single-rollout Asynchronous Optimization with group-relative actor-critic bootstrapping: while the critic is cold, a group-relative advantage trains the actor and a group-centered return trains the critic, after which training switches to single-rollout GAE. Experiments show that Li$^{2}$SAO catches up with or surpasses GRPO in early training and further raises the later performance ceiling. Code is available at https://github.com/jd-cc-coder/Li2SAO.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.40726
