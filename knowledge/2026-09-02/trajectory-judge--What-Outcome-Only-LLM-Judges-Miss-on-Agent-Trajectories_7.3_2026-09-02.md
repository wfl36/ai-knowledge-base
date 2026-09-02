# trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories

**评分：** 7.3  
**状态：** 正常  
**标签：** Agent, LLM-as-a-Judge, 评测方法论, 论文, 实验研究, 工具调用  
**更新日期：** 2026-09-02  
**来源：** rss  

## 项目描述
arXiv:2609.00038v1 Announce Type: new Abstract: Outcome-only evaluation is the production default for LLM agents: show a judge the request and the final reply and ask whether it was handled well. The metric is structurally blind to an agent that reaches the right answer the wrong way. We measure that blind spot where ground truth is known by construction: a deterministic tool-using support-desk environment, a scripted oracle policy that always solves it, and a fault injector that breaks exactly one thing at a known step, stratifying faults by whether the customer-visible outcome survived (silent) or not (loud). Five judges (programmatic rules, outcome-only, step-rubric at two model sizes, and a self-consistency ensemble) are scored on detection, step localisation, fault typing, calibration, and cost over 400 trajectories. The outcome-only judge catches 84% of loud faults but 45% of silent ones while flagging 33% of correct trajectories; a step-rubric judge reaches 77% silent recall with zero false alarms at 3x the cost. No judge reads the final reply: an invented promise appended to an otherwise perfect trajectory evades the rules entirely and the step judge 82% of the time, and self-consistency triples cost while improving nothing. We argue that judge evaluations must stratify recall by outcome survival, and release the environment, the injector, all raw verdicts, and an analysis pipeline that rebuilds every number offline.

## 综合总结
本文揭示了当前LLM Agent评估中被广泛使用的outcome-only judge存在结构性盲区——对过程错误但结果正确的silent fault召回率仅45%。通过在确定性support-desk环境中对比5种judge，提出按outcome survival分层报告recall的评测范式，并配套开源完整实验资产。核心贡献是评测方法论层面的增量改进和具体选型指导，而非新judge架构，适合评估系统设计者参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文针对LLM Agent轨迹评估中outcome-only judge的结构性盲区，提出了系统化的实验设计：在确定性工具调用环境中通过脚本化oracle策略和单点故障注入器，分层评估5种judge在检测、步骤定位、故障分类、校准和成本五个维度上的表现。方法论严谨，包含400条轨迹的对比实验，并提出了按outcome survival分层报告recall的关键洞察——silent fault和loud fault需要分别衡量，这一点在评测方法论上具有增量贡献。但整体更偏实证研究而非新方法/新理论，技术新颖性中等偏上。

### 实用性 (评分: 8.0/10)
对构建LLM Agent评估体系的从业者有直接参考价值。核心结论outcome-only judge对silent fault召回仅45%且33%误报、step-rubric judge以3倍成本获得零误报等数据点，可直接指导judge选型决策。开源环境、故障注入器、原始判定结果和离线分析管道使读者可复现和扩展。但实验局限在单一support-desk领域，泛化性有待验证。

### 社区活跃度 (评分: 6.5/10)
话题切中LLM Agent评测这一当前热点痛点，Agent评估确实是社区关注但成熟方法不多的方向。来源为arXiv，作者为单一研究者（Hadi Mohammadi），机构和合作网络信息有限，权威性中等。发布于2026年9月，未来若被广泛引用将提升影响力。arXiv编号2609.00038为占位编号格式略显异常，可能影响索引。

## 项目链接
https://arxiv.org/abs/2609.00038
