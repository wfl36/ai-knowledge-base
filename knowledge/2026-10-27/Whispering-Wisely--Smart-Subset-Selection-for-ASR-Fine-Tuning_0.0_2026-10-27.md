# Whispering Wisely: Smart Subset Selection for ASR Fine-Tuning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-27  
**来源：** rss  

## 项目描述
arXiv:2610.32997v1 Announce Type: new Abstract: Automatic Speech Recognition (ASR) models such as OpenAIs Whisper have substantially improved speech recognition quality but remain expensive to fine-tune, especially when large amounts of transcribed audio are available. This makes it challenging for many practitioners to adapt these models to new languages or domains. In this work, we introduce an embedding-based subset selection approach for selecting smaller training sets for ASR fine-tuning. Using Whispers pretrained encoder, we map each audio sample into a fixed-dimensional embedding space and apply a greedy k-center algorithm to select diverse and representative subsets of the training data. We evaluate this approach on both Hebrew and Danish, showing that k-center selection often improves upon random sampling, particularly at smaller subset sizes. An analysis of lexical diversity reveals that k-center subsets capture a broader range of linguistic content than random subsets of the same size, which may help explain their observed effectiveness. Overall, our results demonstrate that embedding-based subset selection provides a practical strategy for ASR subset selection in the two evaluated languages, with the clearest recognition benefits observed at smaller sample budgets.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.32997
