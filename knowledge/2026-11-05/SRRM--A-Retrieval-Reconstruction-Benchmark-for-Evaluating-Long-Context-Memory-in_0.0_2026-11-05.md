# SRRM: A Retrieval-Reconstruction Benchmark for Evaluating Long-Context Memory in Small Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-05  
**来源：** rss  

## 项目描述
arXiv:2611.05386v1 Announce Type: new Abstract: Small Language Models (SLMs) are increasingly deployed on consumer-grade hardware, yet their ability to preserve information across progressively longer contexts remains insufficiently understood. Existing benchmarks primarily evaluate retrieval-oriented tasks, providing limited insight into whether successful retrieval reflects comprehensive long-context memory preservation. To address this limitation, this paper introduces Simple Retrieval-Reconstruction Memory (SRRM), a lightweight and fully reproducible benchmark that jointly evaluates Targeted Retrieval and Global Information Reconstruction. This study also proposes the Memory Preservation Ratio (MPR), a benchmark-level metric that quantifies the relationship between retrieval and reconstruction performance. SRRM was evaluated using a synthetic dataset on three Qwen2.5 models (0.5B, 1.5B, and 3B parameters) across context loads ranging from 10 to 100 factual statements. Experimental results show that reconstruction performance deteriorated substantially faster than retrieval accuracy as contextual information increased, indicating that retrieval alone is insufficient to characterize long-context memory preservation. Among the evaluated models, Qwen2.5-1.5B achieved the highest retrieval accuracy (86.7%), reconstruction performance (45.7%), and MPR (0.53), outperforming the larger Qwen2.5-3B model (72.2%, 18.5%, and 0.26, respectively). These findings demonstrate that increasing parameter count does not necessarily improve long-context memory preservation. Overall, SRRM provides a reproducible and extensible benchmark for systematically evaluating long-context memory while revealing complementary memory behaviors that remain hidden under retrieval-only evaluation frameworks.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.05386
