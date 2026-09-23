# Retrieved-Span Training for Efficient Query-Focused Meeting Summarization on QMSum

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-23  
**来源：** rss  

## 项目描述
arXiv:2609.25028v1 Announce Type: new Abstract: QMSum provides no scorer, making query-focused meeting summarization results difficult to compare. We rescore or generate 15 systems under one implementation. Through a common inference port, a released 406M Fusion-in-Decoder specialist loses 6.30 ROUGE-1 when moved from capped long input to 2,000-word retrieved spans. Fine-tuning it on this span regime recovers the loss. On test it scores 36.33 ROUGE-1 versus 35.41 for our 1.2B system; the meeting-cluster 95% interval for the difference is [-0.27, +2.22], so QMSum does not statistically separate them. The smaller system uses about one-third as many total parameters and less than half the peak inference memory. Within the fixed 1.2B base, span-regime fine-tuning adds 5.29 [+4.02, +6.56], while replacing the first 4,500 transcript words with 2,000 retrieved words adds 1.55 on test and 0.29 on validation. Separately, under one concise prompt and reference-overlap scorer, a released 406M specialist exceeds five proprietary hosted models by at least 6.2 ROUGE-1, but output length and absent human or factuality evaluation limit this ordering. Conclusions are limited to QMSum and automatic metrics.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.25028
