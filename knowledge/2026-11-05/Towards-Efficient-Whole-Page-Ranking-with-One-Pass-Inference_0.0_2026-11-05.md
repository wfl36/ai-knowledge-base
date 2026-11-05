# Towards Efficient Whole Page Ranking with One-Pass Inference

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-05  
**来源：** rss  

## 项目描述
arXiv:2611.05542v1 Announce Type: new Abstract: Whole-page ranking jointly optimizes advertisements and organic content to balance business outcomes and user engagement under complex layout and business constraints. Existing non-autoregressive (NAR) approaches enable efficient page generation but typically score candidate items independently of previously selected items, limiting their ability to capture order-dependent interactions. Autoregressive (AR) methods address this limitation through sequential conditioning, but incur substantial inference overhead that challenges large-scale deployment. Bridging this quality-efficiency gap remains a challenge in industrial whole-page ranking. We propose Multi-Item Scoring (MIS), a prefix-aware NAR-style framework that incorporates sequential context into efficient multi-item scoring. MIS integrates global candidate interactions, localized prefix conditioning, and position-aware scoring within a shared representation architecture. By computing reusable representations once per request and performing lightweight prefix-conditioned scoring during constrained beam search, MIS captures important sequential dependencies without repeated full-model inference. Experiments on KuaiRand-1K and RL4RS demonstrate that MIS approaches the generation quality of an autoregressive CGA baseline while achieving 4.07x and 3.54x faster CPU decoding, respectively. In a randomized evaluation on a large-scale social-video platform, MIS improves the realization metric by 0.104% and watch time by 0.058%, while reducing ranking-service CPU consumption by 9.73%. These results demonstrate that prefix-aware multi-item scoring can narrow the quality gap between NAR and AR generation while retaining the efficiency required for industrial scalability.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.05542
