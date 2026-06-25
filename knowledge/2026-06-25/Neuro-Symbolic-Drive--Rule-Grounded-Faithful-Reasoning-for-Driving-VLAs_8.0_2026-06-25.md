# Neuro-Symbolic Drive: Rule-Grounded Faithful Reasoning for Driving VLAs

**评分：** 8.0  
**状态：** 正常  
**标签：** 自动驾驶, VLA, 神经符号系统, 推理, 工程实践  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.23938v1 Announce Type: new Abstract: Driving VLA models incorporating Chain-of-Thought (CoT) reasoning are attractive because they leverage pretrained VLM representations and expose intermediate decisions in natural language, yet current rationales often lack the step-by-step decision semantics needed to keep the rationale causally connected to the planned motion. We introduce Neuro-Symbolic Drive, a neuro-symbolic driving framework that supervises a driving VLA with rule-grounded reasoning traces extracted directly from classical rule-based planners. Our key observation is that rule-based planners are symbolic AI systems that already function as executable reasoning engines: they reason about active safety constraints, search over candidate maneuvers, and select a final trajectory. We instrument these planners in simulation to capture both the executed trajectory and the internal decision trace at each rule-evaluation step. Each trace is serialized into structured rule-grounded reasoning and paired with the trajectory to fine-tune Qwen3.5-4B as a driving VLA. Because these traces are derived directly from the planner states that determine the action, they ensure reasoning is structurally coupled to motion generation by construction, rather than by post-hoc alignment. On our simulator-generated benchmark, detailed rule-grounded reasoning reduces ADE@3s from 0.47 to 0.26 and miss rate from 8.30% to 6.40% under three-camera perception, and from 0.54 to 0.26 and 10.13% to 5.99% under eight-camera perception. Neuro-Symbolic Drive thus converts neuro-symbolic planning logic into structured supervision. Code base: https://github.com/XiangboGaoBarry/Neural-Symbolic-Drive.

## 综合总结
本文提出了Neuro-Symbolic Drive框架，针对当前驾驶VLA模型中Chain-of-Thought推理与实际动作因果脱节的问题，创新性地从传统基于规则的规划器中提取内部决策轨迹，生成结构化的规则接地推理数据，用于微调VLA模型。该方法从结构上保证了推理与动作的耦合，在仿真基准测试中显著降低了ADE和失误率，为神经符号系统在自动驾驶领域的落地提供了极具价值的新范式，并已开源代码。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文提出了一种新颖的神经符号驱动框架，核心洞见在于将传统基于规则的规划器视为可执行的推理引擎，提取其内部规则评估步骤的决策轨迹，并将其序列化为结构化的规则接地推理轨迹，用于微调驾驶VLA模型（Qwen3.5-4B）。这种方法从机制上保证了推理与动作生成的结构性耦合，而非事后对齐，解决了当前基于CoT的VLA模型中推理过程与实际动作因果脱节的问题，论证严谨且具有显著的技术深度与创新性。

### 实用性 (评分: 7.5/10)
该研究对自动驾驶从业者具有很高的参考价值。通过将符号AI的规则逻辑转化为神经网络的监督信号，提供了一种可落地的VLA训练范式。实验表明，在三摄和八摄感知下，3秒平均位移误差（ADE）和失误率均大幅下降，证明了该方法在提升轨迹预测精度和安全性上的有效性。同时，论文开源了代码库，便于研究人员和工程师复现及应用于实际自动驾驶系统中，适用范围明确。

### 社区活跃度 (评分: 8.0/10)
论文发表于2026年，紧扣当前大模型与自动驾驶结合（VLA）的热点前沿，时效性极强。作者团队来自该领域的活跃研究者，且提供了完整的代码库，增强了研究的可信度和可复现性。将神经符号系统引入端到端自动驾驶是当前社区高度关注且极具潜力的方向，该工作在解决VLA幻觉和推理不可靠问题上提供了重要实证，预计将在社区产生积极的影响力。

## 项目链接
https://arxiv.org/abs/2606.23938
