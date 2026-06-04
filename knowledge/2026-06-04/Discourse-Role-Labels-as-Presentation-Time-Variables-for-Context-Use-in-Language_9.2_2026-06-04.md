# Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models

**评分：** 9.2  
**状态：** 正常  
**标签：** 大模型, RAG, 推理, Prompt工程, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04109v1 Announce Type: new Abstract: Context-augmented language model systems often wrap supplied content with labels such as Reference:, Evidence:, Instruction:, Note:, or Example:, but the effect of these labels on reader-model behavior remains underexplored. We introduce a paired fixed-content probe over 500 MMLU-Pro items: each item receives the same misleading answer-bearing assertion under different discourse-role labels, and adoption is measured by whether the model outputs the injected wrong option. Across GPT-5.5, DeepSeek V4 Pro, Llama-3-8B-Instruct, and Qwen2.5-7B-Instruct, Misleading Adoption Rate shifts by 56-84 percentage points. Binding or source-like labels such as Instruction: and Reference: produce high adoption, whereas Example: consistently suppresses it. Paired tests, bootstrap intervals, final-instruction ablations, and Qwen final-step log-probability probes support a label-conditioned candidate preference. Boundary probes show where the effect weakens or persists: arithmetic tasks reduce adoption, passage-shaped external context preserves smaller label gaps, short-answer evaluation rules out option-letter copying, and nested-label conflicts suggest that illustrative framing can delimit adoption scope. A 200-case single-author manual audit confirms that the short-answer contrasts are stable under conservative adjudication. The resulting claim is bounded but practical: context-utilization and reader-side RAG benchmarks should report and control wrapper labels, because presentation choices can change measured reliance on supplied context.

## 综合总结
本文深入研究了上下文增强语言模型中'话语角色标签'对模型行为的决定性影响。实验表明，相同的内容在不同标签（如Instruction:与Example:）下，模型对误导信息的采纳率差异高达56-84个百分点。研究通过严谨的探针与消融实验证实了模型存在标签条件候选偏好，并呼吁RAG评测和上下文利用基准必须控制和报告包装标签，因为内容的呈现方式会显著改变模型对上下文的依赖程度。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
研究视角新颖且论证严谨，首次系统性地将'话语角色标签'（如Reference:, Instruction:, Example:）作为呈现时变量，量化其对大模型上下文采纳行为的深刻影响。通过配对固定内容探针、对数概率探针、边界探针及消融实验等多重严苛验证，证实了仅改变包装标签即可导致模型对误导信息的采纳率发生56-84个百分点的巨变，深刻揭示了模型在上下文利用中存在的'标签条件候选偏好'机制。

### 实用性 (评分: 9.5/10)
对AI从业者具有极高的实践指导价值。研究结论直接指出，在RAG系统设计、Prompt工程及Agent上下文管理中，简单的标签选择即可精准控制模型对注入内容的依赖程度（如用Instruction/Reference增强遵从，用Example抑制幻觉）。同时，强烈呼吁未来的RAG评测与基准测试必须将包装标签作为控制变量进行报告，为工程实践提供了明确的标准优化方向。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，直击当前大模型RAG应用与上下文学习（ICL）中的核心痛点。测试对象涵盖了GPT-5.5、DeepSeek V4 Pro等前沿模型，凸显了该发现在最新一代模型上的普遍适用性。其关于'呈现方式决定上下文依赖度'的结论具有颠覆性，极有可能推动RAG评测基准与Prompt工程最佳实践的标准重构，具有广泛的行业影响力。

## 项目链接
https://arxiv.org/abs/2606.04109
