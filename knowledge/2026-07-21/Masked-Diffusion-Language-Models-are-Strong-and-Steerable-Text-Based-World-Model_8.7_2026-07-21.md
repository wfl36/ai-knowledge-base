# Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 强化学习, 世界模型, 扩散模型, MDLM, 论文  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16204v1 Announce Type: new Abstract: Recent growth in reinforcement learning (RL) has surfaced a need for diverse, specialized training environments. Hand-curated environments with fixed task and reward difficulties become ineffective signals as model performance improves, and sparse rewards over long horizons induce mode collapse on specific workflows or tool structures. World models that simulate environment states have matched pure rollout performance, making them promising for scaling diversity on-demand. However, autoregressive (AR) world models suffer from a left-to-right bias preventing conditioning on globally interdependent state anchors such as tool schemas, prior turns, and expected outcomes. We (i) formalize text-based world modeling as a steerable transition-dynamics problem decomposed into initial state, task context, tool schemas, domain rules, and steering directives, and (ii) curate 239,403 grounded state-action trajectories spanning nine open-source environments and twelve frontier model families. We compare AR LMs and masked diffusion language models (MDLMs), showing MDLMs, via bidirectional anchor-aware denoising, achieve better coherence, groundedness, and empirically validated rollout diversity than LLMs over 4x their parameter size, at comparable inference latency. We introduce a plug-and-play GRPO training framework with deterministic state checks, and perform zero-shot transfer ablations on three OOD environments (ScienceWorld, ALFWorld, AppWorld) across three 1.2B-7B agent backbones (LFM2.5, Qwen3, Mistral), achieving up to 47% absolute gains over baselines without environment-specific fine-tuning. We further conduct behavioral analysis of failure modes under adversarial scenarios and human evaluation on realism, outcome correctness, and training utility. We open-source our work to encourage research in this direction.

## 综合总结
本文提出将掩码扩散语言模型（MDLM）作为基于文本的世界模型，用于智能体强化学习训练。针对自回归模型存在的从左到右偏差，MDLM通过双向锚点感知去噪实现了更好的全局状态依赖和生成多样性，在性能上超越4倍参数量的LLM。研究形式化了可引导的转移动力学问题，引入带确定性状态检查的GRPO框架，在多个OOD环境实现零样本最高47%的性能提升，并开源了大规模轨迹数据集，为智能体训练环境扩展提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
创新性地将掩码扩散语言模型（MDLM）应用于基于文本的世界模型，解决了自回归模型（AR）固有的从左到右偏差问题。通过双向锚点感知去噪机制，MDLM在连贯性、接地性和多样性上超越了4倍参数量的LLM。同时形式化了可引导的转移动力学问题，并引入带确定性状态检查的GRPO训练框架，理论严谨且实验论证充分。

### 实用性 (评分: 8.5/10)
对RL智能体训练具有极高的实用价值。提供了即插即用的GRPO训练框架，并在3个OOD环境和3个主流骨干网络上实现了零样本迁移（最高47%的绝对提升），无需特定环境微调。开源了23.9万条轨迹数据集，极大缓解了RL训练中环境多样性和稀疏奖励的痛点。

### 社区活跃度 (评分: 8.5/10)
紧扣当前AI智能体与强化学习热点，提出用扩散模型替代自回归模型构建世界模型的新范式。arXiv新发论文，数据集规模庞大（9个环境，12个前沿模型家族），包含人类评估和对抗性分析，来源可信且极具引发社区跟进研究的潜力。

## 项目链接
https://arxiv.org/abs/2607.16204
