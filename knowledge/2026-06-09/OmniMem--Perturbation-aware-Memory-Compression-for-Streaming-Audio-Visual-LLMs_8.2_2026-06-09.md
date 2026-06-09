# OmniMem: Perturbation-aware Memory Compression for Streaming Audio-Visual LLMs

**评分：** 8.2  
**状态：** 正常  
**标签：** 多模态, 大模型, 推理优化, KV缓存, 长视频理解, 论文  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.07577v1 Announce Type: new Abstract: Audio-visual large language models (LLMs) hold strong promise for long-form video understanding, yet their long-video inference is fundamentally limited by the linear growth of video tokens and key-value (KV) caches. We present OmniMem, a memory-efficient streaming framework designed specifically for audio-visual LLMs. Unlike existing compression methods that treat all tokens uniformly, OmniMem introduces a modality-aware memory allocation strategy that separately manages visual and audio contexts, addressing the severe token imbalance between the two modalities. OmniMem further preserves informative and non-redundant KV states through perturbation-aware memory selection, enabling compact memory without sacrificing long-range understanding. To strengthen compression under realistic deployment constraints, we also explore budget-aware fine-tuning, which encourages the model to consolidate useful information into retained memory. Experiments on VideoMME Long, LVBench, and LVOmniBench with video-SALMONN 2+ and Qwen-2.5-Omni show that OmniMem consistently improves over strong training-free compression baselines by 2-4% absolute accuracy under the same memory budgets, with an additional 1-2% gain after fine-tuning.

## 综合总结
OmniMem 提出了一种面向流式音视频大模型的内存高效框架，通过模态感知内存分配解决音视频 token 不平衡，利用扰动感知内存选择保留关键 KV 状态，并引入预算感知微调强化压缩效果。实验表明，该方法在同等内存预算下较免训练基线提升 2-4% 准确率，微调后额外提升 1-2%，有效缓解了长视频推理的显存瓶颈并提升了长程理解能力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对音视频大模型长视频推理中 KV cache 线性增长的问题，提出了 OmniMem 框架。技术亮点在于打破了传统均匀压缩 token 的范式，创新性地引入模态感知内存分配策略解决音视觉模态间的 token 严重不平衡，并通过扰动感知内存选择机制保留关键非冗余的 KV 状态，理论依据充分；此外，预算感知微调进一步强化了受限部署下的信息巩固，整体方法新颖且论证严谨。

### 实用性 (评分: 8.0/10)
长视频推理的显存瓶颈是多模态大模型落地的核心痛点之一。OmniMem 提供的流式压缩框架直接针对该问题，且考虑了实际部署的预算约束，对从事多模态大模型推理优化和工程部署的从业者具有极高的参考价值，可直接应用于类似 Qwen-2.5-Omni 等模型的推理加速与显存优化。

### 社区活跃度 (评分: 8.0/10)
长上下文处理与多模态大模型是当前 AI 社区高度关注的前沿热点。该研究结合了音视频理解与 KV cache 压缩两大热门方向，在 VideoMME Long、LVBench 等权威基准上取得了显著提升，来源为 arXiv 论文，具备较高的时效性和学术可信度，有望引发对多模态非均匀压缩机制的进一步探讨。

## 项目链接
https://arxiv.org/abs/2606.07577
