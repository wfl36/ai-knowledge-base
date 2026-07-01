# Indi-RomCoM: Code-Mixed Benchmark for Evaluating LLMs on Romanized Indic-English Instructions

**评分：** 7.7  
**状态：** 正常  
**标签：** 大模型, 多语言, 评估基准, 代码混合, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30790v1 Announce Type: new Abstract: Romanized Code Mixing (RCM), where bilingual speakers fluidly blend local languages with English in Roman script, has emerged as the dominant form of communication across multilingual communities. While Large Language Models (LLMs) perform strongly on monolingual and native-script benchmarks, their ability to follow instructions and reason over RCM-based content remains largely unexplored. To this end, we introduce the Indi-RomCoM benchmark for facilitating systematic evaluation on Indic Romanized Code-Mixed instructions. Our benchmark spans seven instruction-following tasks, four widely spoken Indic languages, and three controlled code-mixing intensity levels. We extensively evaluate a suite of LLMs covering proprietary, open-weight, and Indic-focused models under zero- and few-shot settings. LLMs consistently underperform on RCM instructions, with performance degrading as code-mixing density increases. Furthermore, reasoning tasks suffer less degradation than detection tasks (e.g., Toxicity) because the generated explanations offer necessary context. We believe Indi-RomCoM helps the community in developing inclusive multilingual systems.

## 综合总结
本文提出了Indi-RomCoM基准，用于评估大语言模型在罗马化印地语-英语混合代码（RCM）指令上的表现。该基准涵盖7项任务、4种语言及3种混合强度。实验表明，LLM在RCM指令上表现显著下降，且推理任务比检测任务更具鲁棒性。该工作填补了多语言评估的空白，对开发包容性多语言AI系统具有重要参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
针对罗马化印地语-英语混合代码（RCM）这一普遍但研究不足的语言现象，构建了包含7项任务、4种语言和3种混合强度的Indi-RomCoM基准。研究深度评估了多种LLM，揭示了模型性能随混合密度增加而下降的规律，并发现推理任务因生成解释提供上下文而比检测任务更具鲁棒性，论证严谨且具有启发性。

### 实用性 (评分: 7.5/10)
为面向南亚多语言社区的LLM开发提供了直接的评估工具和优化方向。开发者可利用该基准测试模型在真实口语化场景下的表现，并指导针对RCM的数据增强或微调实践，但适用范围主要局限于印地语系-英语混合场景。

### 社区活跃度 (评分: 7.5/10)
切中当前LLM在非标准多语言真实场景下表现不佳的痛点，话题具有高度时效性。作为arXiv发布的学术成果，为多语言NLP社区提供了重要的评估基准，有助于推动更具包容性的全球化AI系统发展。

## 项目链接
https://arxiv.org/abs/2606.30790
