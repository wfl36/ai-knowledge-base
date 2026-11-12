# khammoon: From a Linguistic Guideline to a Thai Morpheme Segmenter

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-12  
**来源：** rss  

## 项目描述
arXiv:2611.13012v1 Announce Type: new Abstract: Thai is written without spaces between words, making segmentation a foundational step in most Thai NLP pipelines. Existing tools primarily reproduce the word-level conventions of corpora such as BEST; however, because the notion of a "word" in Thai lacks a unified linguistic consensus, these conventions struggle with productive compounding, leading to arbitrary boundaries and ambiguity in downstream representations. Instead, we propose operating at the morphological level, focusing on khammoon, the smallest atomic unit that carries meaning. Segmenting at the morphemic level provides an explicit, consistent morphological representation that eliminates compounding ambiguity. Crucially, this representation benefits downstream learning: models trained on morphemes perform on par with or exceed word-level baselines across part-of-speech tagging, named-entity recognition, and sentiment classification, demonstrating that linguistic consistency improves representation quality without downstream performance penalty. To operationalize this representation, we translate linguistic principles into a formal decision guideline with near-perfect human agreement ($\kappa \approx 0.99$), scale annotation with an LLM, and correct systematic errors with human labels. Finally, we train khammoon, a lightweight 1M-parameter convolutional BiLSTM segmenter designed for efficient CPU inference, achieving a boundary F1 of 0.992 on out-of-domain text. The guideline, datasets, model, and library are all publicly released.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.13012
