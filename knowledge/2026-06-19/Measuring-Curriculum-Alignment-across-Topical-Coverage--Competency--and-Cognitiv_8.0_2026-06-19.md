# Measuring Curriculum Alignment across Topical Coverage, Competency, and Cognitive Depth: A Longitudinal Framework Applied to CS2013 and CS2023

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型应用, RAG, 语义检索, 教育, 课程评估, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19469v1 Announce Type: new Abstract: Undergraduate computer science is governed by international curricular guidelines revised about once a decade, yet programs lack a reliable, reproducible way to measure how completely they cover the current guidelines and how that coverage shifts when the guidelines are restructured. We address this with a human-in-the-loop pipeline that measures a program's coverage of an external body of knowledge, applied longitudinally to one accredited BSc in Computer Science against Computer Science Curricula 2013 (CS2013) and 2023 (CS2023). The pipeline represents the program and each guideline as structured corpora, generates candidate course-to-knowledge-unit matches by semantic retrieval, and confirms them through human judgment under an explicit coverage definition. Of seven benchmarked retrievers, a reciprocal-rank-fusion ensemble was strongest, and a reputed long-context model underperformed a small sentence model, so retriever choice must be measured. Both maps were validated by an independent second rater (Cohen's kappa 0.64 for CS2023, 0.69 for CS2013). The program covers 49.7% of CS2023 and 50.9% of CS2013 knowledge units, near-constant across a decade. Extending the same retrieve-then-confirm design to competency articulation and cognitive depth shows that the program articulates the competency for ~88% of covered units under each guideline, yet delivers it at the recommended depth for 76% of present units under CS2023 against 95% under CS2013, a gap reflecting the newer guideline's raised expectations, not the program. The longitudinal comparison separates persistent structural gaps (parallel and distributed computing, foundations of programming languages, systems fundamentals), uncovered against both guidelines and ABET, from differences that reflect the standard's evolution. The instrument is reusable and available from the authors on request.

## 综合总结
本文提出一种人机协同流水线，利用语义检索与人工确认评估计算机本科课程与CS2013/CS2023指南的对齐度。研究发现长上下文模型检索表现不及小句子模型，且课程在CS2023下的认知深度对齐度因标准提高而显著下降。该框架能有效区分长期结构性缺口与标准演进差异，工具可复用，对高等教育课程评估与设计具有重要实践价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出了一种基于人机协同的流水线，结合语义检索（倒数秩融合集成）与人工判断来测量课程与知识体系的对齐度。实证发现 reputed 长上下文模型在特定检索任务上不如小句子模型，强调了检索器选择必须经过实证测量；并将对齐度评估从主题覆盖扩展至能力表达与认知深度，方法论严谨（通过Cohen's kappa验证了评分者间信度）。

### 实用性 (评分: 8.5/10)
该框架可直接用于高校计算机科学课程与CS2013/CS2023指南及ABET认证的对齐度评估，帮助教育者精准识别长期结构性缺口（如并行与分布式计算等）与标准演进带来的差异。工具具有可复用性，作者可应要求提供，对课程设计和教育管理具有极高的实践指导价值。

### 社区活跃度 (评分: 7.5/10)
紧扣最新发布的CS2023计算机科学课程指南，时效性强。研究由高校学者完成，发布于arXiv，对计算机教育社区及认证机构具有较高的参考价值和可信度，能够为全球高校应对新一轮课程大纲改革提供数据支撑。

## 项目链接
https://arxiv.org/abs/2606.19469
