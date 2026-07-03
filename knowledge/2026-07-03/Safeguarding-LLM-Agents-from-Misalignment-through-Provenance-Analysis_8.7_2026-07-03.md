# Safeguarding LLM Agents from Misalignment through Provenance Analysis

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 大模型安全, 对齐, 溯源分析, 论文  
**更新日期：** 2026-07-03  
**来源：** rss  

## 项目描述
arXiv:2607.01236v1 Announce Type: new Abstract: As LLM agents gain increasing access to powerful tools, ensuring that their actions are aligned with the user's intent becomes critical. When an agent's proposed tool invocation deviates from the user's intent -- a phenomenon called misalignment -- it may lead to harmful consequences that are difficult to undo. Existing runtime guardrails rely on an LLM-as-a-judge paradigm that lacks a systematic framework for reasoning about alignment, often producing judgments that are inconsistent or difficult to audit. Motivated by provenance analysis, we propose a provenance-based conceptual framework that formalizes misalignment detection as determining whether a proposed tool call is supported by traceable evidence in the agent's context. Building on this framework, we propose ProvenanceGuard, a multi-stage pipeline that analyzes the agent's action for three types of misalignment before the selected tool is executed and only allows the action to take place when it is considered aligned with the user's input query. We evaluated our proposed approach on two different benchmarks, Agent-SafetyBench and WorkBench, across 10 backbone LLMs. Compared to the LLM-as-a-judge baseline, ProvenanceGuard reduces error rate on misaligned traces from 42.9% to 1.8% on Agent-SafetyBench and from 32.1% to 17.3% on WorkBench, while reducing intervention burden on task-successful traces from 30.5% to 12.8% and introducing no statistically significant increase in unnecessary interventions on aligned traces. These results demonstrate that structured, provenance-based reasoning provides an effective and practical foundation for safeguarding LLM agents from misalignment.

## 综合总结
本文针对LLM Agent工具调用中的不对齐风险，创新性地提出了基于溯源分析的概念框架，将不对齐检测形式化为可追溯证据的验证过程，并据此设计了ProvenanceGuard多阶段拦截管道。实验表明，相比LLM-as-a-judge基线，该方法在Agent-SafetyBench和WorkBench上将错误率大幅降低（最低至1.8%），同时显著减少了不必要的干预负担，为构建可解释、低误杀的Agent安全护栏提供了突破性且极具落地价值的方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文在技术深度和新颖性上表现突出。针对LLM Agent工具调用中的不对齐问题，创新性地引入了传统数据系统中的溯源分析概念，将不对齐检测形式化为'工具调用是否有上下文中可追溯证据支持'的判定过程。相比现有缺乏系统性、难以审计的LLM-as-a-judge范式，该框架提供了结构化、白盒化的推理路径，并设计了ProvenanceGuard多阶段管道，论证严谨，实验在10个骨干模型上展现了错误率的断崖式下降，技术说服力强。

### 实用性 (评分: 9.0/10)
对从业者的实际参考价值极高。LLM Agent的安全护栏是当前工业界部署Agent的痛点，本文提出的ProvenanceGuard作为运行时护栏，直接在工具执行前进行拦截，具备极强的可操作性。更重要的是，它在大幅降低错误率的同时，将任务成功轨迹的干预负担从30.5%降至12.8%且未增加误杀，有效解决了安全拦截与用户体验之间的矛盾，可直接指导Agent安全系统的工程实践。

### 社区活跃度 (评分: 8.5/10)
话题时效性强，Agent安全与对齐是当前大模型领域的核心前沿。论文来源于arXiv，作者具备学术背景，评估采用了Agent-SafetyBench和WorkBench等权威基准。针对现有LLM-as-a-judge范式不一致、难审计的痛点提出改进，有望成为Agent安全护栏领域的新范式，具备较高的社区影响潜力和可信度。

## 项目链接
https://arxiv.org/abs/2607.01236
