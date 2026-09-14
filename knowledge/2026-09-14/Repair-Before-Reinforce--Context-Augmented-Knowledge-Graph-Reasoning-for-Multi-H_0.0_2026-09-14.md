# Repair Before Reinforce: Context-Augmented Knowledge Graph Reasoning for Multi-Hop Question Answering

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-14  
**来源：** rss  

## 项目描述
arXiv:2609.12230v1 Announce Type: new Abstract: Question-answering often requires reasoning across multiple connected facts rather than retrieving a single isolated relation. Knowledge graphs (KGs) provide a structured way to represent such facts, but training large language models (LLMs) only on isolated KG head-relation-tail triples may limit their ability to learn the surrounding context needed for multi-hop reasoning. In this work, we propose a context-augmented training framework for multi-hop question-answering. Although generally applicable, we validate the framework in the context of disease-specific KGs, extracted using a reliable KG extraction framework called GraphMERT, for Gastroparesis and Diabetes. For each primary KG triple, we attach supporting triples extracted from the same source text chunk to form a context graph (CG). This creates two supervision settings: KG-grounded supervision, which uses only the target KG triple or path, and CG-grounded supervision, which uses the target KG triple or path together with supporting context triples. We train the Qwen3-14B model using supervised fine-tuning (SFT) under both settings, producing KGModel and CGModel variants. To strengthen the lower-hop factual foundation of the models, we introduce an LLM-judged, history-aware adaptive repair pipeline that identifies unresolved one-hop failures, continually fine-tunes on targeted repair examples, and removes or quarantines problematic noisy triples. This repair stage enables the models to reach 100% accuracy on the cleaned retained one-hop validation sets. Finally, we employ reinforcement learning (RL) using lower-hop question-answer items and evaluate generalization on harder 3-hop, 4-hop, and 5-hop tasks. Across both diseases, context-augmented supervision consistently improves multi-hop performance over KG-only supervision. RL initialized from repaired SFT checkpoints yields larger and more stable gains.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.12230
