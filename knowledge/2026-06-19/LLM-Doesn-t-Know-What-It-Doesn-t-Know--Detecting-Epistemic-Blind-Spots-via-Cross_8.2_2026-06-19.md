# LLM Doesn't Know What It Doesn't Know: Detecting Epistemic Blind Spots via Cross-Model Attribution Divergence on Clinical Tabular Data

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 不确定性量化, 医疗AI, 结构化数据, 推理, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19509v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly applied to structured clinical data, yet whether they can recognize the limits of their own knowledge on such tasks remains unexplored. We study this question through the lens of cross-model attribution divergence with the goal of reducing epistemic uncertainty for structured tasks, comparing Qwen 2.5 7B and XGBoost on a prediction task via attribution divergence analysis. We report four findings. First, LLM verbalized confidence is epistemically vacuous, it outputs a near-constant (0.856-0.937) regardless of whether accuracy is 49% or 75.3%, tracking prompt format rather than prediction quality. Second, the LLM exhibits an inverse difficulty effect: accuracy drops to 64.8% when XGBoost is 99% correct, but matches XGBoost (73.8% vs. 73.1%) when it is moderately uncertain. Third, few-shot examples and SHAP-derived feature evidence are orthogonal, super-additive interventions: they reduce the Attribution Disagreement Score (ADS) from 1.54 to 0.38 and improve accuracy from 49% to 75.3% without training. Fourth, a cross-model calibrator that determined LLM reliability using attribution divergence signals reduces expected calibration error from 0.254 to 0.080, replacing uninformative verbalized confidence with patient-specific reliability estimates, without accessing model internals or requiring repeated inference. We frame these findings as a cold start problem for LLMs on structured data and outline a path toward genuine epistemic self-awareness.

## 综合总结
该论文揭示了LLM在结构化临床数据上存在严重的认知盲点：其语言化置信度与实际准确率脱钩，且表现出反直觉的'逆难度效应'。研究提出通过跨模型归因分歧（对比LLM与XGBoost的归因差异）来检测盲点，发现Few-shot与SHAP特征证据结合能显著提升性能并降低分歧。基于此提出的跨模型校准器，无需模型内部访问即可大幅降低预期校准误差，为高风险场景下LLM的可靠性评估与自我认知提供了创新且落地的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究视角新颖，将LLM的'不知道自己不知道'问题（认知盲点）聚焦于结构化临床数据，并通过跨模型归因分歧（LLM vs XGBoost）进行量化。发现了LLM语言化置信度失效和'逆难度效应'等反直觉现象，论证严谨；提出的SHAP与Few-shot正交超加性干预以及跨模型校准器，在方法论上具有较好的深度与创新性。

### 实用性 (评分: 8.0/10)
对医疗AI等高可靠性场景的落地具有极高的参考价值。明确指出了依赖LLM自我报告置信度的不可靠性，并提供了无需访问模型内部或重复推理的实用校准方案（基于归因分歧信号），直接解决了结构化数据上LLM可靠性评估的痛点，SHAP+Few-shot的提效方法也易于工程实现。

### 社区活跃度 (评分: 8.0/10)
话题时效性极强，直击当前大模型领域核心痛点——幻觉与不确定性量化。虽然为arXiv预印本，但针对临床结构化数据的认知盲点研究填补了特定空白，对提升LLM在高风险领域的可信度有显著启发，预计将在AI安全与医疗AI社区引发关注。

## 项目链接
https://arxiv.org/abs/2606.19509
