# Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-28  
**来源：** rss  

## 项目描述
arXiv:2611.33402v1 Announce Type: new Abstract: AI models vary enormously in capability and price. Model routing exploits this by sending easier tasks to cheaper models. However, a single agentic task often combines easy and difficult subtasks, making one model choice for the entire task inefficient. We introduce partial routing, which guides a frontier lead model to delegate suitable subtasks to a cheaper worker model. From both models' past runs, we identify recurring subtasks and measure each model's quality and cost on them. These measurements produce delegation guidance, with a parameter, $\delta$, controlling how much is delegated. The lead decides when and what to delegate during execution, without training either model. On held-out tasks from ViBench and Terminal-Bench 4.0, partial routing achieves higher mean task performance than the lead alone and task-level routing. With $\delta = 0.75$, it raises the lead's ViBench score from 70.2 to 78.5 at 19% lower cost, and its Terminal-Bench pass rate from 54% to 61% at similar cost. Giving the lead only the subtask breakdown, without a worker, also reduces cost on both benchmarks and raises the Terminal-Bench pass rate. These results show that analysis of past runs can support more efficient planning and more effective delegation, with little cost and implementation overhead.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.33402
