# Grab a Coffee: Future-Aware Guidance for Discrete Diffusion with Compiled Objectives

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-30  
**来源：** rss  

## 项目描述
arXiv:2609.35924v1 Announce Type: new Abstract: Discrete diffusion models generate sequences by iteratively resolving multiple tokens in parallel, offering a flexible alternative to left-to-right generation. However, guiding this process with a sequence-level objective is difficult because the value of one unresolved token depends on the other tokens with which it can form a high-reward sequence. Enumerating all such completions makes the whole guidance computation grow exponentially with the number of unresolved positions. We introduce COFFEE, a plug-and-play framework that avoids this enumeration by separating sequence dependence from the objective. At each diffusion step, a target-free carrier absorbs the marginal token distributions predicted by the denoiser to construct a joint model over the unresolved tokens, while a compiled finite-state model records how their combinations affect the sequence-level preference. Pairing their states allows COFFEE to transfer global preferences to unresolved positions and sample a clean reconstruction without retraining the diffusion model. The same framework supports explicit hard constraints and learned soft objectives. We evaluate COFFEE across multiple symbolic, language, and biological benchmarks, where it achieves strong control results with task-dependent quality and diversity trade-offs. By making objectives available to inference rather than only evaluation, COFFEE brings joint conditioning, completion-weighted guidance, and optimization-based constraints into pretrained neural generation, showing the potential of neural-symbolic methods in diffusion guidance.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.35924
