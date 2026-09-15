# Hindsight Bias in Clinical Temporal Reasoning: How Future Data Exposure Affects Large Language Model Judgment

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-15  
**来源：** rss  

## 项目描述
arXiv:2609.13454v1 Announce Type: new Abstract: Clinical decisions are prospective, but clinical language models are often evaluated on retrospective records that reveal the final diagnosis, treatment response, and outcome. Such evaluations may reward the use of future information rather than reasoning under the uncertainty present at the decision point. We introduce a paired benchmark for measuring outcome-conditioned shifts consistent with hindsight bias in clinical temporal reasoning. It contains 171 case reports from the PubMed Central Open Access Subset---40 sepsis and 131 GLP-1/diabetes cases---represented as both textual narratives and human-annotated and LLM-generated textual time series (TTS). For each case, questions are tied to a clinically meaningful cutoff and paired with a prospective reference answer and an outcome-consistent \emph{hindsight trap}. Models answer each question using either a TTS truncated at the cutoff or the complete timeline; additional conditions vary the narrative source (original or synthetic) and TTS annotation source (human or LLM). We evaluate accuracy (Acc), hindsight trap rate (HTR), answer instability rate (AIR), and hindsight bias rate (HBR), each of which captures different signals of hindsight bias. Across GPT 5.6 Sol, Gemma 4, GLM 5.2, and Opus 5, full timeline exposure produces consistent hindsight-sensitive shifts, while temporal masking reduces bias without lowering accuracy.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.13454
