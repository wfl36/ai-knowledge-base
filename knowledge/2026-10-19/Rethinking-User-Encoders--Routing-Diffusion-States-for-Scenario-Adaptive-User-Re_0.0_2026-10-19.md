# Rethinking User Encoders: Routing Diffusion States for Scenario-Adaptive User Representation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-19  
**来源：** rss  

## 项目描述
arXiv:2610.22400v1 Announce Type: new Abstract: Existing large language model (LLM)-based user encoders serialize heterogeneous behavioral logs and compress them into static representations through autoregressive (AR) prediction. However, their unidirectional constraint limits bidirectional information flow, hindering cross-modal interactions and the joint preservation of multi-source signals. Consequently, the learned static representations struggle to accommodate the distinct evidence requirements of diverse downstream scenarios. We address these limitations by unlocking the iterative denoising process of diffusion language models (dLLMs) as a multi-granularity reconstruction space. Based on this insight, we propose FINDERS (FactorIzatioN of Diffusion statEs for Routing across Scenarios), a router-equipped dLLM framework comprising four operations: denoise, factorize, route, and compress. Learnable meta-slots organize complementary denoising states into transferable cross-modal semantics and modality-specific behavioral factors. To provide grounded supervision, we construct BehaviorQA, a large-scale corpus containing explicit behavioral rationales. Guided by scenario queries, a lightweight router dynamically emphasizes relevant slot directions via an input-level residual pathway before cross-source fusion and final compression. Extensive experiments and online A/B tests across ten industrial scenarios demonstrate that FINDERS consistently outperforms state-of-the-art methods in both unified and scenario-adaptive settings. This work effectively pushes the boundaries of dLLMs beyond language generation, demonstrating their immense potential as powerful user representation learners.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.22400
