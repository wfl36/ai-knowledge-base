# ElementCheck: Complexity-Aware Long-Form Text Factuality Evaluation via Sentence Elements

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-29  
**来源：** rss  

## 项目描述
arXiv:2608.26118v1 Announce Type: new Abstract: Existing long-form factuality evaluation relies on the decompose-retrieve-verify pipeline. However, the pipeline suffers from noise from claim decomposition and fixed verification granularity, resulting in unreliable results. We propose ElementCheck, a complexity-aware framework that verifies long-form outputs via sentence elements. Instead of uniformly decomposing sentences into atomic sub-claims, ElementCheck extracts entity pairs that are explicitly linked through verifiable connections in the original sentence as elements, and organizes these into an element graph. The graph topology provides a structural signal for estimating sentence complexity, enabling direct verification for simple sentences and targeted element-level refinement and verification for complex ones. To support fine-grained evaluation, we construct a new benchmark FastFact-Sent by mapping isolated claims from FastFact-Bench back to their source sentences. Experiments on FastFact-Sent and two domain-specific benchmarks show ElementCheck consistently improves factuality verification across five backbone models while maintaining a favorable accuracy-cost trade-off. Further analyses demonstrate that complexity-aware verification reduces unnecessary re-verification and maintains stability across different backbones.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.26118
