# DrawingVQA: A Real-World Benchmark for Multi-Depth Visual-Textual Reasoning on Construction Drawings

**评分：** 7.8  
**状态：** 正常  
**标签：** 多模态, VQA, 建筑工程, 图纸理解, 推理, 论文, 基准测试  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15418v1 Announce Type: new Abstract: We introduce DrawingVQA, the first benchmark designed to evaluate multimodal large language models (MLLMs) on real-world construction drawings -- a core media in architecture, civil, and many other engineering practices. Unlike natural images or schematic floor plans, construction drawings fuse abstract geometry, symbolic notation, tabular data, annotations, and domain-specific text, forming a uniquely complex visual-textual domain core to engineering workflows. DrawingVQA bridges this gap with 33 "Issued for Construction" drawings and 92 expertly curated question-answer pairs, spanning three reasoning depths: perceptual understanding, contextual interpretation, and domain-expert reasoning. To evaluate model capabilities, we present a dual categorization framework to jointly analyze performance across seven construction-engineering and four MLLM capability dimensions -- the first to explicitly map engineering workflows to AI reasoning competencies. Evaluations of state-of-the-art MLLMs reveal a substantial gap between model and expert performance, particularly at higher reasoning depths. This benchmark lays a foundation for domain-specialized multimodal reasoning to allow for advancement on integration of AI-driven understanding and real-world engineering workflows.

## 综合总结
本文提出了DrawingVQA，首个针对真实世界施工图纸的多模态大模型评估基准，包含33份图纸和92个专家QA对。研究创新性地定义了感知、上下文与专家三层推理深度，并构建了映射工程工作流与AI能力的双重分类框架。对SOTA模型的评估揭示了其在高深度工程推理上与专家的显著差距，为领域专用多模态AI的发展奠定了基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
首次提出针对施工图纸的多模态推理基准DrawingVQA，创新性地构建了跨越感知、上下文与专家级的三层推理深度，并首创将工程工作流与AI推理能力映射的双重分类框架。不过，数据集规模（33张图纸，92个QA对）相对较小，对模型泛化性与论证的充分性存在一定限制。

### 实用性 (评分: 8.0/10)
对建筑与土木工程领域的AI落地具有高度参考价值，明确指出了当前MLLM在处理复杂工程符号与高深度推理时的短板，为开发领域专用审图或辅助设计AI提供了评估标准与方向。但当前基准数据量较小，距离大规模工程实践应用仍需扩充与迭代。

### 社区活跃度 (评分: 8.0/10)
话题紧扣当前多模态大模型在垂直专业领域落地的热点与挑战。作为首个针对施工图纸的VQA基准，由领域专家策划，来源权威可信，有望在AI与建筑/土木工程交叉社区产生积极影响并激发后续研究。

## 项目链接
https://arxiv.org/abs/2607.15418
