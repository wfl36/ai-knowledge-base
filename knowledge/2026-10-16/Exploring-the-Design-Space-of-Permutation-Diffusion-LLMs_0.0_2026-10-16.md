# Exploring the Design Space of Permutation Diffusion LLMs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-16  
**来源：** rss  

## 项目描述
arXiv:2610.20635v1 Announce Type: new Abstract: Permutation generation with language models requires both text-conditioned ranking and a global one-to-one assignment between candidates and output positions. We study this problem through three diffusion-LLM parameterizations: hard-assignment prediction over shuffled candidate-index sequences, soft-assignment prediction over doubly stochastic matrices, and direct ordering-score prediction followed by sorting. The three families place permutation constraints at different stages of prediction and decoding and therefore support different training objectives and sampling procedures. We evaluate these designs on recommendation reranking across three Amazon domains with candidate sets of size 10 and 20. At one function evaluation, the hard- and soft-assignment variants achieve Recall@1 comparable to a constrained masked-diffusion baseline, whereas direct ordering-score prediction guarantees valid permutations without Hungarian assignment or Sinkhorn normalization. Additional function evaluations do not consistently improve ranking quality, and their effect depends strongly on the state representation and training objective. These results show that corruption, prediction parameterization, objective, and decoder should be designed jointly for permutation diffusion with language-model denoisers.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.20635
