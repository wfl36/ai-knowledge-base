# Large Language Models as Unified Multimodal Learners for Clinical Prediction

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 医疗AI, 多模态, 临床预测, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15380v1 Announce Type: new Abstract: Electronic health records combine free-text clinical narratives with structured measurements such as vital signs, laboratory values, and comorbidities. Yet most clinical prediction systems still rely on task-specific fusion architectures, pairing dedicated encoders for each modality with learned combination mechanisms that must be re-engineered for every new task and clinical setting. We propose a simpler alternative: convert all patient data, regardless of modality, into a single natural language sequence and fine-tune a pretrained language model end-to-end, with no architectural modification for fusion. We evaluate this approach across three clinically distinct prediction tasks: in-hospital mortality on MIMIC-III, graft failure prediction using longitudinal data from a German transplant center, and emergency triage classification from ambulance records - comparing encoder-based (ModernBERT) and decoder-based (Llama 3.1, Gemma, DeepSeek-R1-Qwen, Qwen3) fine-tuning against established multimodal baselines and, for graft failure, a gradient boosting model currently used in clinical practice for post-transplant patient management. Across all three tasks, unified textual serialization matches or exceeds task-specific multimodal baselines, and outperforms the clinically deployed gradient boosting system on graft failure prediction. These results indicate that a single serialization-based paradigm, without bespoke fusion architectures, is sufficient for multimodal clinical prediction - substantially reducing system complexity while matching or exceeding specialized designs.

## 综合总结
本文针对多模态临床预测系统中融合架构复杂、需针对新任务重新设计的问题，提出将所有患者数据（文本与结构化数据）统一序列化为自然语言序列，直接微调预训练大模型。在院内死亡率、移植物失败预测和急诊分诊三个任务上的实验表明，该无需架构修改的简单范式不仅匹配或超越了专门的多模态基线，还在移植物失败预测中优于临床部署的梯度提升模型，大幅降低了系统复杂性并提升了实用性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文提出了一种反直觉但极具深度的方法：摒弃为多模态临床数据定制复杂融合架构的传统范式，将所有结构化与非结构化数据统一序列化为自然语言，直接微调预训练大模型。虽然‘序列化统一多模态’的思路在之前已有探讨，但本文在临床预测这一特定场景下，跨越编码器（ModernBERT）与解码器（Llama 3.1等）架构进行了全面严谨的实证检验，并与特定融合基线及真实临床部署模型进行对比，论证过程扎实，技术洞见深刻。

### 实用性 (评分: 9.0/10)
该研究对医疗AI从业者具有极高的落地指导价值。传统的多模态融合需要针对不同任务和数据类型重新设计网络架构与组合机制，工程成本高昂；而本文的‘文本序列化+微调’范式大幅降低了系统复杂度和工程门槛，使得任何具备标准LLM微调能力的团队都能快速构建多模态临床预测系统。且其在真实临床场景（德国移植中心）中击败了部署中的梯度提升模型，证明了其实际应用的有效性。

### 社区活跃度 (评分: 8.5/10)
大模型在医疗领域的应用是当前AI社区的高热度话题。本文结合了真实临床数据与前沿开源模型（如Llama 3.1, Qwen3, DeepSeek-R1-Qwen等），时效性极强；作者团队包含临床医学专家与AI研究者，具备跨学科权威性。其‘大道至简’的结论若被广泛验证，将对医疗多模态学习社区产生显著影响，推动行业从定制化融合向统一序列化范式转移。

## 项目链接
https://arxiv.org/abs/2607.15380
