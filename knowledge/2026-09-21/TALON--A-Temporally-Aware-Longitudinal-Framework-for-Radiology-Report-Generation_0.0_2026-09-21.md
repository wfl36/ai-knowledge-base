# TALON: A Temporally Aware Longitudinal Framework for Radiology Report Generation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-21  
**来源：** rss  

## 项目描述
arXiv:2609.20826v1 Announce Type: new Abstract: Current radiology report generation (RRG) models usually produce descriptive reports based on a single examination or only the most recent prior examination, limiting their ability to perform accurate and meaningful longitudinal comparisons and detect subtle interval changes. Although recent approaches have begun to incorporate multiple prior examinations, they usually aggregate a fixed-length history without explicitly modeling the role-dependent relevance of each prior examination before fusion. To address this, we propose TALON, a Temporally Aware LONgitudinal RRG framework that adaptively integrates variable-length patient histories. The underlying Dual-Channel Temporal Fusion Module (DCTFM) compares the current examination with each prior examination through complementary similarity and change channels to capture persistent findings and interval changes, respectively. The specially designed channel-specific attention estimates the relevance of each prior examination, while a learned prior-specific gate adaptively integrates informative longitudinal evidence and suppresses redundancy. Experiments on MIMIC-CXR show that TALON outperforms the current state-of-the-art method on various clinical efficacy and graph-based metrics. When more prior examinations become available, TALON's performance on these metrics improves even further, emphasizing the strength of TALON's DCTFM in modeling longitudinal RRG across longer and more complex patient histories than existing approaches.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.20826
