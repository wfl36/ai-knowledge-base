# When Reasoning Narrows the Move: Diversity Collapse in LLM Game Play

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 推理, Agent, 决策, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19523v1 Announce Type: new Abstract: Supervised fine-tuning (SFT) is widely used to adapt large language models to downstream tasks, but its effect on behavioral diversity in sequential decision-making remains under-explored. We study this question in a controlled suite of deterministic board games based on tic-tac-toe variants, where optimal actions are exactly computable and diversity can be measured directly. Across state-level evaluation, arena gameplay, and training trajectories, we find that reasoning-mode generation frequently suppresses action diversity without uniformly improving action accuracy. Furthermore, standard SFT improves accuracy but often induces premature diversity collapse, which exceeds what is minimally required by the accuracy-diversity tradeoff. We then show that action augmentation, which trains on all optimal actions per state rather than a single demonstrated action, would partially mitigates this effect. Our results identify narrow-support imitation as a source of policy collapse in LLM decision-making and suggest that preserving action support during SFT is important for maintaining exploratory behavior.

## 综合总结
本文研究了SFT和推理模式对LLM在序列决策中行为多样性的影响。通过在井字棋变体中的受控实验，发现推理模式生成会抑制动作多样性且未必提升准确性，而标准SFT虽提升准确性却会导致过早的多样性崩溃。研究指出'窄支持模仿'是策略崩溃的根源，并提出'动作增强'方法（在所有最优动作上训练而非单一动作）来缓解该问题，强调了在SFT中保留动作支持对维持LLM探索行为的重要性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
文章揭示了监督微调（SFT）和推理模式在LLM序列决策中导致的'多样性崩溃'现象。研究设计严谨，通过确定性棋盘游戏（井字棋变体）精确计算最优动作并量化多样性，发现推理模式抑制多样性且未必提升准确性，标准SFT会导致超出精度-多样性权衡所需的过早崩溃。提出的'窄支持模仿'机制解释了策略崩溃的根源，并给出了'动作增强'的缓解方案，逻辑闭环，具有较好的理论深度与洞见。

### 实用性 (评分: 7.5/10)
对构建基于LLM的决策Agent和游戏AI具有直接的实践指导价值。指出了传统SFT仅使用单一演示轨迹的缺陷，建议在训练数据中包含同一状态下的所有最优动作（动作增强）以维持模型的探索能力。但在更复杂、大状态空间的现实场景中，获取'所有最优动作'的数据成本较高，落地时需结合具体任务评估该方法的可行性。

### 社区活跃度 (评分: 8.0/10)
该论文触及了当前LLM推理和Agent领域的热点痛点——模型在决策中的僵化和探索能力丧失。作者来自知名学术机构，研究结论对当前主流的'推理即搜索'范式提出了反思，话题时效性强，对AI Agent开发社区有较高的启发和影响力。

## 项目链接
https://arxiv.org/abs/2607.19523
