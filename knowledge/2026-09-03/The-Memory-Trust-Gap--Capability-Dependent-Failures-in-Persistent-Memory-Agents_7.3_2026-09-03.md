# The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents

**评分：** 7.3  
**状态：** 正常  
**标签：** Agent, 记忆系统, RAG, 大模型, 安全对齐, 论文, 模型评估  
**更新日期：** 2026-09-03  
**来源：** rss  

## 项目描述
arXiv:2609.01852v1 Announce Type: new Abstract: Persistent memory supports personalized agents, but a stale stored fact can override current authoritative evidence without warning. We study when this harm begins as model capability changes. We evaluate a frozen, closed-set, action-scored benchmark with 2 suites that represent 2 different meanings of "no memory" (a Benefit suite, unsolvable without the stored fact, and a Safety suite, in which an authoritative tool always holds the correct value), on a same-family model-size series (Qwen3 0.6/1.7/4/8B). The Memory Trust Gap reflects over-trust rather than confusion. In the Benefit suite, models answer with the stale value 0.92-1.00 of the time at every scale. In the Safety suite, harm below the no-memory baseline under the trap conditions ($\Delta_{\mathrm{mem}}$) is capability-gated, with the larger models collapsing most once a stale note is made to look current. In a $2\times2\times2\times2$ factorial, which feature triggers over-trust depends on both the feature and model scale. Removing a label amplifies over-trust at every size, and a recency feature (stale dated newer) fools the larger models harder. Source authority is weak and scale-flat, and position changes from positive to negative across the Qwen3 model-size series. We confirm these scale interactions with direct cross-size contrast tests rather than overlapping per-model intervals. Mitigation is likewise capability-dependent: exposing metadata improves accuracy for the capable models, but only pre-resolving the conflict restores accuracy for the 2 smaller checkpoints. The same pattern appears on the capable models in an independent Llama-Instruct model-size series and on 2 external datasets (RGB, MisBench). A framing control finds no consistent advantage for the memory label: at the 3 smaller scales, models trust a stale document more than a stale memory; at 8B, the difference is not significant.

## 综合总结
本文研究持续记忆智能体中一个关键安全问题：当存储事实与当前权威证据冲突时，模型存在'过度信任陈旧记忆'的倾向，且这种信任陷阱呈现明显的模型能力依赖性。通过对Qwen3四个规模及Llama-Instruct系列的受控实验，发现：(1)在需要记忆的任务中模型几乎总是使用陈旧值(0.92-1.00)；(2)安全场景下的记忆伤害Δ_mem具有能力门控效应；(3)不同特征(标签、时效、来源、位置)对过信任的触发作用因模型规模而异；(4)缓解措施同样能力依赖——大模型可通过暴露元数据改善，小模型则需预先消解冲突。该工作为持久记忆智能体的安全设计提供了重要实证基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文系统性地研究了持续记忆智能体中'存储事实覆盖当前权威证据'的信任陷阱，提出了'Memory Trust Gap'概念，并设计2×2×2×2析因实验在Qwen3系列(0.6/1.7/4/8B)及Llama-Instruct上进行跨规模验证。方法学亮点包括：(1)区分Benefit与Safety两种'无记忆'语义；(2)使用跨规模对比检验而非重叠区间；(3)考虑标签移除、时效特征、来源权威性、位置等多种特征交互；(4)提出Δ_mem量化陷阱条件下记忆带来的伤害。研究发现记忆过度信任是能力依赖型的，且不同特征触发的过信任取决于模型规模，这一发现新颖且论证严谨。

### 实用性 (评分: 7.5/10)
对构建生产级持久记忆智能体的工程师具有直接指导意义：(1)揭示了'暴露元数据仅对大模型有效，小模型需预先消解冲突'这一关键实践准则；(2)明确了'陈旧记忆的标签移除会放大过信任'，提示系统设计需谨慎处理记忆元信息；(3)跨模型族、跨数据集(RGB、MisBench)的泛化结果增强了结论可信度；(4)但研究为受控基准评估，真实场景中记忆冲突模式更复杂，实际落地仍需进一步验证。对智能体安全与记忆管理模块的设计有较高参考价值。

### 社区活跃度 (评分: 6.5/10)
话题高度契合当前Agent与LLM记忆系统研究的热点前沿(2025-2026年记忆架构、RAG长期记忆是核心议题)，但arXiv ID显示为2609.01852(2026年9月)，发布日期存疑，权威性需谨慎对待。来源为单一研究小组的预印本，尚未显示顶会接收信号。作者来自学术机构(Jundong Hu, Shekar Ramachandran)，但社区影响力尚未充分发酵。作为新发布工作，时效性极强但传播度有限。

## 项目链接
https://arxiv.org/abs/2609.01852
