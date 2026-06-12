# Does AI Reviewer See the Full Picture? Attacking and Defending Multimodal Peer Review

**评分：** 8.3  
**状态：** 正常  
**标签：** 多模态, 大模型, AI安全, 对抗攻击, AI4Science, 论文, 基准测试  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12716v1 Announce Type: new Abstract: The integration of Large Language Models (LLMs) and Multimodal LLMs (MLLMs) into scientific peer-review workflows introduces novel and significant risks for adversarial manipulation, especially given the multimodal nature of scientific papers where figures, not just text, convey core evidence. This creates a significant gap: current robustness studies on AI peer-review are overwhelmingly text-only. Moreover, the problem is distinct from standard jailbreaking, as a peer-review attack seeks to induce a domain-specific, targeted failure (e.g., "inflate this score") rather than a general safety policy violation, for which no practical defenses exist. To address this, we introduce PaperGuard, the first comprehensive benchmark designed to systematically evaluate and defend AI-generated peer-review against these domain-specific, cross-modal attacks. Our framework is built on three pillars: (1) a new multimodal peer-review dataset spanning multiple scientific domains; (2) a unified suite of attacks, including black-box prompt injections and white-box perturbations, specifically designed to target both text (GCG) and figures (PGD); and (3) a practical defense, motivated by the long-context challenge of academic papers, that uses chunk-based embedding search to efficiently localize and mitigate harmful instructions. Our extensive experiments, conducted across state-of-the-art models, confirm that AI reviewers are pervasively vulnerable. PaperGuard establishes the foundational benchmark, protocols, and actionable defense necessary to pioneer trustworthy, attack-resilient AI-assisted scholarly reviewing.

## 综合总结
本文揭示了多模态大语言模型（MLLMs）在科学同行评审中面临的跨模态对抗性操纵风险，指出当前AI审稿鲁棒性研究仅局限于文本且缺乏针对定向评分操纵的防御。为此，作者提出了首个综合基准PaperGuard，包含多模态评审数据集、针对文本和图像的黑白盒攻击套件，以及基于分块嵌入搜索的高效防御机制。实验证实当前先进AI审稿模型普遍存在漏洞，该研究为构建安全可信的AI辅助学术评审奠定了重要基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究切入点新颖，首次系统性揭示了多模态AI审稿系统中图表跨模态攻击的脆弱性，填补了当前仅关注文本鲁棒性的研究空白。论文清晰区分了同行评审攻击（诱导特定领域定向失败，如操纵评分）与传统越狱攻击的本质差异，理论认知深刻。提出的PaperGuard框架完整，包含数据集、黑白盒攻击套件（文本GCG与图像PGD）及基于分块嵌入搜索的防御机制，论证严谨，技术深度高。

### 实用性 (评分: 8.0/10)
随着AI辅助审稿工具在学术界的快速普及，该研究具有极高的现实指导价值。提出的防御方法针对学术论文长上下文的痛点，采用分块嵌入搜索来定位和缓解恶意指令，具备较强的工程可落地性。为OpenReview等学术平台及开发者提供了直接的评估基准、攻击测试协议和可操作的防御方案，适用范围明确。

### 社区活跃度 (评分: 8.5/10)
AI审稿的公平性与鲁棒性是当前学术界和AI社区高度关注且极具争议的痛点，该研究话题时效性极强。arXiv预印本来源，作者团队具备学术背景，可信度良好。研究直击AI审稿系统的核心安全威胁，预计将在AI4Science、AI安全及学术出版界引发广泛关注与讨论，影响力潜力大。

## 项目链接
https://arxiv.org/abs/2606.12716
