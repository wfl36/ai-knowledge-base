# FusionEval: Benchmarking Model Fusion for Large Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-23  
**来源：** rss  

## 项目描述
arXiv:2610.30162v1 Announce Type: new Abstract: Model fusion aims to integrate the capabilities of multi-expert models into a single model. Existing evaluations offer limited coverage of reasoning with long chains of thought and tool use, while strong average performance can mask substantial losses in individual expert capabilities. We introduce FusionEval, a benchmark that provides controlled expert pools, integrates fusion methods with and without additional training, and offers a unified evaluation suite. The pools contain domain experts independently trained from Qwen3 and Llama base models across math, code, science, instruction following, and tool use. The suite evaluates capability retention and computational cost on eight public benchmarks under comparable data access rules, reporting normalized average and worst performance, runtime, and peak GPU memory usage. Extensive experiments show that training-free methods preserve reasoning performance but substantially degrade tool use at both model scales. In contrast, MOPD preserves tool use and achieves a more balanced capability profile, but requires additional data preparation, inference, and training. Jointly retaining reasoning, instruction following, and tool use at low computational cost remains a challenge. We hope FusionEval supports future research on efficient model fusion that jointly preserves expert capabilities. Our code is available at https://github.com/Baicaihaochi/FusionEval_Benchmark.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.30162
