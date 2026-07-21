# RIMS: Preference Optimization via Smoothed Multi-pair Aggregation for Small-Scale LLM Retrieval-Augmented Generation

**评分：** 8.2  
**状态：** 正常  
**标签：** RAG, 偏好优化, 小模型, 鲁棒性, 论文  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16431v1 Announce Type: new Abstract: Small-scale language models (SLMs) are attractive for retrieval-augmented generation (RAG) in resource-constrained settings, but their limited capacity makes them highly sensitive to noisy or spurious retrieved evidence. Existing preference-based methods such as RoseRAG select only the hardest single preference pair via hard argmin/argmax, discarding the remaining signal; others treat multiple pairs as independent binary comparisons, resulting in low data utilization. We propose RIMS, a three-stage preference optimization framework comprising (1) synthetic chain-of-thought preference data generation via rejection sampling using the target SLM itself without relying on proprietary models, (2) a differentiable soft aggregation mechanism that replaces hard selection with a smooth operator, preserving gradient signal from all preference pairs while retaining the discriminative structure of margin-aware selection, and (3) preference optimization with the smoothed objective applied to multiple alignment algorithms. We theoretically show that the smoothed approximation admits a controllable error bound and that smooth aggregation yields provably tighter gradient alignment to the oracle objective than hard selection. Experiments on four multi-hop question answering benchmarks show that our approach outperforms state-of-the-art baselines across multiple SLM backbones, achieving consistent gains in Exact Match and F1 under noisy retrieval conditions. Our implementation is available at https://github.com/tptrix29/RIMS.

## 综合总结
本文提出RIMS框架，通过引入可微软聚合机制和基于目标SLM自身的合成数据生成方法，有效提升了小规模语言模型在RAG场景下的抗噪能力。理论证明其梯度对齐优于硬选择，实验在多个多跳QA基准上取得SOTA，为资源受限环境下的鲁棒RAG提供了高效的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出RIMS框架，针对小模型(SLM)在RAG中易受噪声干扰的痛点，创新性地引入可微软聚合机制替代传统的硬选择（argmin/argmax），保留了所有偏好对的梯度信号。同时提供理论证明，表明该平滑近似具有可控误差界且梯度对齐比硬选择更紧密，技术深度与论证严谨性较高。

### 实用性 (评分: 8.0/10)
框架包含清晰的三阶段流程，且偏好数据生成仅依赖目标SLM自身进行拒绝采样，无需调用专有大模型，极大降低了落地成本。方法在多跳QA任务上表现优异并已开源，对端侧部署、资源受限场景下的RAG系统开发具有直接的实践指导价值。

### 社区活跃度 (评分: 8.0/10)
聚焦SLM与RAG结合这一当前业界热点，针对噪声鲁棒性这一核心挑战。论文发布于arXiv，附带开源代码，作者团队包含相关领域学者，具备较高的可信度与潜在的学术/工程影响力。

## 项目链接
https://arxiv.org/abs/2607.16431
