# RadOnc-Agent: An LLM-Orchestrated Framework for AI Workflows Across the Radiotherapy Care Pathway

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-08  
**来源：** rss  

## 项目描述
arXiv:2610.06923v1 Announce Type: new Abstract: Artificial intelligence has advanced individual radiotherapy tasks, yet these capabilities remain separated across clinical stages, software environments and data modalities. This fragmentation contrasts with the longitudinal radiotherapy workflow from treatment decision-making through follow-up. Here we present RadOnc-Agent, an agentic artificial-intelligence framework that formalizes radiotherapy into four clinical phases and provides 26 callable functions through a conversational interface. A large-language-model controller maps clinical intent to schema-constrained calls, preserves patient and workflow context, and routes requests to specialist services. We evaluated system execution using 2,600 single-function requests (7,800 repeat executions), 200 prespecified synthetic cross-stage scenarios spanning four phases (600 executions), and 120 workflow instances from 60 de-identified patient records (360 clean executions) representing decision-to-planning and planning-to-adaptation. RadOnc-Agent selected the intended function in 98.79% of single-function executions, completed 96.50% of scripted cross-stage workflows, and completed 96.67% of real-patient workflow executions. In comparative ablations, removing longitudinal state reduced cross-stage completion from 96.50% to 84.00%, while disabling schema and identity validation increased mismatched backend dispatch from 0% to 95.28% in a replay/test evaluation. These findings establish the technical feasibility of an LLM-orchestrated architecture for coordinating heterogeneous radiotherapy capabilities and information across longitudinal workflows; they do not establish clinical correctness, clinical utility or prospective benefit.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.06923
