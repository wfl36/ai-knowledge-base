# Perfect Detection, Failed Control: The Geometry of Knowing vs. Steering in Language Models

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 机制可解释性, 表示工程, AI对齐, 幻觉, 论文  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.24952v1 Announce Type: new Abstract: A central aspiration of mechanistic interpretability is controllability: if we know where a behavior is represented in a model's activations, we should be able to modify it. This rests on a hidden premise -- that the direction which detects a behavior and the direction which controls it are the same, or close. We test this geometrically: what is the angle between the direction that best detects a behavior and the one that best causes it? If detection implies control the cosine is near 1; otherwise it quantifies a detection-intervention gap. On Gemma 2-2B-it, output format (clean JSON vs markdown fencing) collapses both roles onto one axis. Hallucination does not: the model detects fake entities with perfect linear separability (AUC = 1.000 from layer 5), yet that direction sits at cos = 0.12 (about 83 degrees) from the direction producing a refusal -- a small, reproducible alignment, far from the cos = 1 that "detection is control" would require. A detector built from activations, with no chosen tokens, likewise fails to align (cos = -0.06). The gap generalizes: across four models from three families and two scales (1B-9B), cos stays in [0.12, 0.20], identical before and after instruction tuning (0.1197 vs 0.1200), placing its origin in pretraining. A 15-degree rotation toward the refusal direction partially bridges it -- 73% and 60% refusal on two held-out fake-entity categories at 1.8% false positives. We then ask whether this cosine predicts steerability, and it does not: detection is a high-dimensional class, not a single direction, and what separates the steerable case is functional, not readable from a static angle. The cosine is a weight-computable signature of the dissociation between knowing and steering, not a predictor of it.

## 综合总结
本文挑战了机制可解释性中“检测即控制”的核心假设，通过几何视角量化了模型内部行为检测方向与控制方向的分离。研究发现，模型虽能完美检测幻觉，但检测与控制方向的余弦相似度极低（cos=0.12），且该鸿沟源于预训练并广泛存在。研究进一步指出静态角度无法预测可控性，揭示了“知道”与“引导”之间的根本性解耦，对AI对齐与表示工程具有重要理论启示。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
论文从几何视角深入剖析了机制可解释性中“检测即控制”的隐含假设，通过计算最佳检测方向与最佳控制方向的余弦相似度，量化了“检测-干预鸿沟”。研究发现，模型虽能完美线性检测幻觉（AUC=1.0），但检测方向与拒绝控制方向夹角极大（cos=0.12），且该现象跨模型、跨规模普遍存在并源于预训练。进一步论证了余弦相似度并非可控性的预测指标，揭示了检测的高维类别本质，论证严谨，洞见深刻。

### 实用性 (评分: 7.5/10)
对大模型安全对齐和表示工程具有关键的警示与指导价值。它证明了基于线性探测的激活控制方法在特定任务（如抑制幻觉）上可能失效，提示从业者在进行Activation Steering时需区分“可读方向”与“功能方向”。论文提出的旋转干预方法也为弥合检测与控制鸿沟提供了初步的工程思路，但整体偏向理论，直接工程转化需进一步探索。

### 社区活跃度 (评分: 9.0/10)
话题聚焦于当前大模型研究前沿的机制可解释性与模型控制，时效性极强。arXiv论文来源可信，其颠覆性的结论对现有“检测即控制”的社区共识构成挑战，有望在AI安全与对齐领域引发重要讨论与后续研究，具有较高的学术影响力。

## 项目链接
https://arxiv.org/abs/2606.24952
