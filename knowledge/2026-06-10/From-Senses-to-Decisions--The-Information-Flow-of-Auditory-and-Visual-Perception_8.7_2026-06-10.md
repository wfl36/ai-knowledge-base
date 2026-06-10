# From Senses to Decisions: The Information Flow of Auditory and Visual Perception in Multimodal LLMs

**评分：** 8.7  
**状态：** 正常  
**标签：** 多模态, 大模型, 可解释性, 推理优化, 信息流, 论文  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.10147v1 Announce Type: new Abstract: Multimodal Large Language Models (MLLMs) can listen and see, but how do audio and visual signals actually travel through the network to shape an answer? Despite their growing role in research and real-world applications, the internal pathways through which audio and visual tokens influence the final prediction remain poorly understood. In this study, we examine audio-visual information flow inside Audio-Visual Large Language Models (AVLLMs), tracing how AVLLMs route, utilize, and integrate audio and visual information across two input configurations, audio-visual video and multiple interleaved audio-visual items. We find that for audio-visual video, AVLLMs follow the sequential information flow pathway established for VLMs and VideoLLMs, with audio and visual contribution flowing along this pathway in proportion to the task's reliance on each modality. In settings with multiple interleaved audio-visual items, this routing shifts to different parallel streams. Furthermore, we demonstrate that audio-visual and other token types can be discarded once their information is transferred to LLM, with minimal impact on the model's prediction or even slight improvement, generalizing across multiple tasks and datasets, enabling more efficient inference. These findings hold across multiple models and scales, Qwen2.5-Omni and Video-SALMONN2 Plus at 3B and 7B scales, leading to hypotheses on why these flow structures emerge. Together, these results deliver the first coherent picture of how AVLLMs orchestrate sound and sight inside the network and lay the groundwork for the next wave of interpretability, design, and efficiency advances in audio-visual and broader MLLMs.

## 综合总结
本文深入探究了音视频大语言模型(AVLLMs)内部的信息流机制，揭示了在不同输入配置下（视频输入为顺序路径，交错输入为并行路径）音视频信息的路由与整合差异。研究发现，一旦音视频信息转移至LLM主干，其原始token即可被丢弃且对预测影响极小甚至略有提升，这一跨模型与规模的通用规律为多模态模型的高效推理（如KV cache压缩与token剪枝）提供了直接的理论依据与实践指导，是AVLLM可解释性领域的重要突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文在AVLLM的可解释性研究上展现了极高的深度与新颖性。研究不仅追踪了音视频token在网络内部的路由与整合路径，还揭示了不同输入配置下信息流的动态切换机制（视频输入下的顺序路径 vs 交错输入下的并行路径）。更重要的是，论证了音视频token在信息转移至LLM主干后即失去必要性甚至产生冗余，这一发现对理解多模态模型的内部运作机制提供了首张连贯图景，技术洞见深刻且论证严谨。

### 实用性 (评分: 8.5/10)
研究具有极高的工程落地价值。文中指出'音视频及其他模态token在信息转移至LLM后即可被丢弃，且对预测影响极小甚至略有提升'，这一结论可直接转化为多模态大模型的推理加速策略（如KV cache压缩、动态token剪枝等），在保持或略微提升性能的同时大幅降低计算开销，对大规模多模态模型的实际部署极具指导意义。

### 社区活跃度 (评分: 8.5/10)
多模态大模型（尤其是音视觉融合模型）是当前AI社区的热点与前沿方向，该论文紧扣核心痛点。作为arXiv上的最新研究，其时效性极强；且在Qwen2.5-Omni和Video-SALMONN2 Plus等主流开源模型及多个规模（3B/7B）上进行了广泛验证，来源与结论可信度高，有望在多模态可解释性与高效推理社区产生显著影响力。

## 项目链接
https://arxiv.org/abs/2606.10147
