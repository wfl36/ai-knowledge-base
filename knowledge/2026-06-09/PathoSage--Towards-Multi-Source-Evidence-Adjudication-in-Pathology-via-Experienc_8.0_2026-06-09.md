# PathoSage: Towards Multi-Source Evidence Adjudication in Pathology via Experience-Aware Agentic Workflow

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, 多模态, 病理学, 推理, 幻觉缓解, 论文  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.07549v1 Announce Type: new Abstract: Recent advances in Multimodal Large Language Models (MLLMs) and agent workflows have shown strong promise for computational pathology, yet reliable patch-level reasoning remains challenging. End-to-end pathology MLLMs often hallucinate morphological features, while recent agentic systems usually merge tool outputs and retrieved knowledge into a shared context, making decisions vulnerable to conflicting evidence and context contamination. We propose PathoSage, a three-stage framework that explicitly separates knowledge retrieval, evidence collection, and evidence adjudication for patch-level pathology multimodal reasoning. Its core component, Structured Evidence Deliberation, independently evaluates heterogeneous evidence from tools, performs conflict analysis, and generates the final judgment in a fresh context to reduce anchoring bias. We further introduce a training-free Beta-Bernoulli experience system with continuous credit assignment to model long-term tool reliability and construct similarity-weighted priors for future tool use. Experiments show that PathoSage effectively mitigates VQA hallucinations and classifier disagreement, outperforming strong pathology MLLM and agentic baselines. Our results highlight explicit evidence adjudication and reliability-aware tool modeling as key ingredients for robust pathology agents.

## 综合总结
PathoSage提出了一种面向病理学多源证据裁决的三阶段Agent框架，通过显式分离知识检索、证据收集与结构化证据审议，在全新上下文中解决冲突以消除锚定偏差与上下文污染；同时引入免训练的Beta-Bernoulli经验系统对工具长期可靠性进行建模与信用分配。实验证明该方法有效缓解了VQA幻觉与分类器分歧，其解耦裁决与可靠性感知的工具调用机制对构建鲁棒的垂直领域Agent具有重要的借鉴意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对当前病理学多模态大模型（MLLM）的幻觉问题以及Agent系统中多源证据合并导致的上下文污染与冲突易感性，提出了三阶段解耦框架PathoSage。其技术创新点显著：一是提出结构化证据审议机制，在全新上下文中独立评估异构证据与冲突，有效减少锚定偏差；二是引入免训练的Beta-Bernoulli经验系统，通过连续信用分配建模工具的长期可靠性，并构建相似性加权先验指导未来工具调用。整体论证严谨，将贝叶斯思想与Agent工作流深度结合，技术深度与新颖性俱佳。

### 实用性 (评分: 7.5/10)
该框架的解耦设计（检索、收集、裁决分离）和免训练的经验系统具有很强的工程参考价值。'在全新上下文中进行裁决'以及'基于历史信用分配评估工具可靠性'的思路，不仅适用于病理学，也可泛化至其他需要多源信息融合与冲突消解的Agent场景（如法律研判、金融研报分析等复杂决策系统）。不过，在垂直领域的落地效果仍高度依赖外部工具的质量与知识库的覆盖度。

### 社区活跃度 (评分: 8.0/10)
多模态大模型与Agent工作流是当前AI社区的核心热点，而医疗/病理学是极具价值与挑战的垂直落地领域。该研究直击MLLM幻觉和Agent上下文污染两大社区痛点，提出的解决方案兼顾了理论优雅与工程实用性，极易引发Agent架构设计领域的讨论与跟进。发布时间新颖，且来自国内知名高校团队，时效性与权威性较高。

## 项目链接
https://arxiv.org/abs/2606.07549
