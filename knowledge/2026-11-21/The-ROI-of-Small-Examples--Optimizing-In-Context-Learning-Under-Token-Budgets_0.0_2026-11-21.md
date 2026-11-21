# The ROI of Small Examples: Optimizing In-Context Learning Under Token Budgets

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-21  
**来源：** rss  

## 项目描述
arXiv:2611.24971v1 Announce Type: new Abstract: In-context learning (ICL) improves large language model performance at inference time without updating model parameters. However, these gains are not free: in practical deployments, longer prompts directly increase inference cost and latency. Under a fixed token budget, prompt construction therefore becomes a resource-allocation problem. While prior work has often focused on how many examples to include in ICL, we study the complementary question of whether the available budget is better spent on a few long demonstrations or on a larger number of shorter ones. We study this aspect in question answering (QA), by organizing candidate demonstrations into length-based bins and constructing prompts from examples within the same length range under fixed budgets. Experiments on two QA benchmarks (\textit{Beat the AI} and \textit{Natural Questions}), using six instruction-tuned LLMs, show that shorter demonstrations are generally the most effective use of prompt space. This effect is especially strong on \textit{Beat the AI}, and remains visible on NQ, although gains are smaller and saturate earlier in the long-context setting. An additional natural language inference experiment on ANLI R3 finds that one of the two shorter bins performs best for five of six models, although longer demonstrations remain competitive. Overall, our results highlight demonstration granularity as an important factor in prompt design.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.24971
