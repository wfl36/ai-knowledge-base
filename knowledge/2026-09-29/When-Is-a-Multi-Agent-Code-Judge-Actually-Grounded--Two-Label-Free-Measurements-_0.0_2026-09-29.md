# When Is a Multi-Agent Code Judge Actually Grounded? Two Label-Free Measurements, and a Judge That Declines to Guess

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-29  
**来源：** rss  

## 项目描述
arXiv:2609.30328v1 Announce Type: new Abstract: When one language model judges whether another's code is correct, it does not report the absence of evidence. It returns a confident verdict with reasoning attached, indistinguishable from a verdict it had grounds for. Multi-agent verification, which decomposes a judgment into checkable claims and verifies each against evidence, is a promising response and works well when the evidence is a set of retrieved documents. We argue such methods require two things of their evidence: it must be independent of the answer under review, and it must differ between the two candidates being compared. The second condition holds automatically with retrieved documents and stops holding in code judging. Running MARCH, a published framework unmodified over 80 condition-by-cell measurements on two code judging benchmarks, we find it declares both solutions equally good on 78 to 95% of comparisons, reaching 4.4% accuracy where the same model asked directly reaches 43.7%. Neither easier problems nor a larger judge changes this. Two measurements taken from the pipeline's own logs explain it without needing labels. Gating on one of them, the pipeline declines the comparisons it cannot make and raises its accuracy from 20.7 to 36.9% while still answering half of all comparisons. The contribution is not a more accurate judge, but a label-free way to tell when a judge has no basis for its answer.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.30328
