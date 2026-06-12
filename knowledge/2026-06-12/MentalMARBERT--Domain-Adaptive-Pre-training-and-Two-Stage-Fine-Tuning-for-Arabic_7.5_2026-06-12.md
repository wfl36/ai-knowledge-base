# MentalMARBERT: Domain-Adaptive Pre-training and Two-Stage Fine-Tuning for Arabic Mental Health Disorders Detection

**评分：** 7.5  
**状态：** 正常  
**标签：** 预训练模型, NLP, 心理健康, 领域自适应, 文本分类, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12649v1 Announce Type: new Abstract: Detecting mental health disorders from Arabic social media text remains challenging due to dialectal variation, informal language, limited high-quality annotated resources, and severe class imbalance. While English mental health natural language processing (NLP) has progressed substantially, Arabic multi-class disorder classification remains insufficiently studied. This study proposes a two-phase framework for Arabic mental health text classification. In phase 1, three Arabic pre-trained language models, AraBERT, CAMeLBERT, and MARBERT, undergo Domain-Adaptive and Task-Adaptive Pretraining (DAPT and TAPT) using a large-scale corpus of unlabeled Arabic mental health tweets. The adapted models are evaluated under a unified protocol to identify the most effective backbone model. In phase 2, the selected model is assessed across four configurations combining single-stage and hierarchical two-stage classification architectures with full fine-tuning and Low-Rank Adaptation (LoRA). To support this study, we constructed a novel annotated Arabic mental health dataset comprising 50,670 tweets across six categories, with strong inter annotator agreement (Krippendorff's Alpha = 0.733, average pairwise agreement = 0.797). Experimental results show that the domain-adapted MARBERT (MentalMARBERT) achieves statistically significant improvements over baseline models in both accuracy and macro-F1. The hierarchical two-stage architecture combined with full fine-tuning achieves the best overall performance, reaching a macro-F1 of 0.861 and an accuracy of 0.877. These findings demonstrate the effectiveness of domain-specific adaptive pretraining and hierarchical classification for Arabic mental health disorder detection.

## 综合总结
本文针对阿拉伯语社交媒体心理健康检测中的方言差异、数据稀缺和类别不平衡挑战，提出了一个两阶段框架。第一阶段通过DAPT和TAPT构建了领域自适应模型MentalMARBERT；第二阶段评估了单阶段与层次化两阶段分类架构及不同微调策略。研究还贡献了一个包含50,670条推文、6个类别的高质量阿拉伯语心理健康数据集。实验表明，MentalMARBERT结合层次化两阶段架构与全量微调取得了最佳效果（macro-F1=0.861），验证了该范式在特定语种垂直领域分类任务中的有效性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
该研究将领域自适应预训练（DAPT/TAPT）与层次化两阶段分类架构系统性地应用于阿拉伯语心理健康文本分类，实验设计严谨，对比了多个骨干模型（AraBERT/CAMeLBERT/MARBERT）及微调策略（全量微调/LoRA）。虽然所用技术均为现有方法的组合，但在阿拉伯语多类别心理障碍分类这一细分领域展现了扎实的论证深度与有效性。

### 实用性 (评分: 8.0/10)
对从业者具有极高的实践指导价值。研究不仅提供了一套清晰的垂直领域适配范式（从预训练模型选择、领域自适应到分类架构设计），还构建并开源了包含5万多条推文、6个类别的阿拉伯语心理健康数据集，可直接用于相关应用的复现、基线对比与二次开发，范式亦可迁移至其他语种或垂直医疗领域。

### 社区活跃度 (评分: 7.0/10)
心理健康NLP与社交媒体分析是当前社区持续关注的热点话题。该论文来源于arXiv，数据集标注规范（Krippendorff's Alpha = 0.733），具备较高的学术可信度。但在大语言模型（LLM）快速发展的背景下，基于BERT架构的微调方法在时效性与影响力上略显局限，更偏向于资源受限场景或传统基线研究。

## 项目链接
https://arxiv.org/abs/2606.12649
