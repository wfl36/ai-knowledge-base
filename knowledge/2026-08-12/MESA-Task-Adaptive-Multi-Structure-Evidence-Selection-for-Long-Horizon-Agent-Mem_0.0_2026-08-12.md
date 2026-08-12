# MESA:Task-Adaptive Multi-Structure Evidence Selection for Long-Horizon Agent Memory

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-12  
**来源：** rss  

## 项目描述
arXiv:2608.10108v1 Announce Type: new Abstract: Long-horizon agents accumulate trajectories spanning hundreds of interleaved reasoning, action, and observation steps, where answering a query may depend on evidence buried far back in the history. External memory stores such trajectories as structured representations, yet each structure provides a distinct and incomplete view. Existing multi-memory systems either read a fixed set of structures for every query, inflating context and introducing noise, or route each query to a single structure, preventing the composition of complementary evidence. A controlled analysis on AMA-Bench shows that the optimal memory configuration is typically neither a single structure nor the full union, but a tailored composition of multiple structural memories that varies with query and task demands. Motivated by these findings, we formulate structure-level dynamic selection: selecting and fusing a query-adaptive subset from a library of specialized memory structures. We propose MESA (a Multi-structure Evidence Selection framework for long-horizon Agent), which builds five complementary structure views of each trajectory and learns from end-to-end answer-level feedback to select and fuse a query-specific subset for a frozen answer model. To learn under this weak supervision, MESA employs harness optimization with prior-guided search and UCB-guided scheduling to balance exploration and exploitation. On AMA-Bench, MESA outperforms the strongest baseline by 8.5% while using 41% fewer evidence tokens than the all-structure alternative.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.10108
