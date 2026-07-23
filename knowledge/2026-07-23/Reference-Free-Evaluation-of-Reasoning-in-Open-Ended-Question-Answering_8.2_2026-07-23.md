# Reference-Free Evaluation of Reasoning in Open-Ended Question Answering

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 推理, 评估, 幻觉检测, 医疗AI, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19678v1 Announce Type: new Abstract: AI-generated answers in high-stakes domains are often fluent but difficult to verify, especially when they contain multi-step reasoning rather than a single final answer. We propose a reasoning-based, reference-free framework for auditing LLM-generated outputs. The method decomposes a generated reasoning trace into segments, labels local premise-target relations using Natural Language Inference (NLI), and organizes these relations into a hypergraph. A deterministic backward AND-OR search then assigns segment-level audit labels that indicate how each segment is grounded within the generated response. We evaluate the framework in two settings: deductive mathematical reasoning with Hard2Verify, and open-ended medical reasoning with UroReason, a new physician-annotated benchmark of LLM reasoning traces from real clinical cases. Across these settings, our NLI-hypergraph audit provides a more reliable reference-free evaluation signal than direct LLM-as-judge baselines. In the clinical setting, state-of-the-art LLM judges often fail to identify problematic reasoning segments, over-accepting fluent but weakly grounded responses. Our results show that QA evaluation should account for how inferential relations compose across a reasoning trace, rather than relying only on final answers or LLMs as verifiers. UroReason will be made available through an API, and our code will be released as open source.

## 综合总结
本文提出了一种基于NLI和超图的无参考推理评估框架，用于审计LLM生成的多步推理输出。该方法通过分解推理轨迹、构建逻辑超图并进行确定性后向搜索，有效解决了LLM-as-judge过度接受流畅但缺乏依据回答的问题。在数学和医疗（新提出的UroReason基准）场景下的实验表明，该框架提供了更可靠的评估信号，对高可靠性领域的LLM应用审计具有重要意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了一种新颖的无参考推理评估框架，将推理轨迹分解并利用自然语言推理（NLI）构建超图，通过确定性AND-OR搜索进行片段级审计。该方法在技术上突破了传统LLM-as-judge的黑盒评估局限，结构化地揭示了推理步骤间的逻辑支撑关系，技术深度和创新性较高。

### 实用性 (评分: 8.0/10)
对高风险领域（如医疗、数学）的LLM输出审计具有极高的实用价值。该框架能有效识别流畅但基础薄弱的推理片段，为RAG和长链推理的幻觉检测与事实一致性审计提供了可落地的工程方案。代码和基准的开放进一步提升了其实践指导意义。

### 社区活跃度 (评分: 8.0/10)
针对当前社区过度依赖LLM-as-judge的痛点，论文揭示了SOTA模型在临床推理评估中的失效模式（过度接受流畅但弱依据的回答），具有强烈的时效性和警示意义。提出的UroReason医生标注基准填补了该领域的空白，对AI安全和评估社区有重要参考价值。

## 项目链接
https://arxiv.org/abs/2607.19678
