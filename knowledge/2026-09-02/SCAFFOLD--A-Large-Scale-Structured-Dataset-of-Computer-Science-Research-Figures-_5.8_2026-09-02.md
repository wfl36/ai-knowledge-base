# SCAFFOLD: A Large-Scale Structured Dataset of Computer Science Research Figures with Diagram QA and Chain-of-Thought Reasoning Traces

**评分：** 5.8  
**状态：** 待复核  
**标签：** 多模态, 数据集, 图表理解, 视觉语言模型, 科学文献, Chain-of-Thought, 论文  
**更新日期：** 2026-09-02  
**来源：** rss  

## 项目描述
arXiv:2609.00018v1 Announce Type: new Abstract: Computer science papers rely heavily on diagrams: architecture drawings, system flowcharts, and pipeline schematics that often carry more information than the text around them. There is currently no public dataset that pairs this specific kind of figure with captions, context, questions, answers, and step-by-step reasoning, which is exactly what is needed to train a vision-language model to understand them. We present \textbf{SCAFFOLD}\footnote{https://github.com/theranjitraut/scaffold}, a large-scale structured dataset of computer science research figures with diagram QA and Chain-of-Thought reasoning traces. This dataset consists of (image, caption, context, question-answer, chain-of-thought) tuples from arXiv computer science papers prepared using layout detection and PDF parsing, with an AI-assisted question-generation step. The resulting large-sized SCAFFOLD-157K dataset spans 3,058 papers with 29,887 figures (157,387 pairs), a medium-sized SCAFFOLD-37K dataset (36,797 pairs), and a small-sized SCAFFOLD-12K dataset (12,000 pairs). We used SCAFFOLD-12K for baseline experiments on Qwen2.5-VL-3B-Instruct.

## 综合总结
SCAFFOLD是一个面向CS论文图表理解的大规模结构化数据集，包含约15.7万对(image, caption, context, QA, CoT)五元组，覆盖3058篇论文近3万张图表。方法上采用版面检测+PDF解析+AI辅助生成QA的流程，并提供了3个不同规模的子集。在Qwen2.5-VL-3B上做了baseline实验。整体属于数据工程类贡献，方法新颖性有限但填补了特定领域的数据空白，对科学图表理解方向有实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.5/10)
该工作提出SCAFFOLD数据集，从arXiv论文中自动提取图表-标题-上下文-问答-CoT五元组，方法上结合了版面检测、PDF解析和AI辅助问题生成。技术贡献以数据工程为主，缺乏新颖的算法或模型设计。baseline实验仅在Qwen2.5-VL-3B一个模型上完成，实验深度有限。但数据集构建流程相对完整，多规模版本（12K/37K/157K）的划分体现了系统性考量。

### 实用性 (评分: 6.5/10)
对做图表理解（diagram understanding）、科学文献多模态研究的从业者有一定参考价值，数据集填补了'CS论文图表+QA+CoT'这一空白领域，可直接用于微调VLM。开源仓库降低了使用门槛。AI辅助生成QA的质量、可信度未深入评估，实际训练效果有待验证。对非视觉理解方向的研究者参考意义有限。

### 社区活跃度 (评分: 5.5/10)
话题贴合多模态大模型与科学文献理解的前沿趋势，arXiv论文图表理解是VLM的重要应用场景，具有一定时效性。但论文于2026年9月发布（arXiv编号格式异常，疑似预印本时间标记有误），来源为普通作者团队，非头部机构或知名实验室，社区影响力有限。仅做了单模型baseline，未与GPT-4V、Gemini等强模型对比，传播度可能受限。

## 项目链接
https://arxiv.org/abs/2609.00018
