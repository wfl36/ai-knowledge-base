# Continuous Audio Thinking for Large Audio Language Models

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 多模态, 音频理解, 推理, 论文  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18273v1 Announce Type: new Abstract: Large audio language models (LALMs) have shown impressive capabilities on diverse audio understanding tasks, ranging from speech transcription to music analysis. However, because LALMs are typically trained to produce text-aligned responses, their hidden states are progressively shaped for text generation rather than for preserving acoustic information. As a result, the diverse acoustic content that audio carries, such as phonetic detail, prosody, sound events, affect, and pitch, is lost along the way and difficult to leverage in the response. We introduce Continuous Audio Thinking (CoAT), a framework that equips audio language models with a continuous latent workspace for organizing acoustic information prior to response generation, grounded by distillation from audio experts. Within the thinking space, the model can utilize the rich acoustic information provided by expert distillation when generating its response. Furthermore, the proposed continuous thinking block can be processed in a single prefill, so CoAT does not require additional autoregressive decoding cost over the baseline. Across three LALMs, Qwen2-Audio, Qwen2.5-Omni-7B, and Audio Flamingo~3, performance gains on a broad benchmark suite spanning audio reasoning, audio understanding, music classification, speech emotion, and speech transcription demonstrate the effectiveness of CoAT. Further analysis confirms that the auxiliary supervision propagates from the thinking positions to the model's textual responses.

## 综合总结
本文提出连续音频思考框架，通过在大型音频语言模型中引入由专家蒸馏指导的连续潜在空间，解决了模型在文本生成过程中声学信息丢失的问题。该方法在不增加自回归解码成本的前提下，显著提升了Qwen2-Audio等模型在音频推理、情感识别等任务上的表现，为音频大模型的架构优化提供了突破性思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
针对大型音频语言模型（LALM）在文本生成过程中声学信息（如韵律、情感、音高等）逐渐丢失的痛点，创新性地提出了连续音频思考框架。通过引入由音频专家蒸馏指导的连续潜在工作空间，模型在响应生成前能够有效组织和保留丰富的声学信息。该机制不仅新颖，且巧妙地通过单次预填充实现，未增加自回归解码成本，实验论证严谨，跨模型和多任务表现均显著提升。

### 实用性 (评分: 8.5/10)
对音频和多模态大模型开发者具有极高的实践指导价值。CoAT作为一种即插即用的模块，在不增加推理延迟的前提下显著提升了模型在音频推理、情感识别和音乐分类等细粒度任务上的表现。其在Qwen2-Audio等主流开源模型上的成功应用，为业界优化音频大模型提供了一条低成本、高收益的落地路径。

### 社区活跃度 (评分: 9.0/10)
研究发布于2026年6月，处于大模型多模态化发展的前沿，时效性极强。涉及Qwen2.5-Omni等最新开源模型，紧扣当前AI社区关注的音频理解与多模态推理热点。arXiv首发且实验覆盖面广，来源可信度高，有望在音频大模型社区引发广泛关注和后续研究。

## 项目链接
https://arxiv.org/abs/2606.18273
