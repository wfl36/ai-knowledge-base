# DecodeShare: Tracing the Shared Subspace of LLM Decode-Time Decisions

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 可解释性, 推理, 机制可解释性, 模型控制, 论文  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20469v1 Announce Type: new Abstract: Large language models (LLMs) handle many tasks with one set of parameters, but under KV-cached inference it is unclear what task-general structure, if any, is used at decode time rather than during prefill. We propose DecodeShare, a protocol that identifies a low-dimensional subspace consistently shared across tasks in decode-time hidden states, and then tests its causal role by removing that subspace only during decoding. In our experiments, disturbing the discovered shared subspace degrades decision performance far more than disturbing either a prefill-derived or random subspace under the same intervention budget. We further show this decode-shared subspace has practical consequences for activation steering: common steering directions can overlap the task-general decode channel. Projecting out this shared subspace directly separates the functional roles of the two components, while evaluating steering vectors at decode-time yields more reliable signal for downstream deployment than prefill-based proxies. Despite its compactness, the shared subspace can serve as a high-leverage causal channel at decode time. Code is available at: https://github.com/Zishan-Shao/decodeshare.git.

## 综合总结
本文提出DecodeShare协议，首次揭示了LLM在KV-cached推理的decode阶段存在跨任务共享的低维子空间。通过因果干预实验证明，该共享子空间对模型决策性能的影响远大于prefill阶段或随机子空间，是decode阶段的高杠杆因果通道。研究进一步将该发现应用于激活引导，指出在decode阶段评估引导向量比prefill阶段更可靠，投影掉该子空间可有效分离功能角色。该成果为LLM的机制可解释性和精准控制提供了重要理论依据与实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文在技术深度与新颖性上表现卓越。当前LLM可解释性研究多集中于prefill阶段，而本文敏锐捕捉到KV-cached推理下decode阶段的机制盲区，提出DecodeShare协议以识别decode阶段跨任务共享的低维子空间。研究不仅停留在表征观察，更通过严谨的因果干预（移除子空间）验证了其决定性作用，证明干扰该共享子空间对性能的破坏远超prefill或随机子空间。将理论发现与activation steering结合，揭示了现有prefill评估方法的局限，技术洞见深刻且论证严密。

### 实用性 (评分: 8.0/10)
对LLM可解释性与控制领域的从业者具有极高的实践指导价值。研究明确指出在decode阶段评估steering vectors比传统基于prefill的代理更可靠，并提供了通过投影共享子空间来分离功能角色的具体方法。这为改进representation engineering、模型操控和推理优化提供了直接的技术路径，且作者已开源代码，大幅降低了复现与应用门槛，适用范围覆盖模型对齐、推理加速与机制分析等前沿工程场景。

### 社区活跃度 (评分: 8.5/10)
话题时效性极强，直击当前大模型社区高度关注的机制可解释性与推理阶段内部运作机制。作者团队包含来自知名学术机构的学者，来源权威可信。随着LLM推理优化和模型控制需求激增，揭示decode-time共享子空间的因果机制有望引发广泛关注与后续研究，对社区理解大模型多任务泛化机制具有重要影响力。

## 项目链接
https://arxiv.org/abs/2607.20469
