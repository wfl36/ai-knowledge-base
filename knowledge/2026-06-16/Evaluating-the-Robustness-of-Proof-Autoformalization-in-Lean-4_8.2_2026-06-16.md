# Evaluating the Robustness of Proof Autoformalization in Lean 4

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 自动形式化, AI4Math, 鲁棒性, 评估基准, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.14867v1 Announce Type: new Abstract: Proof autoformalization aims to translate a mathematical informal proof written in natural language into a formal proof in a formal language such as Lean~4. Several works have developed LLM-based models for proof autoformalization. However, existing evaluations have typically focused on translating well-formed informal proofs from curated datasets. We argue that a robust proof autoformalizer must remain faithful even for informal proofs that diverge from these idealized ones, and we present the first study on the robustness of proof autoformalization models. We formulate two categories of perturbations and evaluate robustness under each: a global perturbation paraphrases the informal proof in a different style, under which the formalization should remain consistent; a local perturbation alters a value, symbol, or proof step, possibly in a counterfactual way, and a robust formalization should faithfully reflect the perturbation rather than reverting to the original one or inferring a different one on its own. We build a benchmark with both perturbations on miniF2F and MATH-500, and automatically measure how stable a proof autoformalization's correctness is under global perturbations and how faithfully its output reflects local perturbations. We evaluate seven recent models, all of which are sensitive to global perturbations and mostly fail to remain faithful under local perturbations. Code and data are available via https://github.com/ucr-rai/robust-proof-autoformalization.

## 综合总结
本文首次系统研究了基于LLM的证明自动形式化模型在Lean 4中的鲁棒性。作者提出了全局扰动（风格改写）和局部扰动（值/符号/步骤改变）两类评估维度，并构建了相应的基准测试。对7个近期模型的评估表明，现有模型对全局扰动高度敏感，且在局部扰动下大多无法忠实反映变化。该研究揭示了当前自动形式化模型的脆弱性，为未来模型的改进提供了重要的评估框架和方向。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
首次系统性地定义并研究了证明自动形式化的鲁棒性问题，创新性地提出了全局扰动（风格改写）和局部扰动（反事实改变）两类评估维度，技术深度和新颖性较高，深刻揭示了当前模型对表面特征过拟合及缺乏逻辑忠实性的缺陷。

### 实用性 (评分: 8.0/10)
构建了基于miniF2F和MATH-500的鲁棒性评估基准，并开源了代码和数据，为后续研究者评估和改进自动形式化模型提供了可直接使用的测试框架和明确的实践指导，对开发更健壮的证明助手具有较高参考价值。

### 社区活跃度 (评分: 8.0/10)
聚焦于LLM与形式化数学（Lean 4）交叉的前沿热点，arXiv首发，作者来自知名学术机构（UCR），开源代码增加了可信度与影响力，对AI4Math和形式化验证社区具有重要的启发和推动作用。

## 项目链接
https://arxiv.org/abs/2606.14867
