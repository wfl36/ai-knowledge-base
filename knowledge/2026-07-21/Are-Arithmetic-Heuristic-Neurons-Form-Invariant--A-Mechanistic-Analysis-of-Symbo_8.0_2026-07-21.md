# Are Arithmetic Heuristic Neurons Form-Invariant? A Mechanistic Analysis of Symbols, Text, and Code in LLMs

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 机制可解释性, 算术推理, 神经元, 论文  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16693v1 Announce Type: new Abstract: Large language models often succeed on one formulation of a problem while failing on an equivalent formulation. Whether these failures arise from distinct internal circuits or different activation states of a shared circuit remains unknown. Recent mechanistic interpretability studies suggest that arithmetic in LLMs emerges from a "bag of heuristics," encoded by a sparse set of MLP neurons that represent distinct arithmetic strategies. We investigate whether arithmetic heuristic neurons are form-invariant across symbolic arithmetic, natural language word problems, and Python code in three Llama-3 models. In each format, we identify arithmetic heuristic neurons using a two-stage pipeline combining attribution patching and activation patching. A compact set of neurons is shared across all three formats, and targeted interventions show this shared circuit is both necessary and sufficient for late-layer arithmetic computation. Transferring the shared neurons' activations from a successful execution in one format to a failed execution in another recovers most incorrect predictions, exceeding 97% for addition and subtraction, indicating that cross-format failures arise from activation states rather than distinct circuits. Moreover, shared neurons consistently belong to the same heuristic families across formats, demonstrating that arithmetic computation in LLMs is largely form-invariant at the neuron level.

## 综合总结
本文研究了LLM在处理等价但不同形式的算术问题时表现差异的原因。通过在Llama-3模型中结合归因修补和激活修补技术，作者识别出一组跨格式（符号算术、自然语言应用题、Python代码）共享的算术启发式神经元。实验表明，这些共享神经元对后期算术计算既必要又充分，且将成功格式的共享神经元激活状态转移到失败格式中，可恢复超97%的加减法错误预测。这证明了LLM的跨格式算术失败源于共享回路的激活状态差异而非不同回路，从神经元层面证实了LLM算术计算的形式不变性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文在机制可解释性领域具有较高深度，创新性地探究了LLM在处理等价但不同形式的算术问题时失败的根本原因。通过结合归因修补与激活修补的两阶段方法，精准定位了跨格式（符号、自然语言、代码）共享的算术启发式神经元，并通过干预实验证实跨格式失败源于共享回路的激活状态差异而非独立回路，论证严谨，揭示了LLM算术计算在神经元层面的'形式不变性'。

### 实用性 (评分: 6.5/10)
对从业者的直接工程落地价值中等偏上，但具有显著的指导意义。研究结论表明跨格式算术失败是激活状态问题，这为模型训练和推理优化提供了新思路：无需针对每种格式单独训练特定回路，而应关注如何统一和修正共享神经元的激活状态，对提升LLM数学推理鲁棒性有参考价值。

### 社区活跃度 (评分: 8.5/10)
机制可解释性与大模型推理能力是当前AI社区的高热度前沿话题。该研究基于主流开源模型Llama-3进行，实验设计扎实，结论（97%以上的错误恢复率）极具说服力。虽然作者并非业界顶尖知名团队，但其直击痛点的研究问题将引起可解释性及LLM能力评估社区的广泛关注。

## 项目链接
https://arxiv.org/abs/2607.16693
