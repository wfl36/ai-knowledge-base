# DC-Leap: Training-Free Acceleration of dLLMs via Draft-Guided Contiguous Leaping Decoding

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 扩散模型, 推理加速, 解码策略, 论文  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20467v1 Announce Type: new Abstract: While parallel decoding is central to the efficiency of Diffusion Large Language Models (dLLMs), current strategies are often hindered by overly conservative confidence thresholds. These thresholds, necessitated by the Joint Probability Dependence Error (JPDE), result in redundant denoising iterations and suboptimal inference speeds. To overcome this, we propose DC-Leap, a training-free framework that enables reliable acceleration of dLLMs in the moderate-confidence regime. DC-Leap introduces a Dynamic Contiguous Verification strategy that integrates strictly-ordered causal constraints into the parallel decoding process. By progressively validating token dependencies, this mechanism effectively neutralizes the JPDE, enabling reliable acceleration with comparable performance. Furthermore, DC-Leap incorporates the draft-guided decoding mechanism, where the draft helps extend the context by leaping forward across multiple tokens, providing look-ahead context and retaining the structural benefits of bidirectional attention during inference. Extensive experiments on standard benchmarks demonstrate that DC-Leap achieves substantial speedups, up to 53.19x on MBPP for long-sequence generation, and up to 105.02x when combined with KV-Cache with comparable generation quality. Code is available at https://github.com/ffh-wyls/DC-Leap .

## 综合总结
本文提出DC-Leap，一种针对扩散大语言模型的免训练推理加速框架。针对并行解码中因联合概率依赖误差(JPDE)导致的保守解码问题，DC-Leap引入动态连续验证策略整合因果约束以中和JPDE，并结合草稿引导机制实现跨token跳跃以保留双向注意力优势。实验证明，该方法在保持生成质量的同时，实现了最高53.19倍及结合KV-Cache后105.02倍的惊人加速，为dLLM的规模化应用提供了关键突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文针对扩散大语言模型并行解码中的联合概率依赖误差(JPDE)问题，提出了免训练加速框架DC-Leap。其技术创新点在于：一是提出动态连续验证策略，将严格有序的因果约束引入并行解码，有效中和了JPDE；二是引入草稿引导机制，通过跨token跳跃提供前瞻上下文，保留了双向注意力的结构优势。理论分析与机制设计严谨，对dLLM解码瓶颈的突破具有深度洞见。

### 实用性 (评分: 8.5/10)
该方案具有极高的工程落地价值。首先，作为一种免训练框架，它可以直接集成到现有的dLLM推理流程中，无需额外的模型微调成本；其次，在MBPP基准上实现了长序列生成53.19倍、结合KV-Cache高达105.02倍的显著加速，且生成质量可比，直击dLLM推理慢的核心痛点；最后，项目已开源，极大降低了从业者的复现与应用门槛。

### 社区活跃度 (评分: 9.0/10)
扩散大语言模型是当前大模型领域的前沿探索方向，其推理效率是制约其发展的关键社区痛点。本文提出的百倍级加速方案极具话题性与震撼力，若实验结论经得起复现，将对dLLM的生态发展产生重大推动作用。论文发布于arXiv且附带开源代码，来源可信度高，时效性强。

## 项目链接
https://arxiv.org/abs/2607.20467
