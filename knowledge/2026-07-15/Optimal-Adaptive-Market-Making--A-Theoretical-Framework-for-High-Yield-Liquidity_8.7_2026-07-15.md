# Optimal Adaptive Market Making: A Theoretical Framework for High-Yield Liquidity Provision in Perpetual Futures Markets

**评分：** 8.7  
**状态：** 正常  
**标签：** 量化交易, 做市商, DeFi, 永续合约, 随机最优控制, 论文  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.11888v1 Announce Type: new Abstract: We develop a rigorous theoretical framework for optimal market making in perpetual futures markets with zero maker fees. We model the market maker's problem as a stochastic optimal control problem on a filtered probability space, where the controls are adaptive bid-ask spreads and inventory hedging decisions across two exchanges. Our contributions include: (i) a PnL decomposition theorem separating revenue into spread income, adverse selection loss, inventory carrying cost, hedging friction, and funding rate exposure; (ii) the Hamilton-Jacobi-Bellman equation for the joint spread-inventory-hedging control problem under CARA utility with a verification theorem; (iii) High-APY Regime Theorems characterizing profitable regions via five dimensionless parameters, culminating in a Master APY Formula; (iv) analysis of zero-fee economics on decentralized perpetual exchanges with optimal entry-exit thresholds; (v) optimal cross-exchange hedging policies with funding rate dynamics and a hedge regime trichotomy; (vi) a robustness margin quantifying parameter uncertainty tolerance; (vii) exponential drawdown probability bounds and a universal APY-VaR identity; (viii) ergodic inventory distribution under optimal control with Bayesian adaptive estimation; (ix) Kelly-optimal leverage with ruin boundaries; and (x) multi-pair portfolio allocation with diversification saturation results. Numerical analysis with twenty-three figures reveals phase transitions between profitable and unprofitable regimes. Our framework unifies and extends the Avellaneda-Stoikov, Gueant-Lehalle-Fernandez-Tapia, and Glosten-Milgrom paradigms for modern decentralized venue microstructure.

## 综合总结
本文提出了一个针对零手续费永续合约市场的最优自适应做市理论框架。通过随机最优控制方法，推导了包含报价、库存与对冲的联合HJB方程，并给出了PnL分解定理与Master APY公式。研究深入分析了资金费率动态、跨所对冲策略、Kelly杠杆及回撤风险，统一了经典做市范式，为DeFi做市商提供了极具深度的理论指导与策略设计蓝图。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
论文将永续合约市场的做市问题建模为随机最优控制问题，推导了CARA效用下的HJB方程及验证定理。创新性地提出了PnL分解定理、High-APY机制定理及Master APY公式，并系统引入了资金费率动态、跨所对冲三分法、Kelly最优杠杆及回撤边界等，从数学上统一并扩展了Avellaneda-Stoikov、Gueant-Lehalle-Fernandez-Tapia和Glosten-Milgrom等经典做市范式，理论深度与严谨性极高。

### 实用性 (评分: 8.5/10)
针对DeFi永续合约零手续费场景，为做市商提供了从报价、库存对冲到杠杆选择和组合配置的全方位理论指导。Master APY公式、APY-VaR恒等式及相变分析可直接辅助量化团队评估收益风险边界与策略参数设定，但实际落地仍需克服参数估计、贝叶斯自适应计算与高频交易工程等挑战。

### 社区活跃度 (评分: 8.0/10)
研究聚焦DeFi永续合约做市这一前沿热点，高度契合当前去中心化衍生品交易所（如零手续费机制）的微结构特征。作为arXiv预印本，其数学论证严密，但尚需同行评审与实盘数据验证，对DeFi量化交易与金融微观结构社区具有较高参考价值与潜在影响力。

## 项目链接
https://arxiv.org/abs/2607.11888
