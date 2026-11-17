# CamSpokenNLI: A Pilot Resource for Cross-Variety Transfer Evaluation in Cameroon Pidgin English and Camfranglais

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-17  
**来源：** rss  

## 项目描述
arXiv:2611.17573v1 Announce Type: new Abstract: Cameroon Pidgin English (a West African Pidgin English variety) and Camfranglais are widely used in Cameroon, yet to our knowledge, neither has a dedicated spoken Natural Language Inference (NLI) resource. We introduce CamSpokenNLI, a pilot dataset of 114 scenario-matched spoken NLI items in each variety (228 in total), recorded by one native speaker from Buea. Each item pairs premise audio and text with a hypothesis, an NLI label, and English glosses. The author assigned labels, so the dataset is an exploratory resource rather than a mature benchmark. The NLI experiments use the reference text; the audio is evaluated separately. XLM-RoBERTa baselines with five-fold item-level cross-validation reach 44.7% on Pidgin and 46.2% on Camfranglais (chance 33.3%). Still, neither is statistically distinguishable from hypothesis-only input, so hypothesis wording may account for much of the accuracy. Under disjoint-item cross-variety transfer, where a test item's counterpart is never seen in training, accuracy is 40.1% (Pidgin to Camfranglais) and 45.6% (Camfranglais to Pidgin). A counterpart-leak audit raises this to 60-64%, illustrating how counterpart leakage can overstate transfer. Zero-shot Whisper transcription of the recordings performs poorly: the best word error rates are 66.6% for Pidgin and 45.5% for Camfranglais, and with automatic language identification, Whisper Large-v3 labels 93 of 114 Pidgin recordings as Yoruba or Swahili. Together, the results suggest that such resources need disjoint-item evaluation and hypothesis-only controls, and that speech recognition must be adapted to these varieties before spoken NLI can be tested end to end.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.17573
