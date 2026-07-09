# Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated Multilingual Transcripts

**评分：** 8.2  
**状态：** 正常  
**标签：** 多模态, 语音情感分析, 知识蒸馏, 跨模态, ASR, 论文  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.06611v1 Announce Type: new Abstract: Automatically recognizing the sentiment, positive or negative, from speech is a challenging task, requiring both the analysis of vocal inflections and the interpretation of uttered words. Recent solutions rely on audio foundation models to solve the task, but it remains unclear if such models can take all aspects into account. To this end, we propose a multimodal solution that integrates audio and text information via cross-modal transformers, where text transcripts are automatically generated via an automatic speech recognition (ASR) tool. Moreover, we create multiple text modalities by automatically translating the transcripts into multiple languages via machine translation tools. Audio and multilingual text features are combined via a cascaded architecture comprising cross-modal transformer blocks that integrate modalities one by one. We further distill knowledge from the multimodal model, called teacher, into a unimodal (audio only) model, called student. We conduct experiments on a large-scale dataset, demonstrating that the automatically generated textual information can bring significant performance boosts in multimodal sentiment polarity classification. Our ablation study confirms that both automatic transcripts and automatic translations are helpful. Moreover, we show that the audio-only model can be enhanced via distillation, boosting performance without any computational overhead during inference. To reproduce the reported results, we publicly release our code at https://github.com/andreidurdun/cross-modal-audio-sentiment.

## 综合总结
本文提出一种基于多语言转录和跨模态融合的语音情感分析方法。通过ASR和机器翻译生成多语言文本，利用级联跨模态Transformer与音频特征融合，并将多模态教师模型蒸馏至纯音频学生模型。实验表明该方法显著提升了情感分类性能，且蒸馏后的单模态模型在推理时无额外计算开销，代码已开源。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文提出了一种新颖的多模态语音情感分析框架，创新性地利用ASR和机器翻译生成多语言文本模态，并通过级联跨模态Transformer进行特征融合。进一步将多模态知识蒸馏至单模态（纯音频）模型，论证严谨，消融实验充分验证了自动转录与多语言翻译的有效性。

### 实用性 (评分: 9.0/10)
对工业界极具参考价值。通过知识蒸馏将多模态模型的性能转移到纯音频模型，实现了推理阶段零计算开销的性能提升，非常适合算力受限的端侧设备或实时语音情感分析场景，落地适用范围广。

### 社区活跃度 (评分: 7.5/10)
语音情感分析与多模态融合是当前AI领域的持续热点。论文由arXiv发布且代码开源，增强了结果的可信度和可复现性，对多模态蒸馏和语音处理社区有较好的实践指导意义与影响力。

## 项目链接
https://arxiv.org/abs/2607.06611
