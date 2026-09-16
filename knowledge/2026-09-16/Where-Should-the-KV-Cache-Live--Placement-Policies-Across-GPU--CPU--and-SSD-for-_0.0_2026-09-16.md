# Where Should the KV Cache Live? Placement Policies Across GPU, CPU, and SSD for Long-Lived Sessions

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-16  
**来源：** rss  

## 项目描述
arXiv:2609.16215v1 Announce Type: new Abstract: GPU high bandwidth memory is scarce and expensive, and KV caches consume much of it as chats, agent loops, and document question answering accumulate state. Systems such as Mooncake, LMCache, FlexGen, InfiniGen, and AttentionStore extend GPU memory with CPU DRAM and SSD. The harder question is which blocks belong in each tier, when to move or evict them, and whether prefetching helps. We study these choices in a discrete event simulator spanning GPU HBM, CPU DRAM, and SSD, calibrated against a random forest execution time predictor. We compare recency, reuse frequency, predicted reuse, and an EWMA predictor with prefetch lookahead across chat, agent, and document question answering workloads. Tiering supports 73.02 times more concurrent sessions per GPU and lowers cost per session by 62.04 times. These gains come from tier capacities of 1 plus 8 plus 64, not placement policy. Decode is compute bound at batch size one in our setup, so placement barely affects throughput. It mainly changes PCIe migration traffic and time to first token. Recency produces 2.30 times less migration traffic than reuse frequency for chat. Reuse frequency performs best for agents and document question answering. The existing predicted reuse policy is byte identical to recency, making its agent recommendation effectively recency. A genuine EWMA predictor changes behavior but still ranks behind reuse frequency on the workloads prediction was expected to help. Prefetching does not justify its bandwidth cost. Across the policy and cache size grid, even an oracle with knowledge of future requests never beats no prefetch on migration traffic. Workload specific placement can reduce data movement, but the predicted reuse and prefetch recommendations are not supported as implemented.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.16215
