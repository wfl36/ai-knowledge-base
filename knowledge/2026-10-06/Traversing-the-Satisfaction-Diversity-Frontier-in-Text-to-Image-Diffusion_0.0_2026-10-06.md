# Traversing the Satisfaction-Diversity Frontier in Text-to-Image Diffusion

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-06  
**来源：** rss  

## 项目描述
arXiv:2610.02372v1 Announce Type: new Abstract: Text-to-image generation enables users to explore several images generated from the same prompt. For these generated images to be useful, each one must reflect the user's preferences, measured by a learned reward, and differ visually from the others to maintain diversity. Existing methods are limited: they either address reward and diversity separately or combine them in one aggregate score, enabling high diversity to offset low rewards. In this paper, we address these limitations by formulating generation as satisficing: every image (candidate) must satisfy a reward floor and the batch of images must satisfy a diversity cutoff. The reward floor controls the balance between worst-candidate reward and batch diversity; we show that varying this floor defines a Pareto frontier. To traverse this frontier, we introduce SatisDive, a training-free inference-time method. SatisDive uses a batch-relative reward cutoff to distinguish lower- from higher-reward candidates, emphasizing reward improvement for candidates below the cutoff and diversity among candidates above it. On Pick-a-Pic, at matched DreamSim, SatisDive improves worst-candidate reward over FK steering by up to 0.43 with FLUX.1-dev as the base model and HPSv3 as the reward, and by up to 0.70 with SANA-1.6B as the base model and ImageReward as the reward. More broadly, across their overlapping DreamSim ranges, SatisDive's satisfaction-diversity curve Pareto-dominates FK steering's curve in each setting.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.02372
