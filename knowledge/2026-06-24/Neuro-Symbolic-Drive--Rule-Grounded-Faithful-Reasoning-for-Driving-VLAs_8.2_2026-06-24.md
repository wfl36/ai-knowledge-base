# Neuro-Symbolic Drive: Rule-Grounded Faithful Reasoning for Driving VLAs

**评分：** 8.2  
**状态：** 正常  
**标签：** 自动驾驶, VLA, 神经符号系统, 推理, 端到端, 论文  
**更新日期：** 2026-06-24  
**来源：** rss  

## 项目描述
arXiv:2606.23938v1 Announce Type: new Abstract: Driving VLA models incorporating Chain-of-Thought (CoT) reasoning are attractive because they leverage pretrained VLM representations and expose intermediate decisions in natural language, yet current rationales often lack the step-by-step decision semantics needed to keep the rationale causally connected to the planned motion. We introduce Neuro-Symbolic Drive, a neuro-symbolic driving framework that supervises a driving VLA with rule-grounded reasoning traces extracted directly from classical rule-based planners. Our key observation is that rule-based planners are symbolic AI systems that already function as executable reasoning engines: they reason about active safety constraints, search over candidate maneuvers, and select a final trajectory. We instrument these planners in simulation to capture both the executed trajectory and the internal decision trace at each rule-evaluation step. Each trace is serialized into structured rule-grounded reasoning and paired with the trajectory to fine-tune Qwen3.5-4B as a driving VLA. Because these traces are derived directly from the planner states that determine the action, they ensure reasoning is structurally coupled to motion generation by construction, rather than by post-hoc alignment. On our simulator-generated benchmark, detailed rule-grounded reasoning reduces ADE@3s from 0.47 to 0.26 and miss rate from 8.30% to 6.40% under three-camera perception, and from 0.54 to 0.26 and 10.13% to 5.99% under eight-camera perception. Neuro-Symbolic Drive thus converts neuro-symbolic planning logic into structured supervision. Code base: https://github.com/XiangboGaoBarry/Neural-Symbolic-Drive.

## 综合总结
本文提出Neuro-Symbolic Drive框架，针对自动驾驶VLA模型中CoT推理与动作脱节的问题，创新性地利用经典规则规划器的内部决策轨迹作为结构化监督信号微调VLA（Qwen3.5-4B）。该方法在构造层面确保了推理与运动生成的因果耦合，在仿真测试中显著降低了轨迹预测误差（ADE@3s）和失误率，并已开源，为可解释且可靠的自动驾驶大模型提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文针对自动驾驶VLA模型中Chain-of-Thought推理与实际动作脱节的问题，创新性地提出了Neuro-Symbolic Drive框架。其核心技术洞见在于将经典规则规划器的内部决策状态提取为结构化的推理轨迹，以此作为监督信号微调VLA模型，从而在构造层面保证了推理过程与运动生成的因果耦合，而非事后对齐。该方法有效缓解了VLA推理中的幻觉问题，将符号AI的可解释性与神经网络的泛化能力深度结合，论证严谨且具有较高技术深度。

### 实用性 (评分: 8.0/10)
该研究为自动驾驶端到端大模型的可解释性与可靠性提供了一条极具参考价值的落地路径。通过提取规则规划器的状态序列化生成CoT数据，并成功在Qwen3.5-4B模型上验证，证明了中小规模模型在结构化监督下的潜力。实验显示其在仿真环境中大幅降低了ADE和失误率，且项目已开源代码，对自动驾驶从业者将规则驱动与数据驱动融合具有直接的工程指导意义。不过，目前验证主要基于仿真环境，真实世界复杂场景的泛化性仍需进一步检验。

### 社区活跃度 (评分: 8.0/10)
VLA与端到端自动驾驶是当前AI与汽车工业交叉领域的核心热点，本文切中时弊，时效性极强。作者团队来自知名学术机构，论文发布于arXiv并附带开源代码库，增强了成果的可复现性与社区可信度。其将神经符号推理引入驾驶大模型的范式，有望在自动驾驶与具身智能社区引发对'可靠CoT'的广泛讨论与跟进研究。

## 项目链接
https://arxiv.org/abs/2606.23938
