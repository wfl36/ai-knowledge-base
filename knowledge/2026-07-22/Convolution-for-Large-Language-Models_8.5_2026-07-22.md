# Convolution for Large Language Models

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 架构优化, 卷积, 注意力机制, 论文  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18413v1 Announce Type: new Abstract: Large language models (LLMs) largely rely on Transformers, where self-attention provides global token interaction but does not explicitly encode the locality of natural language. We study whether lightweight depthwise convolutions can supply this local inductive bias without materially increasing model size. Our macro-level ablation compares convolution at 17 locations in a Qwen3 Transformer block and finds the best results when convolution is applied to the projected queries, keys, and values before attention. A subsequent micro-level study favors a residual depthwise convolution with kernel size $k=3$, without additional normalization or activation. Across Qwen3 models and several pre-training data budgets, this design improves the average accuracy on seven downstream benchmarks while adding less than $0.01\%$ parameters. A representation-level case study further suggests that the convolution makes repeated token IDs more sensitive to their immediate context. These results support depthwise convolution as a lightweight complement to self-attention for modeling short-range token interactions.

## 综合总结
本文研究了在LLM中引入轻量级深度卷积以补充自注意力缺乏的局部归纳偏置。通过详尽的宏观与微观消融实验，发现将核大小为3的残差深度卷积应用于注意力机制前的Q、K、V上效果最佳。该方法仅增加不到0.01%的参数，即可在多个下游任务中稳定提升模型准确率，并增强重复token对上下文的敏感性，是极具落地价值的LLM架构轻量化改进方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
本文针对Transformer自注意力机制缺乏显式局部归纳偏置的问题，深入探索了轻量级深度卷积在LLM中的最优插入位置与配置。研究通过严谨的宏观（17个位置消融）与微观（核大小、残差连接、归一化与激活函数）消融实验，定位了最佳设计（作用于投影后Q/K/V，k=3残差深度卷积），并通过表示层面的案例分析揭示了其使重复token更敏感于上下文的内在机制，论证严谨且具有较好的理论深度。

### 实用性 (评分: 9.0/10)
该方案具有极高的落地价值。其提出的残差深度卷积模块即插即用，仅增加不到0.01%的参数量，几乎不改变模型体积和推理速度，却能在多种参数规模和预训练数据预算下稳定提升7个下游基准的平均准确率。对于大模型研发从业者而言，这是一种成本极低、收益明确的架构改进方案，可直接应用于后续LLM的预训练中。

### 社区活跃度 (评分: 8.5/10)
大模型架构优化是当前AI社区持续关注的核心议题，本文探讨的局部归纳偏置补充极具时效性。作者团队来自华为与清华等知名机构，基于最新的Qwen3模型进行验证，实验规模与数据详实，来源权威且可信度高，对LLM架构设计社区有较强的启发和影响力。

## 项目链接
https://arxiv.org/abs/2607.18413
