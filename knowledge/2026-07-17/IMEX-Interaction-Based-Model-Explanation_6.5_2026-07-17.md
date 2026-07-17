# IMEX Interaction-Based Model Explanation

**评分：** 6.5  
**状态：** 正常  
**标签：** 可解释性, 特征交互, 黑盒模型, 预测建模, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14096v1 Announce Type: new Abstract: In predictive modeling, the ability to explain why a model produces a given target prediction has become increasingly important [5, 10]. Black-box models do not provide a transparent description of the internal mechanisms that generate the prediction, making even accurate predictions difficult to interpret and validate. In critical contexts, predictive accuracy alone is not a sufficient validation metric if the reasons underlying model decisions remain unexplained. The IMEX (Interaction-Based Model Explanation) approach represents a methodological direction within explainable predictive modeling. IMEX is designed to identify which variables contribute most to the target prediction and which interactions among variables are significant in determining the target. The method does not impose limitations on higher-order interaction analysis, allowing the investigation of feature subsets with cardinality greater than two. Beyond the identification of feature importance, IMEX enables the exploration of interaction patterns that may be consistent with latent mechanisms influencing the outcome. Through the application of the IMEX algorithm, it is possible to construct an interpretability map of the predictions. The IMEX framework is built on two complementary metrics: Static Correlation Power (PCS), which quantifies the contribution of individual features, and Interaction Correlation Power (PCI), which captures non-additive effects among features. In the present work, the PCS component is experimentally validated through a comparison with INVASE [18] on three synthetic datasets with known structures. The results indicate that IMEX can recover relevant feature-level structures in the presence of non-linear, conditional, and multicollinear relationships between input features and prediction targets.

## 综合总结
本文提出了一种名为IMEX的基于交互的模型解释方法，旨在解决黑盒模型预测缺乏透明度的问题。IMEX框架通过静态相关能力（PCS）量化单特征贡献，通过交互相关能力（PCI）捕获特征间的非加性高阶交互效应，从而构建预测的可解释性图谱。该方法突破了传统交互分析对特征子集基数的限制。在三个合成数据集上的实验表明，其PCS指标在非线性、条件和多重共线性关系下能有效恢复特征级结构，性能优于INVASE，但PCI指标及真实场景的验证有待后续补充。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
该论文提出了IMEX（基于交互的模型解释）框架，核心创新在于引入了两个互补指标：静态相关能力（PCS）和交互相关能力（PCI），分别用于量化单特征贡献和特征间的非加性高阶交互效应。方法的新颖性在于不限制高阶交互分析（支持基数大于2的特征子集），突破了传统解释方法（如SHAP）多局限于低阶交互的瓶颈。但论证严谨度稍有欠缺，当前工作仅实验验证了PCS组件，且仅在三个合成数据集上与INVASE进行了对比，PCI部分及真实复杂数据集上的表现尚未明确。

### 实用性 (评分: 6.5/10)
对从业者具有较好的参考价值，可解释性（XAI）是医疗、金融等高风险领域的刚需，IMEX提供的高阶交互探索能力有助于揭示潜在的复杂因果或关联机制。然而，高阶交互分析通常伴随着极高的计算复杂度，且当前仅在合成数据上验证了单特征贡献（PCS），在真实大规模业务场景中的落地效果、计算开销及抗噪能力仍有待检验，适用范围目前偏向于结构可控的中小规模预测建模场景。

### 社区活跃度 (评分: 5.5/10)
可解释性AI（XAI）是当前大模型及黑盒模型应用中的持续热点话题，时效性强。但本文目前仅为arXiv预印本，作者Emiliano Massi在社区知名度有限，且尚未经过正式的同行评审，短期内的社区影响力和可信度相对有限，需关注后续在顶会的发表情况。

## 项目链接
https://arxiv.org/abs/2607.14096
