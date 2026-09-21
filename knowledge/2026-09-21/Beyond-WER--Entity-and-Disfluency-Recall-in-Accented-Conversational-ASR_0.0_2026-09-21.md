# Beyond WER: Entity and Disfluency Recall in Accented Conversational ASR

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-21  
**来源：** rss  

## 项目描述
arXiv:2609.20828v1 Announce Type: new Abstract: ASR systems optimised for Word Error Rate (WER) often miss named entities and filled pauses in accented conversational English, both critical for language-learning feedback. We present a three-stage pipeline for speakers from India, Indonesia, and Latin America: (1) heuristic SQL filters curating entity-rich training data at 2.8x the entity density of random sampling, (2) regional LoRA adapters fine-tuned on Qwen2.5-Omni-3B producing both verbatim and corrected transcripts in a single forward pass, and (3) a six-category error taxonomy validated by an LLM-based judge (83.8% agreement, 210 human-labelled samples). The pipeline achieves 80-85% entity recall (up from 53-55%), 76-86% filler recall (up from <5%), and 6-10% WER across 6k test utterances, outperforming Whisper and a commercial ASR on entity recall while matching a zero-shot 30B model with 10x fewer parameters. Paired bootstrap tests confirm that curation alone accounts for 2.8-4.2 pp of entity recall gain (p<0.0001).

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.20828
