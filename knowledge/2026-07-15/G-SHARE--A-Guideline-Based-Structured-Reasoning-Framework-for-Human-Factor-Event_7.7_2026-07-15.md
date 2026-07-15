# G-SHARE: A Guideline-Based Structured Reasoning Framework for Human-Factor Event Diagnosis

**评分：** 7.7  
**状态：** 正常  
**标签：** 大模型, 推理, 垂直领域, 核电, 人因分析, 论文, 工程实践  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.11892v1 Announce Type: new Abstract: Human-factor event diagnosis is essential for learning from operational events in nuclear power plants, yet its quality depends strongly on expert interpretation of narrative reports and guideline-based reasoning.Existing data-driven or one-shot large language model approaches often lack structured reasoning, have limited alignment with formal diagnostic guidelines, and may generate logically inconsistent conclusions. To address this issue, this study proposes G-SHARE, a guideline-based structured reasoning framework that operationalizes the CNNP nine-step human-factor event diagnosis guideline into a multi-stage diagnostic pipeline.The framework consists of evidence extraction, stepwise diagnostic reasoning, and post-hoc consistency repair, enabling explicit use of report evidence, intermediate rationale generation, and logical validation of diagnostic outputs. A dataset of real human-factor event reports was constructed from Chinese nuclear industry sources, and a gold-standard subset annotated by domain experts was used for evaluation. Results show that G-SHARE substantially outperforms one-shot prompting and traditional machine learning baselines, with the strongest version achieving the best overall accuracy and macro-F1. Ablation results further indicate that structured reasoning and consistency enforcement are critical to robust diagnosis, especially under weak prompting conditions. The findings demonstrate the value of transforming expert diagnostic guidelines into auditable reasoning workflows, providing a practical pathway for intelligent human-factor analysis in safety-critical industries.

## 综合总结
本文针对核电领域人因事件诊断中现有数据驱动和单次LLM方法缺乏结构化推理与逻辑一致性的问题，提出了G-SHARE框架。该框架将CNNP九步诊断指南转化为包含证据提取、逐步推理和事后一致性修复的多阶段流水线。基于真实核电数据集的实验表明，G-SHARE显著优于基线方法，验证了将专家指南转化为可审计推理工作流在安全关键行业中的重要价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文提出将核电领域的CNNP九步人因诊断指南转化为多阶段LLM推理流水线（G-SHARE），包含证据提取、逐步推理和事后一致性修复。该方法在领域知识与LLM结合上具有较好的新颖性，论证严谨，消融实验充分验证了结构化推理与一致性修复的作用，但技术本质仍偏向基于工作流的结构化提示工程，底层模型创新有限。

### 实用性 (评分: 8.5/10)
框架对安全关键行业（如核电、航空、医疗）具有极高的落地价值。它解决了LLM在严肃场景下逻辑不一致和黑盒不可控的问题，提供了一条将专家指南转化为可审计推理工作流的实用路径，其多阶段流水线和一致性修复机制可直接迁移至其他具有标准操作流程（SOP）的垂直领域。

### 社区活跃度 (评分: 7.0/10)
话题契合当前大模型在垂直领域落地的热点，强调可解释性与合规性。论文基于真实中文核工业数据集和专家标注进行评估，来源权威且可信度高。但由于领域高度垂直（核电人因分析），其受众和广泛影响力相对受限。

## 项目链接
https://arxiv.org/abs/2607.11892
