# Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-10  
**来源：** rss  

## 项目描述
arXiv:2609.09425v1 Announce Type: new Abstract: Educational data filters have become a practical way to improve language-model pre-training, but most filters treat educational value as a single scalar property. This may be too broad for some applications, especially if the data set already features a high density of educational material. Useful learning material needs to be accurate, engaging, well structured, and appropriate for the intended audience and application (e.g. learner- vs teacher-facing). Following QuRating (Wettig et al. 2024), we introduce Edu-QuRating: a pipeline for multi-dimensional educational data scoring and curation. Edu-QuRating defines education-specific rubrics, uses an LLM judge to label sampled document pairs and distills those pairwise preferences into reusable Edu-QuRaters, which can score individual text chunks on a set of educational criteria. Across two sequence-classification base models and six educational criteria, the best Edu-QuRater recovers held-out GPT-4.1-mini pairwise judgements with mean accuracy 0.917. We then apply the resulting scorers in two applications. First, we investigate the potential of Edu-QuRaters for corpus filtering to improve pretraining of small language models. We scored 322.25M FineWeb-Edu-Fortified documents to obtain a filtered pre-training mixture. In matched single-run pre-training comparisons, models trained with Edu-QuRating-based mixtures reached higher observed aggregate accuracy across nine benchmarks than the FineWeb-Edu baseline, with gains concentrated in particular tasks. Second, we used Edu-QuRater scores as reward terms for GRPO post-training. In held-out pairwise judge evaluations, combining Edu-QuRater and answer-structure rewards produced responses preferred to the Qwen3-4B base model on both pedagogical quality and instruction following.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.09425
