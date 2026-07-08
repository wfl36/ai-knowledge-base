# FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, Agent, AI4Science, 科学发现, 可审计性, 论文  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05682v1 Announce Type: new Abstract: LLM systems for scientific discovery increasingly assist with ideation, literature synthesis, experiment planning, and report generation, but the first research question they propose can remain difficult to audit: it may sound plausible without exposing the mechanism, falsifier, or assumption that a scientist should inspect. We introduce FirstResearch, a first-principles research-question formation framework for scientific LLM agents whose core artifact is a structured Research Question Certificate. The certificate records primitive definitions, assumptions, a mechanism model, a tension or contradiction, a falsifiable hypothesis, a minimal decisive test, and a failure update rule, making the proposed question inspectable before downstream execution. On ten LLM-agent research topics, FirstResearch outperforms controlled prompt-level baselines inspired by AI co-scientist, Agent Laboratory, and AI Scientist-v2 under a primary DeepSeek-blind-judge protocol. A Gemini-2.5-Flash independent-judge rescore of the same 40 baseline packages preserves the system-level ranking, with FirstResearch scoring 4.86/5 versus 4.38/5 for the strongest baseline and Pearson agreement of 0.865 on average score. A one-repeat ablation checkpoint further suggests that the certificate-centered core is the strongest component: certificate-only scoring reaches 4.90/5 under DeepSeek and 4.88/5 under Gemini, while removing certificates drops below 1/5 under both judges. These results are preliminary and use LLM judges rather than human domain experts, but they support a narrow scientific-discovery claim: explicit derivation constraints are a promising mechanism for making LLM-generated scientific questions more auditable. Code, prompts, saved outputs, and reproduction scripts are available at https://github.com/louiswang524/FirstResearch.

## 综合总结
本文提出了FirstResearch框架，针对LLM科学发现Agent生成的问题缺乏可审计性的痛点，创新性地引入了“研究问题证书”机制。该证书强制Agent在提出问题时明确原语定义、假设、机制模型、矛盾点、可证伪假设、最小决定性测试及失败更新规则，使科学问题在被执行前即可被审查。实验表明，该方法在多个科研主题上显著优于现有AI Scientist基线，消融实验证实证书机制是性能提升的核心。该研究为构建更严谨、可审计的AI自动科研系统提供了重要的结构化范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了“研究问题证书”这一核心概念，将科学问题的生成从自由文本生成转化为受约束的、可证伪的结构化推导过程。该方法深度融入了科学哲学中的可证伪性和机制解释，通过定义、假设、机制模型、矛盾点、可证伪假设、最小决定性测试和失败更新规则等7个原语，显著提升了LLM生成科学问题的严谨性和可审计性。消融实验强有力地证明了该证书机制的核心作用（移除证书后评分降至1/5以下），但评估依赖LLM评委而非人类领域专家，论证的绝对严谨性仍有进一步提升的空间。

### 实用性 (评分: 8.0/10)
对AI4Science领域的从业者和Agent开发者具有极高的实践指导价值。该框架提供了一套即插即用的结构化范式，可直接应用于现有的AI Scientist或自动化科研Agent中，以解决其生成问题“听起来合理但缺乏实质机制与可审查性”的痛点。项目开源了代码、提示词和复现脚本，极大降低了AI科研Agent开发者的落地与实验门槛。

### 社区活跃度 (评分: 8.0/10)
紧扣当前AI自动科研（如AI Scientist系列）的热点与痛点，时效性极强。针对LLM在科学发现中“生成看似合理但无法审计的问题”这一普遍社区痛点提出了创新解法，在开源社区和AI4Science领域具有较高的话题性和潜在影响力。尽管单作者且使用LLM作为评委稍显局限，但其开源精神和对前沿痛点的精准打击使其具备良好的社区传播潜力。

## 项目链接
https://arxiv.org/abs/2607.05682
