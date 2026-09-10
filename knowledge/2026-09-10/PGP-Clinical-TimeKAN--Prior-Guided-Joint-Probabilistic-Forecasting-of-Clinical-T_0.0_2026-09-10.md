# PGP-Clinical-TimeKAN: Prior-Guided Joint Probabilistic Forecasting of Clinical Trajectories

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-10  
**来源：** rss  

## 项目描述
arXiv:2609.05488v1 Announce Type: new Abstract: Clinical deterioration unfolds through coupled, partially observed trajectories, not a single diagnostic label. We introduce PGP-Clinical-TimeKAN, a trajectory-first framework for joint probabilistic forecasting of multivariate physiology. It combines missingness-aware temporal encoders, a soft organ-system prior, patient-specific relations, nonlinear Kolmogorov-Arnold messages, and a low-rank multivariate Student-t head. We evaluate 24-hour histories and six-hour forecasts on a frozen MIMIC-IV-derived cohort of 6,882 patients and 54,694 windows. Across five seeds and 13 models, PGP-Clinical-TimeKAN obtains the second-lowest normalized MAE (0.37727 +/- 0.00029) and the lowest RMSE (0.52656 +/- 0.00034). It reduces MAE by 0.52% relative to deterministic TimeKAN. For probabilistic forecasting, it reaches a marginal NLL of 0.66380 and a CRPS of 0.27301. Empirical coverage is 0.533, 0.831, and 0.958 for nominal 50%, 80%, and 95% intervals. Removing relational structure causes the largest ablation loss. Increasing covariance rank improves joint likelihood but has little effect on point accuracy. A trajectory-derived risk score remains weaker than a dedicated GRU-D classifier (AUROC 0.603 versus 0.650), which limits the present clinical claim. Joint trajectory forecasting therefore provides an inspectable intermediate task, but accurate physiology forecasts alone do not ensure a calibrated event detector.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.05488
