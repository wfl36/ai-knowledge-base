# Procedural Memory Distillation: Online Reflection for Self-Improving Language Models

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 强化学习, 自我进化, 推理, 知识蒸馏, 论文  
**更新日期：** 2026-07-03  
**来源：** rss  

## 项目描述
arXiv:2607.01480v1 Announce Type: new Abstract: Reinforcement learning with verifiable rewards (RLVR), along with recent selfdistillation variants such as SDPO, evaluates each rollout against a verifier and updates the policy from that episode-level signal. However, the richer procedural information in the rollout is rarely retained or reused. Across episodes and epochs, the model repeatedly encounters related problems under a changing policy, producing cross-episode signals that episode-local updates cannot capture: which strategies consistently pass verification, which failure modes persist, which patterns recur. We propose Procedural Memory Distillation (PMD), which converts these crossepisode signals into reusable procedural memory and distills it into the policy's weights during training. This memory functions as a training scaffold, absorbed into the policy itself, yielding a memory-free model at inference. PMD organizes the memory at three levels of abstraction: raw trajectories, self-reflected strategies and lessons, and higher-level behavioral patterns that recur across problems, all extracted online from the model's own trajectories. A memory-conditioned self-teacher draws on the accumulated experience to supervise the student on its own rollouts, enabling student to progressively internalize procedural knowledge within its parameters. The central design principle is co-evolution: the policy generates rollouts that update the memory, and memory shapes the supervision that updates the policy. Empirically, across Qwen3-8B and OLMo3-Instruct-7B, PMD improves over SDPO by 3.8-5.5% on SCIKNOWEVAL and 7.9-13.6% on LIVECODEBENCH. Co-evolution powers these gains: freezing either the memory or the policy trails PMD by more than 10% across SCIKNOWEVAL domains.

## 综合总结
本文提出过程记忆蒸馏（PMD），旨在解决现有RLVR方法无法复用跨episode过程信息的问题。PMD通过三层抽象（轨迹、反思、高层模式）在线提取过程记忆，并利用记忆条件自教师将知识内化至模型权重，实现推理时零记忆开销。其核心设计为策略与记忆的协同进化机制。实验表明，PMD在科学推理和代码基准上较SDPO显著提升（最高13.6%），且消融实验证实了协同进化机制的不可或缺性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文提出了过程记忆蒸馏（PMD），创新性地解决了强化学习验证（RLVR）及自蒸馏变体（如SDPO）中跨episode过程信号被忽略的问题。PMD通过三层抽象（原始轨迹、自我反思的策略与教训、跨问题的高层行为模式）在线提取并组织记忆，利用记忆条件自教师将过程知识内化至模型权重，且推理时无需额外记忆模块。其核心的'策略-记忆协同进化'设计（策略生成轨迹更新记忆，记忆塑造监督更新策略）论证严谨，消融实验充分验证了该机制的关键作用，技术深度与新颖性极高。

### 实用性 (评分: 8.0/10)
PMD在推理阶段不引入额外记忆开销，对工程部署非常友好。该方法可直接嵌入现有的RLVR训练流程中，显著提升模型在科学推理和代码生成等复杂任务上的表现（最高提升13.6%）。虽然在线反思与记忆更新机制可能增加训练阶段的算力消耗和工程实现复杂度，但其带来的显著性能收益和免推理开销的特性，对大模型训练团队具有极高的实践指导价值。

### 社区活跃度 (评分: 8.5/10)
该论文聚焦于大模型自我进化与强化学习训练（RLVR），属于当前AI社区极具时效性和热度的前沿方向。作者团队在相关领域具有权威性，实验采用了最新的开源模型（Qwen3-8B, OLMo3-Instruct-7B）和主流高难度基准（LIVECODEBENCH, SCIKNOWEVAL），结果扎实且提升显著。尽管目前为预印本，但其突破性的自进化训练范式有望在学术界和工业界产生广泛影响力。

## 项目链接
https://arxiv.org/abs/2607.01480
