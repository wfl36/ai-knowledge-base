# Physics of Language Models: Part 4.2, Canon Layers at Scale where Synthetic Pretraining Resonates in Reality

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-21  
**来源：** rss  

## 项目描述
arXiv:2611.24963v1 Announce Type: new Abstract: Do standard benchmarks see the architectural differences that matter? We study it with 64 from-scratch pretraining runs of Transformers and three linear-model families at 1.3-8B parameters on 1-2T Nemotron-CC tokens, at a cost of roughly 100k USD per 8B run. In academic-scale pretraining (1.3B parameters, 100B tokens), architectural differences can all but disappear when the models are carefully tuned. Instead, at 1-2T tokens they become measurable: Canon layers, which add local token mixing, consistently improve Transformers, saving about 30% of pretraining tokens for the same MMLU accuracy at 8B. We also introduce GLA5 and GDN2, which improve gated linear attention and Gated DeltaNet with low-rank output gates. Surprisingly, with Canon, the simplest linear model, gated linear attention, matches Gated DeltaNet and outperforms Mamba2 even at 8B/1T. Therefore, the extra machinery of Gated DeltaNet and Mamba2 may do little more than mix neighboring tokens. Even at 8B/1T, however, high scores on standard benchmarks can hide weaknesses in basic in-context skills. In particular, linear models that match or beat Transformers on these benchmarks cannot, in fact, reliably retrieve information from a short 500-token context. Moreover, no model, Transformer or linear, reliably beats random guessing on arguably the simplest two-hop question, stated in a few short sentences, even at this scale. These findings $\textbf{challenge traditional architecture research}$ based primarily on standard benchmark scores. In contrast, small synthetic playgrounds, which predicted the architectural differences above at <100M parameters, can reveal what these benchmarks miss. For practitioners, one lesson is to include in-context reasoning examples in pretraining data from an early stage, rather than reserve them for later mid-training, let alone post-training.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.24963
