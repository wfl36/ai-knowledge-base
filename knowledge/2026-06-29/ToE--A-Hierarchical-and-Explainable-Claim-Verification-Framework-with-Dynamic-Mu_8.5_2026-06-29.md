# ToE: A Hierarchical and Explainable Claim Verification Framework with Dynamic Multi-source Evidence Retrieval and Aggregation

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, Agent, RAG, 推理, 事实核查, 论文  
**更新日期：** 2026-06-29  
**来源：** rss  

## 项目描述
arXiv:2606.27736v1 Announce Type: new Abstract: The rapid spread of fake news poses increasing threats to information ecosystems, especially as AI-generated misinformation under Generative Engine Optimization (GEO) poisoning allows adversarially crafted content to be systematically surfaced by retrieval systems, contaminating LLM reasoning. In this paper, we propose Tree of Evidence (ToE), a hierarchical evidence reasoning framework for automated fact-checking that models each claim as a dynamically expanding argument tree. ToE integrates a reinforcement learning-driven multi-source retrieval agent, an evidence evaluation agent, and an argument tree aggregation algorithm to iteratively decompose, retrieve, and verify claims through an explainable evidence chain. We further provide a theoretical analysis of the retrieval process, deriving a formal error bound that guarantees the learned policy converges to a neighborhood of the information-theoretically optimal policy. Experiments across multiple datasets and backbone LLMs demonstrate that ToE achieves improvements ranging from 4 to 24 percentage points over competitive baselines, with particularly pronounced gains on adversarially poisoned inputs.

## 综合总结
本文针对生成式引擎优化(GEO)中毒导致的虚假信息威胁，提出了层级化可解释的事实核查框架Tree of Evidence (ToE)。ToE通过强化学习驱动的多源检索Agent、证据评估Agent及论证树聚合算法，将声明迭代分解并构建可解释的证据链进行验证。研究不仅提供了检索策略收敛至信息论最优策略邻域的理论误差界限证明，还在多数据集和骨干LLM上验证了其有效性，相比基线提升4-24个百分点，尤其在对抗性中毒输入下表现优异，是AI内容安全与事实核查领域的重要突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文提出了新颖的Tree of Evidence (ToE)层级化论证树推理框架，结合强化学习驱动的多源检索Agent与证据评估Agent，有效应对GEO中毒下的虚假信息核查难题。技术深度与严谨性极高，不仅设计了迭代分解与验证的算法架构，还给出了检索策略收敛至信息论最优策略邻域的形式化误差界限理论证明，论证严密，方法创新性强。

### 实用性 (评分: 8.5/10)
在LLM广泛应用的当下，RAG系统面临数据污染与对抗性输入的巨大风险，ToE框架的模块化设计（检索Agent、评估Agent、聚合算法）对构建鲁棒的事实核查与内容安全系统具有极高的工程参考价值。实验显示其在对抗性中毒输入上提升显著，可直接指导相关防御机制的落地实践。

### 社区活跃度 (评分: 8.0/10)
话题聚焦于生成式引擎优化(GEO)中毒这一新兴且极具威胁的AI安全痛点，时效性与前沿性极强。arXiv预印本来源具备一定权威性，但尚未经过正式同行评审，且发布时间标识为2026年（可能为编号异常或数据偏移），略微影响即时可信度评分，但整体对AI安全与事实核查社区具有较高影响力。

## 项目链接
https://arxiv.org/abs/2606.27736
