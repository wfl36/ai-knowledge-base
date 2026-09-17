# Physics-Constrained Digital Twins for Sensor Integrity in Urban Pedestrian Flow: Detecting Stealthy False Data Injection with Conformal Guarantees

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-17  
**来源：** rss  

## 项目描述
arXiv:2609.17635v1 Announce Type: new Abstract: City pedestrian counting systems now feed economic indicators, planning decisions and safety operations, yet the twins built on top of them treat the incoming stream as ground truth. We study what happens when it is not. We formalise stealthy false data injection for city-scale pedestrian sensing, where the map from latent flow to observation is far more rank deficient than in the power and water networks for which stealth has been characterised. Our twin estimates directed flows on the pedestrian street graph, assimilates counts through a learned graph-localised gain, and is trained against a flow conservation residual that couples metered and unmetered segments. Detection combines the innovation with that residual, and the alarm threshold is set by adaptive conformal calibration rather than by hand. To measure what the physics buys, we define the attack margin, the relative reduction in worst-case corruption of the estimated flow field, achieved against a white-box adversary that optimises directly through the twin. On six years of Melbourne data the margin reaches 0.54 against a single compromised device and falls to 0.19 when a third of the fleet is compromised, on a network where only 1.18 per cent of walkable segments are metered. Replacing the street graph by a distance graph collapses it to 0.09, which shows that the gain comes from the conservation law rather than from locality.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.17635
