# LatticeBridge: Rare-Event Sequential Inference for Faithful Structured Sequence Synthesis

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11203v1 Announce Type: new Abstract: Structured sequence generation often requires a model to satisfy several input-derived constraints in a single output. Standard decoding methods may assign high probability to fluent continuations while placing low mass on continuations that realize all required anchors jointly. We study this regime as a rare-event sequential inference problem. LatticeBridge combines a compact prefix language model, instance-compiled surface automata, and a twisted sequential Monte Carlo (SMC) decoder with resampling, multilevel splitting, and a source-support proposal term derived from instance-provided phrases. The constraint representation is compiled from each input instance and does not rely on manually curated lexical classes. On 2,610 attainable validation tasks spanning CommonGen, E2E NLG, and WikiBio, the particle decoder improves exact anchor satisfaction and mean anchor coverage over greedy, beam-filtered, and best-of-k ancestral baselines under a shared proposal model. Since exact anchor satisfaction alone does not rule out unsupported attribute substitutions, the evaluation reports required-anchor coverage, source coverage, source-intrusion diagnostics, overlap, runtime, and particle statistics jointly. The benchmark characterizes the faithfulness-overlap-latency frontier under a fixed proposal model.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2606.11203
