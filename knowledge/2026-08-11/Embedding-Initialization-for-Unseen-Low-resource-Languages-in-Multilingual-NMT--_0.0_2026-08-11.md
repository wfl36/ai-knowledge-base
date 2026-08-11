# Embedding Initialization for Unseen Low-resource Languages in Multilingual NMT: A Case Study on Limbum-English Translation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-11  
**来源：** rss  

## 项目描述
arXiv:2608.07629v1 Announce Type: new Abstract: Multilingual neural machine translation models such as NLLB-200 cover 200 languages but leave thousands unsupported, including most Grassfields Bantu languages of Cameroon. When fine-tuning these models for an unseen language, practitioners must choose a proxy language token, yet no principled method exists for this selection. We implemented an embedding initialization strategy where a language token is the average of embeddings from multiple typologically related languages already in the mod el. We evaluate this approach on Limbum-to-English translation using a parallel corpus of 8,837 sentence pairs from New Testament text and a bilingual dictionary. We compare models: NLLB-200 zero-shot (chrF2++ = 12.5), a Transformer trained from scratch (chrF2++ = 14.5), NLLB-200 fine-tuned with a Swahili proxy token (chrF2++ = 47.3), and NLLB-200 with our averaged embedding initialization (chrF2++ = 46.7). We find that the multi-language initialization achieves performance comparable to the best single-language proxy. Both NLLB-200 variants improve over the from-scratch baseline by over 32 chrF2++ points. These results show that multilingual transfer is the dominant factor in extremely low-resource Bantu translation while eliminating the need for heuristic proxy selection. However, all systems fail to preserve tonal diacritics, highlighting an open challenge. We make our dataset and code available to support further research.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.07629
