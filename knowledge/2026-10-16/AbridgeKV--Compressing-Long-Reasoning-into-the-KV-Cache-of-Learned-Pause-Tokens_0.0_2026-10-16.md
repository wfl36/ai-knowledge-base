# AbridgeKV: Compressing Long Reasoning into the KV Cache of Learned Pause Tokens

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-16  
**来源：** rss  

## 项目描述
arXiv:2610.20641v1 Announce Type: new Abstract: Long chain-of-thought decoding is memory-bound: the KV cache of the generated tokens grows linearly with the test-time compute being spent. Evicting cache entries does not fix this, because a model never trained on a cache with entries removed generates longer, often up to the length limit. We instead train the model to compress its own output. AbridgeKV compresses each completed block of generated text into the KV entries of a few learned pause tokens. These are extra input tokens with trained embeddings that produce no output. Once the pause tokens have encoded the block, AbridgeKV frees the block's original cache; subsequent tokens attend to the pause tokens' KV entries in its place. Three novel choices make this work: the pause tokens' KV entries take positions inside the block they replace, the cache budget is allocated across layers according to the measured value of each layer's entries, and compression operates on relatively large blocks. On 446 competition problems from AIME, HMMT, AMC, BRUMO, CMIMC and SMT with 32K-token generations, keeping a quarter of the generated cache matches an identically trained full-KV model in accuracy and output length; the strongest published evictor at a matched budget writes far longer, and the closest trained compressor, retrained on the same data, loses 10 points. Served in vLLM, the cache is 3.5x smaller per sequence and a saturated H100 finishes a problem 3.2x faster than with full KV.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.20641
