# SpecOpt: Contact-Diff Reasoning for Agentic Molecule Optimization Toward Binding Specificity

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-22  
**来源：** rss  

## 项目描述
arXiv:2609.21165v1 Announce Type: new Abstract: Off-target protein binding is a major source of adverse effects for small-molecule drugs, yet most structure-based molecular design methods focus on generating selective compounds de novo rather than improving the selectivity of existing, well- characterized drugs. We introduce specificity optimization (SpecOpt), a molecular design task that seeks constrained structural modifications to an existing compound that increase its binding preference for an intended target over known off-targets while preserving its structural identity and drug-like properties. To enable systematic evaluation, we construct a ChEMBL-derived benchmark from compound-target interaction data, identifying intended targets through curated drug-mechanism annotations and off- targets through measured activities. We then develop an agentic framework that docks each compound against its intended target and off-targets, compares the resulting poses through residue-aware atom-protein contacts, and provides these differential interactions to a large language model to propose targeted structural modifications. Candidates are retained only if they satisfy molecular similarity, ADMET, and target-off-target docking selectivity criteria. On 915 compounds, the agent improves the target- off-target binding gap for 84.8% of compounds, shifting the mean gap from -0.72 to +0.47 kcal/mol while maintaining a mean Tanimoto similarity of 0.72 to the starting compounds. Ablation studies identify residue-specific contact information as the critical optimization signal: replacing residue identities with binary contact indicators eliminates improvement on all 29 ablation compounds. These results establish SpecOpt as a distinct molecular design problem and demonstrate residue-aware differential interactions as an effective signal for improving the specificity of existing compounds.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.21165
