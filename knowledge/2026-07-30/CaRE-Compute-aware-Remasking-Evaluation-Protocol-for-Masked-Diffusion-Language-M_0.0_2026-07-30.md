# CaRE Compute-aware Remasking Evaluation Protocol for Masked Diffusion Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-30  
**来源：** rss  

## 项目描述
arXiv:2607.24763v1 Announce Type: new Abstract: Masked diffusion language models (MDLMs) are advancing rapidly, yet the evaluation standards needed to reliably interpret their progress have not kept pace. Despite MDLMs becoming competitive with autoregressive language models, seven recent remasking papers evaluate under incompatible settings, varying nominal step counts, metrics, and sampling temperatures without jointly controlling these factors, rendering their strategy rankings largely incomparable and leaving open whether reported gains reflect algorithmic improvements or evaluation artifacts. We present CaRE, a compute-aware evaluation framework that audits MDLM remasking strategies by standardizing actual number of function evaluations (NFE), enforcing multi-metric reporting, and explicitly controlling stochasticity. Applied to 7 remasking strategies across LLaDA-8B-Base and Dream-7B-Base at 4 stochasticity levels and 3 step budgets on OpenWebText and LM1B, CaRE reveals that: (i) temperature explains the majority of MAUVE variance, (ii) compute-matched comparisons reverse several published strategy rankings, and (iii) informed remasking and stochastic unmasking are in tension, with high-entropy remasking reducing MAUVE by 0.296 at 256 steps at unmask_temp=0.25 (p=0.020). A CaRE leaderboard covering 12 open-weight MDLMs (150M to 8B parameters) shows that this interaction direction holds across architectures and scales. These findings demonstrate that current MDLM evaluations can systematically conflate algorithmic improvements with hidden choices of compute and stochasticity. We release the evaluation protocol, implementation, and leaderboard to ensure future remasking claims are reproducible and comparable.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.24763
