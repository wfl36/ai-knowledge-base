# CARVE-Q: Quantum-Proposed, Classically Certified Interactive Driving Repair

**评分：** 7.0  
**状态：** 正常  
**标签：** 自动驾驶, 量子计算, 形式化验证, 交互规划, 论文  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06531v1 Announce Type: new Abstract: The critical question after a correct driving veto is not only whether a maneuver is unsafe, but whether the blocked interaction admits a lawful, auditable, and responsibility-bounded repair. Prediction and game-theoretic planners can suggest plausible cooperation, yet they do not return a proof that the repair respects hard rules, right-of-way, cost allocation, and ego fallback. We introduce CARVE, Certified Affordable Repair of Vetoed maneuvers via Envelopes, a certificate architecture for prediction-free interactive repair. Given a vetoed maneuver, CARVE constructs a finite repair lattice and emits a structured certificate recording the binding rule, selected joint repair, right-of-way-scaled cooperation envelope, responsibility-weighted cost split, and ego-only fallback. This certificate view reveals the algorithmic bottleneck: multi-owner repair induces a product lattice $M = \prod_j |\mathcal{A}_j|$. We therefore introduce CARVE-Q, a verifier-shielded quantum-AI search layer that applies quantum minimum finding only to this black-box lattice while leaving all safety authority classical. In the conservative verifier-oracle model, exact classical minimum finding requires $\Theta(M)$ queries in the worst case, whereas Durr-Hoyer/Grover minimum finding uses $O(\sqrt{M})$ oracle queries with high probability. We prove verifier-shielded certificate soundness, priority non-elicitation, black-box query separation, and finite-precision reversible-oracle constructibility. We then demonstrate state-vector minimum finding on CARVE repair oracles up to 65,536 assignments and validate certificate preservation on Lanelet2-grounded INTERACTION replay with 100% right-of-way respect, 100% blame consistency, and zero priority false positives. The result is a trust-bounded quantum-AI pattern for certified autonomy: quantum proposes; CARVE certifies.

## 综合总结
本文提出CARVE-Q架构，针对自动驾驶中否决操作的合法修复问题，构建了预测无关的有限修复格与结构化证书体系。为解决多所有者修复导致的乘积格指数级搜索瓶颈，创新性地引入验证器屏蔽的量子AI搜索层，利用量子最小查找实现平方级加速，同时将安全认证权限保留在经典计算中。论文在数学上证明了该模式的证书健全性，并在仿真与INTERACTION数据集上验证了其100%路权尊重与责任一致性，确立了'量子提议，经典认证'的信任有界新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文在技术深度与新颖性上表现卓越。创新性地提出了'量子提议，经典认证'(Quantum proposes, CARVE certifies)的范式，将量子计算（Durr-Hoyer/Grover最小查找算法）应用于自动驾驶交互修复的乘积格搜索中，将最坏情况下的查询复杂度从Θ(M)降至O(√M)。同时，论文在形式化验证层面严谨证明了验证器屏蔽的证书健全性、优先级非诱导性及黑盒查询分离等性质，数学论证严密，技术壁垒极高。

### 实用性 (评分: 4.5/10)
尽管理论框架极具启发性，但短期内落地难度极大。核心的量子搜索加速依赖于容错量子计算硬件的成熟，目前只能在状态向量仿真层面验证（65536个分配），距离车载边缘计算部署尚有鸿沟。不过，其'预测无关的交互修复'与'结构化证书'的经典验证架构部分，对当前自动驾驶安全与形式化验证从业者仍有一定的架构参考价值。

### 社区活跃度 (评分: 7.5/10)
量子计算与自动驾驶/形式化验证的交叉属于极具前瞻性的前沿话题，时效性强。但作为单作者预印本且发布时间标定为2026年，其同行评审状态和学术共同体背书尚不明确。若其理论声明被后续验证成立，将在量子AI与可信自动驾驶交叉领域产生显著影响力。

## 项目链接
https://arxiv.org/abs/2606.06531
