# SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 大模型, 技能库, RAG, 评估, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15557v1 Announce Type: new Abstract: Agent skills, SKILL.md files that package reusable procedural knowledge for an LLM agent, are a popular mechanism for extending agent capabilities. Public repositories now host them in large and growing numbers, yet these artifacts are fragmented, redundant, and uneven in quality, and their value in practice is unclear. A core question remains open, namely how to consolidate this open-source SKILL.md ecosystem into a single usable corpus, and what bounds its benefit on real-world agent tasks. We present SkillCorpus, a framework that aggregates, curates, matches, and evaluates the open skill ecosystem at scale. It filters ~821,000 crawled skills through a multi-stage pipeline into 96,401 skills organised by a 16-class taxonomy and three quality facets (utility, robustness, safety), and pairs them with a fine-tuned retrieval-and-selection stack that matches task-relevant skills. We evaluate end-to-end across three benchmarks (SkillsBench, GDPVal, QwenClawBench), two harnesses, and two open backbones with a frontier robustness check. Integrating SkillCorpus yields consistent gains across all three benchmarks, largest on SkillsBench (+7.5 pp). An operational analysis traces the gains to a coverage boundary and a harness boundary. SkillCorpus is, to our knowledge, the first end-to-end account of when a curated, retrieval-served community corpus improves real agent tasks, and where it does not. The dataset, models, and code will be released upon acceptance.

## 综合总结
该论文提出了SkillCorpus框架，旨在解决LLM Agent开源技能（SKILL.md）碎片化、冗余和质量不均的问题。通过多阶段流水线将82.1万原始技能清洗为9.6万高质量技能，并建立16类分类和三维质量评估体系。结合微调的检索选择栈，在多个基准测试中实现了显著的性能提升（如SkillsBench提升7.5pp）。该研究首次端到端地揭示了社区技能语料库对真实Agent任务的增益及其边界，为Agent技能复用提供了重要的基础设施和理论指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
首次系统性解决LLM Agent开源技能碎片化问题，构建了从数据聚合、多阶段清洗、16类分类、三维质量评估到微调检索匹配的端到端框架。研究不仅验证了技能库在多个基准上的有效性，还深入剖析了收益的覆盖边界与线束边界，研究方法严谨，技术深度与新颖性俱佳。

### 实用性 (评分: 9.0/10)
对Agent开发者具有极高的实用价值。提供的9.6万高质量技能库及检索匹配模型可直接集成至现有Agent框架中，有效解决技能复用与碎片化痛点，显著提升Agent在真实任务中的表现与鲁棒性。

### 社区活跃度 (评分: 8.5/10)
Agent技能生态与知识增强是当前大模型应用落地的核心热点，话题时效性极强。论文来源于arXiv，且承诺数据集、模型与代码开源，具备极高的社区影响潜力和可信度，有望成为Agent技能调用的重要基础设施。

## 项目链接
https://arxiv.org/abs/2607.15557
