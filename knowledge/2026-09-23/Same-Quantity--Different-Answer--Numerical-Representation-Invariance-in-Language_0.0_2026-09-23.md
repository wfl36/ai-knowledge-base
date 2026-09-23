# Same Quantity, Different Answer: Numerical Representation Invariance in Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-23  
**来源：** rss  

## 项目描述
arXiv:2609.25009v1 Announce Type: new Abstract: Numerically equivalent word problems should yield the same canonical answer whether a quantity is written as a decimal, fraction, percentage, number word, scientific notation, or an exactly converted unit. We generate 3,600 exact-rational problems and 8,600 prompts spanning five identity-preserving transformation families, and evaluate five open-weight systems. After a fixed syntax audit that normalizes common answer forms without an LLM judge, canonical accuracy is 0.969-0.996, but orbit correctness falls to 0.848-0.981 and orbit invariance to 0.851-0.981; invariant-but-wrong orbits account for at most 0.003. Most of the broad strict-parser collapse arises because multiplication-form scientific notation lies outside the implemented number grammar, illustrating how evaluator interfaces can masquerade as reasoning failures. A distinct semantic pathology remains: Mistral Small 4 scores 0.699 on unit-converted inputs and produces 265 errors differing from the label by exact powers of ten. In a separate 9,000-call experiment that allocates equal calls to the compared arms, representation consensus does not outperform paraphrase consensus on a low-error subset and produces substantially more false alarms. The accompanying ancillary archive contains the frozen benchmark, evaluation and audit records, consensus raw responses, manifests, analysis code, and a one-command paper build.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.25009
