# Do small language models know what they don't know?

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-21  
**来源：** rss  

## 项目描述
arXiv:2609.20824v1 Announce Type: new Abstract: We explore whether entropy-based confidence signals can be leveraged to improve the accuracy of Small Language Models (SLMs) with fewer than 3 billion parameters, running entirely on consumer hardware. We evaluate seven distinct approaches, including token-level entropy early stopping, semantic entropy estimation, and uncertainty-aware routing to larger expert models, across 7 model pairs and 5 standard NLU benchmarks. Our key finding is that token-level entropy is effectively blind in SLMs: in 91% of dataset-model combinations, mean token entropy is near zero regardless of answer correctness, rendering token-based confidence signals unusable at this scale. We demonstrate that semantic entropy, computed by generating multiple samples, clustering answers by meaning, and measuring distributional uncertainty, recovers a viable confidence signal. Using semantic entropy to selectively route uncertain queries to a larger expert model yields accuracy improvements of up to +50 percentage points. Notably, cross-family routing (e.g., SmolLM 360M to Phi-3.5-mini) averages +22.0% improvement compared to +6.8% for same-family routing, revealing that expert model quality matters more than architectural compatibility. Our results suggest that the value proposition for entropy-based methods in SLMs is not computational savings but intelligent compute allocation: spending more tokens where they matter most.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.20824
