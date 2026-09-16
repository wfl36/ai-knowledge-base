# Latent Undertow: How Ordinary Typos Break Probes

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-16  
**来源：** rss  

## 项目描述
arXiv:2609.15994v1 Announce Type: new Abstract: LLMs handle ordinary typing variation fluently: a typo or missing punctuation leaves both user intent and the model's response substantively unchanged. Yet probes that detect malicious prompts by reading the model's hidden states tell a different story: the same edit rotates the readout vector by 43--56 at the perturbed token, decaying below 15% within ~10 downstream tokens. Stacking ~3 common typos per message cuts a single-position prompt-injection probe's TPR@FPR$=1% by 12.0pp, a gap recalibration alone cannot close. Multi-position aggregation cures localized perturbations (<= 0.5 loss) but only attenuates distributed ones, where even attention- and max-based aggregators still drop ~3.8pp. For single-position probes, we introduce a KV-cache fork: a short fixed suffix appended after the user message lets the probe read a few tokens downstream of the perturbation, exploiting its rapid spatial decay. This closes 95% of the gap (-0.6pp residual) -- an order of magnitude better than perturbation-augmented training (-3.7pp). The rotation-and-decay geometry replicates on Llama-3.1-8B, Qwen3-8B, and Gemma-4-E4B; probe evaluation is on Llama-3.1-8B. Code: https://github.com/eladd-ai/latent-undertow

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.15994
