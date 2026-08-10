# Recovering Lesion Parameters from Aphasic Picture Naming Error Profiles in Large Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-10  
**来源：** rss  

## 项目描述
arXiv:2608.06429v1 Announce Type: new Abstract: Interpretability methods for large language models (LLMs) describe internal state but do not directly test whether that state is causally sufficient to produce the observed behavior. In earlier work, we lesioned LLMs to produce error profiles in picture naming, a central task for assessing aphasia, and found that specific lesions produced errors resembling those of individual stroke survivors. Here we ask the inverse question: given an error profile, can the lesion parameters that produced it be recovered, and what does this inverse problem reveal about transformer computation? Lesions in LLaVA-Vicuna 13B were parameterized by layer index, modification percentage, and noise sigma across 4,840 configurations, and error profiles were characterized by a seven-category clinical taxonomy (correct, semantic, unrelated, formal, mixed, neologism, no-response). We trained a multi-task neural network to map error profiles back to perturbation parameters. The problem admitted a partial solution: across 10 independently trained inverse models, modification percentage and noise sigma were recoverable, whereas layer index was recoverable only within a neighborhood. In counterfactual validation, a fresh model instance perturbed with the recovered parameters reproduced the target behavior in 81.4% of cases. This dissociation between low layer recovery and high counterfactual fidelity is consistent with functional redundancy across transformer layers, a property not captured by standard interpretability methods. As an out-of-distribution test, we applied the trained model to picture-naming error profiles from 278 stroke survivors; recovered parameters were syndrome-discriminative, most strongly for perturbation intensity, indicating generalization beyond the training distribution. Counterfactual validation provides a general framework for LLM interpretability claims beyond inverse mapping.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.06429
