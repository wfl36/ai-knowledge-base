# Benchmarking Confidential GPU Inference on NVIDIA H100 under Intel TDX

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 推理, 机密计算, 性能基准测试, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19353v1 Announce Type: new Abstract: Confidential computing is becoming a practical deployment requirement for AI inference workloads that process sensitive inputs or protect proprietary model assets. However, the performance cost of enabling confidential execution for GPU-accelerated large language model serving remains workload dependent and operationally important. This paper presents a benchmark study comparing standard non-confidential execution with confidential computing mode on a single NVIDIA H100 80GB GPU hosted in an Intel TDX confidential instance. The evaluation uses two representative language models, Mistral-7B v0.1 and Qwen3-30B-A3B, and measures time to first token, end-to-end request latency, per-request token generation throughput, global token throughput, and closed-loop request throughput under increasing concurrency. In fixed request-rate experiments, confidential mode increases average TTFT by 21.8% for Mistral-7B and 27.8% for Qwen3-30B-A3B, while global token throughput drops by 17.7% and 21.1%, respectively. In closed-loop concurrency experiments, throughput gaps remain in the 11.5-20.2% range, but the larger model reaches its saturation knee earlier under confidential mode. The results suggest that confidential GPU inference can retain usable throughput under load, but capacity planning must account for both the steady throughput penalty and the earlier saturation behavior observed for larger models.

## 综合总结
本文针对NVIDIA H100 GPU在Intel TDX机密实例上的大模型推理性能进行了基准测试。通过对比Mistral-7B和Qwen3-30B-A3B在标准与机密模式下的表现，发现机密模式会导致TTFT增加约20%-28%，全局吞吐量下降约17%-21%，且大模型在并发下更早达到性能饱和点。研究为机密GPU推理的容量规划和性能预期提供了关键的实证数据参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文针对机密计算（Intel TDX）在最新GPU（NVIDIA H100）上的推理性能开销进行了严谨的实证基准测试。实验设计合理，覆盖了不同参数规模模型（7B与30B）及多种关键性能指标（TTFT、吞吐量、并发饱和点），并揭示了较大模型在机密模式下更早达到饱和的现象。但本质上属于工程基准测试，缺乏对底层性能瓶颈的深度机制剖析或优化方案创新，研究深度适中。

### 实用性 (评分: 9.0/10)
对AI工程和运维从业者具有极高的落地参考价值。随着数据隐私合规要求趋严，机密计算落地是刚需，本文量化了开启TDX带来的具体性能损耗（如TTFT增加20%-28%，吞吐量下降11%-21%），这些硬核数据可直接指导企业在H100集群上进行机密推理的容量规划、资源分配和成本核算，避免盲目上线导致的性能不达标风险。

### 社区活跃度 (评分: 8.5/10)
机密计算与GPU加速推理的结合是当前AI基础设施领域的热点，时效性极强。测试基于当前最顶级的H100 GPU与Intel TDX技术，硬件平台极具代表性，数据可信度高。虽然作者知名度一般，但研究主题直击行业痛点，对云厂商和AI服务提供商具有较大影响力。

## 项目链接
https://arxiv.org/abs/2607.19353
