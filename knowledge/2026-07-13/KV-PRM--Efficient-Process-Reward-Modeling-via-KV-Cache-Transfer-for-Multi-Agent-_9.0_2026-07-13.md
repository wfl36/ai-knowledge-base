# KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling

**评分：** 9.0  
**状态：** 正常  
**标签：** 大模型, 推理, Agent, 过程奖励模型, KV-Cache, 论文  
**更新日期：** 2026-07-13  
**来源：** rss  

## 项目描述
arXiv:2607.09153v1 Announce Type: new Abstract: Process Reward Models (PRMs) have been proven to be highly effective in guiding test-time scaling (TTS) methods, which significantly boost the capabilities of LLM-based multi-agent systems. However, existing PRMs are text-based: they re-encode the entire trajectory text from scratch. In long multi-agent rollouts, the scoring cost, growing quadratically with respect to sequence length L, creates a severe computational bottleneck, severely limiting PRMs' application in long-context scenarios. To resolve this, we introduce KV-PRM, a highly efficient process reward model that eliminates the heavy text re-encoding by directly reading the KV cache produced naturally during the LLM's generation phase. By processing a single "verify token" against the pre-existing KV cache, KV-PRM reduces the scoring cost from O(L^2) to O(L). We formally prove that the KV cache contains strictly greater information capacity than text, and is more efficient for downstream reward modeling. Empirically, across the MATH, GSM8K, and AIME benchmarks, KV-PRM matches or strictly outperforms text-PRMs under various TTS methods such as Beam Search, MCTS, and Weighted Voting, with up to a 5,000x reduction in scoring FLOPs, a 37x reduction in latency, and a 34x reduction in per-sequence memory footprint compared to text-based PRMs.

## 综合总结
本文针对现有过程奖励模型（PRM）在长多智能体推理中因重新编码文本导致计算成本呈二次方增长的瓶颈，提出了KV-PRM。该方法直接复用LLM生成阶段的KV Cache，通过插入单个验证token进行评分，将计算复杂度从O(L^2)降至O(L)。理论上证明了KV Cache比文本具有更大的信息容量；实验表明，在MATH等基准上，KV-PRM不仅性能匹配或超越传统PRM，还实现了高达5000倍的FLOPs降低、37倍的延迟降低和34倍的内存节省，极大提升了PRM在长上下文场景下的可用性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文提出了一种极具洞见的系统级算法创新，将过程奖励模型（PRM）的输入从纯文本转换为LLM生成阶段自然产生的KV Cache。通过引入单个'verify token'直接复用缓存，成功将评分的计算复杂度从O(L^2)降至O(L)。同时，作者从信息论角度严格证明了KV Cache比纯文本具有更大的信息容量，理论论证严谨，技术深度极高。

### 实用性 (评分: 9.5/10)
该工作对大模型推理扩展实践具有极高的指导价值。在MATH、GSM8K等基准测试中，KV-PRM不仅性能匹配甚至超越传统文本PRM，更带来了高达5000倍的FLOPs降低、37倍的延迟降低和34倍的内存节省。这使得在长上下文和多智能体场景下部署PRM变得切实可行，可直接应用于Beam Search、MCTS等主流推理扩展框架中。

### 社区活跃度 (评分: 8.5/10)
Test-Time Scaling (TTS) 和过程奖励模型（PRM）是当前大模型推理领域的核心热点。本文精准切中了长序列和多智能体场景下PRM计算成本过高的痛点，提出的解决方案极具颠覆性。虽然作为最新发布的arXiv论文尚需更广泛的社区复现验证，但其展现出的性能提升和成本缩减足以引发学术界和工业界的高度关注。

## 项目链接
https://arxiv.org/abs/2607.09153
