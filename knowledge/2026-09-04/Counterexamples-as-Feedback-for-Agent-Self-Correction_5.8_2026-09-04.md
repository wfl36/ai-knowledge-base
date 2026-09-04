# Counterexamples as Feedback for Agent Self-Correction

**评分：** 5.8  
**状态：** 待复核  
**标签：** Agent, 代码生成, 自我修正, NL2Regex, 反例引导, 论文, 评估方法  
**更新日期：** 2026-09-04  
**来源：** rss  

## 项目描述
arXiv:2609.02892v1 Announce Type: new Abstract: Single-turn code-generation metrics understate a central property of deployed agents: whether they can repair a wrong artifact after receiving concrete feedback. This paper presents A-CEGIS, a lightweight framework that uses counterexamples as feedback for evaluating multi-turn refinement in natural-language-to-regex synthesis. An agent proposes a regex, a deterministic oracle checks it under full-match semantics, and compact false-positive or false-negative witnesses guide the next turn. On 30 NL-RX-Turk tasks, diagnostic counterexample feedback solves 90\% of tasks within a four-turn ablation budget, compared with 17% for zero-shot generation, 27% for generic self-correction, and 23% for error-only feedback. In a full diagnostic run with hardening, all tasks are solved on the hidden set by the final turn, with mean time-to-success of 2.7 turns and robust success of 77% after targeted probing. These results show that A-CEGIS measures how efficiently an agent improves across turns while adding a practical robustness check beyond the original held-out cases.

## 综合总结
A-CEGIS是一个面向NL2Regex任务的轻量级多轮修正评估框架，利用确定性oracle生成的反例反馈引导Agent迭代改进。实验在30个任务上证明反例反馈显著优于零样本生成和通用自修正方法（90% vs 17-27%）。工作观点正确——多轮修复能力比单轮指标更反映实际部署价值——但任务范围和基准规模限制了其普适性贡献，属于在小众场景下验证已有思路的扎实工程性工作。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
论文提出A-CEGIS框架，将反例作为反馈驱动多轮修正，用于自然语言到正则表达式的生成任务。核心思路不算全新（反例引导的归纳编程CEGIS已有较长历史），但在LLM Agent语境下重新包装为多轮自我修正评估框架有一定新意。技术深度有限：确定性oracle验证、紧凑见证生成在NL2RX场景相对直接；30个任务的基准规模较小，实验虽展示了显著对比（90% vs 17%/27%/23%），但缺乏对不同LLM后端、泛化性、oracle构造复杂度的深入分析。论证整体合理但深度不足。

### 实用性 (评分: 6.0/10)
对从事NL2代码生成、Agent评估或自动程序修复的研究者/工程师有一定参考价值。框架轻量、易复现，且强调多轮修正能力比单轮指标更贴近实际部署场景，观点切中行业痛点。但局限在于：仅在NL2Regex这一狭窄任务上验证，正则合成的oracle构造相对简单，迁移到更复杂的代码生成（如Python函数）时可行性存疑；30个任务的benchmark规模也限制了结论的普适性。

### 社区活跃度 (评分: 5.0/10)
arXiv预印本，发布时间标注2026年（疑似未来日期或笔误），作者来自学术机构但知名度不高。话题（Agent自修正、反例反馈）属于当前LLM Agent研究的热门方向，但该工作聚焦子任务（NL2Regex）较为小众，影响力有限。无明显顶会背书（如NeurIPS/ICML/ACL），社区关注度和传播度预计中等偏低。

## 项目链接
https://arxiv.org/abs/2609.02892
