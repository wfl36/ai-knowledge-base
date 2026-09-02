# From Detection to Refusal: Safer LLMs via Circuit-Guided Weight Scaling

**评分：** 7.6  
**状态：** 正常  
**标签：** 大模型, 安全对齐, 可解释性, 机制可解释性, 对抗鲁棒性, 论文  
**更新日期：** 2026-09-02  
**来源：** rss  

## 项目描述
arXiv:2609.00051v1 Announce Type: new Abstract: Despite extensive alignment efforts, Large Language Models (LLMs) remain vulnerable to generating unsafe content under adversarial prompting, yet the internal mechanisms by which safety behaviors are implemented remain poorly understood. We study LLM safety from a mechanistic interpretability perspective and characterize a multi-stage *safety circuit* that organizes refusal behavior, consisting of (i) $\textbf{Harmful Detection Heads}$ that respond to harmful inputs, (ii) $\textbf{Safety Neurons}$ that mediate and stabilize safety signals in the residual stream, and (iii) $\textbf{Refusal Heads}$ that translate these signals into safe response generation. Using targeted attention-head and neuron-level interventions, we provide causal evidence consistent with this circuit organization, showing that suppressing upstream Harmful Detection Heads disrupts downstream refusal behavior and that safety neurons mediate this interaction. We validate that this decomposition recurs across multiple LLM architectures and adversarial attack settings, and use simple, architecture-preserving weight scaling as a mechanistic probe to test its functional relevance. Across six LLMs, circuit-guided scaling improves safety rates under attacks by 26.5%, while incurring only a 1.7% accuracy drop across four standard benchmarks. Overall, our results support a circuit-level interpretation of LLM safety and suggest that mechanistic abstractions can reveal stable and transferable patterns underlying aligned behavior.

## 综合总结
该工作从机制可解释性角度系统揭示了LLM安全拒绝行为的内部电路结构(Harmful Detection Heads、Safety Neurons、Refusal Heads三阶段),并通过因果干预与跨架构验证支持该电路模型。基于此提出轻量级的circuit-guided weight scaling方法,在6个LLM上以极小通用能力代价显著提升对抗攻击下的安全性,兼具理论洞见与实用价值,是LLM安全可解释性方向的扎实进展,但理论框架的原创性与工程化落地仍有提升空间。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.2/10)
论文从机制可解释性视角系统刻画了LLM安全拒绝行为的三阶段电路(Harmful Detection Heads → Safety Neurons → Refusal Heads),并通过注意力头与神经元级别的因果干预(抑制/缩放)验证了该电路结构的功能因果性,跨越多种架构与对抗攻击场景复现了该模式,技术深度较高,因果论证较为严谨。但整体仍属于电路级机制的发现与验证,理论新颖性中等偏上,未提出全新的基础理论框架。

### 实用性 (评分: 7.0/10)
提出的circuit-guided weight scaling方法在6个LLM上将对抗攻击下的安全率提升26.5%,仅带来1.7%的通用基准准确率下降,工程效果显著且具有可操作性,为LLM安全对齐提供了一种轻量级、架构保留的干预手段。但作为weight scaling干预,其对生产环境部署的稳定性、可解释性保障和规模化成本仍需进一步验证,落地路径尚需工程化打磨。

### 社区活跃度 (评分: 7.5/10)
论文主题契合当前LLM安全与可解释性两大热点,arXiv预印本,发布时间标注为2026-09(疑为占位/笔误,实际可能为2025-09),但选题和方向具有较强时效性。机制可解释性+安全对齐的结合是社区活跃方向,具备一定影响潜力;但作者团队知名度与论文发表渠道(尚未看到顶会接收信息)对其权威性与可信度有所限制。

## 项目链接
https://arxiv.org/abs/2609.00051
