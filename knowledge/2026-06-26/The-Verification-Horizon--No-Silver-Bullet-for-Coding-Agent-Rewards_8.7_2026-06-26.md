# The Verification Horizon: No Silver Bullet for Coding Agent Rewards

**评分：** 8.7  
**状态：** 正常  
**标签：** Coding Agent, 奖励模型, 奖励黑客, RLHF, 对齐, 论文  
**更新日期：** 2026-06-26  
**来源：** rss  

## 项目描述
arXiv:2606.26300v1 Announce Type: new Abstract: A classical intuition holds that verifying a solution is easier than producing one. For today's coding agents, this intuition is being inverted: as foundation models develop stronger reasoning capabilities and engineering harnesses grow more sophisticated, generating complex candidate solutions is no longer difficult -- reliably verifying them has become the harder problem. Every verifier we can build is only a proxy for human intent, never the intent itself. This makes verification subject to a twofold difficulty: first, intent is underspecified by nature, making it inherently hard to faithfully check whether it has been fulfilled; second, during model training, optimization widens the gap between proxy and intent -- manifesting as reward hacking or signal saturation. To address this, we characterize the quality of verification signals along three dimensions -- scalability, faithfulness, and robustness -- and argue that achieving all three simultaneously is the central challenge. We further study four reward constructions: a test verifier for general coding tasks, a rubric verifier for frontend tasks, the user as verifier for real-world agent tasks, and an automated agent verifier for long-horizon tasks. Across different task types and policy capability levels, we conduct in-depth analysis and experiments on the core challenges of reward design and how to more effectively leverage reward signals. Experiments show that targeted verification design can effectively suppress reward hacking, improve task completion quality, and achieve significant gains across multiple internal and public benchmarks. These experiences collectively point to a core observation: no fixed reward function can remain effective as policy capability continues to grow; and verification must co-evolve with the generator.

## 综合总结
本文反转了“验证比生成容易”的传统直觉，指出在Coding Agent中可靠验证已成为更困难的瓶颈。作者剖析了验证器作为人类意图代理所面临的意图欠规范与优化差距双重困境，提出验证信号的可扩展性、忠实度与鲁棒性“不可能三角”。通过对四种不同任务场景的奖励构造进行深入实验，证明针对性验证设计能有效抑制奖励黑客并提升质量，最终得出核心结论：没有固定的奖励函数能随策略能力增长持续有效，验证必须与生成器共同进化。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
反转了“验证比生成容易”的传统直觉，指出在Coding Agent时代可靠验证已成为瓶颈。深入剖析了验证器作为人类意图代理所面临的双重困境（意图欠规范与优化导致的代理-意图差距），创造性地提出验证信号的“不可能三角”（可扩展性、忠实度、鲁棒性），理论剖析深刻，论证严谨。

### 实用性 (评分: 8.5/10)
针对通用编码、前端、真实世界及长周期任务分别提出了四种奖励构造方案（测试、规则、用户、自动代理验证器），实验证明针对性验证设计能有效抑制奖励黑客并提升任务完成质量，对Agent训练和RLHF的工程实践具有极高的落地指导价值。

### 社区活跃度 (评分: 8.5/10)
直击当前大模型与Agent领域最核心的Reward Hacking与对齐难题，话题极具时效性与前沿性。作者团队背景扎实，研究成果对社区在奖励模型设计上的认知有重要启发，预计将产生较高影响力。

## 项目链接
https://arxiv.org/abs/2606.26300
