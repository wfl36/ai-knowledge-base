# LLM-Based Scientific Peer Review: Methods, Benchmarks, and Reliability Challenges

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 同行评审, 综述, RAG, 对齐, 鲁棒性, AI安全  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.25057v1 Announce Type: new Abstract: The rapid growth of scientific submissions has pushed traditional peer review toward its scalability limits, motivating the exploration of large language models (LLMs) as intelligent automated evaluation assistants. Although recent studies show that LLMs can generate fluent critiques and approximate reviewer scores, their reliability, robustness, and security as decision-support systems remain insufficiently understood. This survey offers a systems-level analysis of LLM-based scientific peer review, focusing on two core evaluative functions: critique generation and score prediction. We present a structured taxonomy of modeling approaches (including prompt-based, supervised, retrieval-augmented, and alignment-optimized approaches), and synthesize empirical findings across existing benchmarks. We analyze dataset constraints, evaluation shortcomings, and domain concentration biases that limit current assessment practices. Beyond performance metrics, we identify emerging robustness risks, including prompt injection, data poisoning, retrieval vulnerabilities, and reward hacking, which expose automated review pipelines to strategic manipulation. From a data mining perspective, we outline key open challenges in modeling subjective disagreement and cross-domain generalization. By reframing automated peer review as a high-stakes, multi-objective decision problem, this survey provides a roadmap for developing robust, transparent, and trustworthy AI-assisted scientific evaluation systems.

## 综合总结
本文系统综述了LLM在科学同行评审中的应用，聚焦评审生成与分数预测两大核心功能，提出了涵盖提示、监督、RAG及对齐优化的方法分类法。文章综合了现有基准的实证发现，分析了数据集与评估的局限性及领域偏见，并重点揭示了提示注入、数据投毒等鲁棒性风险。最终将自动评审重构为高风险多目标决策问题，为构建鲁棒、透明、可信的AI辅助评审系统提供了发展路线图。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
从系统级视角对LLM辅助科学同行评审进行了深度剖析，不仅构建了包含提示、监督、RAG和对齐优化的方法分类法，还前瞻性地揭示了提示注入、数据投毒和奖励黑客等安全与鲁棒性风险，并将其重新定义为高风险多目标决策问题，展现了较强的理论深度与系统性。

### 实用性 (评分: 7.5/10)
对学术会议组织者、AI评审系统开发者及科研政策制定者具有高参考价值，明确指出了现有基准的局限性和安全漏洞，可直接指导AI评审系统的安全防护设计与评估体系优化，但距离普通开发者直接落地应用仍有一定距离。

### 社区活跃度 (评分: 8.0/10)
LLM辅助同行评审是当前学术界极具争议与关注度的前沿热点，arXiv预印本保证了话题的极高时效性。该议题触及学术发表的根基与公平性，极易引发学术社区、出版机构及AI研究者的广泛讨论与关注。

## 项目链接
https://arxiv.org/abs/2606.25057
