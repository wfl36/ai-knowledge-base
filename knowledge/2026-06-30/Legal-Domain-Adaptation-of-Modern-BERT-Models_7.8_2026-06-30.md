# Legal Domain Adaptation of Modern BERT Models

**评分：** 7.8  
**状态：** 正常  
**标签：** 大模型, 领域自适应, 法律NLP, 信息检索, 嵌入模型, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28538v1 Announce Type: new Abstract: We investigate domain adaptation of modern BERT models in the legal domain. We further pre-train ModernBERT on all US court opinions using the masked language modeling objective. Although ModernBERT has been trained on roughly 500x more data than original BERT, we still find that this model benefits from further pre-training and domain adaptation in the legal domain: we report significant improvements compared to vanilla ModernBERT on all datasets connected to US court opinions. We find gains similar to those reported in early work on domain adaptation of BERT-like models. However, from scratch pre-training does not match the performance of further pre-training an existing ModernBERT checkpoint in our experiments. The resulting models are capable of processing sequences up to 8,192 tokens, and can be used to compute meaningful embeddings of legal passages, or could quickly rerank hundreds of legal passages for a given search query. We release all model checkpoints publicly.

## 综合总结
本文研究了ModernBERT在法律领域的自适应，通过在美国法院意见书数据上进行继续预训练，发现即使基础模型预训练数据量巨大，领域自适应仍能带来显著性能提升，且效果优于从头训练。开源的模型支持8192 tokens长文本，在法律文本嵌入与检索重排任务中具有极高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
本文将经典的领域自适应方法（继续预训练）应用于最新的ModernBERT模型，验证了即使基础模型已在海量数据上训练（约原版BERT的500倍），在特定垂直领域（法律）进行继续预训练仍能带来显著提升。研究严谨地对比了继续预训练与从头预训练，得出继续预训练效果更优的实证结论，虽然方法本身缺乏颠覆性创新，但为‘大模型时代是否仍需领域自适应’提供了有价值的实验依据。

### 实用性 (评分: 8.5/10)
对法律NLP从业者具有极高的落地参考价值。模型支持8192 tokens的长文本处理，可直接应用于法律文本嵌入计算和检索重排等核心业务场景。作者公开了所有模型检查点，开箱即用，大幅降低了法律领域专用编码器的研发与训练成本。

### 社区活跃度 (评分: 8.0/10)
ModernBERT作为较新的基础模型，针对其进行领域自适应研究具有较好的时效性。法律与AI的交叉领域受关注度持续走高，且作者开源了模型权重，具备较高的来源可信度和社区影响力，能够有效推动法律科技社区的后续研究和应用。

## 项目链接
https://arxiv.org/abs/2606.28538
