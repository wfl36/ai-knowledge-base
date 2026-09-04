# Where Does Harness-Optimization Value Live? Localized Gains and the Budget-Splitting Trap in Self-Evolving LLM Agents

**评分：** 6.7  
**状态：** 正常  
**标签：** Agent, Prompt Optimization, Self-Evolving Agent, 论文, Harness Optimization, Credit Assignment  
**更新日期：** 2026-09-04  
**来源：** rss  

## 项目描述
arXiv:2609.02889v1 Announce Type: new Abstract: A growing body of work improves frozen large language models (LLMs) as agents by evolving their harness: the textual scaffolding around the model, including persona, strategy, format rules, and control heuristics. Existing reflective prompt-evolution methods usually optimize this harness as one flat string. We instead ask where the optimization value actually resides. We introduce HARNESSEVO, which decomposes the harness into four separately evolvable slots: role, task-strategy, tool/format-rules, and reflection/control. Using the same reflective optimizer under an iso-budget setting, we pair this decomposition with leave-one-in and leave-one-out attribution to measure the contribution of each slot. On ALFWorld with a frozen 7B backbone, HARNESSEVO does not significantly improve the overall binary success rate over either the stock harness or flat-string evolution: 0.657 versus 0.642 and 0.642, respectively. However, the slot-level analysis reveals that nearly all useful optimization value is localized in the reflection/control slot, which achieves a leave-one-in gain of +0.119. The other slots are individually null. We further show that uniform budget splitting is harmful: allocating 64 rollouts across four slots leaves only 16 per slot, below the optimizer's effective search floor, causing every slot to freeze at its empty seed. Concentrating the budget on the high-credit control slot recovers the lost gain, reaching 0.761 with half the split budget. The effect is task-contingent. On WebShop, all slots freeze empty and all methods tie, indicating a genuine absence of recurrent, verbalizable control failures rather than budget starvation. Overall, our results suggest that harness value is localized, uniform budget splitting can be actively harmful, and credit assignment should precede structured agent-evolution.

## 综合总结
本文针对self-evolving LLM agent中harness-optimization价值定位问题，提出HARNESSEVO框架，将harness分解为四个slot进行独立演化与归因分析。核心发现：(1) 优化价值高度局部化——在ALFWorld上几乎全部价值集中在reflection/control slot（leave-one-in增益+0.119），其他slot贡献为零；(2) uniform budget splitting有害——64 rollouts均分给4个slot导致每个slot低于optimizer有效搜索阈值而全部冻结，集中预算则可恢复增益（0.761，使用一半预算）；(3) 效果具有任务依赖性，WebShop上所有slot冻结为空，说明该任务缺乏可verbalize的控制失败。论文主张credit assignment应先于structured agent evolution。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文提出HARNESSEVO框架，将agent harness分解为role、task-strategy、tool/format-rules、reflection/control四个可独立演化的slot，并结合leave-one-in/out归因分析，方法设计较为严谨。核心洞见是发现优化价值高度局部化于reflection/control slot，其他slot贡献接近为零，这一发现对现有prompt evolution研究是有意义的反直觉结论。同时揭示了uniform budget splitting的陷阱（budget below search floor导致所有slot冻结），提出了credit assignment前置的实践准则。方法论上的局限在于仅在ALFWorld和WebShop两个任务上验证，且整体success rate提升不显著（0.657 vs 0.642），主要贡献来自分析而非性能提升。

### 实用性 (评分: 6.5/10)
对从事agent prompt engineering和self-evolving agent研究的从业者具有较高参考价值：(1) credit assignment应先于structured evolution的准则可指导实验设计；(2) budget allocation策略——集中预算于高credit slot而非均匀分配，是可立即落地的实践启示；(3) 任务依赖性结论（WebShop上slot全部冻结为空）提示研究者要诊断failure类型后再决定是否需要evolution。但实际落地存在门槛：需要先做归因分析、且效果依赖任务类型，对急于提升benchmark分数的工程团队吸引力有限。

### 社区活跃度 (评分: 6.0/10)
话题处于self-evolving agent与prompt optimization的交叉前沿，时效性较好。来源为arXiv预印本，作者机构信息不够突出（arXiv ID格式2609.02889暗示日期为2026年9月，较为新颖但社区影响力尚未形成）。话题属于agent领域的细分方向（harness optimization的归因分析），受众相对小众，尚未见顶会发表或广泛讨论的迹象，整体社区影响力中等偏低。

## 项目链接
https://arxiv.org/abs/2609.02889
