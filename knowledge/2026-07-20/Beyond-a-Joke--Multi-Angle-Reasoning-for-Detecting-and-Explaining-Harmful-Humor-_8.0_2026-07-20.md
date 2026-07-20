# Beyond a Joke: Multi-Angle Reasoning for Detecting and Explaining Harmful Humor in Memes

**评分：** 8.0  
**状态：** 正常  
**标签：** 多模态, 内容安全, 可解释性, VLM, 推理, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15442v1 Announce Type: new Abstract: Internet memes intertwine visual cues, textual content, and cultural context, making them particularly challenging to interpret in scenarios where humor, sarcasm, and harmful intent coexist. These complexities highlight the need for explainable meme understanding systems that can provide reliable and structured reasoning to support both accurate classification and human interpretability. However, existing multimodal classifiers either overlook these interdependencies or provide only limited interpretability. In this paper, we introduce MAR-12, a novel framework that leverages Vision Language Models (VLMs) for meme detection and understanding in settings where humorous and hateful elements may coexist. The framework first interprets each meme through twelve structured perspectives derived from humor and hate theories. It then applies a role-aware soft-gated attention mechanism to learn how much each perspective should contribute, followed by a prototype-based classifier for the final prediction. Finally, explanations are synthesized using both perspective-specific reasoning and learned attention weights, ensuring transparent and context-grounded justifications. We evaluate MAR-12 on the PrideMM and Memotion datasets, where it achieves up to 80.3% accuracy for humor detection and 75.9% accuracy for hate detection, outperforming state-of-the-art approaches. Furthermore, both human and GPT-4-based evaluations confirm that MAR-12 produces coherent and persuasive explanations, particularly for memes in which humorous and harmful cues co-occur.

## 综合总结
本文提出MAR-12框架，通过基于幽默与仇恨理论的12个结构化视角对多模态模因进行推理，利用软门控注意力机制融合视角特征并进行原型分类，在幽默和仇恨检测任务上取得SOTA表现，同时生成连贯且有说服力的可解释性分析，为复杂模因的内容安全审核提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了MAR-12框架，创新性地从幽默和仇恨理论中提取12个结构化视角来解构多模态模因，结合角色感知软门控注意力机制与原型分类器，不仅实现了SOTA的检测准确率（幽默80.3%，仇恨75.9%），还通过注意力权重与视角推理合成高质量的可解释性依据，技术深度与理论结合度高。

### 实用性 (评分: 7.5/10)
该研究对社交媒体平台的内容安全审核具有极高的参考价值，能够有效识别并解释带有幽默外衣的有害模因。不过，12个视角的推理流程可能带来一定的计算开销，在实际工业级落地时需考虑推理延迟与成本的平衡。

### 社区活跃度 (评分: 8.0/10)
多模态有害内容检测是当前AI安全和治理领域的热点，该论文在PrideMM和Memotion基准上取得SOTA，并采用人类与GPT-4双重评估验证解释质量，来源权威，话题极具时效性和社区关注度。

## 项目链接
https://arxiv.org/abs/2607.15442
