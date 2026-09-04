# Do GUI Agents Know When Not to Act? Enabling Conflict-Aware Termination for Multimodal GUI Agents

**评分：** 7.3  
**状态：** 正常  
**标签：** Agent, 多模态, GUI Agent, 可靠性, 安全性, 论文, 基准测试  
**更新日期：** 2026-09-04  
**来源：** rss  

## 项目描述
arXiv:2609.03438v1 Announce Type: new Abstract: Graphical user interface (GUI) agents are increasingly used to execute natural-language instructions on user interfaces, yet real users may issue infeasible instructions due to benign mistakes. A reliable agent should not only know how to act, but also when not to act. In this work, we introduce CONFLICTGUI, a benchmark covering instruction-internal conflicts and instruction-GUI context conflicts to study conflict-aware termination. Our evaluation reveals severe execution-biased overcompliance: agents that perform well on feasible tasks often continue to execute blindly under conflicting instructions. To mitigate this behavior, we propose CONFLICTGUARD, an inference-time framework that aligns an agent's feasibility awareness with its action generation. CONFLICTGUARD contains two coupled components: a feasibility verification protocol that guides the agent to assess instruction logic and GUI-side evidence before acting, and a conditional action modulation mechanism that steers agents from over-compliant execution into termination-oriented behavior. Experiments across five widely-used agents demonstrate that CONFLICTGUARD improves average conflict task success rate significantly, while preserving normal GUI-task performance. These results validate that a lightweight inference-time intervention can substantially boost GUI Agent's competence to identify inappropriate execution scenarios and refrain from unnecessary actions.

## 综合总结
本文针对 GUI Agent 在面对不可行指令时过度执行的问题，提出了 CONFLICTGUI 基准和 CONFLICTGUARD 推理时干预框架。通过可行性验证与条件动作调制两个耦合组件，使 Agent 能够在识别指令冲突时主动终止而非盲目执行。该工作在五个主流 GUI Agent 上验证了有效性，同时保持正常任务性能，体现了'知道何时不行动'这一 Agent 可靠性的重要原则，为 GUI Agent 的安全部署提供了实用方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文聚焦于一个被忽视但重要的可靠性问题：GUI Agent 在面对不可行指令时的'过度顺从'行为。作者提出 CONFLICTGUI 基准测试来系统性地评估指令内部冲突与指令-GUI上下文冲突，并设计 CONFLICTGUARD 推理时干预框架，包含可行性验证协议和条件动作调制机制两部分。问题定义清晰，benchmark 设计具有针对性，方法兼顾了推理时轻量级介入与正常任务性能保持，技术路径合理。但方法本身并未引入全新的模型架构或训练范式，更多是工程化的推理时对齐方案，理论深度有限。

### 实用性 (评分: 7.0/10)
CONFLICTGUARD 作为推理时框架具有较强的实用价值：无需重新训练模型即可部署，对工业界 GUI Agent 的可靠性提升有直接参考意义。覆盖五个主流 GUI Agent 的实验验证增强了方法的可迁移性。在真实用户场景中，用户误发指令是常见情况，该工作直接回应了这一实际痛点，对构建更安全的 AI 助手有指导作用。但实际部署效果、性能开销、对不同 Agent 架构的适配细节等工程问题仍需进一步说明。

### 社区活跃度 (评分: 7.5/10)
GUI Agent 是当前 AI Agent 研究的热门方向之一，可靠性与安全性话题在 LLM 应用落地中受到高度关注。该工作切中'Agent 何时不行动'这一重要且前沿的研究问题，具有较好的时效性。作者团队在多模态与 Agent 领域有一定积累，arXiv 发布增强了可访问性。但发布时间标注为 2026 年，且为单一论文（非综述或里程碑式工作），社区影响力有待观察。

## 项目链接
https://arxiv.org/abs/2609.03438
