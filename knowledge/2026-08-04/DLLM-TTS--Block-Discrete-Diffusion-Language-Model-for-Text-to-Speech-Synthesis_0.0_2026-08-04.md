# DLLM-TTS: Block Discrete Diffusion Language Model for Text-to-Speech Synthesis

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-04  
**来源：** rss  

## 项目描述
arXiv:2608.00011v1 Announce Type: new Abstract: Current text-to-speech systems face a trade-off: autoregres- sive codec language models produce highly intelligible speech but require large-scale models and training data and decode tokens sequentially, while non-autoregressive approaches im- prove speed at the cost of linguistic accuracy. We present DLLM-TTS, a framework that formulates TTS as conditional block discrete diffusion over X-Codec2 neural audio codec to- kens. The model decomposes sequences into blocks and applies masked diffusion within each block while processing blocks se- quentially, learning both local acoustic coherence and global text-speech alignment. During inference, parallel token pre- diction within blocks enables efficient generation with a real- time factor (RTF) of 0.15. A 0.6B-parameter model trained on 20K hours achieves competitive performance on the Seed- TTS-eval benchmark, demonstrating that block discrete diffu- sion language models enable practical and data-efficient speech synthesis with parallel generation.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.00011
