# SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision

**评分：** 9.2  
**状态：** 正常  
**标签：** 大模型, 知识蒸馏, LLM训练, 强化学习, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28562v1 Announce Type: new Abstract: On-policy distillation (OPD) has a property absent in offline distillation and RL: teacher supervision quality depends on student competence. Incoherent rollouts yield noisy gradients; already-mastered tokens yield redundant ones. This creates waste at three scales (tokens, training phases, and prompts) yet existing methods supervise uniformly. We introduce SEAD, which uses entropy as a unified probe of this competence-dependent degradation at three scales: (1) joint teacher-student entropy partitions tokens into zones receiving tailored divergences or zero gradient (approx. 50% skipped); (2) a cosine schedule anneals from forward to reverse KL as competence grows; (3) a competence-gated curriculum introduces prompts easy-to-hard. These components are symbiotically necessary: token selection requires coherent rollouts (curriculum), annealing requires monotonic improvement (also curriculum). On OLMo-3 (7B to 32B), SEAD achieves +4.8 avg accuracy over vanilla OPD across six math benchmarks, with ablations confirming super-additive interactions.

## 综合总结
本文提出SEAD方法，针对On-policy蒸馏中教师监督质量受限于学生能力的问题，利用熵作为统一探针，在token、训练阶段和prompt三个尺度实现能力感知的动态监督与优化。该方法通过跳过冗余计算、动态KL退火和课程学习，在OLMo-3 (7B-32B)上实现了平均+4.8的准确率提升，并大幅节省了计算开销，具有极高的理论与工程价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文深刻揭示了On-policy蒸馏中“教师监督质量受限于学生能力”的核心痛点，创新性地引入熵作为统一探针，在token（零梯度/定制散度）、训练阶段（前向至反向KL退火）和prompt（易到难课程）三个尺度实现能力感知的动态监督。组件间的共生必要性及超加性消融实验进一步彰显了其理论深度与严谨性。

### 实用性 (评分: 9.5/10)
极具工程落地价值。SEAD通过跳过约50%的冗余token计算，显著降低了On-policy蒸馏的训练算力成本；同时在大规模模型（7B至32B）上取得显著的精度提升（+4.8 avg），直接回应了工业界大模型蒸馏中的算力与效果平衡痛点，可无缝集成至现有LLM训练流程中。

### 社区活跃度 (评分: 9.0/10)
话题处于大模型蒸馏与训练优化的前沿热点，发布时间新，具有极强的时效性。基于OLMo-3等主流大模型的大规模实验验证及详尽的消融分析，赋予了该工作极高的学术可信度，有望在LLM训练与推理优化社区产生广泛影响。

## 项目链接
https://arxiv.org/abs/2606.28562
