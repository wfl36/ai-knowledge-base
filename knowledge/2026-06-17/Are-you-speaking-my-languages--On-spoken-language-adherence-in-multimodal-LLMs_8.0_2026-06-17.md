# Are you speaking my languages? On spoken language adherence in multimodal LLMs

**评分：** 8.0  
**状态：** 正常  
**标签：** 多模态, 大模型, 语音识别, 多语言, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17281v1 Announce Type: new Abstract: While Large Language Model (LLM) based Automatic Speech Recognition (ASR) enables seamless multilingual use, models often misidentify the output language, compromising transcription fidelity and downstream application quality. To preserve flexibility and code-switching capabilities, we propose a soft prompting approach that hints at potential spoken languages without strictly constraining the output. We formally define this challenge as a lack of language adherence, introduce a novel metric to quantify violations, and evaluate three mitigation strategies: (1) zero-shot prompting for robust guidance under uncertainty, (2) supervised fine-tuning (SFT) to improve prompt adherence, and (3) Chain-of-Thought (CoT) reasoning to enforce adherence during decoding. We present a comparative analysis of these methods across multiple languages, evaluating effectiveness in reducing the language violation while maintaining overall ASR performance. Finally, we discuss trade-offs to guide strategy selection under various compute constraints.

## 综合总结
本文针对多模态大模型在自动语音识别（ASR）中经常错误识别输出语言的问题，提出了一种保留语码转换能力的软提示方法。研究首次形式化定义了'语言依从性'并引入量化违规指标，系统评估了零样本提示、监督微调（SFT）和思维链三种缓解策略，并对比了它们在多语言下的表现与计算权衡，为工业界在不同资源约束下优化多语言ASR系统提供了实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文针对多模态大模型在ASR任务中输出语言混淆的痛点，首次形式化定义了'语言依从性(language adherence)'问题，并创新性地提出了量化语言违规的新指标。在方法上，系统性地对比了零样本提示、SFT和CoT推理三种不同范式的缓解策略，并深入分析了它们在多语言环境下的效果与计算权衡，研究方法严谨，具有较好的理论深度和实验说服力。

### 实用性 (评分: 8.5/10)
多语言ASR中的语言误识别是工业界语音交互系统常见的痛点，本文提出的软提示方法及三种缓解策略（尤其是零样本提示和SFT）对从业者具有极高的参考价值。论文不仅提供了具体的实现路径，还讨论了不同计算资源约束下的策略选择，能够直接指导多模态语音大模型在实际产品中的落地与优化。

### 社区活跃度 (评分: 7.5/10)
多模态大模型与语音处理是当前AI社区的热门研究方向，该问题切中多语言场景下的实际痛点，具有较好的时效性。arXiv预印本来源具备一定权威性，作者团队来自业界，研究背景扎实。虽然方法组合未带来颠覆性震撼，但对社区在多语言ASR评估和优化方向上有积极的推动作用。

## 项目链接
https://arxiv.org/abs/2606.17281
