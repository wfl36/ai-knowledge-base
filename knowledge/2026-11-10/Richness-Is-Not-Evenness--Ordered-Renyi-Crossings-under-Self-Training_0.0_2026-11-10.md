# Richness Is Not Evenness: Ordered Renyi Crossings under Self-Training

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-10  
**来源：** rss  

## 项目描述
arXiv:2611.08892v1 Announce Type: new Abstract: Recursive self-training of language models, a setting studied in model collapse, can reduce vocabulary while making frequent words, mostly function words, less dominant. We fine-tune English GPT-2 on its own output for nine generations, vary the training-data sampling temperature, and measure every model with one fixed sampler. As training temperature rises, Renyi entropy changes turn from loss to gain at distinct temperatures: min-entropy first, then collision entropy, Shannon entropy and observed richness. Between the outer crossings, word types fall while the most-common word becomes less dominant. Untruncated training at T = 1 lies in this interval: at 13,000 words, generation 9 has 24% fewer types than generation 0 yet collision entropy is 0.91 bits higher. The ordering persists with a finer grid, different measurement samplers, a fixed word budget and five fresh training seeds. Min-entropy again crosses before richness in four further settings (in Hindi only at interpolated roots) and in 12 of 13 distinct measurements under eight text representations. Next-token identities and a categorical simulation isolate decoding and sampling effects; the crossing order remains empirical. Fine-tuning on human text can produce the same split while likelihood improves, and no single order's sign reliably identifies worse likelihood across the tested settings. We recommend reporting entropy profiles at stated budgets with an independent quality measure.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.08892
