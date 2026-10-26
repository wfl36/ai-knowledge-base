# Don't Forget What You Just Learned: Self-Directed Repair Turns Agent Mistakes Into Lasting Lessons

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-26  
**来源：** rss  

## 项目描述
arXiv:2610.31846v1 Announce Type: new Abstract: Intelligent agents should learn from their mistakes so that experience leads to continuous improvement. Yet today's agents recover from a mistake only temporarily: in-context reflections are easily forgotten across sessions and compete for limited context, while full-parameter fine-tuning is expensive and can interfere with existing capabilities. We introduce Self-Direction, a mechanism for agents to learn from mistakes that combines the benefits of temporary in-context retries and policy updates. When an agent fails a task, it reflects on its own trajectory in order to extract a lesson and immediately distills it into a lightweight low-rank adapter. By keeping the original weights frozen, Self-Direction prevents adapter training from overwriting base-model parameters while training additional parameters equivalent to ~0.02% of the base model's parameter count for each adapter. The agent then saves these adapters in a persistent library of lessons, automatically routing them to solve related problems later. Experiments with agents based on open-weight models from the Qwen family across open-ended research (GAIA), tool-use workflows (Claw-Eval), and terminal tasks (Terminal-Bench 2.1) show that our method improves overall success rates by 8.9 to 17.0 percentage points and performs competitively with frontier systems. We find that Self-Direction reduces repeated mistakes across future encounters of a task, nearly doubling the reliability of an agent's corrections. Learned lessons also transfer: a handful of adapters generalize to dozens of new tasks without additional training. Ultimately, this self-directed repair transforms everyday mistakes into lasting lessons.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.31846
