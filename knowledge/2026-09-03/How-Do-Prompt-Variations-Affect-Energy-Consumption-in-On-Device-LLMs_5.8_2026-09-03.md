# How Do Prompt Variations Affect Energy Consumption in On-Device LLMs?

**评分：** 5.8  
**状态：** 待复核  
**标签：** 端侧LLM, 绿色AI, 能效优化, Prompt Engineering, 论文, 实证研究, 移动计算  
**更新日期：** 2026-09-03  
**来源：** rss  

## 项目描述
arXiv:2609.01798v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly deployed on mobile devices, making energy efficiency a key deployment constraint, yet the energy impact of prompt design remains underexplored. This paper aims to understand how two prompt properties, cognitive load and phrasing pattern, shape the energy behavior of on-device LLM inference. We conduct a broad empirical study covering prompt properties, datasets, models, and devices, with phase-level profiling that separates prefill and decode energy. We find that cognitive load primarily affects the energy cost per token, while phrasing pattern affects energy largely through token usage. Our energy-quality analysis further shows that prompt design reshapes the attainable frontier differently across models, highlighting the need for model-aware prompt design in energy-efficient on-device LLM inference. Code, datasets, and scripts are available at https://amai-gsu.github.io/PromptProperty/.

## 综合总结
本文对端侧LLM推理中prompt设计对能耗的影响进行了系统性实证研究，将prompt属性分解为认知负载和措辞模式两个维度，通过phase级别能耗测量发现二者通过不同机制影响能耗：前者影响per-token成本，后者影响token使用量。研究强调了在能效优化中需要model-aware的prompt设计。代码和数据集已开源。整体为一项扎实的实证分析工作，填补了prompt设计与端侧能耗这一交叉领域的空白，但理论深度和工程落地指导性仍有提升空间。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
论文从认知负载(cognitive load)和措辞模式(phrasing pattern)两个维度系统研究了prompt设计对端侧LLM推理能耗的影响，采用phase级别(区分prefill和decode)的能耗profiling方法，在多个数据集、模型和设备上进行了广泛的实证研究。方法论层面有一定系统性，结论也颇具洞察：认知负载主要影响per-token能耗，措辞模式主要通过token使用量影响总能耗。但整体属于实证分析型工作，理论贡献有限，未提出新的算法或理论框架，技术新颖性中等。

### 实用性 (评分: 6.0/10)
对在移动/端侧设备部署LLM的从业者具有一定参考价值，揭示了prompt设计选择与能耗之间的具体关系，提醒开发者关注model-aware prompt design。代码、数据集和脚本均已开源，便于复现和后续研究。但实际落地指导较为浅层，结论偏向观察性而非可操作性的优化方案，缺少具体的prompt改写策略或能耗预算工具，对工程实践的直接帮助有限。

### 社区活跃度 (评分: 5.0/10)
话题具有较好时效性，端侧LLM部署和绿色AI是当前AI领域的重要议题。来源为arXiv论文，作者来自多家机构(包含工业界)，有一定可信度。但发布时间标注为2026年(预印本编号2609.01798)，社区影响力尚不可知，尚未经过同行评审。作为一个交叉方向(LLM+移动计算+能耗)的研究，属于较新的细分领域，受众面相对窄。

## 项目链接
https://arxiv.org/abs/2609.01798
