# OriginBlame: Record- and Token-Level Data Provenance for AI Training Datasets

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 数据溯源, 机器遗忘, 数据合规, 隐私保护, 论文  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.13037v1 Announce Type: new Abstract: When a data contributor requests removal, model trainers face a practical gap: unlearning algorithms require a forget set, yet no tool can locate which training records belong to a given author. Existing provenance systems operate at file or dataset level, forcing catastrophic over-deletion. We present ob, a record- and token-level data provenance system that propagates author identity through data processing pipelines and resolves revocation requests into precise forget sets via deterministic queries. Evaluation on 219,555 Wikipedia pages demonstrates that record-level provenance eliminates dataset-level over-deletion (from 101x to 1.3x), while integration adds 1.3-4.0% throughput overhead (HuggingFace) and 2.1-19.0% (Datatrove) on wiki data. On a 1.7B model, provenance-based forget sets improve unlearning by 42% over random baselines.

## 综合总结
该论文提出了OriginBlame (ob)，一种针对AI训练数据的记录级和Token级数据溯源系统，旨在解决数据撤销请求中的过度删除问题。通过在数据处理管道中传播作者身份，系统能将撤销请求精准解析为遗忘集。实验表明，该系统将过度删除率从101倍降至1.3倍，在主流数据处理框架中引入的吞吐量开销极低（1.3%-19.0%），并在1.7B模型上使机器遗忘效果提升了42%，为大模型数据合规与隐私保护提供了高效且可落地的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文针对大模型数据遗忘中的过度删除痛点，创新性地提出了记录级和Token级的数据溯源机制，突破了现有系统仅支持文件或数据集级溯源的局限。技术实现上，通过在数据处理管道中传播作者身份信息，结合确定性查询精准定位遗忘集，论证严谨且量化指标详实（过度删除率从101x降至1.3x，遗忘效果较随机基线提升42%），系统开销控制在较低水平（1.3%-19.0%），展现了较高的技术深度与新颖性。

### 实用性 (评分: 9.0/10)
对AI从业者及企业具有极高的落地指导价值。随着数据隐私法规（如GDPR）的收紧，模型精准遗忘特定贡献者数据成为刚需。该系统在HuggingFace和Datatrove等主流数据处理框架上开销极低，可直接集成至现有大模型训练流水线中，有效避免因粗粒度删除导致的模型性能灾难性下降，为数据合规与版权保护提供了切实可行的工程方案。

### 社区活跃度 (评分: 8.0/10)
话题极具时效性，数据溯源与机器遗忘是当前大模型合规与安全领域的核心热点。arXiv预印本来源具备一定权威性，且直击行业痛点，预计将在AI安全与数据治理社区产生较大影响力。不过作为单一作者的新发表预印本，其长期影响力仍需等待同行评审与更广泛的社区验证。

## 项目链接
https://arxiv.org/abs/2607.13037
