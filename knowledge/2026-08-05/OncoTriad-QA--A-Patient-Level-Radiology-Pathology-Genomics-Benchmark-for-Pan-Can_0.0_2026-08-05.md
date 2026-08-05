# OncoTriad-QA: A Patient-Level Radiology-Pathology-Genomics Benchmark for Pan-Cancer Reasoning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-05  
**来源：** rss  

## 项目描述
arXiv:2608.02615v1 Announce Type: new Abstract: Cancer diagnosis and characterization require integrating complementary evidence from radiology, pathology, genomics, and clinical metadata. However, most medical large language model (LLM) and vision-language model (VLM) benchmarks focus on isolated modalities or narrow image-text tasks, leaving patient-level oncology assessment across multiple evidence streams largely untested. We introduce OncoTriad-QA, a patient-level radiology-pathology-genomics benchmark for pan-cancer question answering. OncoTriad-QA contains 86.1k semantic questions across 9,281 TCGA patient cases from 32 cancer cohorts, aligning CT/MRI radiology, whole-slide histopathology, somatic mutations, copy-number alterations, DNA methylation, bulk RNA-seq, and clinical metadata. Case-specific annotations are constructed through a source-grounded LLM-assisted pipeline using curated labels, diagnostic reports, molecular profiles, and modality-derived evidence as primary sources of truth, with automated consistency checks and clinician review. We also introduce OncoVLM, a reference multimodal model that maps modality-native radiology, pathology, DNA methylation, and RNA-seq evidence into an LLM interface through learned projectors. Experiments show that existing general-purpose and medical LLMs remain limited on comprehensive pan-cancer QA, especially when questions require integrating imaging findings, tumor morphology, and molecular evidence. After fine-tuning on OncoTriad-QA, OncoVLM exceeds MedGemma-4B by an average of 10.7 points when using MCQ accuracy and BERTScore-F1, with consistent gains across multiple-choice and open-ended questions under radiology-only, pathology-only, and all-available settings. These results demonstrate the benchmark's value for training and evaluating models for integrated cancer question answering.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.02615
