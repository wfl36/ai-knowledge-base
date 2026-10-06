# CUEing User Simulators: Calibrated User Embeddings for Multi-Turn Benchmarking

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-06  
**来源：** rss  

## 项目描述
arXiv:2610.02460v1 Announce Type: new Abstract: Recent benchmarks rely on user simulators to evaluate AI agents in multi-turn interaction. While existing simulation techniques demonstrate surface fidelity to human style and behavior, ecologically valid interactive benchmarking also requires alignment in when and how agents fail across simulated and real user populations. We find that existing simulators lack outcome calibration: agreement with observed success rates and failure patterns when real users interact with the same agent. We introduce Calibrated User Embeddings (CUE), a framework that both encodes observed sessions and samples continuous representations, then decodes them into persona commands to steer LLMs to act as user simulators without training. Through this, we evaluate user-conditioned replay of past sessions and aggregate metric agreement when sampling novel personas for the same tasks. On $\tau^2$-Bench, CUEd simulators commit fewer simulator-attributed errors and more faithfully reproduce real-user agent failure modes, aggregate success rates, and outcomes for specific task-user pairs than other persona-based simulation methods. These gains coexist with competitive user fidelity as measured using metrics established in prior work. After being fit to mostly customer support interactions, the same CUEd simulators generalize to document creation, math tutoring, and casual conversation, and remain effective across different simulator LLMs without CUE retraining.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.02460
