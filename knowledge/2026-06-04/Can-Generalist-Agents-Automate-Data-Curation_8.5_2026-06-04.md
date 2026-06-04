# Can Generalist Agents Automate Data Curation?

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 数据整理, 大模型, 视觉语言模型, 论文, 基准测试  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04261v1 Announce Type: new Abstract: Curating training data is among the most consequential yet labor-intensive parts of modern AI development: practitioners iteratively propose, implement, evaluate, and revise data policies against noisy benchmark feedback. We ask whether generalist coding agents can automate this data-curation loop. We introduce *Curation-Bench*, an agent-centric benchmark that fixes the model, training recipe, and evaluation suite while giving agents command-line access to inspect data, implement policies, submit them to a fixed training/evaluation pipeline, and revise. In a vision-language instruction-tuning instantiation, out-of-the-box agents reach strong published data-selection baselines within ten iterations. However, trajectory analysis reveals a persistent *execution-research gap*: agents mainly tune local policy variants rather than explore new policy families, even when given strategy guides and paper references. Scaffolds requiring each iteration to cite, instantiate, and adapt a prior method shift agents toward method-guided exploration. The scaffolded agent autonomously composes -- without human design input -- a data-selection policy that outperforms strong published baselines at one-tenth their data budget. Overall, current agents can run the curation loop, but reliable data research requires scaffolded method adaptation, not open-ended prompting alone. Code and benchmark are open-sourced.

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了Curation-Bench基准，用于评估通用Agent自动化数据整理的能力。研究深入揭示了Agent在科研任务中的'执行-研究差距'（倾向于局部调参而非探索新策略族），并创新性地引入了'脚手架'机制（要求迭代时引用、实例化和调整先验方法），成功引导Agent进行方法级探索，最终在1/10数据预算下自主组合出超越强基线的策略，论证严谨且具有深刻的技术洞见。

### 实用性 (评分: 8.0/10)
该研究对AI从业者具有极高的实践指导价值。数据整理是AI开发中最耗时且关键的环节，论文证明了Agent在脚手架辅助下能有效自动化此流程，大幅降低数据预算和人力成本。开源的Curation-Bench及代码使得从业者可直接复现并应用于自身数据集的清洗与筛选，脚手架机制也为构建自动化数据工程Pipeline提供了明确的工程范式。

### 社区活跃度 (评分: 9.0/10)
研究处于Agent自动化科研的最前沿，时效性极强。作者团队包含Dawn Song等知名学者，来源权威性高。论文开源了代码和基准，且核心结论（Agent+脚手架可超越人类设计基线）极具话题性和启发性，预计将在AI Agent和数据工程社区产生广泛影响。

## 项目链接
https://arxiv.org/abs/2606.04261
