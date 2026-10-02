# Conformal Factuality Control for Multi-Hop Retrieval-Augmented Generation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-02  
**来源：** rss  

## 项目描述
arXiv:2609.38222v1 Announce Type: new Abstract: Retrieval-augmented generation (RAG) can ground large language models in external evidence, but retrieved context does not guarantee that generated claims are factually supported. This problem is especially relevant in multi-hop RAG, where retrieval and reasoning proceed through multiple dependent stages. We study whether claim-level conformal factuality control, previously developed for RAG, remains effective in this setting. We apply split-conformal claim filtering to multi-hop RAG and evaluate it on HotpotQA, Natural Questions, and TriviaQA using Llama 3.1 8B and GPT-4o-mini, together with a single-hop reference experiment. Across all six multi-hop model-dataset configurations, increasingly stringent conformal targets consistently increase the fraction of responses whose retained claims are fully supported. At the 95% target, this rate ranges from 95.80% to 97.20%, compared with 55.60%-76.03% without filtering. However, the improvement is strongly selective: only 4.41%-31.09% of generated claims are retained and 9.70%-51.40% of responses remain non-empty at the 95% target. These results show that conformal factuality extends to multi-hop RAG, while demonstrating that nominal reliability must be interpreted jointly with claim retention and abstention.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.38222
