# Encoding EEG Signals to Examine Human-Like Next-Word Prediction Behaviour in Language Models

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 认知对齐, EEG, 可解释性, 论文  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16549v1 Announce Type: new Abstract: Language models (LMs) are trained to excel at predicting the next word in the sequence given prior context, and humans also share this predictability in reading comprehension. Neuroscience research reveals that next-word predictability influences brain response, as recorded at millisecond resolution using electroencephalography (EEG). While our evidence indicates that advanced LMs achieve accuracies closely aligned with human performance at the next-word prediction task, this raises the question: Does higher prediction accuracy necessarily mean that these models adequately capture the cognitive signals associated with human reading comprehension? Here, we generate regressors for both humans and LMs based on two information measures, including top-1 prediction and surprisal, to predict event-related potential (ERP) elicited from EEG recordings which reflect different stages of cognitive processing during reading. We argue that modelling ERP patterns offers fine-grained analysis of the cognitive plausibility of various LMs during reading. Our results indicate that only surprisal potentially correlates with language-processing ERPs, especially for open-class words with high semantic content. Moreover, our findings challenge the assumption that scaling LMs with increased parameters and computational budgets will consistently lead to improved convergence with human-like linguistic processing.

## 综合总结
本文通过编码EEG信号，研究了语言模型在下一词预测任务中与人类认知处理的对齐程度。研究发现，LMs的惊奇度而非top-1预测准确率与人类阅读时的ERP信号相关，且主要针对高语义内容的开放类词。更重要的是，研究挑战了“扩大模型参数和计算量必然导致更接近人类语言处理”的假设，为评估大模型的认知合理性提供了神经科学视角的实证。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究将认知神经科学（EEG/ERP）与大语言模型评估深度结合，具有显著的跨学科创新性。通过引入信息论指标（惊奇度/surprisal与top-1预测），精细刻画了模型预测与人类认知处理不同阶段的关联，并严谨地论证了模型规模扩大并不必然带来认知机制上的趋同，研究深度与论证逻辑出色。

### 实用性 (评分: 6.0/10)
对AI工程实践的直接落地指导有限，但为模型评估提供了全新的“认知合理性”视角。研究结论提示开发者在追求模型规模扩展时需警惕与人类认知机制的脱节，对可解释性AI、类脑计算及新型评估基准的开发具有重要参考价值。

### 社区活跃度 (评分: 8.0/10)
话题极具时效性和争议性，挑战了当前业界盲目崇拜Scaling Law的普遍认知，指出参数量增加不等于认知层面的类人化。arXiv论文来源保证了学术可信度，对大模型发展方向的反思具有较强的影响力和启发性。

## 项目链接
https://arxiv.org/abs/2607.16549
