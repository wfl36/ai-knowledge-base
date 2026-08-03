# Evaluating Federated Pre-Training: On the Reliability of Downstream Fine-Tuning and Intrinsic Evaluation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-03  
**来源：** rss  

## 项目描述
arXiv:2607.28658v1 Announce Type: new Abstract: Federated pre-training offers a way to train foundation models on private or distributed data without centralizing the underlying datasets. However, evaluating federated pre-training remains challenging because differences in client participation and local data availability can make directly comparable evaluation difficult. Moreover, pre-training test perplexity is tied to the pre-training distribution, while downstream benchmarks introduce task-specific adaptation that may not faithfully reflect the test perplexity established during pre-training. In this work, we study which evaluation protocol more reliably reflects federated pre-training quality. Using a controlled set of centralized and federated-trained models of a 16M parameter transformer model trained on identical client data, we assess evaluation protocols by whether they preserve a reference ranking established on the same pre-training testset. We compare downstream fine-tuning on GLUE, including full, head-only, and reduced-data variants, with next-token prediction on GLUE text as an intrinsic evaluation signal. Our results show that downstream fine-tuning does not reliably preserve the pre-training ranking, whereas direct next-token prediction exhibits a strong correspondence with the pre-training test perplexity. These findings suggest that downstream fine-tuning alone can be misleading when comparing federated pre-trained models, and that evaluation signals closer to the original pre-training objective deserve greater attention.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.28658
