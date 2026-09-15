# Clinical Reasoning Under a Partially Observed Objective in Cone Beam CT Report Generation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-15  
**来源：** rss  

## 项目描述
arXiv:2609.13238v1 Announce Type: new Abstract: Maxillofacial report generation from cone beam computed tomography is scored here by a composite objective placing 80% of its weight on a large language model judgement of factual entailment and 20% on lexical overlap, of which only the lexical fifth is visible during development. The grader's BLEU-4 and METEOR routines are reproduced in pure Python and match the reference to machine precision, and an offline entailment surrogate, which tells a report written for one patient from one written for another at an area under the curve of 0.987, makes the composite objective cheap enough to optimise directly. Over the 622-case public release, a report selected against the visible lexical ranking scores 0.2909, whereas one selected against the composite objective scores 0.4122, because pursuing n-gram overlap drives entailment precision from 0.522 down to 0.266. A 29 million parameter encoder fine-tuned on the release reaches a prevalence-weighted out-of-fold area under the curve of 0.486 over 985 statements, indistinguishable from the corpus prior, while nine numbers read from the image header reach 0.945 for mandible coverage and 0.872 for condyle coverage, and acquisition centre alone predicts sentence choice at 0.718 against 0.663 for the image-derived model, identifying dictation convention rather than anatomy as the quantity the lexical metrics reward. The delivered system emits eight unconditional statements and five gated on header geometry under polarity, laterality and tooth-level consistency constraints, and reaches METEOR 0.3542 over 50 held-out cases from an unseen centre. The dataset and code are available at https://github.com/GIND123/CBCT-Clinical-Reasoner

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.13238
