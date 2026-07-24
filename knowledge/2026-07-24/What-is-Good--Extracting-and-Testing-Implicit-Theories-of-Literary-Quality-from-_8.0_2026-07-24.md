# What is Good? Extracting and Testing Implicit Theories of Literary Quality from LLM Reasoning Traces

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 推理, 评估, 计算美学, 可解释性, 论文  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20425v1 Announce Type: new Abstract: What makes writing "good" remains a persistent question in literary studies and computational linguistics. We present a two-study investigation of how reasoning-enabled LLMs evaluate literary quality. In Study 1, we construct a benchmark of 30 real texts spanning six quality tiers, from canonical literature to anonymous forum posts, and extract the model's implicit theory of quality from its reasoning traces. Across five DeepSeek replications, the model achieves 79.3% mean tier-classification accuracy. The traces reveal a consistent stated theory: the model values intentionality over correctness, prioritizing craft, depth, and distinctive voice. A familiarity experiment with style-matched but unrecognizable passages suggests that source recognition may inflate scores, although this is confounded by genuine quality differences between canonical originals and researcher-written pastiches. In Study 2, we probe this theory through systematic degradation of five canonical prose passages. We apply six manipulations - vocabulary simplification, rhythm flattening, imagery removal, voice genericization, structure simplification, and combined degradation - and reevaluate each version. Vocabulary simplification causes the smallest quality loss (0.41 +/- 0.46 points), far below structure (2.78) or voice (2.34) loss. Combined degradation is devastating (-5.64) but subadditive. An exploratory comparison with Qwen QwQ shows the same broad qualitative pattern. Together, these studies suggest that LLM judgments of writing quality are holistic, author-specific, and more sensitive to structural than lexical features, with implications for automated writing feedback and computational aesthetics.

## 综合总结
本文探讨了具备推理能力的LLM如何评估文学质量。研究通过构建多层级文本基准提取模型的隐式评价理论，并设计系统性文本退化实验进行验证。结果表明，LLM对写作质量的判断具有整体性，对结构特征和独特声音的敏感度远高于词汇特征，且来源识别可能带来评分偏差。该研究为理解LLM评估机制及开发自动化写作反馈系统提供了重要参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究设计严谨且具有方法论创新，采用两阶段设计（理论提取+干预验证）。通过分析推理轨迹提取LLM的隐式文学评价理论，并创造性地使用6种系统性文本退化操作（如词汇简化、结构简化等）进行因果验证，揭示了LLM重结构轻词汇的整体性评估机制，论证扎实，技术深度较高。

### 实用性 (评分: 7.5/10)
对自动化写作反馈、AI作文批改及文本生成质量评估具有直接的指导意义。明确了LLM在评价文本时更看重结构与声音而非词汇，可指导开发者优化评估提示词或设计更合理的自动评价指标，但偏学术性质，需进一步工程化封装才能落地。

### 社区活跃度 (评分: 8.0/10)
话题切中当前推理大模型（如DeepSeek、QwQ）的可解释性与能力评估热点，结合了计算语言学与文学研究，视角新颖。arXiv首发，具备一定的学术权威性与讨论价值，能引起AI评估与计算美学社区的关注。

## 项目链接
https://arxiv.org/abs/2607.20425
