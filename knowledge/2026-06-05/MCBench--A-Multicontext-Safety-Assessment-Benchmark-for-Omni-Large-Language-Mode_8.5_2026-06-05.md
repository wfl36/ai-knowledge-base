# MCBench: A Multicontext Safety Assessment Benchmark for Omni Large Language Models

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 多模态, 安全对齐, 评测基准, 跨模态推理, 论文  
**更新日期：** 2026-06-05  
**来源：** rss  

## 项目描述
arXiv:2606.05177v1 Announce Type: new Abstract: Existing multimodal safety benchmarks focus solely on visual inputs and cannot assess Omni Large Language Models (LLMs) that process vision, audio, and text. We introduce MCBench, a benchmark with 1196 scenarios spanning four safety categories that require integrating multiple modalities for accurate safety assessment. Each unsafe scenario is paired with a minimally different safe counterpart to assess model sensitivity. Our evaluations of state-of-the-art models reveal significant challenges. Omni LLMs struggle with subtle or non-physical risks but perform better when salient visual or acoustic cues are present. Analysis of reasoning traces shows that, although models can extract modality-specific information, they often fail to integrate these cues effectively for safety judgments. Our findings reveal that current Omni LLMs lack robust cross-modal reasoning in safety-critical settings, underscoring the need for improved architectures and training strategies for multimodal safety.

## 综合总结
本文提出了MCBench，首个针对处理视觉、音频和文本的Omni LLM的多上下文安全评估基准。该基准包含1196个场景，通过配对最小差异的安全/不安全场景来精准评估模型敏感性。实验发现当前SOTA模型在显著线索下表现尚可，但在处理微妙或非物理风险及跨模态信息整合时存在严重不足，揭示了现有Omni LLM在安全关键场景下缺乏稳健的跨模态推理能力，亟需架构与训练策略的改进。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对Omni LLM的安全评估提出了创新的MCBench基准，填补了音频+视觉+文本多模态安全评估的空白。通过构建最小差异的安全/不安全场景配对，严谨地测试了模型对微妙风险的敏感度，并深入剖析了跨模态推理整合失败的根因，研究深度与论证严谨度均属上乘。

### 实用性 (评分: 8.0/10)
对多模态大模型研发团队具有极高的实践指导价值。MCBench可直接作为Omni LLM安全对齐与红蓝对抗的评测工具，其关于“模型难以整合跨模态线索”的发现，为后续改进模型架构和训练策略提供了明确的优化方向。

### 社区活跃度 (评分: 9.0/10)
随着全模态大模型的爆发，Omni LLM的安全问题正处于社区关注的风口浪尖，话题时效性极强。作者团队具备权威学术背景，基准的发布有望成为该细分领域的重要标准，具有较高影响力和可信度。

## 项目链接
https://arxiv.org/abs/2606.05177
