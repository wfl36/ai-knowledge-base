# Register Bias in Complexity-Based Large Language Model Routing

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-17  
**来源：** rss  

## 项目描述
arXiv:2609.17542v1 Announce Type: new Abstract: Large language model services increasingly route each query to one of several models of differing capability, using a cheap estimate of query complexity to send easy queries to small models and hard queries to large ones. I show that this routing step is not register neutral: text written in a non-standard English register, African American English or the English of second-language writers, is systematically assigned a lower-capacity tier than a meaning-equivalent standard-English version of the same query. The effect is driven by a specific, common routing signal, input length, because non-standard registers omit function words and thus look shorter and therefore simpler; other complexity signals do not carry it. I demonstrate the disparity on 37,704 authentic learner sentence pairs and on a controlled parallel corpus. I then measure the quality consequence on a device, edge, and cloud model ladder and find that the harm is driven by pervasive model bias, every tier, including a frontier cloud model, answers non-standard-register queries significantly less accurately, while the marginal quality cost of the routing decision itself is not significant on this benchmark. Complexity-based routing thus compounds the exposure of the users that the models already serve worst.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.17542
