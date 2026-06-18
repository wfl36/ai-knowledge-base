# VISUALSKILL: Multimodal Skills for Computer-Use Agents

**评分：** 9.1  
**状态：** 正常  
**标签：** Agent, CUA, 多模态, MCP, 技能库, 论文  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18448v1 Announce Type: new Abstract: Computer-use agents (CUAs) approach human-level performance on standardised benchmarks but still struggle on long-horizon tasks and unseen software. Existing skill libraries address this with reusable skills, but represent the skill artifact as text only, despite the visual nature of GUI interaction. We propose VISUALSKILL: a hierarchical multimodal skill, tailored to each target application and organised as a central index over per-topic files, which the agent consumes through a load_topic MCP tool that fetches the relevant topic's text and figures on demand. We construct each skill with a two-stage pipeline that combines authored documentation with live-application UI exploration. On two CUA benchmarks, CUA-World and OSExpert-Eval, a Claude Code CLI agent backed by Claude Opus 4.6 reaches an average score of 0.456 with VISUALSKILL, a +15.3 point absolute lift over the no-skill baseline (0.303). Against a matched text-only skill that is generated from the same source content and differs from VISUALSKILL only in modality, VISUALSKILL yields a further +8.3 point absolute gain over the matched text-only skill (0.373 vs. 0.456), providing direct evidence that retaining visual figures in the skill artifact, rather than verbalizing them away, helps the agent both identify UI elements and verify workflow state after each action. Our code is available at https://github.com/XMHZZ2018/VisualSkills.

## 综合总结
本文提出VISUALSKILL，一种针对计算机使用代理(CUA)的分层多模态技能库。针对现有技能库纯文本表示的局限，VISUALSKILL保留了视觉图像信息，通过两阶段流水线（文档+UI探索）构建技能，并利用MCP工具按需加载。实验表明，该方法相比无技能基线绝对提升15.3%，相比纯文本技能绝对提升8.3%，有力验证了视觉信息在GUI交互中的重要性，为CUA的技能构建提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
指出现有计算机使用代理(CUA)技能库纯文本表示的局限性，创新性地提出多模态技能表示VISUALSKILL，结合MCP工具按需加载视觉与文本信息。通过严谨的对照实验（对比无技能基线与纯文本技能基线），直接且量化地证明了保留视觉信息在UI元素识别和工作流状态验证中的关键作用，技术论证扎实且具有说服力。

### 实用性 (评分: 9.2/10)
对CUA和RPA从业者具有极高的实践指导意义。提出的两阶段技能构建流水线（文档结合UI探索）可直接复用于新软件的技能生成；基于MCP的按需加载机制契合当前Agent工程实践的主流范式；且代码已开源，落地门槛低，适用范围覆盖所有GUI自动化与交互场景。

### 社区活跃度 (评分: 9.3/10)
计算机使用代理(CUA)和MCP协议均为当前AI社区的前沿热点，话题时效性极强。作者团队包含Jacob Andreas等知名学者，基于Claude Opus 4.6等最前沿模型进行实验，基准测试专业，来源权威性与可信度极高，对Agent开发社区具有显著的影响力与启发价值。

## 项目链接
https://arxiv.org/abs/2606.18448
