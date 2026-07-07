# Automated Data Readiness for Scientific AI

**评分：** 8.8  
**状态：** 正常  
**标签：** AI4Science, 数据工程, HPC, Agent, 数据治理, 论文, 框架, 工程实践  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02771v1 Announce Type: new Abstract: Leadership computing facilities steward large-scale scientific datasets that routinely require substantial transformation before serving as AI training data. However, no existing framework fully unifies automated transformation, readiness assessment, provenance tracking, and agent-native deployment. We present REDI, an open-source framework that addresses this gap through a unified five-stage pipeline (ingest, preprocess, transform, structure, and output) with per-stage instrumentation for reproducibility and deployment as an agent-callable skill; companion tool SetGo automates FAIR compliance and catalog publication. Evaluated across climate, proteomics, materials science, and nuclear fusion, REDI transforms all datasets from raw to AI-ready, with outputs validated against domain-expert references, and preliminary results show near-ideal parallel scaling to 100 nodes on Frontier for the climate case. Provenance-instrumented profiling reveals file I/O as the dominant pipeline cost, with format selection a first-order optimization lever. These results establish REDI as a cross-domain platform providing automated data readiness for scientific AI, transforming data preparation bottlenecks into reproducible, reusable community assets.

## 综合总结
本文提出了REDI，一个面向科学AI的开源数据就绪框架，旨在解决大规模科学数据在用于AI训练前需大量转换且缺乏统一自动化流程的痛点。REDI通过五阶段流水线集成了自动转换、就绪度评估、溯源追踪及Agent原生部署能力，并搭配SetGo工具实现FAIR合规。该框架在气候、蛋白质组学、材料科学和核聚变四个领域成功验证，并在Frontier超算上展现出近理想的百节点并行扩展能力。性能剖析指出文件I/O是主要瓶颈，为后续优化指明方向。REDI将数据准备瓶颈转化为可复用的社区资产，对AI4Science领域的数据基础设施建设具有重要价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究在系统架构和工程实现上展现了较高的深度与创新性。首次将自动转换、就绪度评估、溯源追踪和Agent原生部署统一到单一框架（REDI）中，提出了严谨的五阶段流水线模型。技术验证不仅涵盖了气候、蛋白质组学等四个异构科学领域，还在Frontier超算上实现了近理想的百节点并行扩展，且通过溯源分析精准定位了文件I/O为性能瓶颈，论证过程扎实且具有深度。

### 实用性 (评分: 9.0/10)
对AI4Science从业者具有极高的落地价值。科学数据预处理一直是阻碍AI落地的重大瓶颈，REDI作为开源框架，不仅提供了标准化的自动化流水线，还支持Agent调用和FAIR合规发布，能直接嵌入现有的HPC和AI工作流中。其跨领域的适用性和在超算环境下的扩展性，使其具备成为科学数据基础设施标准工具的潜力。

### 社区活跃度 (评分: 9.0/10)
AI4Science是当前学术界与工业界的热点，而高质量数据供给是其核心痛点，该工作时效性极强。作者团队来自主导Frontier超算的顶尖国家实验室，权威性极高。该框架将数据准备从成本中心转化为可复用的社区资产，契合开放科学趋势，有望在科研社区产生广泛影响并推动数据标准化进程。

## 项目链接
https://arxiv.org/abs/2607.02771
