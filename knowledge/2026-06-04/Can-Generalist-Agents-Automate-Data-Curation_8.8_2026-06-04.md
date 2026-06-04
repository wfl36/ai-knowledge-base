# Can Generalist Agents Automate Data Curation?

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, 数据整理, 视觉语言模型, 基准测试, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04261v1 Announce Type: new Abstract: Curating training data is among the most consequential yet labor-intensive parts of modern AI development: practitioners iteratively propose, implement, evaluate, and revise data policies against noisy benchmark feedback. We ask whether generalist coding agents can automate this data-curation loop. We introduce *Curation-Bench*, an agent-centric benchmark that fixes the model, training recipe, and evaluation suite while giving agents command-line access to inspect data, implement policies, submit them to a fixed training/evaluation pipeline, and revise. In a vision-language instruction-tuning instantiation, out-of-the-box agents reach strong published data-selection baselines within ten iterations. However, trajectory analysis reveals a persistent *execution-research gap*: agents mainly tune local policy variants rather than explore new policy families, even when given strategy guides and paper references. Scaffolds requiring each iteration to cite, instantiate, and adapt a prior method shift agents toward method-guided exploration. The scaffolded agent autonomously composes -- without human design input -- a data-selection policy that outperforms strong published baselines at one-tenth their data budget. Overall, current agents can run the curation loop, but reliable data research requires scaffolded method adaptation, not open-ended prompting alone. Code and benchmark are open-sourced.

## 综合总结
该论文研究了通用Agent自动化数据整理的可行性，提出了Curation-Bench基准。研究发现现成Agent虽能快速达到现有基线，但存在只做局部调优的'执行-研究差距'。通过引入要求迭代引用和适配先验方法的脚手架机制，Agent能够进行方法引导的探索，并自主组合出在1/10数据预算下超越强基线的数据选择策略。这表明可靠的自动化数据研究需要脚手架方法适配，而非单纯的开放式提示。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文提出了极具深度的研究视角，探讨通用Agent自动化数据整理循环的可行性。创新性地构建了Curation-Bench基准，并深刻揭示了当前Agent存在的'执行-研究差距'（倾向于局部调优而非探索新策略族）。通过引入要求迭代引用和适配先验方法的脚手架机制，成功引导Agent进行方法引导型探索，论证逻辑严密，从发现问题到提出解决方案形成了完整的闭环。

### 实用性 (评分: 8.5/10)
对AI数据工程从业者具有极高的参考价值。数据整理是AI开发中最耗资源的环节之一，该论文证明脚手架Agent能在1/10数据预算下自主组合出超越强基线的策略，可直接指导自动化数据筛选流水线的构建。开源的Curation-Bench基准和代码也便于业界复现与实际应用落地，不过目前验证主要集中在视觉语言指令微调场景，泛化到其他领域尚需工程适配。

### 社区活跃度 (评分: 9.0/10)
话题处于Agent与自动化机器学习交叉的前沿热点，极具时效性。作者阵容包含Dawn Song等业界权威学者，arXiv首发可信度高。其揭示的'执行-研究差距'现象及脚手架解决方案，对后续Agent工作流设计具有启发意义，开源基准有望推动数据自动化社区的进一步发展，影响力显著。

## 项目链接
https://arxiv.org/abs/2606.04261
