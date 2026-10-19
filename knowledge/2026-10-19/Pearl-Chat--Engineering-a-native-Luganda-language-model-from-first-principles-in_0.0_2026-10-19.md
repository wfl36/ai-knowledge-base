# Pearl-Chat: Engineering a native Luganda language model from first principles in JAX and Flax NNX

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-19  
**来源：** rss  

## 项目描述
arXiv:2610.22529v1 Announce Type: new Abstract: Autoregressive foundation language models predominantly target high-resource Indo-European languages, imposing computational and morphological penalties on under-represented African languages. Generic multilingual tokenizers routinely exceed fertility rates of 3.2 tokens per word on agglutinative Bantu languages, degrading context efficiency and inflating latency. We present Pearl-Chat, an 8,473,122-parameter ($\sim$8.5M) causal decoder-only transformer engineered for Luganda (Oluganda, ISO 639-2: lg), a low-resource Niger-Congo Bantu language spoken by over 10 million people in East Africa. Built from first mathematical principles in JAX and Flax NNX, Pearl-Chat uses explicit functional state decomposition (nnx.split and nnx.merge), deterministic resumable data streaming via Google Grain, and SPMD tensor parallelism using jax.sharding.Mesh. We introduce a byte-level byte-pair encoding (BPE) subword tokenizer trained from scratch on curated Luganda corpora ($V = 8,192$), achieving 4.88 characters per token compression and 1.60 tokens per word fertility, a two-fold compression improvement over LLaMA-3 (128K) and Gemma (256K). The model is trained with a two-stage curriculum: Stage 1 pre-training on 59,501 sequences across parallel, biblical, encyclopedic, and journalistic corpora, and Stage 2 instruction fine-tuning on 510 dialogues with assistant-only loss masking. Across 4,000 optimization steps, validation cross-entropy loss drops monotonically from 9.4695 (perplexity: 12,958.98) to 0.1818 (perplexity: 1.20), a decrease of 9.2877 nats. On a three-tier held-out diagnostic benchmark, Pearl-Chat achieves 0.9792 ROUGE-L and 0.9405 BLEU while maintaining concordial agreement across Bantu noun classes. We provide a Python Server-Sent Events (SSE) streaming runtime and open-source all weights, tokenizers, and code.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.22529
