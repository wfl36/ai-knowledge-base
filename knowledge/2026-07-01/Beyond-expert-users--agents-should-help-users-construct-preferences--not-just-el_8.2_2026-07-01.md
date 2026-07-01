# Beyond expert users: agents should help users construct preferences, not just elicit them

**评分：** 8.2  
**状态：** 正常  
**标签：** Agent, 交互设计, 推荐系统, 偏好学习, 信息经济学, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30863v1 Announce Type: new Abstract: Agents typically assume an expert user -- one with well-formed preferences about what they want -- and default to clarifying questions whenever the task is underspecified. We argue this assumption is unrealistic. Users often lack the domain knowledge to have completely specified preferences; if asked about their preference on some feature, the user may be unable to answer without the agent helping the user to learn some domain knowledge needed to form a preference for that feature, e.g., via examples or explanations. To formalize these principles, we draw on the Search-Experience-Credence framework from Information Economics to introduce CoPref, a model of how users construct preferences based on agent dialog actions. We then study these ideas concretely in agentic recommender systems, proposing CoShop, an interactive benchmark. In CoShop, an agent converses with and makes recommendations for a CoPref user. The agent's performance depends on whether it can help the user gain the knowledge needed to specify the task well. Evaluating five frontier models, we find that no agent exceeds 56% accuracy on CoShop despite five turns of interaction. Failures stem not from agents' ability to find items, but from how little the interaction expands what users know about what they want.

## 综合总结
本文挑战了当前AI Agent假设用户为‘专家’并仅通过澄清问题获取偏见的常规范式。作者指出，用户往往缺乏形成明确偏好的领域知识，Agent应帮助用户‘构建’而非仅仅‘引出’偏好。基于信息经济学框架，论文提出了CoPref偏好构建模型，并开发了CoShop交互式基准进行验证。对五个前沿模型的测试表明，最高准确率仅56%，揭示了当前Agent在扩展用户认知方面的严重不足。该研究为下一代Agent的交互设计提供了重要的理论依据和评估工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文在技术深度与洞见上表现出色。它挑战了当前Agent系统普遍假设用户具有明确偏见的常规设定，指出在任务未明确时仅通过澄清性问题是不够的。引入信息经济学中的Search-Experience-Credence框架来形式化用户偏好构建过程，并提出了CoPref模型，具有跨学科的理论新颖性。同时，提出了CoShop交互式基准，将理论落地为可计算的评估方法。对五个前沿模型的测试显示最高准确率仅56%，揭示了当前模型在帮助用户构建偏好上的严重不足，论证严谨且具有深刻的启发性。

### 实用性 (评分: 8.0/10)
对AI Agent开发者、产品经理及交互设计师具有极高的实际参考价值。论文指出了当前Agent交互设计的盲区——从‘引导/询问’转向‘教育/构建’，这直接指导了下一代推荐系统、对话式AI的交互范式重构。CoShop基准为评估Agent的偏好构建能力提供了具体的测试集，可帮助从业者在开发中优化Agent的交互策略，提升在非专家用户场景下的产品体验和转化率。

### 社区活跃度 (评分: 8.0/10)
话题具有极强的时效性和前瞻性。随着大模型驱动的Agent成为AI应用的主流范式，如何处理长尾/非专家用户的交互成为核心痛点。作者团队（包含Ludwig Schmidt, Carlos Guestrin等知名学者）在AI领域具有高度权威性和影响力。论文指出的‘前沿模型在偏好构建上表现不佳’的结论，切中当前AI社区的要害，有望引发关于Agent交互范式和评估标准的广泛讨论。

## 项目链接
https://arxiv.org/abs/2606.30863
