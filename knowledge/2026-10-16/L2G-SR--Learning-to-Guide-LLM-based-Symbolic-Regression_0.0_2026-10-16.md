# L2G-SR: Learning to Guide LLM-based Symbolic Regression

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-16  
**来源：** rss  

## 项目描述
arXiv:2610.20685v1 Announce Type: new Abstract: Symbolic regression searches for an equation that explains observed data. Numerical error is commonly used to guide the search, but it alone can favor an accurate surrogate over a candidate with the right structure. We propose L2G-SR, a framework for LLM-based symbolic regression that guides search with a learned structural verifier. We construct structural supervision signal using tree edit distance (TED), accounting for commutative operators and alternative expression forms. A verifier first aligns numerical observations with the formulas, then learns to score a candidate's structural similarity to the target formula. At search time, the target formula is hidden and the verifier complements numerical error in parent selection. An analyst then uses verifier feedback and diagnostic tools to propose revisions, which a generator converts into refined expressions. On LLM-SRBench, L2G-SR achieves state-of-the-art numerical fit, equation level accuracy and TED across the evaluated LLM backbones and domains. L2G-SR demonstrates the value of learned structural guidance for LLM-based symbolic regression.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.20685
