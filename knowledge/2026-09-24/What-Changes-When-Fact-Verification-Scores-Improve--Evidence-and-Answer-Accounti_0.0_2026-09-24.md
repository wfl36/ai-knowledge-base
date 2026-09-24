# What Changes When Fact-Verification Scores Improve? Evidence and Answer Accounting Across Trained Verifiers and LLMs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-24  
**来源：** rss  

## 项目描述
arXiv:2609.27064v1 Announce Type: new Abstract: A joint fact-verification score assesses answers and submitted evidence together. When the score improves, how much of the gain remains if the answers are held fixed? On FEVEROUS, strict score is the percentage of claims with a correct answer and a complete annotated evidence group in the submitted evidence. Across four trained DeBERTa checkpoints and 7,890 claims, replacing DCUF evidence with UnifEE evidence raises strict score by 9.61 percentage points, compared with 1.96 percentage points in answer accuracy. The paired 95% interval for the strict-score gain is [8.77, 10.43], conditional on these checkpoints. Replacing only the evidence passed to the scorer accounts for 7.92 or 9.08 percentage points when we retain the answers generated from DCUF or UnifEE evidence, respectively. To examine how this evidence gain depends on evaluation choices, we generate 470,400 responses from two 8B LLMs on FEVER, FEVEROUS, and SciFact under two answer formats and two context budgets. Increasing context from 256 to 2,048 tokens raises the fixed-answer evidence gain on FEVEROUS by 3.84 and 3.10 percentage points for Qwen and Llama, respectively. The effects fall short of the prespecified cross-dataset criterion, while some intervals extend beyond the two-point small-effect bound. Post-hoc analyses quantify changes in answers and submitted evidence, and show when aggregate accuracy and evidence-coverage rates miss the claim-level pattern. The four answer-evidence score combinations reveal changes that endpoint and aggregate metrics leave unresolved.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.27064
