# Larger Context Window, Fewer Overcorrections: Optimizing Prompts and Batching for Minimal-Edit Grammatical Error Correction

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-11  
**来源：** rss  

## 项目描述
arXiv:2609.10810v1 Announce Type: new Abstract: Minimal-edit Grammatical Error Correction (GEC) is a challenging task for zero- and few-shot prompted Large Language Models (LLMs), which systematically overcorrect and degrade $F_{0.5}$ by rewriting well-formed spans. While fine-tuning provides an effective solution, it imposes substantial infrastructure demands. We introduce a prompt-based approach that closes the gap to fine-tuned models through three advances in GEC prompting methodology. First, we introduce taxonomy-based instructions to enforce minimal-edit constraints with a comprehensive list of grammatical error rules, equipping the LLM with a bounded, metric-aligned scope of correctable edits, which benefits the strongest models while remaining model-dependent overall. Second, we show that batching multiple uncorrected sentences into a single input context acts as a targeted regularizer against overcorrection, systematically reducing the edit rate across diverse LLM families; we hypothesize this arises from attention dilution effect induced by the bounded capacity of self-attention scores. Finally, LLM-assisted Prompt Optimization refines these instructions. Powered by Gemini 3.1-Pro, our prompt achieves $F_{0.5}=78.32$ on the BEA-2019 test set - establishing a new prompt-based SOTA while shrinking the gap to the fine-tuned single-model SOTA (Staruch et al., 2025) to a mere $0.38$ points. Code, prompts, and outputs are publicly available.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.10810
