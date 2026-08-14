# Reliability-Aware Sexism Detection: Combining DPO with Annotator Agreement and Token-Level Confidence Scoring

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-14  
**来源：** rss  

## 项目描述
arXiv:2608.12330v1 Announce Type: new Abstract: The detection of online sexism remains an open problem. Sexism detection is inherently subjective, yet most existing systems reduce multi-annotator labels to a single majority decision and treat all instances uniformly. This ignores two informative signals: annotator agreement and model uncertainty. We propose RA-DPO (Reliability-Aware Direct Preference Optimization), which integrates annotator agreement, model confidence, and a token-level uncertainty signal into a single reliability score. RA-DPO uses this score to select high-value preference pairs during training and to support inference-time abstention, which allows the model to trade coverage for accuracy. We evaluate RA-DPO on 6,920 multilingual posts from EXIST 2023, fine-tune OpenAI gpt-4o base via DPO, and validate on two open-weight 3B models (Llama, Qwen). Results show that training on the top 30% most reliable pairs matches full-data DPO, which indicates that reliability-aware selection can reduce training cost without sacrificing performance. At inference, selective prediction reaches 96.2% accuracy at 50% coverage in the true-agreement setting and 88.7% in the deployable predicted-agreement setting, both exceeding the 85.3% no-agreement baseline. These results suggest that accounting for annotation uncertainty is beneficial for both efficient training and reliable deployment in subjective classification.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.12330
