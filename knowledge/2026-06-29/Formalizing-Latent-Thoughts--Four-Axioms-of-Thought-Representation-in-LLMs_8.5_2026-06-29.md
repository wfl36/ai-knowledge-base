# Formalizing Latent Thoughts: Four Axioms of Thought Representation in LLMs

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 推理, 可解释性, 表征学习, 论文  
**更新日期：** 2026-06-29  
**来源：** rss  

## 项目描述
arXiv:2606.27378v1 Announce Type: new Abstract: We introduce an axiomatic evaluation framework for latent thought representations in LLMs, comprising metrics that are independent of downstream benchmark scores and reveal representational failures that benchmark accuracy masks. Existing evaluations conflate representation quality with model capacity. Therefore, failures cannot be attributed to the representation rather than to the model that processes it. We formalize four functional axioms (Causality, Minimality, Separability, and Stability) and define a quantitative measure for each, computed directly on the representation independently of downstream accuracy. We audit open-weight LLMs across 23 reasoning tasks (e.g., Spatial Reasoning, Factual QA). We find that no candidate satisfies all four axioms simultaneously, that the representations distinguish task type reliably but cannot distinguish between two questions within the same task, and that the representations encode little information beyond what is already present in the input embedding. The failure is consistent across dense, reasoning-distilled, and RL-trained model families, indicating that the gap is structural rather than a property of model size or training procedure.

## 综合总结
该论文提出了一种评估大语言模型潜在思维表征的公理化框架，包含因果性、最小性、可分离性和稳定性四个公理，旨在独立于下游任务准确率来衡量表征质量。通过对23个推理任务的开源LLM审计发现，没有任何模型（涵盖密集、蒸馏和RL训练）能同时满足四个公理，且表征极少包含超出输入嵌入的额外信息，无法区分同类任务内部问题。这表明当前LLM的推理表征存在结构性缺陷，揭示了基准准确率掩盖下的深层局限。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文提出了极具创新性的公理化评估框架，将LLM的潜在思维表征从下游基准准确率中剥离，定义了因果性、最小性、可分离性和稳定性四个功能公理及量化指标。其论证严谨，深刻揭示了当前LLM表征未能编码超出输入嵌入的额外信息，且无法区分同类任务中的不同问题，证明了这种表征缺陷是结构性的，与模型规模或训练范式（密集、蒸馏、RL）无关，技术深度与洞见极高。

### 实用性 (评分: 7.5/10)
提出的四个公理及量化指标可直接在模型表征上独立计算，为模型开发者、可解释性研究员提供了一套无需依赖下游任务的诊断工具，能有效发掘被基准测试掩盖的表征缺陷。但对偏应用层的工程实践（如RAG、Agent构建）直接指导意义有限，更适用于基础模型研发与迭代评估。

### 社区活跃度 (评分: 9.0/10)
探讨LLM是否真正具备推理能力是当前AI社区最核心的争议之一。该研究直击痛点，指出基准准确率掩盖了表征的系统性失败，且得出所有主流范式模型均存在此结构性缺陷的结论。这一颠覆性发现具有极高的话题性与时效性，极易引发学术界和工业界对当前大模型评估体系与推理本质的广泛反思与讨论。

## 项目链接
https://arxiv.org/abs/2606.27378
