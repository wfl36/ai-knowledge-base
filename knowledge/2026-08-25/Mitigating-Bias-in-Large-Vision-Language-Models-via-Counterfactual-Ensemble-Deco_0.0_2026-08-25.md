# Mitigating Bias in Large Vision-Language Models via Counterfactual Ensemble Decoding

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-25  
**来源：** rss  

## 项目描述
arXiv:2608.21415v1 Announce Type: new Abstract: Large Vision-Language Models (LVLMs) have achieved remarkable performance across a wide range of tasks; however, they often inherit social biases from their training data, resulting in biased behavior when processing portraits from different social groups. Existing debiasing approaches typically compare token probabilities between the original and biased generations during decoding, but they are fundamentally limited by their reliance on a single, stereotyped viewpoint and fail to account for the diversity of social perspectives. Inspired by the social science principle that diversity fosters fairness, we propose Counterfactual Ensemble Decoding (CED), a novel framework that constructs multi-group counterfactual perspectives within the visual representation space and integrates them during decoding to promote equitable model behavior. CED first performs counterfactual steering in the visual space by identifying semantic directions associated with each social group and generating counterfactual representations along these directions, thereby offering diverse perspectives that disrupt stereotypical narratives. During decoding, CED locates the decoder layer exhibiting the greatest divergence among these perspectives and ensembles their token distributions using uncertainty-aware weights, prioritizing high-confidence tokens from different groups to yield a more balanced probability distribution that guides fairer generation. Extensive experiments on three social bias evaluation benchmarks demonstrate that \tool achieves substantial improvements over leading baselines, reducing bias by up to 47.97% across scenarios involving occupations, descriptors, and persona traits. Moreover, CED also preserves the core capabilities of the original model with minimal degradation.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.21415
