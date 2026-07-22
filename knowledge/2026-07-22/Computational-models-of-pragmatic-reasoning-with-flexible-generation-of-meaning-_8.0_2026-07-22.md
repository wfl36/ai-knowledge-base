# Computational models of pragmatic reasoning with flexible generation of meaning and expression alternatives

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 推理, 语用学, 认知科学, 神经符号, 论文  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18443v1 Announce Type: new Abstract: Pragmatic language use requires reasoning about alternatives: the alternative expressions a speaker might have chosen, or the alternative interpretations a listener might entertain. Formal and computational models of pragmatics must therefore specify the sets of alternatives that interlocutors reason over, which is often done through manual specification. Here we propose a framework, ScAffolded Generative models for Explanation (SAGE), that combines the explanatory transparency of cognitive models with the generative flexibility of language models (LMs). SAGE decomposes a pragmatic process into three kinds of modules: proposers, which use LMs to generate an open-ended space of candidate alternatives; evaluators, which assess those alternatives (e.g., their semantics, complexity, or typicality); and selectors, which implement the rule-based computational steps of a cognitively motivated task analysis. We assess SAGE in three case studies spanning pragmatic generation and interpretation-referential expression generation, manner (M-)implicatures, and Gricean conversational implicatures. SAGE models are evaluated critically using established methods from computational cognitive modeling, including ablations, baseline comparisons, and quantitative fit to human data. Across studies, SAGE models achieved high accuracy and often outperformed baselines, but component-level analyses reveal an asymmetry: LM proposers reliably generated alternatives well-suited to pragmatic modeling, whereas LM evaluators are better at providing intuitive judgements rather than judgements of theoretical or formal measures. We discuss the promise and the limitations of neuro-symbolic models as candidate explanatory accounts of human pragmatic language use.

## 综合总结
本文提出了SAGE神经符号框架，通过结合语言模型的生成能力与认知模型的规则推理，解决了计算语用学中替代方案需手动设定的痛点。SAGE将语用推理分解为提议、评估和选择三个模块，在指代表达生成、方式含义和格莱斯会话含义三项研究中表现优异。研究还揭示了LM在语用建模中的不对称性：擅长生成替代方案，但评估能力偏向直觉而非理论度量，为神经符号模型在人类语用解释中的应用提供了重要洞见与警示。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文提出了SAGE框架，创新性地将认知模型的可解释性与语言模型的生成灵活性相结合，采用神经符号架构解决计算语用学中替代方案需手动指定的瓶颈。框架将语用过程解耦为提议、评估和选择三个模块，论证严谨。研究不仅通过消融实验和人类数据拟合验证了模型有效性，还深入剖析了LM在生成与评估环节的不对称性（擅长生成替代方案，但在理论/形式度量评估上存在局限），展现了极高的研究深度与客观性。

### 实用性 (评分: 7.0/10)
SAGE框架的模块化设计（生成-评估-选择）为构建需要精细语用控制的AI系统（如对话系统、意图理解、可解释推理）提供了可直接参考的工程范式。然而，由于该研究主要面向计算认知科学和语用学理论验证，其直接落地到通用工业场景的适用范围相对垂直，LM评估器在理论度量上的局限性也提示从业者在实际应用中需谨慎设计评估模块。

### 社区活跃度 (评分: 8.5/10)
该论文发布于2026年7月，属于前沿探索。作者团队在计算语用学领域具有深厚积累，研究结合了当前大热的LLM与传统认知科学，切中了大模型语用推理与符号化解释的行业痛点。其发现LM在生成与评估上的不对称性对社区具有高度启发性，话题时效性强，来源权威可信，预计将在AI推理与认知科学交叉领域产生积极影响。

## 项目链接
https://arxiv.org/abs/2607.18443
