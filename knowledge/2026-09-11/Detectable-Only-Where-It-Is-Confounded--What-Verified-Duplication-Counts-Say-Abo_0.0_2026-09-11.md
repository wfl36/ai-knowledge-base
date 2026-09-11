# Detectable Only Where It Is Confounded: What Verified Duplication Counts Say About Membership Evidence in Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-11  
**来源：** rss  

## 项目描述
arXiv:2609.10830v1 Announce Type: new Abstract: When a language model finds a sentence unusually cheap to predict, it is tempting to conclude that the sentence was in its training data. Almost every published test of that inference has had to guess which sentences were in the training data, the members, and which were not. This paper removes the guessing. Two model families, OLMo-2 and Pythia, publish their pretraining corpora, and a public index over those corpora returns the exact number of times any sentence appeared in each. Those counts make three questions answerable directly. The answers form a pincer, closing from two sides. At the duplication levels ordinary text actually has, five models from 1B to 13B parameters carry at most a faint trace of their own exposure. We measure that trace with a design that reads the same sentence through two models, which cancels fluency and quality by construction, and it comes to a rank correlation near -0.08, where -1 would be a perfect relation and 0 none. Where the trace does become strong, above roughly a thousand copies, the two corpora agree on which sentences those are, because they are the famous ones, so exposure can no longer be told apart from fame. Two further measurements show how apparent membership signal gets manufactured. A common way to build a non-member is to change one word of a member. The model does prefer the original, but the gap is the same whether the original appeared once or a hundred times, so what the model is rewarding is the author's word choice, not memory. Above a thousand copies the gap grows with model size on the twelve sentences we can test there, at the same boundary where the pincer closes. And swapping the controls for sentences that differ from the members in register moves a detector from 0.83 to 0.94 AUC, on a scale where 0.5 is a coin flip and 1.0 is perfect separation. We release the sentence banks, counts, and code.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.10830
