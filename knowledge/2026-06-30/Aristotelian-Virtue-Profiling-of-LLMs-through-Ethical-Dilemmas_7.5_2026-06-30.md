# Aristotelian Virtue Profiling of LLMs through Ethical Dilemmas

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 对齐, 伦理评估, AI安全, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28683v1 Announce Type: new Abstract: Large Language Models (LLMs) often face ethical tradeoffs in which several responses may be defensible but express different priorities, such as fairness, honesty, courage, or restraint. We introduce VirtueMap, a framework for describing these patterns through an Aristotelian virtue-ethics lens. Instead of asking for a single correct answer, VirtueMap asks humans or LLMs to rank all five responses to each of seven general, non-lethal, non-political, and non-religious ethical dilemmas. To define the reference orderings used for scoring, we first proposed, for each dilemma and virtue, an ordering of the five responses from most to least expressive of that virtue. We then collected more than 100 respondent evaluations per ordering and retained it as operational ground truth only when at least 95% confirmed it. Rankings are scored against these retained orderings using normalized Borda alignment, yielding profiles over Practical Wisdom, Justice, Truthfulness, Courage, and Temperance. We apply VirtueMap to nine LLM families in a repeated-run evaluation and find high mean rank consistency (90.3%), with the largest differences appearing on Courage, Temperance, and Justice. We also release an interactive website that computes profiles locally in the browser and compares respondents with measured LLM profiles.

## 综合总结
本文提出了VirtueMap框架，基于亚里士多德美德伦理学对LLM在伦理困境中的表现进行多维画像。该框架摒弃了单一正确答案的评估方式，转而让模型对5个回答进行排序，并利用高一致性（>95%同意）的人类标注作为基准，通过归一化Borda对齐量化模型在实践智慧、正义、诚实、勇气和节制五个维度的表现。对9个LLM家族的测试表明模型排序一致性高（90.3%），但在勇气、节制和正义上存在显著差异，为LLM价值观评估提供了新颖的量化工具和哲学视角。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
本文创新性地引入亚里士多德美德伦理学视角来评估LLM的伦理倾向，突破了传统单一正确答案的对齐评估范式。通过要求模型对多选项进行排序，并采用严格的人类标注共识（>95%确认率）构建基准，结合归一化Borda对齐算法进行量化评分，方法论严谨且具有哲学深度。但评估困境数量较少（仅7个），在刻画复杂伦理空间时的广度受限。

### 实用性 (评分: 7.0/10)
VirtueMap为LLM的安全对齐和价值观微调提供了细粒度的评估工具，能够直观展示模型在实践智慧、正义、诚实、勇气和节制五个维度的差异。配套的交互式网站增强了易用性，有助于开发者和研究者进行模型选型和偏见检测。然而，由于测试场景规模较小且剔除了政治、宗教等高风险敏感话题，在工业级大规模落地和复杂真实场景应用中仍需扩展。

### 社区活跃度 (评分: 7.5/10)
LLM伦理对齐是当前AI社区的核心关注点，本文从美德伦理学切入，提供了区别于传统功利主义或规则对齐的新颖视角，话题具有较强时效性。作为arXiv上的学术论文，其构建的高共识基准和开源工具具备一定的学术传播潜力，但跨学科（哲学与AI）的属性可能使其在主流AI工程社区的影响力受限。

## 项目链接
https://arxiv.org/abs/2606.28683
