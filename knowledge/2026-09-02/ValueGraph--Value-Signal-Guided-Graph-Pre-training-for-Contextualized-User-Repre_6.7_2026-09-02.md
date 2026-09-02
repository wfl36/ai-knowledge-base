# ValueGraph: Value-Signal Guided Graph Pre-training for Contextualized User Representation

**评分：** 6.7  
**状态：** 正常  
**标签：** 用户表征, 图预训练, 对比学习, 社交媒体分析, 价值对齐, 论文  
**更新日期：** 2026-09-02  
**来源：** rss  

## 项目描述
arXiv:2609.00057v1 Announce Type: new Abstract: Value signals are aggregated user-level moral representations that capture users' inferred value-related tendencies from their online discourse. User behavior on social media is shaped not only by what users say or whom they interact with, but also by the value signal through which they express attitudes. Existing user representation methods largely miss this value-relevant dimension. We propose ValueGraph, a graph pre-training framework that uses automatically inferred moral-value signals as noisy auxiliary signals for contextualized user representation. From post-reply graphs, ValueGraph learns semantic and structural representations and further aligns users through relative value similarity with contrastive and clustering objectives. Rather than treating inferred values as gold psychological labels, ValueGraph uses them as soft constraints for representation learning. Experiments on stance detection and twitter bot detection show consistent gains over strong text-based, graph-based, and text-only LLM baselines, highlighting value-signal guidance as a useful inductive bias for socially informed user modeling.

## 综合总结
ValueGraph 提出了一种利用自动推断的道德价值信号引导图预训练的用户表征学习方法，将价值信号作为软约束而非金标签，结合对比学习与聚类目标在 post-reply 图上学习用户表征。在立场检测和 Twitter 机器人检测任务上优于文本、图及 LLM 基线，展示了价值信号作为归纳偏置的实用价值。方法思路清晰、实验充分，但在创新深度上与现有属性辅助信号方法有相似性，且存在元数据异常，需谨慎评估其可信度。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
文章提出 ValueGraph，将自动推断的道德价值信号作为噪声辅助信号融入图预训练框架，用于上下文用户表征学习。技术贡献体现在：(1) 将价值信号视为软约束而非心理标签，避免了标签噪声问题；(2) 结合对比学习和聚类目标，通过相对价值相似度对齐用户；(3) 在 post-reply 图上联合学习语义与结构表征。方法设计具有较好的理论动机，但在创新深度上，将价值信号作为归纳偏置的思路与现有基于属性/人口统计的辅助信号方法存在一定相似性，缺乏对图预训练范式本身的根本性突破。

### 实用性 (评分: 6.5/10)
实验在 stance detection 和 Twitter bot detection 两个下游任务上验证，相对文本基线、图基线以及纯文本 LLM 基线均取得一致提升，表明方法具有较好的实际效果。代码与数据若公开可复现，对社交媒体分析、舆情检测、虚假账号识别等领域的从业者有直接参考价值。但价值信号的自动推断质量依赖上游模型，部署时存在传递性偏差风险，且应用场景主要集中在社交媒体分析，适用范围有一定局限。

### 社区活跃度 (评分: 6.5/10)
论文聚焦用户表征学习与社交媒体分析，属于 NLP 与社交计算的交叉热点话题。arxiv ID 为 2609.00057（注：arXiv ID 格式异常，可能为 2509.00057 之误），发布时间标注为 2026 年（疑似元数据异常），需进一步核实。从话题本身看，用户表征与价值对齐是当前 AI 伦理与社会计算领域受到较多关注的方向，但论文尚未显示顶会发表信息或广泛引用，权威性与影响力尚需观察。

## 项目链接
https://arxiv.org/abs/2609.00057
