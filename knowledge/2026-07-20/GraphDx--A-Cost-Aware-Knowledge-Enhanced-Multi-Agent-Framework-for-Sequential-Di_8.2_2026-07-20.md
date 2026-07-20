# GraphDx: A Cost-Aware Knowledge-Enhanced Multi-Agent Framework for Sequential Diagnosis

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, Agent, 知识图谱, 医疗诊断, 推理, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15280v1 Announce Type: new Abstract: Sequential diagnosis requires balancing diagnostic accuracy against resource costs through iterative information gathering. Existing Large Language Model (LLM) approaches exhibit a critical knowledge-reasoning gap: despite encoding extensive medical knowledge, they struggle to reason systematically under cost constraints, often resorting to excessive testing. We propose GraphDx, a knowledge-enhanced framework with two core innovations. First, we design an automated pipeline that leverages LLMs to construct Medical Diagnosis Knowledge Graphs (MDKGs) with quantized typicality, action-centric topology, and dual-objective attributes for both diagnostic relevance and cost-sensitivity. Second, we introduce three collaborative agents (Perception, Reasoning, and Decision) where the Perception and Decision Agents handle language understanding and generation, while the Reasoning Agent performs deterministic evidence scoring and cost-aware planning on the MDKG. Experiments on MedQA and MIMIC-IV across three LLM backbones (DeepSeek-V3, Kimi-k2, Llama-3.3) show that GraphDx improves diagnostic success rates from 50--68% to 79--93% while reducing test costs by 20--54%, providing a robust, economical, and interpretable solution for automated clinical diagnosis.

## 综合总结
GraphDx提出了一种成本感知的知识增强多智能体框架，用于序贯诊断。针对LLM在成本约束下易过度检查的问题，该框架通过自动化流水线构建具有成本敏感性的医学诊断知识图谱(MDKG)，并设计感知、推理、决策三个协作智能体，将语言处理与确定性图推理分离。在MedQA和MIMIC-IV上的实验表明，该方法将诊断成功率提升至79-93%，同时降低20-54%的测试成本，为自动化临床诊断提供了高效、经济且可解释的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文针对LLM在序贯诊断中存在的知识-推理鸿沟及成本控制缺陷，提出了创新性的解决方案。技术上两大亮点：一是构建了包含量化典型性、行动中心拓扑和双目标属性的医学诊断知识图谱(MDKG)，实现了诊断相关性与成本敏感性的结构化融合；二是设计了感知、推理、决策三智能体解耦架构，将LLM的语言理解生成优势与基于图谱的确定性推理规划相分离，有效克服了纯LLM推理的随意性，论证严谨且方法新颖。

### 实用性 (评分: 8.0/10)
该框架在医疗诊断这一高价值且对成本极度敏感的场景中具有极高的落地潜力。通过将诊断成功率提升至79-93%的同时削减20-54%的检查成本，直击临床实践中过度检查的痛点。自动化构建MDKG的流水线也降低了知识图谱的构建门槛，对医疗AI系统开发者和临床辅助决策系统建设者具有直接的指导意义，但实际临床部署仍需通过严格的合规与安全性验证。

### 社区活跃度 (评分: 8.0/10)
医疗AI与大模型Agent的结合是当前学术界与工业界高度关注的前沿领域。该研究基于MedQA和MIMIC-IV等权威数据集，并采用DeepSeek-V3、Kimi-k2、Llama-3.3等最新主流大模型作为基座进行验证，结果极具说服力和时效性。其在准确率与成本控制上的双重显著提升，有望在AI医疗社区产生较大影响力。

## 项目链接
https://arxiv.org/abs/2607.15280
