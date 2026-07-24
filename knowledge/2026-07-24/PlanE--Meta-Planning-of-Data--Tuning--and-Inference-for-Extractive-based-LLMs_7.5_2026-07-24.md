# PlanE: Meta Planning of Data, Tuning, and Inference for Extractive-based LLMs

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 微调, 数据工程, 推理, 论文, 工程实践  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20470v1 Announce Type: new Abstract: Enhancing the task-specific capabilities of Large Language Models (LLMs) primarily requires substantial instruction-tuning datasets. However, the sheer volume of such data imposes a considerable annotation cost, and a lack of optimization methods for tailoring LLMs to specific tasks. To address the above issues, we propose a \textbf{Plan}ning framework for constructing \textbf{E}xtractive-based LLMs called \textbf{PlanE}, which includes data decomposition, instruction tuning, and prompt inference. Additionally, we introduce a Data-Tuning-Inference (DTI) planner, aimed at selecting the optimal base-LLM and its DTI combinations for specific datasets to improve construction efficiency. The experimental results demonstrate the effectiveness of our PlanE from two views: (1) across different datasets using the same base-LLM, and (2) on the same dataset using different base-LLMs. Furthermore, we validate the generalizability of the proposed DTI planner under different optimization objectives. The codes are publicly available at https://github.com/gugugu-469/PlanE.

## 综合总结
本文提出了PlanE框架，旨在解决构建抽取式LLM时指令微调数据标注成本高和缺乏任务特定优化方法的问题。该框架整合了数据分解、指令微调和提示推理三个阶段，并引入DTI规划器以自动选择最优基础模型及其DTI组合，从而提升构建效率。实验验证了框架的有效性和DTI规划器的泛化能力，且代码已开源，对垂类大模型的低成本构建具有较高实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文提出了PlanE框架，将数据分解、指令微调和提示推理三个阶段统一到一个规划框架中，并创新性地引入了Data-Tuning-Inference (DTI) planner。该planner能够针对特定数据集自动选择最优的基础大模型及DTI组合，实现了从数据到推理的元规划，在系统级优化和方法论上具有一定的深度和新颖性。

### 实用性 (评分: 8.0/10)
该研究直击大模型微调中数据标注成本高和缺乏任务特定优化方法的痛点，提供了从数据构建、模型微调到推理的完整解决方案。DTI planner的自动寻优功能能够显著降低开发者构建抽取式任务大模型的试错成本，且项目已开源，对工业界构建垂类模型具有很高的实际指导意义和落地参考价值。

### 社区活跃度 (评分: 7.0/10)
大模型微调优化与数据工程是当前AI社区持续关注的热点方向。该论文作为arXiv预印本，提供了开源代码，具备较好的可复现性和时效性。但由于作者团队知名度相对有限且尚未经过同行评审，其权威性和社区影响力仍有待进一步观察。

## 项目链接
https://arxiv.org/abs/2607.20470
