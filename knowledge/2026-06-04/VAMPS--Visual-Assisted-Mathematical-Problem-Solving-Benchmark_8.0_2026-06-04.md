# VAMPS: Visual-Assisted Mathematical Problem Solving Benchmark

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 多模态, 推理, 评测基准, Agent, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04244v1 Announce Type: new Abstract: Multimodal large language models are increasingly capable of complex reasoning, yet their performance often degrades when they must externalize a problem through a tool and then reason over the tool's output, specifically when they rely on visual aids. This gap is especially important because real engineering and scientific workflows often rely on visualization tools for analysis, validation, and decision-making. To study this discrepancy, we introduce VAMPS (Visual-Assisted Mathematical Problem Solving), a benchmark for graph-assisted mathematics. VAMPS contains 1,168 multimodal, bilingual multiple-choice question-answer pairs drawn from Iranian University Entrance Exam algebra and calculus problems and expanded with human-reviewed LLM-generated synthetic variants, all selected so that plotting provides a natural solution strategy by revealing intersections, extrema, asymptotes, etc. Designed for both benchmarking and diagnosis, VAMPS goes beyond prior multimodal benchmarks that primarily evaluate reasoning over fixed visual inputs by testing whether a model can benefit from constructing a useful graph and grounding its answer in the resulting visualization. Overall, we found that across a diverse set of models, direct analytical solving surprisingly outperforms tool-enabled visual solving, even on problems where plotting is a natural strategy.

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了VAMPS基准，创新性地评估了多模态大模型在'主动构建可视化工具并基于其输出推理'的能力，而非传统的被动图像理解。研究发现了一个反直觉但极具价值的结论：当前模型直接解析求解的表现优于借助画图工具求解，暴露了模型在'工具调用-视觉反馈-逻辑闭环'上的严重缺陷，技术洞见深刻，论证严谨。

### 实用性 (评分: 7.0/10)
对大模型研发人员和Agent系统开发者具有较高参考价值，指出了当前MLLM在科学计算与可视化工作流中的瓶颈，为后续优化工具调用与多模态对齐提供了明确的评测抓手。但对非底层研发人员的直接工程落地指导相对有限，主要作为评测与诊断工具使用。

### 社区活跃度 (评分: 8.5/10)
话题紧扣当前多模态大模型与Agent工具调用热点，研究结论（画图辅助反而降低准确率）具有强烈的反直觉特征，极易引发社区关注与讨论。来源为arXiv学术论文，作者团队背景专业，具备较高的权威性与社区传播潜力。

## 项目链接
https://arxiv.org/abs/2606.04244
