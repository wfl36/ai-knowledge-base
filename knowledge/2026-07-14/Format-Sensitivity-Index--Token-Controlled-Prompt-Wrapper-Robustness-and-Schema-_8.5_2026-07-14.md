# Format Sensitivity Index: Token-Controlled Prompt Wrapper Robustness and Schema Compliance in LLM Benchmarking

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 评测基准, 结构化输出, 论文, 实证研究  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09665v1 Announce Type: new Abstract: Prompt wrappers often differ only in formatting, yet they can change model scores enough to flip leaderboard conclusions. We study this variance under a token-controlled protocol and introduce two complementary metrics: the Format Sensitivity Index (FSI), the accuracy range induced by wrapper choice, and the Parseability Sensitivity Index (PSI), the corresponding range in answer parseability. Across 140,000 OpenRouter generations spanning 7 QA tasks, 5 wrapper families, and 4 instruct models from 7B to 72B parameters, we find that mean FSI varies by over 30x across models and is largely explained by compliance failures. A fixed-effects regression shows that parseability remains a strong predictor of accuracy even after controlling for task, model, and wrapper. We argue that reporting accuracy without wrapper variance and compliance is statistically fragile, and we give practical recommendations for both benchmarking and structured-output deployments.

## 综合总结
本文针对LLM基准测试中Prompt格式变化导致模型得分大幅波动的问题，提出了格式敏感性指数（FSI）和可解析性敏感性指数（PSI）。通过14万次生成实验发现，不同模型的FSI差异超30倍，主要由格式合规性失败引起。研究指出当前仅报告准确率的评测方式在统计上是脆弱的，甚至可能翻转排行榜结论，并为基准测试和结构化输出部署提供了重要实践建议。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文揭示了LLM基准测试中Prompt格式微小变化对模型得分的巨大影响，创新性地提出了FSI（格式敏感性指数）和PSI（可解析性敏感性指数）两个量化指标。通过14万次大规模生成实验和固定效应回归分析，严谨地证明了格式合规性失败是导致得分波动的核心原因，指出现有仅报告准确率的评测体系在统计上是脆弱的，研究深度与论证严谨性俱佳。

### 实用性 (评分: 9.0/10)
对LLM评测从业者和工程开发者具有极高的指导价值。直接指出仅报告准确率而不考虑格式方差和合规性的做法存在缺陷，并为基准测试设计和结构化输出（如JSON输出）部署提供了具体的实践建议，能够有效指导开发者构建更鲁棒的LLM应用和更公平稳定的评测体系。

### 社区活跃度 (评分: 8.0/10)
话题极具时效性和行业痛点，直击当前大模型排行榜结果不可复现、易受格式扰动影响的争议核心。arXiv论文发布，虽为单一作者，但实验规模庞大（7任务/5格式/4模型/14万次生成），结论对当前大模型评测社区具有强烈的警示和纠偏意义。

## 项目链接
https://arxiv.org/abs/2607.09665
