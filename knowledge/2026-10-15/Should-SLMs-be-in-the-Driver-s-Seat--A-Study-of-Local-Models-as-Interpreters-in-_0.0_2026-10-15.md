# Should SLMs be in the Driver's Seat? A Study of Local Models as Interpreters in Cloud-Written Agent Programs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-15  
**来源：** rss  

## 项目描述
arXiv:2610.14209v1 Announce Type: new Abstract: The most accurate agents executing user-provided tasks are driven by large, cloud-hosted models, which solve them by reading the private data of the user. Agents powered by models small enough to run on edge devices keep that data local, but yield far worse results. A third option is to have cloud models write a program that devices execute: the data stays local, but as the program is written before any data is seen, it fails whenever a step depends on interpreting content that appears only at run time. We explore an intermediate architecture, in which the cloud-written program defers bounded questions over user data to a small local model through an ordinary function call. On AppWorld this improves the success rate of a code-only agent in all six combinations of backbone model and test partition we evaluate, by up to 14.9pp, recovering a substantial part of the gap to a cloud-hosted ReAct loop while keeping user data on the device.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.14209
