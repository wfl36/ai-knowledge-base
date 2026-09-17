# Relation Before Entity: Deferred Commitment in Language Model Factual Recall

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-17  
**来源：** rss  

## 项目描述
arXiv:2609.17537v1 Announce Type: new Abstract: We ask whether relation-type information (e.g., capital-of) and entity-specific information (e.g., France to Paris) become causally active at the final-token position at the same depth during recall. Using four complementary causal diagnostics across four decoder-only models and eight prompt families, we find a robust temporal asymmetry: relation information becomes generation-controlling before entity information does. Relation onset precedes entity onset by 10-16 tested layers (31-44% of network depth) at threshold 0.4, with the ordering holding across all 16 model-threshold combinations for thresholds 0.2-0.5. Critically, entity information is not absent early: entity-token patching succeeds at 90-100% in early layers. Instead, entity commitment to generation is deferred: entity information is available at the entity-token position but becomes generation-controlling at the final token only after being routed there.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.17537
