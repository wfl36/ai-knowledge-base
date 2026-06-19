# Pruning via Causal Attribution Preserves Reasoning Performance in Large Language Models

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 推理, 模型压缩, 剪枝, 因果推断, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19350v1 Announce Type: new Abstract: Large language models (LLMs) excel at multi-step reasoning but incur substantial inference cost. We introduce Causal Attribution Pruning (CAP), a training-free method that identifies critical attention heads by measuring their causal impact on reasoning tasks and uses these head-level scores to guide fine-grained weight pruning. For each attention head, CAP estimates the expected performance degradation when the head is masked during forward passes on a small calibration set of reasoning problems. These causal scores are then converted into weight-level importance values for the corresponding projection matrices. Unlike magnitude-only or activation-based criteria, CAP's interventional measurement directly captures each head's functional contribution, yielding relative accuracy gains of up to 61% over Wanda on ARC-Challenge at 20% sparsity. We evaluate CAP on GSM8K, StrategyQA, and ARC-Challenge using Llama-3-8B-Instruct and Mistral-7B-Instruct at 10%, 20%, and 50% sparsity. At moderate sparsity (10-20%), CAP improves over Wanda in most model-benchmark configurations. with especially large gains on ARC-Challenge for Llama-3. Our results suggest that attention-head-level causal attribution can better preserve reasoning performance on downstream benchmarks than correlational pruning criteria at equivalent sparsity, while remaining limited by coarse MLP attribution at 50% sparsity.

## 综合总结
本文提出了一种免训练的因果归因剪枝方法（CAP），通过评估注意力头对推理任务的因果影响来指导细粒度权重剪枝。与基于相关性的传统剪枝方法不同，CAP通过干预测量直接捕获功能贡献。在Llama-3和Mistral上的实验表明，在10-20%稀疏度下，CAP在GSM8K、StrategyQA和ARC-Challenge等推理基准上优于Wanda，尤其在ARC上实现了高达61%的相对准确率提升，为在降低大模型推理成本的同时保持推理能力提供了有效方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.2/10)
提出了一种基于因果归因的剪枝方法（CAP），通过干预式测量（前向传播中掩码注意力头）评估其对推理任务的因果影响，并将头级分数转化为权重级重要性。相比仅基于幅度或激活值的关联性剪枝标准，该方法更精准地捕获了各组件的功能贡献，论证严谨，且诚实指出了50%稀疏度下MLP归因粗糙的局限性，技术深度与创新性兼具。

### 实用性 (评分: 7.8/10)
对大模型推理部署降本具有较高参考价值。CAP无需重训练，仅需少量校准集即可实施，工程落地门槛适中。在10-20%中等稀疏度下能显著保持甚至提升推理准确率，适用于Llama、Mistral等主流大模型架构，但在极高稀疏度（50%）下效果受限，实际应用中需结合具体业务对稀疏度和精度的要求进行取舍。

### 社区活跃度 (评分: 8.7/10)
话题极具时效性，直击大模型推理成本高昂与剪枝后推理能力严重退化这一行业痛点。arXiv新发论文，基于主流开源模型和权威推理基准测试，数据可信度高。在ARC-Challenge上相对Wanda最高61%的准确率提升极为亮眼，预计将在模型压缩与高效推理社区引起较大关注与后续讨论。

## 项目链接
https://arxiv.org/abs/2606.19350
