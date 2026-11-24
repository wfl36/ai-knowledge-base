# Rethinking Full-Weight LoRA with Domain and Task Adapter Scaling for Question Answering over Portuguese Well Drilling Reports

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-24  
**来源：** rss  

## 项目描述
arXiv:2611.26833v1 Announce Type: new Abstract: Adapting large language models (LLMs) to specialized domains remains challenging, particularly for technical documents such as Portuguese well drilling reports, where annotated data are scarce and domain adaptation may compromise instruction-following capabilities. Although Low-Rank Adaptation (LoRA) is widely used for parameter-efficient adaptation, its scaling after training remains insufficiently explored. This study investigates the impact of LoRA adapter scaling on question answering over Portuguese drilling reports using Qwen2.5-7B and Llama-3.1-8B. Domain-adaptive pretraining (DAPT) is performed either directly on instruction-tuned models or on their base counterparts, with subsequent adapter transfer, while task-specific adapters are trained on WellQuest, an open-source question-answering dataset derived from Portuguese drilling reports. The two adapters are also combined using complementary weights. Scaling factors ranging from 0.1 to 1.0 are evaluated across multiple training checkpoints using BERTScore. Results show that fractional scaling consistently improves DAPT performance over full-weight application, increasing F1 from 68.8\% to 71.9\% for Qwen2.5-7B and from 63.2\% to 68.5\% for Llama-3.1-8B. QA adapters perform best at high but fractional weights, while base-to-instruct transfer yields better results than direct DAPT on instruct-tuned models. Adapter merging provides a modest improvement for Llama-3.1-8B. Overall, these findings demonstrate that post-training adapter scaling can improve domain adaptation without additional data or training.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.26833
