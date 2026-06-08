# Attack Selection in Agentic AI Control Evaluations Meaningfully Decreases Safety

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, AI安全, 评估, 红蓝对抗, 论文  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06529v1 Announce Type: new Abstract: An attacker that strategically chooses when to attack is much harder to catch than one that attacks indiscriminately. AI control is a safety framework for deploying capable but untrusted AI agents under the oversight of a weaker, trusted monitor and a limited human audit budget. Control evaluations stress-test these protocols by pitting a red-team attack policy against the blue-team monitor, but current evaluations typically assume attackers that do not strategically select when to attack. We study this capability, attack selection, in agentic settings by decomposing attack decisions into a start policy, which decides when an attacker should attack, and a stop policy, which decides when an attacker should abort an ongoing attack. Across two agentic settings, BashArena and LinuxArena, both policies substantially lower measured empirical safety without changing the underlying attack capability. At a 1% audit budget, our start policy reduces safety by 20pp on both BashArena and LinuxArena, and our stop policy reduces safety by 20pp on BashArena and 28pp on LinuxArena. These reductions should be interpreted as upper bounds on the effect of attack selection. Existing control evaluations may therefore yield overly optimistic safety estimates against selective attackers. We recommend that future evaluations, system cards, and safety cases elicit attack selection to produce more realistic safety estimates.

## 综合总结
该论文揭示了当前AI控制评估中忽略攻击者策略性选择时机的问题，提出将攻击选择分解为'开始策略'和'停止策略'。实验表明，在Agent环境中，这两种策略能显著降低实测安全性（在1%审计预算下降低20-28pp），证明现有评估对选择性攻击者可能过于乐观。研究建议未来的安全评估、系统卡和安全案例必须纳入攻击选择机制，以提供更真实的安全估计。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文指出了当前AI控制评估框架中的一个重要盲点：假设攻击者是不加选择地发起攻击。研究创新性地将攻击选择分解为'开始策略'（决定何时攻击）和'停止策略'（决定何时中止攻击），并在BashArena和LinuxArena两个Agent环境中进行了严谨的实证验证。结果表明策略性攻击选择能大幅降低实测安全性（降低20-28pp），论证逻辑严密，对现有评估方法论的局限性有深刻洞见。

### 实用性 (评分: 8.0/10)
对AI安全评估从业者具有极高的实践指导价值。研究直接指出了现有红蓝对抗测试的缺陷，并提供了可操作的改进方向：在未来的控制评估、系统卡和安全案例中必须引入攻击选择机制。虽然论文未提供开箱即用的完整防御方案，但其揭示的评估偏差足以指导安全团队立即调整其测试流程，以获得更真实的安全基线。

### 社区活跃度 (评分: 8.5/10)
Agent安全与对齐是当前大模型落地应用的核心痛点，该研究紧扣前沿热点，时效性极强。作为arXiv预印本，其学术规范性良好，且直击当前AI Control评估体系的软肋，对推动社区建立更严格、更现实的Agent安全评估标准具有重要影响力，预计将在AI安全与对齐社区引发广泛讨论。

## 项目链接
https://arxiv.org/abs/2606.06529
