# Why Limit the Residual Stream to Layers and Not Tokens? Persistent Memory for Continuous Latent Reasoning

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 推理, 潜在推理, 论文, 记忆机制  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.07720v1 Announce Type: new Abstract: Large language models (LLMs) have demonstrated remarkable reasoning abilities on mathematical and multi-hop planning tasks. The CoCoNuT (Chain of Continuous Thought) paradigm~\cite{hao2024coconut} extends this by enabling models to reason in latent space, exploring multiple reasoning paths simultaneously rather than committing to a single chain early on. However, we identify a limitation we term the \textbf{concept bottleneck}. At each reasoning pass, intermediate hidden states are overwritten, causing the model to lose critical facts computed in earlier steps as reasoning depth increases. We observe this empirically. On HotpotQA, vanilla CoCoNuT (10.4\% EM) fails to improve over the CoT baseline (11.0\% EM), and performance degrades with curriculum depth on GSM8K. To address this, we propose \textbf{AGCLR} (Adaptive Gated Continuous Latent Reasoning), which augments CoCoNuT with a \textit{Gated Concept Stream}. A persistent residual memory maintained across all reasoning passes, controlled by three learned gates: a \textit{write} gate that commits intermediate facts to memory, a \textit{read} gate that retrieves relevant prior states, and a \textit{forget} gate that prunes irrelevant context. Evaluated on GSM8K, HotpotQA, and ProsQA using GPT-2 as our base model, AGCLR achieves consistent improvements across all types of datasets. With the performance gap compounding as curriculum depth increases, directly resolving the concept bottleneck. Code available at https://anonymous.4open.science/r/JJJJ/README.md

## 综合总结
本文针对大模型连续潜在推理（CoCoNuT）中存在的'概念瓶颈'（即中间状态被覆盖导致信息丢失）问题，提出了AGCLR方法。该方法通过引入由写门、读门和遗忘门控制的持久残差记忆流，使模型能够在深度推理过程中动态存储和检索关键事实。实验表明，AGCLR在GSM8K、HotpotQA和ProsQA等数据集上显著缓解了性能退化问题，随着课程学习深度增加，优势进一步扩大。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文敏锐地识别出连续潜在推理范式（CoCoNuT）中的'概念瓶颈'问题，即中间隐藏状态在推理过程中被覆盖导致早期关键信息丢失。为解决此问题，创新性地引入了类似LSTM门控机制的持久残差记忆流，包含写门、读门和遗忘门，实现了跨推理步的信息保持与动态更新，技术路径清晰且论证严谨。

### 实用性 (评分: 6.5/10)
对大模型推理机制的研究者和工程师具有较高的参考价值，指出了潜在推理落地的关键痛点。然而，该方法需要修改模型底层架构（增加额外的门控流和记忆模块），且当前实验仅在GPT-2等较小参数模型上验证，在超大参数模型上的训练成本、推理效率及实际落地效果仍有待验证，可落地性中等偏上。

### 社区活跃度 (评分: 7.5/10)
潜在推理是当前大模型提升推理能力的前沿热点方向，该论文针对知名范式CoCoNuT的缺陷进行改进，话题时效性强。论文已在arXiv公开并附带代码，具备一定的可复现性和学术可信度，但作者相对新锐，且基于小模型的实验可能限制了其在社区内的即时影响力。

## 项目链接
https://arxiv.org/abs/2606.07720
