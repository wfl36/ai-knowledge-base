# From Relevant Posts to Attributable Spans: Explicit Symptom Evidence for Depression Questionnaire Inference

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-12  
**来源：** rss  

## 项目描述
arXiv:2611.12900v1 Announce Type: new Abstract: Longitudinal social-media histories offer an opportunity to assess depression, potentially supporting the inference of standardized depression questionnaire responses. However, this task requires evidence that is semantically relevant to a symptom and attributable to the user, while being sufficiently specific to support an individual questionnaire item. Existing approaches rely on semantic similarity to retrieve posts, which can introduce misleading or non-attributable evidence, particularly in multi-symptom posts and discussions of others' experiences. We propose SREE (Symptom Retrieval and Evidence-Grounded InfErence), an evidence-grounded pipeline that extracts first-person and symptom-specific text spans, selects a representative subset using a Facility Location-inspired objective, and performs Evidence-Gated Inference over the selected evidence. We evaluate evidence retrieval on BDI-Sen and evidence-conditioned questionnaire inference on eRisk 2019-2021. Compared with state-of-the-art retrieval approaches, SREE achieves relative improvements of 70% in post-level precision and 59% in F1, while retaining at least 30% fewer posts. On multi-symptom sentences, it also outperforms dense retrieval in precision and F1 even with twice the retrieval budget. Across all three eRisk collections, SREE achieves the highest exact item-level agreement while remaining competitive on ordinal and aggregate metrics. These results highlight the importance of localizing attributable evidence and controlling its composition before inferring depression questionnaire responses.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.12900
