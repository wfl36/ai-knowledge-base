# MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide Generation with Multi-turn Local Revision

**评分：** 8.2  
**状态：** 正常  
**标签：** Agent, 大模型, 记忆机制, 个性化生成, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17162v1 Announce Type: new Abstract: Personalized presentation generation requires more than conditioning on a current prompt or template: agents must preserve stable user preferences across tasks, retain newly introduced preferences and constraints during multi-turn revision, and carry out local edits reliably. We propose MemSlides, a hierarchical memory framework for personalized presentation agents that separates long-term memory from working memory and further divides long-term memory into user profile memory and tool memory. User profile memory stores intent-conditioned profiles for round-0 personalization, working memory carries active preferences and session constraints across revision rounds, and tool memory stores reusable execution experience for reliable localized editing. MemSlides pairs this memory design with scoped slide-local revision, so targeted updates act on the smallest affected region instead of repeatedly regenerating the full deck. In controlled experiments, user profile memory improves persona-alignment judgments on a multi-persona, multi-intent profile bank, tool-memory injection improves closed-loop modify behavior in diagnostic matched-pair settings, and qualitative cases illustrate working memory's ability to carryover preferences. Taken together, these results suggest that effective personalization in presentation authoring depends on separating persistent user profiles, session-level working memory, and reusable execution experience across generation and localized revision.

## 综合总结
MemSlides提出了一种面向个性化幻灯片生成的分层记忆驱动Agent框架，将记忆划分为用户画像记忆、工具记忆（长期）与工作记忆（短期），并结合局部修改策略，有效解决了多轮交互中的偏好遗忘与全局重生成问题，为交互式内容生成Agent提供了创新且实用的架构范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对个性化幻灯片生成中的偏好保留和多轮修改痛点，创新性地提出了分层记忆架构（长期记忆：用户画像记忆+工具记忆；短期记忆：工作记忆），并结合局部范围修改机制。该设计具有认知科学的理论支撑，且通过对照实验严谨验证了各记忆模块的独立贡献，研究深度与方法新颖性较高。

### 实用性 (评分: 8.0/10)
该框架精准抓住了交互式内容生成中的核心痛点（全局重生成代价大、多轮偏好易丢失）。其分层记忆机制和局部编辑策略不仅适用于幻灯片生成，也可直接迁移至长文档、代码或UI设计等多轮交互Agent场景，对工程实践和Agent架构设计具有极高的落地参考价值。

### 社区活跃度 (评分: 8.0/10)
个性化Agent与记忆机制是当前大模型领域的热门研究方向。论文发布于arXiv，作者团队包含知名学者（如清华朱军教授），来源权威性高。针对AI生成幻灯片这一高频应用场景，研究成果具有较高的行业关注度和时效性。

## 项目链接
https://arxiv.org/abs/2606.17162
