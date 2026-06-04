# Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, RAG, Prompt工程, 上下文学习, 模型行为, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04109v1 Announce Type: new Abstract: Context-augmented language model systems often wrap supplied content with labels such as Reference:, Evidence:, Instruction:, Note:, or Example:, but the effect of these labels on reader-model behavior remains underexplored. We introduce a paired fixed-content probe over 500 MMLU-Pro items: each item receives the same misleading answer-bearing assertion under different discourse-role labels, and adoption is measured by whether the model outputs the injected wrong option. Across GPT-5.5, DeepSeek V4 Pro, Llama-3-8B-Instruct, and Qwen2.5-7B-Instruct, Misleading Adoption Rate shifts by 56-84 percentage points. Binding or source-like labels such as Instruction: and Reference: produce high adoption, whereas Example: consistently suppresses it. Paired tests, bootstrap intervals, final-instruction ablations, and Qwen final-step log-probability probes support a label-conditioned candidate preference. Boundary probes show where the effect weakens or persists: arithmetic tasks reduce adoption, passage-shaped external context preserves smaller label gaps, short-answer evaluation rules out option-letter copying, and nested-label conflicts suggest that illustrative framing can delimit adoption scope. A 200-case single-author manual audit confirms that the short-answer contrasts are stable under conservative adjudication. The resulting claim is bounded but practical: context-utilization and reader-side RAG benchmarks should report and control wrapper labels, because presentation choices can change measured reliance on supplied context.

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究设计严谨且视角独特，通过配对固定内容探针实验，量化揭示了上下文包装标签（如Instruction:, Reference:, Example:）对语言模型信息采纳行为的显著影响（误导采用率变化达56-84个百分点）。结合消融实验、对数概率探针、边界探针及人工审计，深入论证了标签条件下的候选偏好机制，填补了模型对上下文呈现形式敏感性的研究空白。

### 实用性 (评分: 9.0/10)
对Prompt工程和RAG系统设计具有极高的实践指导价值。从业者可通过选择特定的话语角色标签（如用Instruction:增强指令遵从，用Example:抑制对上下文的盲从）来精细控制模型对注入信息的依赖程度。同时，研究明确提醒开发者在构建RAG评测基准时必须控制和报告标签变量，以避免评测失真。

### 社区活跃度 (评分: 8.5/10)
研究发布于2026年，且测试覆盖了GPT-5.5、DeepSeek V4 Pro等最新前沿模型，时效性极强。其结论直接挑战了当前RAG评测中忽略上下文呈现形式的默认假设，对社区建立更严谨、更科学的上下文利用评测标准具有重要推动力和影响力。

## 项目链接
https://arxiv.org/abs/2606.04109
