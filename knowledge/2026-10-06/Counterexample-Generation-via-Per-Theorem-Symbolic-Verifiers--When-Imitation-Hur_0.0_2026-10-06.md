# Counterexample Generation via Per-Theorem Symbolic Verifiers: When Imitation Hurts and Reinforcement Repairs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-06  
**来源：** rss  

## 项目描述
arXiv:2610.02444v1 Announce Type: new Abstract: Large language models often solve a theorem forward yet fail to disprove a closely related false one: a falsification gap that supervised fine-tuning does not close and can actively worsen. We frame counterexample generation as constrained witness emission against a deterministic per-theorem Python verifier, and release SymCE, a corpus of 4,707 false undergraduate-algebra and real-analysis conjectures, each paired with executable verifiers. The verifier also serves as the reward function, making SymCE a training environment. Training Qwen3-4B with SFT followed by GRPO under this oracle reveals an imitation trap: counterexample-only SFT collapses true-theorem recognition from 0.27 to 0.00, while RLVR with a sparse outcome-only reward repairs this and exceeds the base, to 0.66. The collapse replicates across four seeds and on Gemma-3-4B. Sparse and dense rewards yield statistically indistinguishable in-domain success yet diverge by 33 points on a held-out calibration probe, a dissociation we trace to the partial-credit term. Our 4B model outperforms every evaluated 7B open-weights math specialist, remains competitive with six frontier commercial APIs, and transfers under unchanged prompting to GSM8K, MATH-500 and MMLU-college-math. A human audit of 177 verifier decisions finds 97.7% accuracy. Code, data, verifier modules and annotations: https://github.com/ce-rlvr/SymCE.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.02444
