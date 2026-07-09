# Grounding Spatial Relations in a Compact World Model: Instruction Leakage and a Goal-Free Dynamics Fix

**评分：** 8.8  
**状态：** 正常  
**标签：** 世界模型, 具身智能, 指令泄漏, 目标条件, 视觉接地, 论文  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.06925v1 Announce Type: new Abstract: Compact world models that condition on a language goal promise to ground relations such as ``put the red block left of the blue block'' using a sparse set of explicit \emph{reference anchors}. We ask when such references actually ground a relation, and identify a trap: a goal-conditioned predictor reaches a striking $0.90$ relation-readout accuracy, yet this is \emph{instruction transcription}, not perception. Withholding the goal collapses it to chance ($0.90\!\to\!0.27$, three seeds) and a counterfactual instruction makes the predicted anchors follow the \emph{false} instruction $94.5\%$ of the time (true scene $2.3\%$; $N{=}256$). Tested across three settings and a within-task ablation, our central claim characterizes the confound: \textbf{instruction leakage occurs when the scored quantity is transcribable from the instruction (when the instruction names the answer) and is essentially independent of how predictive the non-instruction inputs are.} Our tabletop and the external BabyAI benchmark leak, whereas a Language-Table forward-dynamics world model whose instruction names \emph{referents} does not, until the instruction is augmented to name the direction; and degrading the action never increases leakage, the opposite of what predictor-competition predicts. The diagnosis prescribes the fix: keep the goal out of the dynamics (it belongs to the planner's cost) and supervise the \emph{read} path, recovering genuine, instruction-independent grounding ($0.88$, identical with and without the goal). The detection protocol and remedy apply to any goal-conditioned world model whose instruction names the scored quantity.

## 综合总结
本文揭示了目标条件世界模型中存在的'指令泄漏'陷阱，即模型在空间关系任务上的高准确率可能仅是对语言指令的转录而非真实的场景感知。通过严谨的实验验证了该现象后，作者提出将目标从动力学中移出、仅监督读取路径的修复方案，成功恢复了模型独立于指令的真实接地能力，为世界模型的评估与架构设计提供了重要警示与指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.2/10)
研究深度极高，精准识别并定义了目标条件世界模型中的'指令泄漏'陷阱。通过严谨的对照实验（隐藏目标、反事实指令、消融实验），有力证明了模型的高准确率往往源于对指令的直接转录而非真实的视觉感知，并给出了明确的理论解释与'目标无关动力学'的修复方案，论证逻辑严密且具有启发性。

### 实用性 (评分: 8.5/10)
对构建具身智能和世界模型的从业者具有极高的实践指导价值。提出的'指令泄漏'检测协议和修复方案（将目标从动力学中剥离，交由规划器成本函数处理，并监督读取路径）可直接应用于类似架构，帮助开发者避免评估指标的虚假繁荣，确保模型真正实现视觉接地。

### 社区活跃度 (评分: 8.8/10)
世界模型与具身智能是当前AI社区的热点前沿，本文指出的评估盲区具有极强的时效性和普遍警示意义。arXiv新文，来源可信，其揭示的'虚假接地'现象直击当前该领域评估体系的痛点，有望引发社区对目标条件模型评估范式的重新审视与广泛讨论。

## 项目链接
https://arxiv.org/abs/2607.06925
