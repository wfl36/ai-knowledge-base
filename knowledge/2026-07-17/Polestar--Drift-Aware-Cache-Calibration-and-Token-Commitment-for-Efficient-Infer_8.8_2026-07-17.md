# Polestar: Drift-Aware Cache Calibration and Token Commitment for Efficient Inference of Diffusion LLMs

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 扩散模型, 推理优化, KV缓存, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14107v1 Announce Type: new Abstract: The inference efficiency of diffusion large language models (dLLMs) is constrained by two challenges: bidirectional attention precludes efficient KV-cache reuse, while increasing decoding parallelism with static confidence thresholds can compromise generation quality. We observe that both challenges arise from a shared phenomenon: as tokens are decoded, their contextual integration through bidirectional attention causes token representations to drift (evolve) across decoding steps. This insight motivates Polestar, a training-free inference framework that uses token representation drift as a unified signal to jointly address both challenges. Polestar comprises two components: Polestar-Cache, which identifies stale KV-cache positions via drift and performs sparse KV-cache refreshes to enable efficient reuse, and Polestar-Commit, which detects sharp drift events to reliably identify commit-ready tokens. Across mathematics and coding benchmarks on several dLLM families, Polestar sets a new state of the art on the accuracy-throughput Pareto frontier, achieving up to 10.73% accuracy improvement, up to 3.7x higher throughput, and high decoding parallelism of 3.67 tokens per forward pass over existing baselines.

## 综合总结
本文针对扩散大语言模型推理效率受限于双向注意力导致KV缓存难以重用及静态阈值并行解码损害质量的问题，提出免训练推理框架Polestar。作者创新性地发现这两个问题均源于token表示在解码过程中的'漂移'现象，并据此设计了Polestar-Cache（基于漂移稀疏刷新KV缓存）和Polestar-Commit（基于急剧漂移检测可提交token）。实验表明，该框架在数学和编程基准上实现了准确率与吞吐量的帕累托最优，吞吐量最高提升3.7倍，准确率最高提升10.73%。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文具有极高的研究深度与新颖性。作者敏锐地洞察到扩散大语言模型中双向注意力阻碍KV缓存重用与静态置信度阈值限制并行解码这两个看似独立的问题，其底层均源于同一现象：token表示在解码步骤中的'漂移'。基于此统一视角提出的Polestar框架，通过漂移信号分别设计Cache校准与Token提交机制，逻辑严密，论证极具说服力，并在实验中取得了帕累托前沿的SOTA表现。

### 实用性 (评分: 8.5/10)
对dLLM从业者具有极高的落地参考价值。首先，Polestar是一个免训练的推理框架，可直接插入现有dLLM的推理流程中，部署成本极低；其次，其在吞吐量（3.7x提升）和准确率（10.73%提升）上的显著收益，直击dLLM实际应用中的推理效率痛点，能够直接指导并加速扩散模型在数学、代码等场景的工程实践。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，dLLM作为大模型生成范式的新兴热点，其推理效率是决定其能否大规模落地的关键瓶颈。论文来源于arXiv，作者团队在体系结构与AI系统优化领域具有权威性。其显著的性能提升数据（SOTA）预示着该工作将在dLLM推理优化社区产生重要影响力。

## 项目链接
https://arxiv.org/abs/2607.14107
