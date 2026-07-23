# FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, LLM Serving, 系统优化, 数据集, 工作负载, 论文, 工程实践  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19349v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly deployed as always-on online services, making efficient LLM serving a critical systems challenge. Achieving low latency and high throughput under volatile demand requires deep understanding of real-world serving workloads, yet existing studies often rely on proxy traces or coarse-grained characterizations that fail to capture the heterogeneity of modern multi-model LLM platforms. We present FineServe, an in-the-wild, multi-model LLM serving workload dataset collected from a global commercial marketplace, enabling fine-grained characterization of real-world serving dynamics across heterogeneous models and tasks. Leveraging FineServe, we conduct a comprehensive analysis of arrival dynamics and token behavior, revealing fundamentally different fluctuation regimes across model architectures, scales and task intents. Building on these insights, we develop the FineServe workload generator, which composes fine-grained model-aware workloads into configurable mixtures tailored for benchmarking multi-model serving platforms. By exposing these fine-grained workload dynamics, FineServe provides a realistic foundation for evaluating routing, scheduling, and capacity-planning strategies in LLM serving systems. FineServe is available at https://github.com/hihiztc1/FineServe.

## 综合总结
本文提出了FineServe，一个来自全球商业市场的多模型LLM服务工作负载细粒度数据集，旨在解决现有研究依赖代理数据或粗粒度特征而无法捕捉多模型平台异构性的问题。基于该数据集，作者深入分析了请求到达动态和token行为，揭示了不同模型架构、规模与任务意图间差异显著的波动机制。此外，作者开发了FineServe工作负载生成器，支持为多模型服务平台构建可配置的混合工作负载以进行基准测试。该工作为LLM服务系统中的路由、调度和容量规划策略提供了真实的评估基础，并已完全开源。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文填补了真实世界多模型LLM服务工作负载细粒度数据集的空白。不同于以往依赖代理追踪或粗粒度分析的研究，本文基于全球商业市场真实数据，深入剖析了请求到达动态和token行为，揭示了不同模型架构、规模和任务意图下截然不同的波动机制，研究方法严谨，分析维度具有深度和新颖性。

### 实用性 (评分: 9.0/10)
对LLM系统研发和运维人员具有极高的实践指导价值。论文不仅开源了细粒度数据集，还提供了FineServe工作负载生成器，能够直接用于多模型服务平台的基准测试、路由调度算法优化以及容量规划，落地路径清晰且适用范围广泛。

### 社区活跃度 (评分: 8.5/10)
LLM Serving是当前大模型产业落地的核心痛点，该研究话题时效性极强。数据源自全球商业市场，真实性与权威性高；且论文配套开源了数据集与工具，能够有效吸引系统与基础设施领域的关注，具备较好的社区影响力和参考信誉。

## 项目链接
https://arxiv.org/abs/2607.19349
