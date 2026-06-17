# SkillChain-Gym: A Benchmark for Reskilling-Aware Production-Inventory Control under Disruptions

**评分：** 8.0  
**状态：** 正常  
**标签：** 强化学习, 运筹优化, 供应链管理, 基准测试, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17266v1 Announce Type: new Abstract: Production planning increasingly has to treat workforce capability as a decision variable: certifications lapse when skills are not maintained, new products require skills the current workforce does not hold, and reskilling competes for the same worker hours needed for production. Existing operations benchmarks usually treat labor as exogenous, while workforce-planning models with skills and learning are rarely released as reusable testbeds. We introduce SkillChain-Gym, a benchmark specification for reskilling-aware production-inventory control: a single-site environment with stylized worker skill-state dynamics, hard threshold certification, forgetting, and capacity-consuming training actions constrained by the same per-worker time budget as production. The benchmark includes seed-controlled disruption scenarios, three feasibility modes with projection diagnostics, deterministic replay, and metrics covering operations, resilience, capability growth, and training-access distribution. We evaluate production-only, reactive adaptive, water-filling adaptive, and static-insurance policies with budget variants over 60-shift horizons with paired statistical tests. The results are regime-dependent rather than a ranking. Training-capable policies dominate the production-only baseline, and maintenance training is necessary under forgetting even without disruptions. Among training-capable classes, adaptive training helps when bottlenecks are visible in the forecast, while a lean static cross-training plan, a deliberately favorable comparator whose structure encodes relevant skill contingencies, acts as strong insurance under surprise shocks and absenteeism. Capacity slack and the forgetting rate govern the boundary between these regimes. No policy class dominates across regimes, motivating forecast-driven controllers that decide when to buy skill insurance and when to react.

## 综合总结
本文提出了 SkillChain-Gym，一个针对考虑重新技能化的生产-库存控制的基准环境。该基准将劳动力技能作为内生决策变量，引入了技能遗忘、硬阈值认证及培训与生产竞争工时等动态特性。通过对多种策略的评估，研究发现没有单一策略在所有机制下占优：自适应培训在瓶颈可预测时有效，而静态交叉培训在突发冲击下更具韧性。该基准填补了运筹优化领域劳动力内生动态测试床的空白，为开发预测驱动的技能保险与反应控制器提供了重要工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文创新性地将劳动力技能状态（包括遗忘、硬阈值认证、培训与生产的工时竞争）作为内生决策变量引入生产-库存控制问题，填补了现有运筹学基准将劳动力视为外生变量的空白。通过严谨的实验设计（多种可行性模式、配对统计检验等），揭示了不同策略在不同机制（产能冗余与遗忘率）下的权衡关系，论证深度较高。

### 实用性 (评分: 8.5/10)
提供了可复用的基准测试环境 SkillChain-Gym，包含受控的中断场景、评估指标和基线策略，对运筹优化、供应链管理和强化学习领域的从业者具有直接的实践指导意义。研究者可利用该测试床快速验证和开发新的预测驱动控制算法，尽管环境设定有一定抽象，但极具参考价值。

### 社区活跃度 (评分: 7.5/10)
论文发布于arXiv，探讨了供应链韧性和劳动力再培训这一极具时代时效性的议题。虽然单作者影响力相对有限，但提供的标准化基准填补了该细分领域的空白，对运筹学与强化学习交叉社区有较好的吸引力和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.17266
