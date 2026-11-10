# Forcing a Letter Suppresses Refusal: Mechanistic Evidence from WMDP

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-10  
**来源：** rss  

## 项目描述
arXiv:2611.08639v1 Announce Type: new Abstract: Safety benchmarks for large language models (LLMs) commonly use multiple-choice question (MCQ) format. However, prior studies documented that MCQ format reduces refusal rates, which may significantly affect the safety behavior of the model. We provide a first mechanistic explanation of this effect on the Weapons of Mass Destruction Proxy (WMDP) dataset across two models - Llama-3.1-8B and Qwen3-8B. First, we use the tuned lens technique to show that when processing MCQ the model commits to an answer-letter token very quickly, which is in contrast to the gradual refusal build-up in open-ended formats. Additionally, we observe that activations on the MCQ format lie roughly 3x further from the refusal direction, compared with their open-ended counterparts. Moreover, ablating the attention heads that carry the MCQ format answer increases the refusal, which is a direct evidence that the MCQ answer-selection competes with refusal. These findings indicate that MCQ safety scores primarily measure knowledge capabilities and do not assess the safety-mechanisms.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.08639
