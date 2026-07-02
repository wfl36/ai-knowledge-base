# Identifying and Resolving Pitfalls of Knowledge-Based VQA Benchmarks: Auditing, Repairing, and Augmenting

**评分：** 8.3  
**状态：** 正常  
**标签：** VQA, 多模态, 评估基准, 视觉语言模型, 知识推理, 论文  
**更新日期：** 2026-07-02  
**来源：** rss  

## 项目描述
arXiv:2607.00159v1 Announce Type: new Abstract: Knowledge-Based Visual Question Answering (KB-VQA) aims to evaluate whether Visual Language Models (VLMs) can retrieve, ground, and reason over external structured knowledge beyond visual evidence. In practice, answer accuracy is widely adopted as the primary evaluation metric, implicitly treating correctness as a proxy for knowledge-grounded reasoning. However, for existing KB-VQA benchmarks, this proxy relies on critical assumptions that are often overlooked and rendered unreliable by benchmark issues: annotated answer must be derivable from the associated knowledge base, question must be well-posed with sufficient constraints, and visual setting must meaningfully require grounded disambiguation. In this work, we show that these assumptions are systematically violated in existing KB-VQA benchmarks. Our audit reveals substantial instances with missing or contradicted answers and underspecified questions that render accuracy a misleading metric. Furthermore, we find that existing datasets rely on visually trivial, single-entity scenes that bypass the need for sophisticated visual-to-knowledge mapping. We demonstrate that even with controlled architectures, these flaws lead to distorted model rankings and overestimations of reasoning capabilities. To address this, we introduce (1) a principled audit-and-repair protocol that restores answer derivability and question clarity, and (2) a controlled multi-entity augmentation protocol that introduces visual ambiguity to challenge initial retrieval and grounded reasoning. Re-evaluation under corrected and augmented settings yields markedly different performance trends. Our findings call for rethinking evaluation protocols and designing more interaction-aware KB-VQA benchmarks that prioritize verifiable reasoning over simple matching.

## 综合总结
本文系统性地揭示了现有知识驱动视觉问答(KB-VQA)基准中的三大系统性缺陷（答案缺失/矛盾、问题约束不足、视觉场景过于简单），指出这些问题导致准确率成为误导性指标并扭曲了模型排名。为此，作者提出了审计与修复协议及多实体增强协议，通过引入视觉歧义来挑战模型的真实检索与推理能力。重新评估结果显示模型性能趋势发生显著变化，有力地呼吁社区重新思考评估协议，构建注重可验证推理而非简单匹配的KB-VQA基准。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文对知识驱动视觉问答(KB-VQA)基准进行了深度的逆向工程与系统性剖析，精准指出了现有基准在答案可推导性、问题约束充分性及视觉消歧必要性上的三大系统性缺陷。提出的方法论包含严谨的审计修复协议与多实体增强协议，不仅从理论层面解构了'准确率即推理能力'的伪命题，更通过控制变量实验证实了基准缺陷对模型排名的扭曲，论证逻辑严密，洞察深刻。

### 实用性 (评分: 8.0/10)
研究具有极高的工程指导价值。审计与修复协议可直接用于现有KB-VQA数据集的清洗与纠错，多实体增强协议则为构建新一代抗捷径、强推理的数据集提供了标准化的数据扩增范式。对VLM研发团队和评测机构而言，该工作提供了避免高估模型推理能力、修正评测偏差的实操工具。

### 社区活跃度 (评分: 8.5/10)
在VLM评估屡遭质疑的当下，该论文直击多模态推理评估的痛点，时效性极强。揭示现有SOTA模型可能仅是在做'简单匹配'而非'知识推理'，对当前大模型社区盲目追求榜单高分的现象敲响了警钟，其反思评估范式的呼吁极易引发广泛共鸣与讨论。

## 项目链接
https://arxiv.org/abs/2607.00159
