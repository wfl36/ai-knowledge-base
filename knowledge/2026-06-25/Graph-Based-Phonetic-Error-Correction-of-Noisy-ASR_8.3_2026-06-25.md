# Graph-Based Phonetic Error Correction of Noisy ASR

**评分：** 8.3  
**状态：** 正常  
**标签：** ASR, 错误纠正, GNN, LLM, 论文  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.24889v1 Announce Type: new Abstract: Automatic speech recognition (ASR) systems, despite low overall word error rates, produce residual lexical errors that disproportionately affect semantically critical tokens such as named entities, negations, and sentiment-bearing words. These errors are often structured, arising from phonetic similarity rather than random noise, making naive token-level correction insufficient. We propose a structured ASR correction framework, that we call G-SPIN, that combines phonetic graph modeling with contextual language understanding. A graph neural network (GNN) first constructs acoustically plausible candidate neighborhoods for flagged tokens, explicitly restricting the correction search space to phonetic alternatives. A masked language model (MLM) then provides local contextual scoring, and an instruction-tuned large language model (LLM) performs final context-aware re-ranking over this compact candidate set. By decoupling structured phonetic reasoning from contextual semantic selection, our method avoids unconstrained generation while improving correction accuracy. The framework is lightweight, modular, and operates entirely at inference time.

## 综合总结
本文提出G-SPIN框架，用于解决ASR系统中影响关键语义的残留语音错误。该框架通过解耦策略，先由GNN构建语音候选图限制搜索空间，再经MLM局部评分，最后由指令微调LLM进行上下文感知重排序。此方法避免了LLM无约束生成的幻觉，提升了纠错准确性，且框架轻量、纯推理运行，极具工业落地价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
创新性地将ASR纠错解耦为结构化语音推理与上下文语义选择，利用GNN构建语音候选图限制搜索空间，结合MLM与指令微调LLM进行分层重排序，有效避免了LLM无约束生成的幻觉问题，方法设计巧妙且具有较好的技术深度与严谨性。

### 实用性 (评分: 9.0/10)
针对ASR在关键语义token（如命名实体、否定词）上的残留错误这一工业界痛点，提出了轻量级、模块化且完全在推理时运行的纠错框架，无需重新训练原有ASR模型，即插即用，具有极高的实际落地价值和广泛的适用场景。

### 社区活跃度 (评分: 7.5/10)
话题结合了ASR纠错与LLM应用，属于当前AI社区的热点探索方向；论文发布于arXiv，虽未经同行评审，但直击语音处理领域的核心痛点，具备产生较好社区影响力的潜力。

## 项目链接
https://arxiv.org/abs/2606.24889
