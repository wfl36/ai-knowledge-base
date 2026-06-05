# Can Generalist Agents Automate Data Curation?

**评分：** 9.2  
**状态：** 正常  
**标签：** Agent, 数据管理, 数据选择, VLM, 基准测试, 论文  
**更新日期：** 2026-06-05  
**来源：** rss  

## 项目描述
arXiv:2606.04261v1 Announce Type: new Abstract: Curating training data is among the most consequential yet labor-intensive parts of modern AI development: practitioners iteratively propose, implement, evaluate, and revise data policies against noisy benchmark feedback. We ask whether generalist coding agents can automate this data-curation loop. We introduce *Curation-Bench*, an agent-centric benchmark that fixes the model, training recipe, and evaluation suite while giving agents command-line access to inspect data, implement policies, submit them to a fixed training/evaluation pipeline, and revise. In a vision-language instruction-tuning instantiation, out-of-the-box agents reach strong published data-selection baselines within ten iterations. However, trajectory analysis reveals a persistent *execution-research gap*: agents mainly tune local policy variants rather than explore new policy families, even when given strategy guides and paper references. Scaffolds requiring each iteration to cite, instantiate, and adapt a prior method shift agents toward method-guided exploration. The scaffolded agent autonomously composes -- without human design input -- a data-selection policy that outperforms strong published baselines at one-tenth their data budget. Overall, current agents can run the curation loop, but reliable data research requires scaffolded method adaptation, not open-ended prompting alone. Code and benchmark are open-sourced.

## 综合总结
本文探讨了通用智能体自动化数据管理的可行性，提出了Curation-Bench基准。研究发现，虽然开箱即用的Agent能达到现有数据选择基线，但存在'执行-研究差距'（偏向局部调优而非全局探索）。为此，论文引入了脚手架机制，强制Agent在迭代中引用和适配已有方法。该脚手架Agent在无需人类设计输入的情况下，自主组合出的数据策略在1/10数据预算下超越了强基线。这为Agent驱动的自动化数据工程和自主科研提供了重要范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文提出了Curation-Bench基准，用于评估通用编码智能体自动化数据管理循环的能力。研究不仅验证了开箱即用的Agent能达到现有数据选择基线水平，更深入揭示了Agent存在的'执行-研究差距'（倾向于局部参数调优而非探索新策略族）。通过引入要求迭代引用和适配先前方法的脚手架机制，成功引导Agent进行方法驱动的探索，展现了深刻的技术洞察与严谨的论证。

### 实用性 (评分: 9.0/10)
该研究对AI从业者具有极高的实践指导价值。数据管理是模型训练的核心痛点，论文提出的脚手架方法（强制Agent进行方法引用与适配）可直接应用于现有的Agent框架中，实现数据策略的自动搜索与优化。实验证明该方法仅需十分之一数据预算即可超越强基线，在数据成本高昂的大模型时代具有显著的落地效益与成本优势。

### 社区活跃度 (评分: 9.5/10)
论文发布于2026年，探讨Agent在数据工程中的自动化应用，切中当前AI开发的核心痛点，时效性极强。作者团队包含Dawn Song等知名学者，权威性高；代码与基准开源，保证了研究的可复现性和社区影响力。该工作有望引发对'Agent自主科研范式'及'数据工程自动化'的广泛讨论与跟进。

## 项目链接
https://arxiv.org/abs/2606.04261
