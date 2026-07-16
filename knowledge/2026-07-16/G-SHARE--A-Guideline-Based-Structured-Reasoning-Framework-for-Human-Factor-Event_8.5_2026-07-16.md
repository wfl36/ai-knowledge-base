# G-SHARE: A Guideline-Based Structured Reasoning Framework for Human-Factor Event Diagnosis

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 推理, 核电/工业安全, 人因分析, 论文, 工程实践  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.11892v1 Announce Type: new Abstract: Human-factor event diagnosis is essential for learning from operational events in nuclear power plants, yet its quality depends strongly on expert interpretation of narrative reports and guideline-based reasoning.Existing data-driven or one-shot large language model approaches often lack structured reasoning, have limited alignment with formal diagnostic guidelines, and may generate logically inconsistent conclusions. To address this issue, this study proposes G-SHARE, a guideline-based structured reasoning framework that operationalizes the CNNP nine-step human-factor event diagnosis guideline into a multi-stage diagnostic pipeline.The framework consists of evidence extraction, stepwise diagnostic reasoning, and post-hoc consistency repair, enabling explicit use of report evidence, intermediate rationale generation, and logical validation of diagnostic outputs. A dataset of real human-factor event reports was constructed from Chinese nuclear industry sources, and a gold-standard subset annotated by domain experts was used for evaluation. Results show that G-SHARE substantially outperforms one-shot prompting and traditional machine learning baselines, with the strongest version achieving the best overall accuracy and macro-F1. Ablation results further indicate that structured reasoning and consistency enforcement are critical to robust diagnosis, especially under weak prompting conditions. The findings demonstrate the value of transforming expert diagnostic guidelines into auditable reasoning workflows, providing a practical pathway for intelligent human-factor analysis in safety-critical industries.

## 综合总结
本文针对核电站人因事件诊断中现有方法缺乏结构化推理和逻辑一致性的问题，提出了G-SHARE框架。该框架将CNNP九步诊断指南转化为包含证据提取、逐步推理和事后一致性修复的多阶段流水线。基于中文核电真实数据集的实验表明，该方法显著优于单次提示和传统机器学习基线，消融实验验证了结构化推理与一致性修复的关键作用，为安全关键行业的智能化人因分析提供了可审计、可落地的实践路径。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究针对核电领域人因事件诊断中现有数据驱动和单次大模型方法缺乏结构化推理、与专业指南对齐不足及逻辑不一致的问题，创新性地提出了G-SHARE框架。该框架将CNNP九步诊断指南操作化为多阶段流水线（证据提取、逐步推理、事后一致性修复），技术路径清晰，论证严谨，消融实验充分验证了结构化推理与一致性修复机制的有效性，展现了较好的方法新颖性与技术深度。

### 实用性 (评分: 9.0/10)
该框架将专家诊断指南转化为可审计的推理工作流，不仅提升了诊断准确率，还显著增强了结果的可解释性与逻辑一致性，对核电及航空、医疗等安全关键行业的智能化人因分析具有极高的实际参考价值与落地指导意义，适用范围明确且工程可实现性强。

### 社区活跃度 (评分: 8.0/10)
论文为arXiv新发布文献，聚焦核电安全这一高门槛垂直领域。作者团队基于中国核工业真实数据构建数据集并进行专家标注，来源权威且数据可信度高。虽然在通用AI社区受众相对垂直，但在工业安全与AI交叉领域具有较强的影响力和时效价值。

## 项目链接
https://arxiv.org/abs/2607.11892
