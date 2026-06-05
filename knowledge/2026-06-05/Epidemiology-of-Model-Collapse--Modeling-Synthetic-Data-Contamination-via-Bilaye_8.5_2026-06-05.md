# Epidemiology of Model Collapse: Modeling Synthetic Data Contamination via Bilayer SIR Dynamics

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 数据治理, 模型崩溃, 跨学科, 论文  
**更新日期：** 2026-06-05  
**来源：** rss  

## 项目描述
arXiv:2606.05168v1 Announce Type: new Abstract: Training on synthetic data causes model collapse, but existing analyses treat this as single-chain degradation. In reality, the AI ecosystem involves cross-contamination: models ingest synthetic data from other models, produce new synthetic text, and contaminate shared corpora. We propose a bilayer coupled SIR/SIRS framework -- a phenomenological mean-field model treating data corpora and AI models as two interacting populations, each with susceptible, infected, and recovered compartments linked by cross-layer transmission. The SIRS variant (our primary recommendation) incorporates immunity waning, reflecting that filtered corpora and retrained models remain susceptible to re-contamination. We derive the basic reproduction number $R_0 = \sqrt{\beta_D \beta_M / [(\gamma_D+\mu_D)(\gamma_M+\mu_M)]}$ via the Next Generation Matrix and apply standard epidemic threshold results to the bilayer system. Illustrative scenario-based calibration from public AI text prevalence data yields supercritical dynamics ($R_0 > 1$) across three scenarios; Sobol sensitivity analysis identifies synthetic-text detection as the highest-leverage parameter. A bipartite-network agent-based model confirms mean-field consistency ($R^2 > 0.96$) for dense networks but degrades under heterogeneity. GPT-2 contamination chain experiments (192 runs across WikiText and Shakespeare) show dose-response degradation and diversity loss qualitatively consistent with the threshold picture. Matched-budget source-diversity experiments (1,088 runs) provide suggestive evidence that multi-source mixing modestly attenuates collapse, but the effect vanishes at lower contamination fractions. Intervention analysis identifies detection-based filtering and herd immunity as the highest-leverage strategies.

## 综合总结
本文创新性地采用流行病学双层 SIR/SIRS 动力学模型，研究了AI生态中跨模型的合成数据交叉污染与模型崩溃问题。推导出基本再生数R0并证实当前AI生态存在超临界崩溃风险，通过大量GPT-2实验验证了退化阈值与多样性损失。研究指出，合成数据检测过滤与群体免疫是最高效的干预策略，而简单的多源数据混合在低污染率下作用有限，为构建防污染的AI数据生态提供了深刻的理论指导与实践路径。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
该论文在研究深度和新颖性上表现卓越。传统模型崩溃研究多聚焦于单模型的递归退化，而本文创新性地引入流行病学中的双层耦合 SIR/SIRS 动力学模型，将数据语料库与AI模型视为两个交互的群体，精准刻画了真实AI生态中的交叉污染与免疫力衰减现象。通过推导基本再生数R0、Sobol敏感性分析、ABM仿真以及大规模GPT-2实验（192次污染链+1088次多样性实验），论证严谨，从宏观动力学与微观实证双重维度揭示了模型崩溃的阈值特性与剂量反应关系。

### 实用性 (评分: 7.5/10)
对AI工程实践和数据治理具有极高的参考价值。论文不仅指出了多源数据混合在低污染率下失效的局限性，更重要的是通过干预分析明确了'合成数据检测过滤'和'群体免疫'是最高杠杆的缓解策略。这直接指导了AI公司在构建训练数据池时的清洗策略、数据配比设计以及防污染机制，但在实际大规模大模型训练中，SIRS模型参数的精确标定和高效过滤器的部署仍面临工程成本挑战。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，切中当前大模型生态面临的'合成数据污染'这一核心痛点。随着AI生成内容在互联网上呈指数级增长，模型崩溃已成为影响下一代大模型发展的关键瓶颈。论文将流行病学跨学科引入AI数据生态，视角极具启发性，且arXiv发布时间（2026年）具有前瞻性，预计将在AI安全与数据治理社区引发高度关注与讨论。

## 项目链接
https://arxiv.org/abs/2606.05168
