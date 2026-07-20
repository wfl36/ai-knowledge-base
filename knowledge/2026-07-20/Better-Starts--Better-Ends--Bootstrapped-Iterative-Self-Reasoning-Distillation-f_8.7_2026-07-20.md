# Better Starts, Better Ends: Bootstrapped Iterative Self-Reasoning Distillation for Compressed Reasoning

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 推理, 模型压缩, 蒸馏, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15736v1 Announce Type: new Abstract: Large reasoning models often solve problems through long chain-of-thought (CoT) traces, yet much of this computation is spent on redundant derivations, repeated self-verification, and detours that do not improve the final answer. Existing on-policy self-distillation methods reduce this cost by matching a student model to a concise copy of itself on prefixes sampled from the student's own rollouts. We show that this objective has an initialization bottleneck. Since supervision is applied only to visited prefixes, training from a verbose base model places the KL loss on contexts that are often noisy, redundant, or already off track. In such regions, a concise teacher can provide only local corrections, while the student continues to explore trajectories that an efficient reasoner should avoid. In this paper, we propose BIRD(Bootstrapped Iterative Self-Reasoning Distillation), a two-stage self-reasoning distillation method that improves the rollout distribution before on-policy training. BIRD first samples concise solutions from the base model under a brevity instruction, keeps only answer-correct traces, and performs a lightweight prompt-switch SFT step. The traces are generated with the brevity instruction but learned under the original task prompt, turning instruction-induced conciseness into a default reasoning behavior. Starting from this warm model, BIRD then applies on-policy reverse-KL distillation with a concise self-teacher, now on cleaner and more informative prefixes. Across Qwen3 series models, BIRD achieves a stronger accuracy-efficiency trade-off than prompting and cold-start on-policy distillation on MATH-500 and AIME benchmarks. On Qwen3-8B, it improves MATH-500 accuracy from 86.2% to 92.0% while reducing the average response length from 3,099 to 1,115 tokens. These results highlight prefix support as a central factor in efficient reasoning distillation.

## 综合总结
本文指出现有on-policy自蒸馏在压缩推理链时存在初始化瓶颈，导致模型难以逃离冗余推理轨迹。为此提出BIRD方法，先通过prompt-switch SFT将简洁性内化为默认行为作为热启动，再进行on-policy reverse-KL蒸馏。实验表明，BIRD在Qwen3-8B上不仅将平均响应长度从3099缩短至1115，还将MATH-500准确率从86.2%提升至92.0%，实现了推理效率与准确率的双赢。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
针对现有on-policy自蒸馏在压缩推理时存在的“初始化瓶颈”进行了深入分析，指出冗余初始模型产生的噪声prefix限制了局部纠正的效果。提出两阶段的BIRD方法，先通过prompt-switch SFT将指令诱导的简洁性内化为默认推理行为作为热启动，再进行on-policy reverse-KL蒸馏。理论分析深刻，方法设计逻辑严谨且具有新颖性。

### 实用性 (评分: 9.0/10)
直接解决大模型长链推理成本高昂的工业界痛点，两阶段训练流程清晰且易于在现有模型训练管线中实现。实验数据亮眼，在大幅缩短推理长度（降低64%）的同时反而提升了准确率，打破了常规的长度-准确率权衡，对推理模型的实际部署和成本控制具有极高的指导价值。

### 社区活跃度 (评分: 8.5/10)
探讨当前极受关注的大模型推理冗余与CoT压缩问题，极具时效性。提出的方法在Qwen3系列模型上取得了效率与准确率双重提升的显著效果，容易引起学术界和工业界的广泛关注。来源为arXiv学术预印本，具备较高的权威性与影响力。

## 项目链接
https://arxiv.org/abs/2607.15736
