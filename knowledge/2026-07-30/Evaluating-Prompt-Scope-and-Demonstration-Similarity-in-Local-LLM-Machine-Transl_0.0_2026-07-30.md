# Evaluating Prompt Scope and Demonstration Similarity in Local LLM Machine Translation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-30  
**来源：** rss  

## 项目描述
arXiv:2607.26286v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used as general-purpose translation systems, but their behavior is usually evaluated under a single prompt shape: translate one source sentence into one target language. In practice, users may ask for one target language, for several related languages at once, or for translations conditioned on examples. This paper studies prompt scope and demonstration selection as experimental variables for local LLM machine translation. We evaluate English-to-Romance and English-to-Germanic translation on the full FLORES devtest split for nine official European Union languages. We compare three local instruction-tuned LLMs, llama3.2:3b, mistral:latest, and qwen2.5:14b, against dedicated MT baselines from OPUS-MT and NLLB-200. We test zero-shot prompting and k=5 few-shot prompting with random, lexical-similarity, and embedding-similarity demonstration selection. We also compare single-target prompts with JSON-formatted family-scope prompts that request all languages in a family at once. Results show that dedicated MT systems remain strongest overall, especially for Germanic languages. Few-shot prompting helps mistral:latest and qwen2.5:14b, but hurts llama3.2:3b; embedding retrieval is best on average for the stronger LLMs, but its advantage over random and lexical examples is modest. Family-scope prompting is feasible for stronger local LLMs but exposes structured-output failures in smaller models. These findings motivate evaluating LLM translation not only by language pair and metric, but also by prompt scope, retrieval strategy, and multi-target compliance.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.26286
