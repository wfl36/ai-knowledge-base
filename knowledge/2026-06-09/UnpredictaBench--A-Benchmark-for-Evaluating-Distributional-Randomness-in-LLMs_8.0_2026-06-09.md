# UnpredictaBench: A Benchmark for Evaluating Distributional Randomness in LLMs

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 评估基准, 分布采样, 社会模拟, Agent, 论文  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.06622v1 Announce Type: new Abstract: We introduce UnpredictaBench, an evaluation that tests the ability of large language models (LLMs) to capture true underlying distributions. As LLMs are increasingly used as substitutes for other entities (e.g., for humans in economic simulations), the tendency of many models to collapse towards a single plausible answer means a failure to capture the unpredictability of real systems. Recent work on improving output diversity is insufficient for this setting: simulation requires samples that are calibrated to a target distribution, not merely varied outputs. UnpredictaBench isolates a simplified but fundamental version of this problem: sampling outcomes from individual target distributions, including canonical statistical distributions, distributions induced by stochastic programs, and natural-language scenarios that describe random processes. We introduce 448 such problems together with KS@N, a general-purpose evaluation metric that quantifies how well a model outputs approximate black-box target distributions via the Kolmogorov-Smirnov statistical test. This is the rate at which we fail to reject model samples of size N against ground-truth samples, with larger N indicating greater difficulty. Tested across open and proprietary models, we find a large spread in distributional capabilities. For instance, when models generate samples of size 100 (KS@100, our standard metric), scores range from near 0 to over 20%. No model is able to achieve over 40% at KS@100, showing significant headroom in distributional sampling as a capability. Although adding reasoning can somewhat increase scores, we find no immediate solution for this issue. UnpredictaBench shows that even simple distributional simulation remains challenging, making it a necessary first step toward using LLMs as stand-ins for complex systems.

## 综合总结
UnpredictaBench提出了一种评估大语言模型捕获真实底层分布能力的新基准，揭示了LLM在作为复杂系统替代品时存在的“分布坍缩”问题。该研究区分了“输出多样性”与“分布校准”的差异，构建了448个涵盖统计分布、随机程序和自然语言场景的测试问题，并引入基于KS检验的KS@N指标进行量化评估。实验表明，当前主流模型在分布采样上表现不佳（KS@100最高得分不足40%），即使引入推理能力也无法根本解决，凸显了LLM在真实系统不可预测性模拟上的巨大挑战与提升空间。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文精准指出了当前LLM在作为模拟代理时的核心缺陷——分布坍缩，并清晰区分了“输出多样性”与“分布校准”在模拟场景下的本质差异。提出的KS@N指标基于Kolmogorov-Smirnov检验，为量化模型拟合黑盒目标分布的能力提供了严谨的统计学基础，问题定义和方法论具有很高的新颖性和学术深度。

### 实用性 (评分: 7.5/10)
对于从事LLM社会模拟、经济仿真和Agent行为建模的研究者与工程师具有极高的参考价值。KS@N指标和448个测试问题可直接复用于评估和筛选模型。但当前所有模型表现均不佳（最高不足40%），说明短期内难以在需要高保真分布拟合的复杂系统模拟中完美落地，该基准更多是指出问题而非提供即插即用的解决方案。

### 社区活跃度 (评分: 8.0/10)
LLM作为模拟器替代人类或其他实体是当前Agent与多智能体系统研究的前沿热点，话题时效性极强。作者来自UBC等知名学术机构，具备较高的权威性。该基准填补了LLM分布拟合能力评估的空白，且实验揭示的当前顶级模型在分布采样上的严重不足具有较强警示意义，有望引发社区的广泛讨论与跟进。

## 项目链接
https://arxiv.org/abs/2606.06622
