# IMEX Interaction-Based Model Explanation

**评分：** 6.3  
**状态：** 正常  
**标签：** 可解释性, 特征交互, 机器学习, 论文  
**更新日期：** 2026-07-18  
**来源：** rss  

## 项目描述
arXiv:2607.14096v1 Announce Type: new Abstract: In predictive modeling, the ability to explain why a model produces a given target prediction has become increasingly important [5, 10]. Black-box models do not provide a transparent description of the internal mechanisms that generate the prediction, making even accurate predictions difficult to interpret and validate. In critical contexts, predictive accuracy alone is not a sufficient validation metric if the reasons underlying model decisions remain unexplained. The IMEX (Interaction-Based Model Explanation) approach represents a methodological direction within explainable predictive modeling. IMEX is designed to identify which variables contribute most to the target prediction and which interactions among variables are significant in determining the target. The method does not impose limitations on higher-order interaction analysis, allowing the investigation of feature subsets with cardinality greater than two. Beyond the identification of feature importance, IMEX enables the exploration of interaction patterns that may be consistent with latent mechanisms influencing the outcome. Through the application of the IMEX algorithm, it is possible to construct an interpretability map of the predictions. The IMEX framework is built on two complementary metrics: Static Correlation Power (PCS), which quantifies the contribution of individual features, and Interaction Correlation Power (PCI), which captures non-additive effects among features. In the present work, the PCS component is experimentally validated through a comparison with INVASE [18] on three synthetic datasets with known structures. The results indicate that IMEX can recover relevant feature-level structures in the presence of non-linear, conditional, and multicollinear relationships between input features and prediction targets.

## 综合总结
本文提出了IMEX（基于交互的模型解释）框架，旨在解决黑盒模型的可解释性问题。该框架通过静态相关能力(PCS)和交互相关能力(PCI)两个指标，分别量化单个特征的贡献和特征间的非加性交互效应，并支持高阶特征交互分析。初步实验表明，在非线性、条件性和多重共线性关系下，其PCS指标能有效恢复特征级结构。但当前研究仅部分验证，缺乏真实场景测试，高阶交互的计算可行性亦待考察。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
提出IMEX框架，基于静态相关能力(PCS)和交互相关能力(PCI)两个指标来量化特征贡献及非加性交互效应。其亮点在于支持无限制的高阶特征交互分析，理论上能挖掘与潜在机制一致的交互模式。但当前实验仅验证了PCS组件，PCI及高阶交互的实证支撑不足，论证严谨性有所欠缺。

### 实用性 (评分: 6.5/10)
对于需要解释黑盒模型决策的领域（如医疗、金融风控）具有参考价值，能帮助从业者构建预测的可解释性图谱。然而，高阶交互分析在实际应用中通常面临计算复杂度极高的挑战，且当前缺乏真实数据集的验证，限制了其当下的工程落地性。

### 社区活跃度 (评分: 5.5/10)
可解释AI是当前机器学习领域的持续热点，该论文紧扣需求。但作为arXiv上的单作者预印本，尚未经过同行评审，且缺乏广泛的社区验证和影响力，权威性与可信度处于初始阶段。

## 项目链接
https://arxiv.org/abs/2607.14096
