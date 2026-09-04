# Contamination Inflates Scores but Rarely Reorders Large Language Model Leaderboards

**评分：** 7.8  
**状态：** 正常  
**标签：** 大模型评测, Benchmark Contamination, 数据污染, Leaderboard, 论文, 方法论, LLM  
**更新日期：** 2026-09-04  
**来源：** rss  

## 项目描述
arXiv:2609.02899v1 Announce Type: new Abstract: Benchmark contamination, the leakage of test items into training data, is widely described as a threat to the reliability of large language model (LLM) leaderboards. We argue that this concern conflates two distinct questions: whether contamination inflates absolute scores, and whether it reorders the ranking of models. We recast contamination as a violation of anchor-item invariance and measure it through the differential functioning of original versus semantically equivalent paraphrased items, a within-item contrast that holds the measured skill fixed and isolates memorization from capability. Using per-instance responses from 47 publicly released models and 74 models finetuned with a known dose of contamination, across four benchmarks (ARC, GSM8K, HellaSwag, MMLU), we first calibrate the measure against ground truth: it recovers injected contamination dose-responsively (a corrected effect of +0.187 accuracy points for test-set leakage) and never flags a negative-control model trained only on the legitimate training split (-0.012). We then quantify leaderboard impact: the rank correlation between a standard leaderboard and a paraphrase-controlled leaderboard is 0.997, and a sensitivity analysis shows that the observed differential contamination is far below the level needed to move rankings, with only 3 of 188 model-by-benchmark cases showing differential contamination corroborated across two references. Contamination among these public models is therefore largely uniform: it inflates absolute scores without reordering the leaderboard, and ranking distortion requires the rare case of differential contamination. We provide a calibrated invariance audit, released as a reference implementation, and recommend that leaderboards report paraphrase-controlled rankings alongside confidence intervals.

## 综合总结
该论文针对LLM benchmark contamination问题，提出将其分解为'膨胀分数'与'打乱排名'两个独立维度，并基于'anchor-item invariance'原则设计了通过原始题与语义改写题的within-item对比来量化污染的方法。实验涵盖121个模型与4个主流基准，验证了测量的剂量响应校准性，并得出核心发现：现有公开模型的污染大多均匀分布，虽会抬高绝对分数但极少改变排名（rank correlation达0.997），仅3/188案例出现跨参考交叉验证的差异性污染。论文提供了开源审计工具，建议leaderboard同时报告paraphrase-controlled排名与置信区间。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.2/10)
论文提出了一个新颖的概念框架，将benchmark contamination区分为'是否膨胀绝对分数'与'是否打乱排名'两个独立问题，并引入'anchor-item invariance'作为衡量准则。方法上采用'原始题目vs语义等价改写题目'的within-item对比设计，控制被测能力不变、隔离记忆效应，这种思路在测量学上具有较高的严谨性。实验覆盖47个公开模型+74个注入已知污染剂量的微调模型，覆盖ARC/GSM8K/HellaSwag/MMLU四个基准，并通过ground-truth校准验证了测量的剂量响应关系（+0.187 accuracy points）与负控制（-0.012），论证链条完整。方法论贡献明显高于工程贡献，但理论层面并未提出全新机制，而是对已有现象的更精细分解。

### 实用性 (评分: 7.8/10)
对LLM评测从业者具有直接参考价值：提供了一个经过校准的不变性审计工具，可作为leaderboard报告的补充实践。核心结论（污染通常均匀膨胀分数而不打乱排名）对leaderboard设计者、benchmark维护者具有明确的实践指导意义——建议报告paraphrase-controlled rankings并附置信区间。代码作为reference implementation开源，进一步降低了落地门槛。不过该方法对每个模型都需要额外的paraphrase题目响应数据，部署成本不可忽视，且主要验证在四类选择题/数学题基准上，对开放式生成、代码评测等场景的外推性有限。

### 社区活跃度 (评分: 7.5/10)
主题（benchmark contamination）是LLM评测领域长期关注的热点问题，2024-2025年以来随着训练数据透明度讨论升温而持续高热。文章发布于arXiv，作者来自Stanford等机构，具备一定学术权威性。实验规模（121个模型、4个数据集）以及提供的reference implementation增强了可信度与可复现性。话题对学术界和工业界LLM评测实践均有直接影响，但作为单篇方法学论文，其传播影响力可能集中于评测研究社区，对更广泛的AI从业者辐射有限。

## 项目链接
https://arxiv.org/abs/2609.02899
