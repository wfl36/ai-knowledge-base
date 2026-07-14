# Closed-Loop Control with Rule-Aligned Small Language Models and Multi-Agent Self-Correction

**评分：** 8.5  
**状态：** 正常  
**标签：** 小语言模型, Agent, 多智能体, 工业控制, 边缘计算, 闭环控制, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09713v1 Announce Type: new Abstract: A key step toward autonomous industrial operation is the ability to create and reconfigure control policies from natural-language requirement specifications, with minimal or no manual redesign. In this setting, policy generation by AI agents can be a credible path when paired with a plant-aware validator (e.g., a digital twin) that can check generated candidate actions before execution. However, practical deployment is constrained by inference latency and compute footprint: large cloud-based models are often too slow, opaque, or data-sensitive for edge closed-loop use. This work investigates whether a compact Small Language Model (SLM) can be retrained for control reasoning and embedded in a validator-guided correction loop. We use a Qwen2.5-1.5B model aligned via Group Relative Policy Optimization (GRPO), combined with (i) an action agent, (ii) a symbolic/digital-twin-style validation layer, and (iii) a reprompting agent that iteratively steers outputs toward valid actions. In randomized thermal-control simulations (30 experiments with 500 steps each), the framework achieves 91.5% average action-alignment accuracy (86.3%--100% across cases) at 3.84\,s mean inference latency. Under symbolic re-mapping, it maintains a 95% in-range rate, indicating robust physical regulation despite reduced token-level agreement. These results support SLM+validator architectures as a practical path toward reconfigurable autonomous control at the edge.

## 综合总结
本文提出了一种基于规则对齐的小语言模型（Qwen2.5-1.5B+GRPO）与多智能体自纠错相结合的闭环控制架构。通过动作智能体、数字孪生验证层和重提示智能体的协同，实现了从自然语言需求到边缘控制策略的安全、自动生成与纠错。热控制仿真实验表明，该框架在3.84s平均延迟下达到91.5%的动作对齐准确率，并在符号重映射下保持95%的物理调节鲁棒性，验证了SLM+验证器架构在边缘侧可重配置自主控制中的实用可行性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文在技术架构上具有显著新颖性，将小型语言模型（SLM）通过GRPO算法进行规则对齐，并创新性地结合多智能体自纠错机制（动作智能体+数字孪生验证层+重提示智能体）构建闭环控制。论证严谨，通过30组随机热控制仿真实验，量化了动作对齐准确率（91.5%）与推理延迟（3.84s），并引入符号重映射验证了物理调节的鲁棒性（95% in-range rate），为SLM在工业控制中的推理与纠错提供了坚实的技术验证。

### 实用性 (评分: 9.0/10)
对工业AI和边缘计算从业者具有极高的落地参考价值。针对大模型在边缘闭环控制中延迟高、算力消耗大及数据敏感等痛点，提出了'轻量级SLM+外部验证器'的务实解法。该架构既保留了自然语言配置控制策略的灵活性，又通过数字孪生验证层保障了工业执行的安全性和可靠性，可直接指导边缘侧自主控制系统、工业机器人的低算力部署实践。

### 社区活跃度 (评分: 8.0/10)
话题处于当前AI与工业自动化交叉领域的最前沿，SLM边缘部署、多智能体协同及工业自主控制均是热点。论文来源于arXiv，数据详实，方法透明，具备较高的学术可信度。尽管3.84s的延迟对硬实时系统仍具挑战，但其验证的架构范式对工业界和学术界均有重要启发，预期在边缘AI与控制系统社区将产生良好影响力。

## 项目链接
https://arxiv.org/abs/2607.09713
