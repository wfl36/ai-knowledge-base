# MedJev: Evaluating Zero-Shot System-One Decision Making in Medicine

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-28  
**来源：** rss  

## 项目描述
arXiv:2610.36006v1 Announce Type: new Abstract: System One decision models such as Jev answer structured questions in a single forward pass without generating text, offering fast and computationally efficient clinical decision support. We evaluate MedJev, an open System One model that runs locally on a laptop, across ten medical benchmarks spanning medical knowledge, diagnosis, and patient level prediction using MIMIC IV and MIMIC IV ED. We compare MedJev against zero shot LLM baselines, published GPT results, and supervised models. MedJev achieves accuracies of 72.5 percent on MedQA, 75.4 percent on USMLE, and 80.1 percent on NEJM, approaching published GPT 4 performance while maintaining well calibrated confidence estimates (ECE 0.028 to 0.063). On patient level tasks, MedJev achieves an AUROC of 0.926 for In Hospital Mortality, exceeding XGBoost (0.902), but underperforms supervised models on operational outcomes such as ED Triage Admission (0.745 vs. 0.809). Patient level predictions also exhibit substantial miscalibration (In Hospital Mortality ECE 0.286). We introduce a lightweight, two parameter recalibration method that adapts predictions to local patient populations using 50 to 200 labeled examples, reducing ECE to 0.007. Our findings establish open System One models as a promising zero shot baseline for medical AI, combining competitive predictive performance with low computational cost and efficient local calibration. We release our code and evaluation harness to support future research.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.36006
