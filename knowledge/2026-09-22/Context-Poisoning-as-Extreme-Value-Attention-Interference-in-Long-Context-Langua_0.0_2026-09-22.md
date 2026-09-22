# Context Poisoning as Extreme-Value Attention Interference in Long-Context Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-22  
**来源：** rss  

## 项目描述
arXiv:2609.22101v1 Announce Type: new Abstract: Large language models can process increasingly long prompts, yet their ability to locate and use decisive evidence may degrade as irrelevant or confusable context is added. We formulate this phenomenon, which we call context poisoning, as extreme-value interference in attention: the decisive-evidence score is upper-bounded, while the maximum score among effective distractors grows with their number. Under a softmax retrieval abstraction, we derive a finite-sample upper bound showing that maintaining a fixed accuracy target above base rate requires the evidence margin to scale as $\Omega(\sqrt{\log N})$, where N denotes the effective distractor count rather than necessarily the raw context length. The analysis connects long-context degradation to score aliasing, positional aliasing, and softmax dilution. Controlled experiments show that retrieval accuracy decreases as total context grows in the presence of embedded hard negatives, that the same-format condition produces the largest observed accuracy drop among the tested distractor constructions at fixed context length, and that retrieval gating can improve evidence use while its net benefit depends on preserving evidence recall. These results motivate evidence bottlenecks, alias-resistant representations, retrieve-then-reason architectures, verifier-mediated memory, and contrastive anti-poison training.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.22101
