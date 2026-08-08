# SemiAdapt-Instruct: Extensible Instruction Tuning via Latent Domain-Specialised Adapters

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-08  
**来源：** rss  

## 项目描述
arXiv:2608.05161v1 Announce Type: new Abstract: Instruction-tuned LLMs are deployed into environments where domains evolve, yet extending a fine-tuned model's capabilities without full retraining remains an unsolved practical challenge. We present SemiAdapt-Instruct, a modular framework that discovers latent instruction domains, trains per-domain LoRA adapters in parallel, and performs parameter-free routing, incorporating new domains via single-adapter training without modifying existing components. SemiAdapt-Instruct outperforms full model fine-tuning across all configurations on both ROUGE-L and LLM-as-a-judge evaluation, while matching single LoRA fine-tuning and delivering extensibility that monolithic approaches cannot provide. We empirically demonstrate this extensibility by showing that updating a single adapter with new domain data outperforms all monolithic baselines. Our study also finds that independent discovery methods converge on the same specialisation-friendly domains. These findings demonstrate that decomposing heterogeneous instruction data into latent domains enables extensible NLP systems where evolving domains require only targeted single-adapter updates, eliminating the need for full model retraining.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.05161
