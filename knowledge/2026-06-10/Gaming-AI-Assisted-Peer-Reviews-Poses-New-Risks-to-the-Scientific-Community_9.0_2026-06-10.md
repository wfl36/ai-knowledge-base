# Gaming AI-Assisted Peer Reviews Poses New Risks to the Scientific Community

**评分：** 9.0  
**状态：** 正常  
**标签：** AI安全, 对抗攻击, 同行评审, 大模型, 论文  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.10159v1 Announce Type: new Abstract: AI is increasingly used to support scientific peer review, from manuscript screening, reviewer assistance to editorial triage. Although such systems promise to reduce reviewer burden and accelerate publication, their robustness to strategic manipulation remains poorly understood. Here we show that AI-mediated peer review is vulnerable to a simple, low-cost manipulation: superficial rephrasing of the manuscript abstract. Without changing the underlying scientific content and communication, and even without knowledge of the reviewing model, adversarially rewritten abstracts substantially improve AI review outcomes. We see this across disciplines and publication venues, for both human-written and AI-generated papers. Our strongest attack achieves an attack-success-rate of about 38%, increasing acceptance ratings by +1.31 for Gemini 3 Flash reviewers and by +0.88 for GPT 5.4 Mini reviewers on a 10-point scale. When the original AI review suggests 'reject', the success rate rises to more than 50%. This effect extends beyond overall score inflation, increasing review confidence and scores on core scientific criteria such as soundness, significance and perceived contribution. The attack is practical, requiring only about 5 minutes and $1 for a 10-page AI conference submission, and is hard to distinguish from ordinary scientific editing. Inflated AI reviews could bias downstream human decision-making, shifting editorial recommendations from rejection towards acceptance. These findings reveal a general vulnerability in AI-assisted scientific evaluation: when AI-generated review influence editorial decisions, authors may be incentivized to optimize manuscripts for AI judgment rather than scientific merit. Our results suggest that AI tools should not be treated as neutral evaluators in high-stakes peer review without systematic robustness testing, transparent safeguards and careful human oversight.

## 综合总结
本研究揭示了AI辅助同行评审系统面临的新型对抗风险：仅需对摘要进行低成本、表面化的改写，即可显著提升AI评审的接受率和各项评分，甚至误导人类编辑的最终决策。该漏洞跨模型、跨学科普遍存在，表明当前AI工具在缺乏鲁棒性测试和人工监督的情况下，不应作为高风险同行评审的中立评估者。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究揭示了AI辅助同行评审系统存在严重的对抗性漏洞。通过简单的摘要表面改写（不改变科学内容），攻击者能以极低成本（5分钟/1美元）显著提高AI评审的接受率（整体提升约38%，原本被建议拒绝的论文成功率超50%），甚至提升评审置信度和各项核心科学指标评分。该漏洞在跨学科、跨模型（如Gemini 3 Flash和GPT 5.4 Mini）中均普遍存在，论证严谨且量化分析充分。

### 实用性 (评分: 9.0/10)
对学术出版界、会议组织者和AI系统开发者具有极高的实践指导意义。研究证明AI评审分数的膨胀会实质性地误导人类编辑的下游决策，因此强烈建议在引入AI辅助评审时必须增加系统性鲁棒性测试、透明保障措施和严格的人工监督，避免作者为迎合AI判断而优化文稿而非提升科学价值。

### 社区活跃度 (评分: 9.5/10)
话题极具时效性与权威性，由Yarin Gal等知名学者发布。在AI广泛介入学术评审的当下，该研究敲响了警钟，指出AI不能被视为中立评估者，对维护学术公平和出版规范具有重大影响，势必引发学术界和工业界对AI评审安全性的广泛关注与规则反思。

## 项目链接
https://arxiv.org/abs/2606.10159
