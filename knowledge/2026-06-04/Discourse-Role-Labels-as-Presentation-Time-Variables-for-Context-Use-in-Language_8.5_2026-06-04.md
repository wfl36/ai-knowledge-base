# Discourse-Role Labels as Presentation-Time Variables for Context Use in Language Models

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, RAG, 上下文学习, 提示工程, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04109v1 Announce Type: new Abstract: Context-augmented language model systems often wrap supplied content with labels such as Reference:, Evidence:, Instruction:, Note:, or Example:, but the effect of these labels on reader-model behavior remains underexplored. We introduce a paired fixed-content probe over 500 MMLU-Pro items: each item receives the same misleading answer-bearing assertion under different discourse-role labels, and adoption is measured by whether the model outputs the injected wrong option. Across GPT-5.5, DeepSeek V4 Pro, Llama-3-8B-Instruct, and Qwen2.5-7B-Instruct, Misleading Adoption Rate shifts by 56-84 percentage points. Binding or source-like labels such as Instruction: and Reference: produce high adoption, whereas Example: consistently suppresses it. Paired tests, bootstrap intervals, final-instruction ablations, and Qwen final-step log-probability probes support a label-conditioned candidate preference. Boundary probes show where the effect weakens or persists: arithmetic tasks reduce adoption, passage-shaped external context preserves smaller label gaps, short-answer evaluation rules out option-letter copying, and nested-label conflicts suggest that illustrative framing can delimit adoption scope. A 200-case single-author manual audit confirms that the short-answer contrasts are stable under conservative adjudication. The resulting claim is bounded but practical: context-utilization and reader-side RAG benchmarks should report and control wrapper labels, because presentation choices can change measured reliance on supplied context.

## 综合总结
该研究揭示了在上下文增强语言模型中，内容包装标签（如Instruction:, Reference:, Example:）对模型采纳信息的倾向有巨大影响，误导采纳率变化幅度高达56-84个百分点。实验表明，指令和参考类标签会显著提高模型对内容的采纳率，而示例类标签则会抑制采纳。研究强烈建议，在RAG和上下文利用基准测试中必须控制和报告这些呈现变量，因为它们会显著改变模型对提供上下文的依赖度与评估结果。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究设计严谨，通过配对固定内容探针、消融实验、边界探针及人工审计等多维度方法，深入揭示了话语角色标签对大模型上下文利用行为的显著调控作用。56-84个百分点的误导采纳率变化极具说服力，不仅证实了标签作为呈现时变量的强干预效应，还细致刻画了不同任务类型（如算术推理）和上下文形态下的边界条件，对理解LLM的上下文处理机制具有较深洞见。

### 实用性 (评分: 9.0/10)
对RAG系统开发者、Prompt工程师及基准测试设计者具有极高的实践指导价值。研究明确指出包装标签会剧烈改变模型对上下文的依赖度，并给出了具体标签（如Instruction/Reference促发高采纳，Example抑制采纳）的差异化影响，直接指导从业者在系统设计时必须将标签选择作为关键变量进行控制与优化，避免因呈现方式不当导致的幻觉或信息遗漏。

### 社区活跃度 (评分: 8.0/10)
话题紧扣当前大模型应用的核心痛点（RAG与上下文利用），arXiv预印本发布具备一定的学术时效性与可信度。尽管为单作者研究且发布时间显示为未来（可能存在元数据异常），但其指出的'评估基准未控制呈现变量'这一系统性缺陷，对LLM评估社区具有强烈的警示和规范推动作用。

## 项目链接
https://arxiv.org/abs/2606.04109
