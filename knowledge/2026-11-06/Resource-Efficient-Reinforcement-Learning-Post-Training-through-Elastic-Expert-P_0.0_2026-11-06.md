# Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-06  
**来源：** rss  

## 项目描述
arXiv:2611.06984v1 Announce Type: new Abstract: Reinforcement learning post-training improves the capabilities of large language models, but generating training responses is a major computational bottleneck. In mixture-of-experts models, workers that finish their assigned responses may remain occupied because their experts are still needed by workers processing longer responses. Consequently, approximately one-third of occupied worker time in the baseline occurs after local response generation finishes. Here we present FlexFloor, a system that enables earlier resource release during synchronous response generation while preserving the expert computation required by ongoing responses. FlexFloor jointly adapts response scheduling and the active group of workers. It uses historical response lengths and memory constraints to guide batching and prompt placement, then progressively releases workers while maintaining expert availability and correct communication. Compared with the verl baseline, FlexFloor generates approximately 65.40% more response tokens per unit of occupied computing time and increases response generation throughput by 52.74%, with little observed variation in rollout reward. By making reinforcement learning post-training more efficient, FlexFloor supports faster development and iterative improvement of large language models and AI agents.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.06984
