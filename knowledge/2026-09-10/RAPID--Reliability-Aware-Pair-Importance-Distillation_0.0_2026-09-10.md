# RAPID: Reliability-Aware Pair Importance Distillation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-10  
**来源：** rss  

## 项目描述
arXiv:2609.05481v1 Announce Type: new Abstract: Inter example relational distillation transfers a teacher's representation geometry by matching relations among examples within a mini batch. Computing all pairs has quadratic complexity in the batch size, whereas uniform subsampling may use a limited relation budget inefficiently. We introduce Reliability Aware Pair Importance Distillation, or RAPID, which separates a reliability gated relational target from a full support adaptive pair proposal. Reliability determines which teacher relations are emphasized, while calibrated teacher entropy and detached student-teacher residuals determine which relations are evaluated. Exact inverse proposal correction makes the loss and gradient estimators conditionally unbiased with respect to the gated mini batch target. We evaluate RAPID in two text classification settings: AG News with BERT-to-DistilBERT distillation using three paired seeds and a relation budget of 256, and SST-2 with DistilBERT to DistilBERT distillation using three paired seeds and a relation budget of 64. Reliability gated relational distillation achieves the highest observed mean student accuracy on both datasets: 94.285 plus or minus 0.054 percent on AG News and 88.800 plus or minus 0.532 percent on SST-2. RAPID ranks second, achieving 94.241 plus or minus 0.025 percent and 88.685 plus or minus 0.462 percent, respectively, compared with 94.154 plus or minus 0.124 percent and 87.271 plus or minus 0.162 percent for the cross entropy baseline. Pilot evaluations are counted toward the same total budget as the main relation evaluations. Across both settings, the gated target yields the highest mean accuracy, while the adaptive proposal remains within seed-level variation. These results support the modular view that target reliability and evaluation priority are separable design dimensions.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.05481
