# Exposing the Unsaid: Visualizing Hidden LLM Bias through Stochastic Path Aggregation

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 偏见/对齐, 可视化, 可解释性, 论文, 工具  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19344v1 Announce Type: new Abstract: Large Language Models (LLMs) exhibit representational and syntactic biases that are difficult to evaluate due to the stochastic nature of text generation. Standard auditing methods rely on a single output inspection or static automated metrics. These approaches obscure the underlying probability distributions and fail to capture biases hidden in lower-probability generation branches. This paper introduces TreeTracer, a visual analytics tool designed to evaluate LLM bias through aggregated comparison. Using a systematic perturbation analysis pipeline, the tool replaces ontology-defined terms in each input prompt, aggregates hundreds of stochastic generations into a syntax-aligned hierarchical structure, and then performs classification-aware node merging with an auxiliary language model. The resulting structure is visualized through a custom Sankey diagram. By juxtaposing two ontology-driven trees, the workspace enables direct comparison between semantic contexts and supports systematic bias detection. Because any visualization reflects only a subset of the model's learned behavior, the system further applies contrastive inference to compute and directly display counterfactual token probabilities across contexts, reducing the risk of misinterpreting the presence of bias. We validate the workspace through case studies comparing an unaligned baseline model GPT-2 XL against the constitutionally aligned Apertus models. The visual aggregation successfully exposes hidden representational harms, such as counterfactual pronoun suppression and conversational marginalization of individuals. A preliminary user study confirms that the aggregated comparative interface reduces cognitive load and effectively supports analysts in detecting systemic biases.

## 综合总结
本文提出TreeTracer，一种用于评估LLM隐藏偏见的可视化分析工具。针对传统审计方法忽略低概率生成分支的问题，该工具通过系统扰动分析、随机生成路径聚合及辅助模型节点合并，构建语法对齐的层次结构，并以桑基图进行可视化对比。同时引入对比推理计算反事实token概率，避免偏见误判。案例研究表明，该工具能有效揭示模型中隐藏的表征危害（如代词抑制），初步用户研究也验证了其在降低认知负荷和辅助系统性偏见检测方面的有效性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对LLM随机生成掩盖底层概率分布和低概率分支偏见的问题，提出了结合扰动分析、随机路径聚合、辅助模型节点合并与对比推理的创新方法。技术栈完整，逻辑严密，能够有效揭示反事实代词抑制等深层表征偏见，研究深度较高。

### 实用性 (评分: 7.5/10)
TreeTracer作为可视化分析工具，为LLM审计员提供了直观的对比界面，降低了认知负荷，对模型公平性评估和对齐工作具有直接的工程参考价值。但当前验证主要基于GPT-2 XL等较小模型，在超大规模模型上的计算开销和可扩展性有待进一步验证。

### 社区活跃度 (评分: 8.0/10)
LLM偏见与对齐是当前AI领域的核心热点，话题时效性极高。文章来自arXiv预印本，学术来源可信。虽然案例研究使用的基座模型较老，但其提出的可视化审计视角对社区具有较好的启发意义和影响力。

## 项目链接
https://arxiv.org/abs/2606.19344
