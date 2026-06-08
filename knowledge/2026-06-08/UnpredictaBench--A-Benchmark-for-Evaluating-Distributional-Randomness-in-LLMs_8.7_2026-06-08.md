# UnpredictaBench: A Benchmark for Evaluating Distributional Randomness in LLMs

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 评估基准, 模拟, 分布采样, 随机性, 论文  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06622v1 Announce Type: new Abstract: We introduce UnpredictaBench, an evaluation that tests the ability of large language models (LLMs) to capture true underlying distributions. As LLMs are increasingly used as substitutes for other entities (e.g., for humans in economic simulations), the tendency of many models to collapse towards a single plausible answer means a failure to capture the unpredictability of real systems. Recent work on improving output diversity is insufficient for this setting: simulation requires samples that are calibrated to a target distribution, not merely varied outputs. UnpredictaBench isolates a simplified but fundamental version of this problem: sampling outcomes from individual target distributions, including canonical statistical distributions, distributions induced by stochastic programs, and natural-language scenarios that describe random processes. We introduce 448 such problems together with KS@N, a general-purpose evaluation metric that quantifies how well a model outputs approximate black-box target distributions via the Kolmogorov-Smirnov statistical test. This is the rate at which we fail to reject model samples of size N against ground-truth samples, with larger N indicating greater difficulty. Tested across open and proprietary models, we find a large spread in distributional capabilities. For instance, when models generate samples of size 100 (KS@100, our standard metric), scores range from near 0 to over 20%. No model is able to achieve over 40% at KS@100, showing significant headroom in distributional sampling as a capability. Although adding reasoning can somewhat increase scores, we find no immediate solution for this issue. UnpredictaBench shows that even simple distributional simulation remains challenging, making it a necessary first step toward using LLMs as stand-ins for complex systems.

## 综合总结
本文提出了UnpredictaBench，首个专门评估大语言模型捕捉真实底层分布能力的基准。研究指出，LLM在模拟复杂系统时存在收敛至单一答案的倾向，现有的输出多样性方法无法满足分布校准的需求。作者构建了448个测试问题，并引入基于KS检验的KS@N指标量化模型逼近目标分布的能力。实验表明，当前所有模型在分布采样上表现极差（KS@100最高不超过40%），即使引入推理机制也无法根本解决。该研究揭示了LLM在真实随机性模拟上的核心缺陷，为LLM驱动的仿真应用敲响了警钟并提供了关键评估工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文提出了深刻且新颖的洞见：区分了LLM的'输出多样性'与'分布校准性'，指出当前LLM在作为复杂系统（如人类行为）的模拟替代品时，倾向于收敛至单一合理答案，从而无法捕捉真实世界的随机性。技术上，创新性地引入了基于Kolmogorov-Smirnov统计检验的KS@N评估指标，严谨地量化了模型输出逼近黑盒目标分布的能力，并构建了448个涵盖统计分布、随机程序和自然语言场景的测试集，论证充分且揭示了当前模型在分布采样上的根本性瓶颈。

### 实用性 (评分: 8.0/10)
对从事社会模拟、经济仿真和Agent-based modeling的从业者具有极高的指导价值。它明确警示了直接使用LLM替代人类进行随机模拟的风险，并提供了一套可量化的评估工具（KS@N及448个测试问题），可用于筛选和评估适合模拟任务的模型。虽然适用场景相对垂直，但在LLM驱动的复杂系统模拟领域，其落地参考价值无可替代。

### 社区活跃度 (评分: 9.0/10)
话题极具时效性，切中了当前LLM作为世界模拟器驱动多智能体交互的前沿热点。研究结论（当前最强模型在KS@100上得分均不超过40%）对社区具有强烈的警示意义。来源为arXiv学术论文，作者团队具备学术公信力，该基准有望成为评估LLM分布采样能力的标准工具，对后续大模型在仿真领域的发展产生深远影响。

## 项目链接
https://arxiv.org/abs/2606.06622
