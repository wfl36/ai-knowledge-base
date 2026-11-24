# Memorization and Generalization in Generative Models: A Perspective From Energy-based Modeling and Associative Memory

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-24  
**来源：** rss  

## 项目描述
arXiv:2611.26797v1 Announce Type: new Abstract: Generative models now write working code, produce realistic images, and hold long conversations, yet the mechanisms behind their intelligence still evade our understanding. This thesis explores that puzzle through Associative Memory (AM), in which patterns are stored as energy minima and retrieved through attractor dynamics. Beyond their capacity, AMs form new minima known as spurious states, long regarded as a failure of memory. We argue that this failure is where creativity begins, and that memorization and generalization can coexist as outcomes of one retrieval process. First, we show that diffusion models behave as AMs. With little data, a diffusion model forms a distinct basin of attraction around each training sample. As the data grows, these basins shrink, and spurious states emerge as attractors that blend stored samples yet match none of them. They are the first signs of generative capability. We characterize this transition by measuring the volume, energy, and curvature of these basins across datasets and architectures, including Stable Diffusion. We then turn to language and move beyond the energy-based view of AM. We show that uniform-state discrete diffusion models are AMs capable of retrieving unseen data, with basins of attraction that arise from conditional likelihood maximization alone. As the training set grows, basins around training examples contract while basins around unseen examples expand, until corrupted test sentences are recovered as reliably as training ones. Conditional entropy exposes this coexistence within a single sequence and cheaply diagnoses where a model lies along the transition. Together, these results suggest that AM is a general principle defined by basins of attraction, and that memorization and generalization can coexist within one model. AM thus offers a framework for asking when a generative model recalls and when it creates.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.26797
