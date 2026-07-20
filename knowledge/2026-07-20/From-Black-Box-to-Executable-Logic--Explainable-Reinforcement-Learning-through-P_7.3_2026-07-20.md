# From Black Box to Executable Logic: Explainable Reinforcement Learning through Prolog Expert Systems

**评分：** 7.3  
**状态：** 正常  
**标签：** 强化学习, 可解释AI, 神经符号, 专家系统, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15459v1 Announce Type: new Abstract: A trained deep reinforcement learning policy is a black box, and we ask whether it can be made explainable by rewriting it as an executable logic program that reproduces its behaviour and that a person can read, a logic engine can run, and an optimizer can edit. We present a three-stage post-hoc transformation that extracts a frozen proximal policy optimization teacher, induces an ordered rule list from its decisions in the manner of classical relational learning, and emits the result as a Prolog program whose every decision is executed by an off-the-shelf logic engine; a subsequent expansion stage edits the rule base and accepts an edit only when policy evaluation certifies a return increase. We prove four guarantees. A return-loss bound makes the distilled program a machine-checkable certificate in a finite Markov decision process, and the expansion loop improves monotonically and terminates. For the continuous-observation setting we answer whether the conversion is possible at all: the propositional threshold instantiation converts the network to arbitrary fidelity as the resolution B grows, with disagreement O(1/B) and a return gap that closes at the same rate, and a matching lower bound shows the cost is exponential in the observation dimension for an oblique decision boundary. Empirically, on a two-room key-and-door task with 16,944 reachable states the expanded Prolog program attains exact optimal return in every seed and, in a budget-capped regime, exceeds the stochastic teacher on exact return in ten of ten seeds. On three continuous-control tasks the emitted program substitutes the network, matching the neural teacher within noise on Acrobot with eleven clauses and recovering about 97% of its return on CartPole, while on the finer-control LunarLander it recovers only partially, exactly the ceiling the exponential lower bound predicts.

## 综合总结
本文提出了一种将深度强化学习黑盒策略转化为可执行Prolog逻辑程序的三阶段事后转换方法，以实现策略的可读、可运行与可优化。该方法通过提取PPO教师、归纳规则列表并生成Prolog程序，随后通过扩展阶段优化规则库。研究给出了四个理论保证，包括回报损失界限和单调改进终止，并严格证明了在连续观察空间中转换保真度与分辨率的关系及维数灾难下的指数级下限。实验在离散和连续控制任务上验证了方法的有效性，同时也印证了高维精细控制任务受限于指数级成本的理论上限。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究在神经符号AI与可解释强化学习交叉领域展现了极高的理论深度与严谨性。提出将深度RL黑盒策略事后转化为可执行Prolog逻辑程序的三阶段方法，并给出了四个坚实的理论保证：包括有限MDP下的回报损失界限、扩展循环的单调收敛性，以及连续空间下保真度随分辨率O(1/B)闭合的证明。尤为深刻的是，论文给出了连续观察空间中倾斜决策边界转换成本随维度指数级增长的下限证明，从理论层面清晰界定了该方法的适用边界，论证极其严密。

### 实用性 (评分: 6.0/10)
对从业者的实际参考价值存在明显边界。在低维离散状态空间（如两房间任务）或简单连续控制（如Acrobot、CartPole）中，该方法能以极简的Prolog子句完美或高度近似替代神经网络，具备可解释部署价值。然而，理论推导的指数级下限直接揭示了其在高维连续观察空间（如LunarLander及更复杂的现实机器人控制）中的维数灾难瓶颈，加之Prolog专家系统在现代工程栈中生态较为边缘，限制了其在工业级复杂场景的广泛落地。

### 社区活跃度 (评分: 7.5/10)
可解释性是当前AI领域的核心痛点，将黑盒RL转化为白盒逻辑程序的议题具有极强的时效性与学术吸引力。arXiv平台保证了传播的即时性，且该工作理论完备，必将在可解释RL及符号回归社区引发关注。但受限于Prolog语言的复古属性及高维连续场景的理论天花板，其跨圈层的广泛影响力可能受限。

## 项目链接
https://arxiv.org/abs/2607.15459
