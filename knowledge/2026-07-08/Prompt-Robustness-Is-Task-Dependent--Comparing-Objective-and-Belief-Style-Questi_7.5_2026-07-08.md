# Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 评估, 鲁棒性, 对齐, 论文  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05554v1 Announce Type: new Abstract: Survey-style evaluations of large language models often treat a prompted response as a measure of a model's values or beliefs. This assumption is particularly fragile when responses are read as evidence of political values, social attitudes, or beliefs. We ask whether prompt robustness differs between objective questions with fixed answers and subjective questions that ask for opinions or values. We evaluate four instruction-tuned model families on three objective datasets (MMLU, ARC, and CulturalBench) and three subjective datasets (Political Compass Test, ValueBench, and World Values Survey). For each question/statement, we apply multiple types of prompt changes, such as variations in wording, framing, and format, and measure whether the model gives the same answer across variants. Using a binomial generalized estimating equation, we find significant effects of model, dataset, prompt category, and their interactions. The dataset type effect is also significant, and the interaction between dataset type and prompt category is large. These results show that prompt robustness depends on the question type, the prompt change, and the model.

## 综合总结
本文研究了LLM在客观题与主观信念题上的提示鲁棒性差异。通过对4个模型家族和6个主客观数据集的实证分析，发现提示鲁棒性高度依赖于任务类型、提示变化方式及模型本身，主观问题的鲁棒性显著低于客观问题。该研究警示从业者在评估模型价值观时需谨慎对待提示设计，避免将单次响应过度解读为模型固有信念。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文通过对比客观问题与主观（信念/价值观）问题，深入研究了LLM评估中的提示鲁棒性问题。采用二项式广义估计方程对4个模型家族在6个数据集上的表现进行严谨的统计分析，发现提示鲁棒性显著受问题类型、提示变化类别及模型本身的三重交互影响，主观问题的鲁棒性明显弱于客观问题，挑战了将主观题响应直接等同于模型固有信念的假设。

### 实用性 (评分: 8.0/10)
研究结果对LLM评估集设计、红队测试及对齐研究具有直接指导意义。提醒从业者在评估模型政治倾向、社会价值观等主观属性时，必须考虑提示措辞、框架和格式带来的偏差，不能简单将单次提示结果视为模型稳定信念，需通过多提示变体测试验证鲁棒性。

### 社区活跃度 (评分: 7.0/10)
话题切中当前大模型价值观对齐与安全评估的社区热点，arXiv来源具备一定权威性。研究通过严格的统计方法量化了“主观评测易受提示干扰”这一社区隐忧，虽结论部分符合直觉，但提供了坚实的实证数据支撑，对评测社区有较好的警示价值。

## 项目链接
https://arxiv.org/abs/2607.05554
