# When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 评估, 校准, 置信度, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30814v1 Announce Type: new Abstract: Calibration evaluates whether a model confidence aligns with its empirical accuracy. Existing studies often compare the calibration of different large language models using global calibration metrics such as Expected Calibration Error and Brier Score. We begin by showing, both theoretically and empirically, that such comparisons are confounded by differences in model accuracy. For fairer cross-model comparison, we then propose ACE, an accuracy-controlled evaluation framework with three complementary views: Instance-Aligned, Distribution-Aligned, and Candidate-Aligned calibration. Across multiple benchmarks, model families, and confidence elicitation methods, we use ACE to study two practically important comparison axes, small versus large models and thinking versus non-thinking models. We find that many previously reported calibration advantages under raw global metrics weaken substantially after accuracy control. We also find that ranking reversal is frequent: models favored by raw metrics often cease to be favored once accuracy is controlled. Our results show that raw global calibration metrics are not robust for cross-model comparison, and that fair calibration comparison requires accuracy-aware evaluation.

## 综合总结
本文指出传统全局校准指标在比较不同LLM时受模型准确率差异的混淆，导致评估不公。为此提出ACE（准确率控制评估）框架，包含实例、分布和候选三种对齐视角。实验表明，在控制准确率后，许多原本的校准优势大幅减弱甚至出现排名反转，强调跨模型校准比较必须考虑准确率因素。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
揭示了传统全局校准指标（如ECE和Brier Score）在跨模型比较时受准确率差异混淆的根本性缺陷，提出ACE（准确率控制评估）框架，从实例对齐、分布对齐和候选对齐三个互补视角进行公平评估。理论结合实证，发现排名反转现象，论证严谨，研究深度和新颖性极高。

### 实用性 (评分: 8.5/10)
对LLM评估和选型具有直接指导意义。从业者可应用ACE框架在控制准确率的条件下公平比较模型校准度，避免因全局指标误导而做出错误的模型选择，尤其在大小模型和思考/非思考模型对比场景中极具实操参考价值。

### 社区活跃度 (评分: 8.0/10)
LLM校准与置信度评估是当前大模型对齐与安全领域的热点话题。该研究直击现有评估体系的痛点，来源为arXiv学术论文，作者团队具备学术背景，结论对社区现有认知有较大冲击，具备较高时效性和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.30814
