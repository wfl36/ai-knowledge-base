# On the Computational Complexity of Structural Generalization

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 推理, 计算复杂性, 神经符号, 泛化, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19573v1 Announce Type: new Abstract: Structural generalization has been measured repeatedly by several benchmarks, yet it has never been formally defined. We give a definition that translates the two premises (compositional structure and unbounded generalization) into mathematical language. The definition itself is neutral: a compiler that hard-codes the rules satisfies it just as well. But structural generalization becomes a scientific question only insofar as the capacity can autonomously emerge from finite data. This question pits the computational lower bound $\mathrm{NC}^1$ against the learnable ceiling $\mathrm{TC}^0$ of pure Transformers. Under a Montagovian instantiation, each compositional rule splits into two projections: a syntactic face ($F_\gamma$) and a semantic face ($G_\gamma$). Tree evaluation on the $G_\gamma$ side is an instantiation of BFVP, which is $\mathrm{NC}^1$-complete (Buss, 1987). A pure Transformer must learn both faces at once, but Kraus et al. (2026) prove that its learnable class $\subseteq \mathrm{TC}^0$. Under the standard assumption $\mathrm{TC}^0 \neq \mathrm{NC}^1$, a pure Transformer cannot learn structural generalization. Neuro-symbolic systems achieve the best benchmark scores precisely because they inject $G_\gamma$, sidestepping the genuinely hard half. Benchmark scores cannot distinguish "learned" from "given." This is what this paper sets out to make clear.

## 综合总结
本文从计算复杂性理论的角度，形式化定义了结构泛化，并严格证明了纯Transformer无法实现真正的结构泛化。作者指出组合规则包含语法和语义两面，语义面的树评估属于NC^1完全问题，而纯Transformer的可学习上限为TC^0。在TC^0≠NC^1的标准假设下，纯Transformer无法跨越这一计算鸿沟。此外，文章揭示了当前神经符号系统在基准测试中表现优异仅是因为直接注入了语义规则，绕过了最困难的计算部分，从而指出当前基准测试无法区分'真正学到的'与'预先给定的'能力，是对现有大模型泛化评估体系的深刻反思。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
本文在技术深度与理论严谨性上表现卓越。作者首次将结构泛化（组合结构与无界泛化）转化为严格的数学定义，并创造性地引入计算复杂性理论进行分析。通过将组合规则拆分为语法面和语义面，证明了语义面的树评估是NC^1完全的，而纯Transformer的可学习类别上限为TC^0。在TC^0≠NC^1的标准假设下，严密论证了纯Transformer在理论上无法实现结构泛化。同时，精准剖析了神经符号系统高分背后的'捷径'本质（直接注入语义面绕过复杂计算），逻辑链条闭环，洞见深刻。

### 实用性 (评分: 7.0/10)
对AI从业者的架构设计具有长远的指导价值。虽然作为不可能性结论，它无法直接转化为可落地的工程代码，但它为纯Transformer的能力边界划定了清晰的理论红线，警示业界不要对端到端大模型的结构泛化能力抱有不切实际的幻想。同时，它为神经符号系统的发展提供了强有力的理论背书，指导开发者在设计需要严格组合推理的系统时，必须考虑外部符号机制的注入，而非单纯依赖模型缩放。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，直击当前大模型推理能力与泛化边界的研究热点。来源为arXiv论文，理论推导自洽且引用了经典与前沿（如2026年）的复杂度结论，具有极高的学术权威性与可信度。该结论若被广泛接受，将对现有以纯Transformer为主的LLM评估体系产生颠覆性影响，有望在AI理论社区和架构研发圈引发高度关注与广泛讨论。

## 项目链接
https://arxiv.org/abs/2607.19573
