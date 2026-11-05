# A Feasibility Condition for Confidence-Gated Tiered LLM Inference

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-05  
**来源：** rss  

## 项目描述
arXiv:2611.05394v1 Announce Type: new Abstract: Tiered inference distributes large language model computation across a hierarchy of devices, from on-device and edge hardware to the datacenter, and is increasingly offered as the route to cheaper, lower-latency, and more private serving. Most such systems orchestrate frozen model checkpoints, and most decide what to resolve locally and what to escalate using a confidence signal produced by a forward-deployed model. We give a closed-form condition for when no threshold on that signal makes a tiered cascade worthwhile relative to sending every query to the backstop. Modeling the routing decision as a binary test and separating local from escalation cost through an architecture cost ratio $\kappa$, we derive a feasibility condition bracketed by a signal-free floor, below which a cascade is feasible at any signal quality, and a perfect-signal ceiling, above which none is. Read along the $\kappa$ axis the condition inverts: where local compute is billed, cost binds, matching a recent empirical finding; where it is sunk, on decentralized hardware, feasibility becomes unconditional and signal quality instead sets what the cascade achieves. We turn the condition into three design requirements that existing trained-in primitives satisfy only in isolation, and we propose, as future work, a co-designed architecture and a protocol to test it. The condition and the inversion hold independently of that architecture; they are the paper's contribution.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.05394
