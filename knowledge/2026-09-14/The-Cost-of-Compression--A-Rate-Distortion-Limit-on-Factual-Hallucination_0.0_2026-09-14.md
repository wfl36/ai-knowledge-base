# The Cost of Compression: A Rate-Distortion Limit on Factual Hallucination

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-14  
**来源：** rss  

## 项目描述
arXiv:2609.12111v1 Announce Type: new Abstract: Factual hallucination in closed-book question answering is often treated as a coverage problem: a model fails because the relevant fact is absent from its internal memory. This view misses a second source of error. Even when a fact has been observed, finite memory may force it to be stored only approximately. We study this effect through a simple coverage--compression model of factual recall. We consider an unstructured question-answering task with $N$ possible queries and $K$ possible answers. A learner observes $M$ training facts, compresses them into at most $B$ bits, and answers uniformly drawn test queries without retrieval. For a uniformly random ground-truth mapping, we prove $\mathcal{E} \geq \frac{M}{N}\delta^\star\!\left(\frac{B}{M}\right) + \left(1-\frac{M}{N}\right)\left(1-\frac{1}{K}\right)$, where $\delta^\star(r)$ is the inverse rate-distortion function of a uniform $K$-ary source under zero-one loss. The two terms separate compression distortion on observed facts from missing coverage on unobserved facts. The bound gives a compact way to reason about selective memory, forced compression, structure, retrieval, abstention, and long-context organization. We study the predicted signatures with theory-implied simulations and controlled fact-injection probes in modern language models that vary fact load and effective trainable memory. The result is not a complete theory of hallucination, but an information-theoretic account of a separable failure mode: lossy recall of observed facts under finite memory.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.12111
