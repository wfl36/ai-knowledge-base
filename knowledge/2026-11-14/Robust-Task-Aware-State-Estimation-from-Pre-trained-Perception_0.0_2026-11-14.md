# Robust Task-Aware State Estimation from Pre-trained Perception

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-14  
**来源：** rss  

## 项目描述
arXiv:2611.14781v1 Announce Type: new Abstract: Agents that perform state estimation using pretrained perception models, e.g., Vision-Language Models (VLMs), face the fundamental challenge that predictions are uncertain. Still, most approaches determinize these predictions into a single best-guess state and make decisions as if it were ground truth. This is brittle because when the guess is wrong, the agent's decisions may be unsafe or infeasible. At the other extreme, maintaining a full probability distribution over symbolic states is often intractable. We propose a middle path, drawing on the underlying probabilities the perception model already produces (e.g., a VLM's output-layer token distributions) to construct a $\theta$-confidence Minimal Belief Set (MBS$_\theta$), a minimal subset of states whose cumulative probability meets a user-specified belief-mass threshold. The minimality of an MBS$_\theta$ ensures that the agent considers only the most likely states, enhancing robustness in downstream decision-making while maintaining computational tractability. Using a novel three-layered belief system, we efficiently approximate individual state probabilities from per-feature predictions and task-level constraints. On this belief construction, we base our MBS$_\theta$ construction, while maintaining only a lean factored representation of the belief. Our algorithm, Probability-Ranked Valid State Search (PRaVaSS), takes advantage of the unique structure of this belief system to construct an MBS$_\theta$ with correctness guarantees and polynomial complexity in the unconstrained case. Using a VLM as the backbone of our state estimator, we validate our method's theoretical properties, scalability with problem size, and improvement of downstream decision-making when used in a task-planning pipeline.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.14781
