# Environment Steering: Using Data Flow Control to Improve Agent Utility and Safety

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-30  
**来源：** rss  

## 项目描述
arXiv:2609.35807v1 Announce Type: new Abstract: LLM agents can make unsafe tool calls even when instructed to behave safely. Existing defenses constrain agents before execution, modify tool inputs/outputs, or rely on LLM judges; these approaches may depend on model behavior or block unsafe actions without helping the agent recover. We argue that the execution environment should instead enforce safety as the agent runs and steer it toward safe alternatives when violations occur---we call this Environment Steering. We implement this by modeling the agent and harness execution state as database tables, track the record-level data flows, and check these data flows against declarative policies during runtime. When violations are detected, policy- and context-specific feedback steers the agent toward safe trajectories. On AgentDyn, this enables the agent to improve task success rate over no-defense while achieving 0% attack success rate.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.35807
