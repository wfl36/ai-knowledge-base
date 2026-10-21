# When Planning Problems Become Hard for LLMs: Separating Structural Complexity from Semantic Interpretability

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-21  
**来源：** rss  

## 项目描述
arXiv:2610.26964v1 Announce Type: new Abstract: Large language models (LLMs) struggle with classical planning, but benchmarks rarely distinguish structural difficulty from the difficulty of interpreting symbolic vocabulary. We examine seven STRIPS domains with BFS-optimal plan lengths. For predicting structural difficulty without solving an instance, the zero-training delete-relaxation heuristic $h_{\mathrm{add}}$ outperforms learned alternatives on held-out domains (mean Spearman $|\rho|=0.931$), including ridge regression ($0.707$), object count ($0.657$), and the episodic retrieval architecture ARC ($0.400$). ARC also fails to outperform a linear model using the same features. To isolate semantic effects, we progressively rename predicates while preserving states, transitions, and optimal plans. Valid LLM planning success drops from $67.5\%$ to $40.0\%$ between $0\%$ and $100\%$ renaming, while refusals remain at $0\%$. An LLM supplied with ARC's conditioning information predicts difficulty in context better than trained ARC (mean $|\rho|=0.826$). Hybrid routing between an LLM and a symbolic planner depends more on calibration to the target LLM's outcomes than on the structural score selected. Thus, established symbolic heuristics already estimate structural difficulty well; improving hybrid planning requires modeling LLM behavior sensitive to predicate semantics rather than developing more structural predictors.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.26964
