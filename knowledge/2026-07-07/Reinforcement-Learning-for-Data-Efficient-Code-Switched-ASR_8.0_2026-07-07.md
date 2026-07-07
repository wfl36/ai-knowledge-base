# Reinforcement Learning for Data-Efficient Code-Switched ASR

**评分：** 8.0  
**状态：** 正常  
**标签：** 语音识别, 大模型, 强化学习, 语码转换, 多语言, 论文  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02757v1 Announce Type: new Abstract: Audio-language models can be prompted for code-switched speech, but their decoding is not optimized for code-switching and often fails at language boundaries. We propose a practical reinforcement learning with verifiable rewards recipe for data-efficient adaptation of audio-language models to code-switched ASR using group relative policy optimization, combining an error rate reward with a script fidelity reward that penalizes wrong writing systems and a two-pass draft-and-refinement procedure. Using Qwen2-Audio as a reproducible testbed across 10 language pairs, training on only TTS code-switched speech, we show that RLVR with 10% of the data matches LoRA supervised fine-tuning trained on the full dataset, with the largest gains on typologically distant pairs. The error rate reward eliminates translation errors while the script fidelity reward separately reduces script contamination without degradation. These gains transfer zero-shot to a human-recorded code-switching corpus.

## 综合总结
本文提出了一种基于强化学习(RLVR)的数据高效语码转换ASR适配方法。通过结合错误率与书写系统保真度的双重奖励机制及两遍解码策略，仅用10%的TTS数据即可匹配全量LoRA微调效果，有效消除了翻译错误和书写污染，且能零样本迁移至真实语料，为低资源多语言语音识别提供了高效的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文针对语码转换(ASR)中语言边界解码失败的问题，创新性地引入了基于组相对策略优化(GRPO)的强化学习配方(RLVR)。技术亮点在于设计了双重奖励机制（错误率奖励+书写系统保真度奖励）及两遍起草-精炼过程，有效解耦并解决了翻译错误和书写系统污染问题，论证严谨且方法新颖。

### 实用性 (评分: 8.0/10)
该方案具有极高的工程落地参考价值。仅使用10%的TTS合成数据即可达到全量数据LoRA监督微调的效果，大幅降低了数据标注与训练成本。同时，其效果能零样本迁移至真实人类录制语料，为多语言ASR系统的低资源适配提供了可直接复用的实践范式。

### 社区活跃度 (评分: 7.5/10)
语码转换ASR与强化学习微调(RLVR/GRPO)均为当前AI社区的前沿热点。该研究基于Qwen2-Audio在10个语言对上进行了可复现的验证，来源可信；但在多语言语音领域的广泛影响力仍有待社区后续的检验与跟进。

## 项目链接
https://arxiv.org/abs/2607.02757
