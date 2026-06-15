# When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, 城市计算, 社会仿真, 人类移动性, 评估框架, 论文, 实证研究  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13835v1 Announce Type: new Abstract: LLM-based generative agents are increasingly used in urban simulators, yet it remains unclear whether they reproduce empirically realistic human mobility patterns or merely generate plausible mobility narratives. We introduce a validation framework for evaluating the mobility of generative agents of LLM-based urban simulators against real-world mobility data. For this, we use mobility laws, temporal rhythms, network motifs, semantic activity transitions, and behavioral mobility profiles. Using datasets from the Greater Paris region and Shanghai, we evaluate AgentSociety and CitySim across multiple dimensions of mobility realism. Our analysis reveals a substantial gap between narrative plausibility and empirical mobility realism. Although the simulators capture some high-level semantic activity distributions, they struggle to reproduce core spatial and temporal constraints, including realistic trip-length distributions, origin-destination flows, dwell times, and transition dynamics. We further observe that realistic mobility diversity is unstable across default prompting configurations and may require explicit profile-aware initialization. To support reproducible evaluation, we also contribute scalable and open LLM-driven infrastructure for regional-scale map generation, observability-enhanced simulation, mobility-metric computation, and traffic simulation. Our findings highlight the need for rigorous empirical validation of LLM-based urban simulators and provide practical tools for building more realistic and reproducible urban simulation systems.

## 综合总结
该论文针对基于LLM的城市模拟器中智能体移动模式'看似合理但不符合现实'的问题，提出了一套多维度验证框架。通过对AgentSociety和CitySim在巴黎和上海数据集上的实证评估，揭示了现有模拟器在核心时空约束和动态转换上的显著缺陷，并指出移动多样性对提示词配置的敏感性。此外，论文贡献了可扩展的开源基础设施，为构建更真实、可复现的城市仿真系统提供了关键工具和评估基准，对LLM社会仿真领域具有重要的警示与指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文敏锐地指出了基于LLM的城市模拟器中存在的'叙事合理性'与'经验现实性'之间的巨大鸿沟。研究不仅停留在理论探讨，还构建了包含移动定律、时间节律、网络模体等多维度的严谨验证框架，并在大巴黎和上海的真实数据集上对主流模拟器进行了深入实证分析，揭示了LLM在捕捉核心时空约束和动态转换方面的本质缺陷，研究深度与论证严谨性俱佳。

### 实用性 (评分: 8.0/10)
对从事智能体模拟、城市计算和社会仿真的从业者具有极高的参考价值。论文不仅指出了当前LLM模拟器的局限性（如出行距离分布、停留时间等失真），提醒开发者不能盲目依赖LLM生成的叙事，还提供了可扩展的开源基础设施（涵盖地图生成、模拟观测、指标计算等），为构建更真实、可复现的城市仿真系统提供了直接的工程工具和评估基准。

### 社区活跃度 (评分: 8.5/10)
随着LLM-based Agent在社会模拟和城市计算领域的爆发，如何评估其真实性成为亟待解决的行业痛点。该论文切中时弊，话题时效性极强；arXiv首发且提供了开源工具链，增强了研究的可复现性和可信度。其揭示的'看似合理实则脱离现实'的结论，对整个LLM社会仿真社区具有强烈的警示和纠偏作用，有望成为该细分领域的重要基准研究。

## 项目链接
https://arxiv.org/abs/2606.13835
