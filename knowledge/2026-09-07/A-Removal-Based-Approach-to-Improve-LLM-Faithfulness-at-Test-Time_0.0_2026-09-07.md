# A Removal Based Approach to Improve LLM Faithfulness at Test-Time

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-07  
**来源：** rss  

## 项目描述
arXiv:2609.04343v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used for consequential decisions, making their explanations an important tool for auditing model behavior. Unfortunately, these explanations can be unfaithful, failing to reflect the actual reasoning underlying the model's decisions. We consider a setting in which an LLM provides both an answer and an explanation in response to a question. We identify two distinct dimensions of unfaithful explanations: incompleteness, meaning that the explanation omits factors that influence the answer, and unsoundness, meaning that the explanation cites factors that did not influence the model's answer. Existing approaches to improving LLM faithfulness include training-time methods, which require access to model weights and extensive computational resources, and test-time methods that largely focus on addressing unsoundness. We introduce a test-time approach that directly targets incompleteness. We remove from the input the concepts not credited in the model's explanation and re-query the model on the reduced input. This eliminates unmentioned influences while preserving the influence of mentioned concepts. Across two datasets, multiple model families, and two independent faithfulness metrics, our approach improves explanation faithfulness compared to both standard prompting and prompting to encourage faithfulness. Our method is model-agnostic and can be applied at inference time without modifying model parameters, providing a flexible mechanism for reducing hidden influences and improving the reliability and safety of LLM-assisted decision making.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.04343
