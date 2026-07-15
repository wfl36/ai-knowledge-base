# MAGE: Understanding Stability-Performance Trade-offs in Multi-component Prompt Optimization

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, 提示词工程, Agent, 推理, 论文  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.11944v1 Announce Type: new Abstract: How do different components of iterative prompt optimization interact, and what happens when they are combined? We investigate this through MAGE (Memory-Augmented Goal-directed Prompt Evolution), a controlled analysis framework for studying component interaction in prompt optimization. MAGE is not proposed as a superior optimizer in absolute terms; it integrates episodic memory, multi-objective Pareto selection, and adaptive evaluation as a platform for controlled ablation. Our experiments uncover a previously unreported phenomenon, the Prompt Optimization Coupling Effect (POCE): when multiple stochastic optimization signals operate within a closed reflective loop, they interact in ways that simultaneously improve performance and amplify variance, behavior that cannot be predicted by analyzing components in isolation. Three main findings emerge. First, failure-grounded reflection is essential: methods relying only on scores (OPRO) or abstract critique (Self-Refine) fail to improve prompts. Second, MAGE achieves 46.4% versus GEPA's 34.0% on GSM8K-Hard (+12.4%, P(MAGE>GEPA)=0.998, 5 seeds on gpt-4o-mini), with comparable variance (7.3% vs. 7.0%). Third, increasing candidate diversity reveals the clearest POCE signal: expanding the candidate pool from n=3 to n=5 improves mean accuracy by +21.6% while increasing variance by 3.7x. We further validate on Llama 3.1 8B and show POCE is headroom-dependent: when the base model already achieves high accuracy, variance amplification disappears. Finally, in low-data regimes (Ntrain=30), well-designed fixed prompts outperform all reflective optimizers, indicating that scaffold choice dominates optimizer choice. Our results suggest prompt optimization systems behave as coupled stochastic processes and should be evaluated in terms of both performance and stability, not just peak accuracy.

## 综合总结
该论文提出了MAGE框架，用于研究多组件提示优化的交互作用，并发现了“提示优化耦合效应（POCE）”——多个随机优化信号在闭环中交互会同时提升性能和放大方差。研究指出基于失败的反思至关重要，而仅靠分数或抽象批评无效；MAGE在GSM8K-Hard上显著优于GEPA；增加候选多样性会加剧方差放大；在低数据量下，固定提示优于反思优化器。论文呼吁提示优化系统应同时评估性能与稳定性，而非仅看峰值准确率。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
提出了提示优化耦合效应（POCE），揭示了多组件随机优化信号在闭环中交互时性能与方差同步放大的非直觉现象。通过严格的消融实验和统计验证（如5种子P值验证），论证了基于失败的反思优于纯分数或抽象批评，并指出低数据量下脚手架选择优于优化器，研究深度和严谨性极高。

### 实用性 (评分: 7.8/10)
对提示词工程和智能体开发具有高参考价值。研究结论直接指导实践：提醒从业者在多组件优化中警惕方差放大，强调基于失败案例的反思机制设计，并指出在低数据场景下精心设计的固定提示优于复杂的反思优化器，适用范围广且可操作性强。

### 社区活跃度 (评分: 8.2/10)
话题紧扣当前大模型提示词优化与反思机制的热点。针对OPRO、Self-Refine等主流方法提出挑战，揭示了被忽视的稳定性问题，具有高度时效性。来源为arXiv预印本，实验覆盖主流模型（GPT-4o-mini, Llama 3.1），数据详实，在学术界和工程界易引发关注与讨论。

## 项目链接
https://arxiv.org/abs/2607.11944
