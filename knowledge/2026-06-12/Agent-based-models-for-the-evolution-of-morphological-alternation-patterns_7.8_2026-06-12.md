# Agent-based models for the evolution of morphological alternation patterns

**评分：** 7.8  
**状态：** 正常  
**标签：** 多智能体, 计算语言学, 历史语言学, LLM评估, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12748v1 Announce Type: new Abstract: Why is the past of English "go" the apparently unrelated "went"? Such alternations are frequent in languages. They neither aid communication nor learnability, yet they can be persistent, surviving over centuries or millennia. We present a multi-agent simulation of the emergence of morphological stem and inflection alternations. Alternate forms arise by phonological changes or, as with "go/went", from lexical alternatives associated with a subset of the population. When an agent 'hears' another agent use a novel form for a slot in the paradigm of a word (say, the past tense of go), they will with some probability adopt that form, possibly spreading its use to other slots in the paradigm that shared the same original form. Thus alternative forms can spread through the population and become entrenched as stem or inflectional marker alternants. Unlike many previous computational studies, our system allows for naturalistic lexical forms, realistic phonological rules, lexicons with hundreds or thousands of entries, and agent populations in the tens or hundreds. It supports several network topologies, diffusion patterns and agent adoption policies. One issue with such simulations is evaluation: how realistic is the resulting morphology compared to those of real languages? We introduce the AI Historical Linguist, a novel Large Language Model-driven system that models a debate between two historical linguists. We use this to compare a set of real language morphologies, disguised morphologies, and experimentally evolved morphologies. The results suggest that among the factors that favor more plausible morphologies are scale-free social networks and random Bernoulli adoption of forms. We also present three case studies modeling attested historical changes, allowing us to test what might have happened if history had been different. All code and data are released.

## 综合总结
该论文提出了一种多智能体模拟系统，用于研究语言中形态交替模式的演化机制。研究创新性地引入了基于大语言模型的“AI Historical Linguist”系统，通过模拟历史语言学家辩论来评估模拟生成的形态逼真度。实验表明，无标度社交网络和随机伯努利采纳策略有助于产生更合理的形态，并通过三个反事实案例验证了模型的有效性。该工作为计算语言学和演化模拟提供了新工具与新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
结合多智能体模拟与LLM驱动的评估机制，创新性地解决了计算语言学中形态演化模拟的评估难题。系统支持自然词汇、复杂语音规则及多种网络拓扑，实验设计严谨，反事实案例研究进一步增强了论证深度与学术价值。

### 实用性 (评分: 7.0/10)
开源代码和数据提升了可复现性，多智能体模拟框架和LLM评估机制对计算语言学和认知科学领域具有较高参考价值。但研究偏向基础科学，对工业界NLP应用的直接指导意义有限，落地场景相对垂直。

### 社区活跃度 (评分: 8.0/10)
发布于2026年，时间极新。作者Richard Sproat为计算语言学领域权威学者，可信度高。将LLM引入历史语言学的评估范式具有较强的话题性和跨学科吸引力，有望在AI与语言学交叉社区产生积极影响。

## 项目链接
https://arxiv.org/abs/2606.12748
