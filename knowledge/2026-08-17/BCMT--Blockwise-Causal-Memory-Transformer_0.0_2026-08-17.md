# BCMT: Blockwise Causal Memory Transformer

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-17  
**来源：** rss  

## 项目描述
arXiv:2608.13578v1 Announce Type: new Abstract: Transformer architectures rely on dense self-attention to model long-range dependencies, but this mechanism exhibits quadratic complexity with respect to sequence length. We introduce BCMT (Blockwise Causal Memory Transformer), an architecture for long-context language modeling that decouples local token interactions from global context propagation. Dense causal self-attention is applied independently within local blocks, while each block produces an adaptive summary aggregated through an exponential causal memory. This memory is subsequently injected back into the token representations, enabling efficient propagation of long-range contextual information without relying on explicit global attention. Unlike standard Transformers and recurrent memory architectures, BCMT maintains neither dense interactions between distant tokens nor learned memory states. Its memory mechanism is fully parallelizable and remains compatible with standard implementations of dense self-attention. Experiments on language modeling with context lengths of up to 1024 tokens show that BCMT achieves validation performance comparable to that of Dense Transformers while significantly improving training throughput and reducing memory consumption. An ablation study further confirms that these improvements arise from the proposed memory mechanism. These results demonstrate that an exponential causal memory constructed from block summaries provides an effective alternative to dense global attention mechanisms for long-context language modeling.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.13578
