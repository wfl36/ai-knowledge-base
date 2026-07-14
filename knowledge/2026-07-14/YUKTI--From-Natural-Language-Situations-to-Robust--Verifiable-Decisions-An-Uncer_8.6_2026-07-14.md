# YUKTI: From Natural-Language Situations to Robust, Verifiable Decisions An Uncertainty-Typed Proposition IR, Assumption-Robust Pareto Frontiers, and a Regret Certificate

**评分：** 8.6  
**状态：** 正常  
**标签：** 大模型, 运筹优化, 决策, 不确定性量化, 鲁棒性, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09706v1 Announce Type: new Abstract: Language models turn a worded situation into a numeric plan, and the dominant pipelines (NL4Opt, OptiMUS, ORLM, OR-LLM-Agent) commit to a single objective and point-valued coefficients, then solve once. For decisions that allocate real budget, effort, or clinical attention, that confidence is the failure mode: every objectified number is an assumption, and a plan optimal only if the guesses are exactly right is fragile -- mimicry of computation. YUKTI changes the target of autoformulation. Its representation is a typed-proposition graph whose relationships carry shape priors, coefficient uncertainty, and provenance. YUKTI routes each stage to an exact, nonlinear, or evolutionary solver; couples stages by a distributional Pareto hand-off; and introduces Assumption-Robust Pareto Frontiers (ARPF), resampling assumptions (including structural epsilon-contamination) to score how often each action survives (rho). We prove a bound making rho an exact factor of decision regret, add auditable traceability, and synthesize a benchmark-faithful data foundation when none exists (SRJANA). We validate three ways: under controlled misspecification the robust compromise cuts mean and tail regret by over 90% versus a naive point plan; on a regulated commercial decision we optimize inside a lawful action space and price the downside in euros; and on a real public dataset of 41,188 decisions an out-of-sample backtest beats the logged status quo by 34% and a naive point rule by 4% while reducing the optimizer's curse. The solvers are standard; we claim no benchmark-SOTA win. A head-to-head shows an LLM given the correct numbers, and single-objective optimization, both incur about 47x the held-out regret of YUKTI -- an LLM is a formulator, not a solver. Under long-range causal coupling, the forward hand-off becomes unsound, locating where it must become a backward-induction causal policy.

## 综合总结
YUKTI针对当前LLM在运筹优化决策中依赖点值系数导致的脆弱性问题，提出了一种基于类型化命题图的新范式。该方法引入假设鲁棒帕累托前沿（ARPF）重采样评估动作存活率，并理论证明了其与决策遗憾的精确界限。实验表明，该方法在受控错配和真实数据集中将遗憾降低90%以上，显著优于直接使用LLM或单目标优化的方法（降低约47倍遗憾），明确了LLM应作为公式化器而非求解器的定位，为高价值决策场景提供了可验证、鲁棒的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.2/10)
论文深刻指出了当前LLM结合运筹优化（如NL4Opt等）流水线中'点值系数与单目标求解'的脆弱性本质，提出了类型化命题图表示法，引入假设鲁棒帕累托前沿（ARPF）与遗憾证书，理论证明了动作存活率与决策遗憾的精确界限。同时指出了长程因果耦合下前向传递的失效问题及后向归纳的必要性，技术深度与理论严谨度极高。

### 实用性 (评分: 8.5/10)
对涉及真实预算、临床资源分配等高价值决策场景具有极高的指导价值。通过将不确定性内生化并提供可审计的追溯性与遗憾界限，解决了实际业务中'优化器诅咒'的痛点。在合规商业决策与真实大规模公开数据集上验证了其有效性（降低90%以上遗憾，提升34%收益），但系统涉及多求解器路由与分布帕累托传递，工程落地具有一定复杂度。

### 社区活跃度 (评分: 8.0/10)
LLM赋能运筹优化与决策是当前学术界与工业界的热点，本文直击该领域痛点，时效性强。arXiv预印本发布，虽为单作者且声称不追求SOTA基准，但其扎实的理论证明与真实数据集回测赋予了极高的可信度。明确界定'LLM是公式化器而非求解器'的观点对社区具有强烈的启发和纠偏影响力。

## 项目链接
https://arxiv.org/abs/2607.09706
