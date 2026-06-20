# LLM Doesn't Know What It Doesn't Know: Detecting Epistemic Blind Spots via Cross-Model Attribution Divergence on Clinical Tabular Data

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 推理, 表格数据, 校准, 认知不确定性, 医疗AI, 论文  
**更新日期：** 2026-06-20  
**来源：** rss  

## 项目描述
arXiv:2606.19509v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly applied to structured clinical data, yet whether they can recognize the limits of their own knowledge on such tasks remains unexplored. We study this question through the lens of cross-model attribution divergence with the goal of reducing epistemic uncertainty for structured tasks, comparing Qwen 2.5 7B and XGBoost on a prediction task via attribution divergence analysis. We report four findings. First, LLM verbalized confidence is epistemically vacuous, it outputs a near-constant (0.856-0.937) regardless of whether accuracy is 49% or 75.3%, tracking prompt format rather than prediction quality. Second, the LLM exhibits an inverse difficulty effect: accuracy drops to 64.8% when XGBoost is 99% correct, but matches XGBoost (73.8% vs. 73.1%) when it is moderately uncertain. Third, few-shot examples and SHAP-derived feature evidence are orthogonal, super-additive interventions: they reduce the Attribution Disagreement Score (ADS) from 1.54 to 0.38 and improve accuracy from 49% to 75.3% without training. Fourth, a cross-model calibrator that determined LLM reliability using attribution divergence signals reduces expected calibration error from 0.254 to 0.080, replacing uninformative verbalized confidence with patient-specific reliability estimates, without accessing model internals or requiring repeated inference. We frame these findings as a cold start problem for LLMs on structured data and outline a path toward genuine epistemic self-awareness.

## 综合总结
该论文研究了LLM在结构化临床数据上的认知盲点问题，发现LLM的口头置信度无法真实反映预测准确性（呈现空洞性），且存在'逆难度效应'。作者提出通过跨模型归因分歧（比较LLM与XGBoost）来检测认知盲点，发现Few-shot与SHAP特征证据结合能显著降低归因分歧并提升准确率。此外，基于归因分歧信号的跨模型校准器大幅降低了预期校准误差，无需访问模型内部即可提供患者级别的可靠性评估，为LLM在结构化数据上实现真正的认知自我意识提供了新路径。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
该论文在研究深度和新颖性上表现突出。首次通过跨模型归因分歧（LLM vs XGBoost）的视角来探测LLM在结构化数据上的认知盲点，揭示了LLM口头置信度的空洞性及反直觉的'逆难度效应'。结合SHAP与Few-shot正交超叠加效应的论证严谨，提出的无需访问模型内部或重复推理的跨模型校准器技术深度高，为解决LLM'不知道自己不知道'的认知不确定性问题提供了创新且严密的解法。

### 实用性 (评分: 8.5/10)
对医疗AI及结构化数据处理从业者具有极高的实践指导价值。论文明确指出LLM原生置信度不可靠，并提供了即插即用的解决方案：通过SHAP特征证据与Few-shot结合的Prompt工程可大幅提升准确率（49%至75.3%）；基于归因分歧信号的校准器能将预期校准误差从0.254降至0.080，且无需访问模型内部，工程落地友好，可直接应用于高风险临床预测场景的可靠性评估。

### 社区活跃度 (评分: 8.0/10)
论文发布于2026年6月，时效性强。LLM的幻觉、置信度校准及认知边界是当前AI安全和医疗AI社区的核心痛点与热点话题。虽然作者并非顶级明星团队，但研究直击LLM在垂直领域落地的关键瓶颈（自我认知缺失），结论对社区现有认知具有强冲击力，预计将在医疗AI和模型可解释性领域产生显著影响力。

## 项目链接
https://arxiv.org/abs/2606.19509
