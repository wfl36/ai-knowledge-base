# DuplexSpeechBench-IFEval: Evaluating Implicit Instruction Following in Full-Duplex Voice Agents

**评分：** 7.0  
**状态：** 正常  
**标签：** 全双工语音Agent, 语音交互, 评测基准, 指令遵循, 角色建模, 论文  
**更新日期：** 2026-09-04  
**来源：** rss  

## 项目描述
arXiv:2609.03423v1 Announce Type: new Abstract: Full-duplex voice agents must continuously decide when to listen, backchannel, interrupt, handle speech overlaps, take the floor, and yield. Existing benchmarks largely test these behaviors through explicit turn-management instructions, while deployed agents are often configured through roles or personas from which the appropriate conversational behavior must be inferred. We introduce DuplexSpeechBench-IFEval (DSB-IFEval) for evaluating implicit instruction-following in real-time spoken interaction. (DSB-IFEval) comprises 1,038 test cases spanning eight diverse assistant roles and evaluates five conditioning protocols for instruction-following: default behavior, explicit behavioral instructions, persona-implied behavior, combined persona--rule conditioning, and instruction conflict. We measure real-time floor management using a deterministic Instruction Adherence Score (IAS) and persona-consistent content using LLM-judged Persona Adherence Score (PAS). Across six real-time speech systems, we find architecture-dependent trade-offs. Full duplex models like F-Actor and PersonaPlex are more sensitive to whether conversational behavior is stated explicitly or must be inferred from a persona, with adherence dropping by 9.7% and 4.5%, respectively, under persona-only conditioning. In contrast, GPT-Realtime, MiniCPM-o, and Fun-Audio-Chat strongly adhere to persona-consistent content, but their floor behavior does not adapt across explicit and persona-only instructions and remains constrained on several proactive actions. We further find that even if systems reliably follow conflicting directives to their prescribed persona, they still struggle to override them under safety conflict. These results show that inferring the behavior implied by a role, executing it at the appropriate conversational moment, and resolving competing instructions remain distinct challenges for full-duplex voice agents.

## 综合总结
本文提出全双工语音Agent的隐式指令遵循评测基准 DSB-IFEval，系统评估了6个主流实时语音系统在8种角色、5种指令条件下的表现，揭示了现有系统在从persona推断行为、适时执行、以及处理冲突指令三个层面的核心不足。研究对推动全双工语音Agent从显式配置向隐式角色驱动演进具有重要参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
提出了 DuplexSpeechBench-IFEval (DSB-IFEval) 评测基准，包含1038个测试用例，覆盖8种助手角色和5种条件协议。设计了确定性的 Instruction Adherence Score (IAS) 和 LLM-judged 的 Persona Adherence Score (PAS) 两类评估指标，对6个实时语音系统进行了系统评测。方法论较为严谨，覆盖了显式/隐式指令遵循、角色推断、指令冲突等关键维度，技术贡献在于揭示了不同全双工架构在行为推断与执行上的本质差异，但指标设计和基准构建本身属于评测创新而非底层模型或算法突破。

### 实用性 (评分: 7.0/10)
对全双工语音Agent的研发者具有较高参考价值：明确指出了不同架构（F-Actor、PersonaPlex vs GPT-Realtime、MiniCPM-o、Fun-Audio-Chat）在地板管理、行为适配、安全冲突覆盖等方面的具体短板，为后续模型改进提供了清晰方向。评测协议可复现，涵盖的5种条件协议对实际部署中的prompt engineering和角色设计具有直接指导意义。不过评测聚焦于特定子系统，实际落地还需结合具体业务场景进一步验证。

### 社区活跃度 (评分: 6.5/10)
话题聚焦全双工语音Agent这一当前热门但尚不成熟的方向，时效性强。arXiv预印本，尚未经过同行评审，权威性受限。作者Puneet Mathur和Dinesh Manocha在语音/音频领域有一定积累（Manocha是知名学者），但该工作的社区影响力取决于后续是否被顶会接收及业界引用情况。论文编号为2609（2026年），属于未来时间戳的预印本，实际影响有待观察。

## 项目链接
https://arxiv.org/abs/2609.03423
