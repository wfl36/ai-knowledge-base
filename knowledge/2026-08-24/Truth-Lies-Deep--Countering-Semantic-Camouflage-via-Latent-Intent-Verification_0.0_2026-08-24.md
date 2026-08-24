# Truth Lies Deep: Countering Semantic Camouflage via Latent Intent Verification

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-24  
**来源：** rss  

## 项目描述
arXiv:2608.20378v1 Announce Type: new Abstract: Safety alignment in Large Language Models (LLMs) is often superficial, relying on refusal mechanisms that trigger only at the final stages of generation without erasing the foundational knowledge of harmful concepts acquired during pretraining. This study demonstrates that this architectural disconnect leaves models vulnerable to Semantic Camouflage -- adversarial attacks that wrap harmful intent in benign narrative contexts (e.g., creative writing), effectively bypassing standard input and output guardrails. By analyzing the latent activation trajectories of three distinct Small Language Model (SLM) families (Phi-3, Qwen2.5, and Gemma-2b) under adversarial stress, this research identifies a universal ``Intent Horizon'' -- a critical depth (typically 15--20\% of total layers) where the model's distinct, pre-trained representation of harmful intent collapses as it contextualizes the query into a ``safe'' narrative. Results indicate that while late-layer representations of camouflaged attacks are mathematically indistinguishable from safe queries (Detection Rate $< 20\%$), early-layer representations retain a distinct, detectable ``harm signature.'' Leveraging this insight, this paper proposes Latent Intent Verification (LIV), a lightweight probing defense. Experiments on the PKU-SafeRLHF dataset demonstrate that LIV outperforms standard guardrails by a margin of 20--50\% across all tested architectures, effectively neutralizing zero-day semantic attacks without requiring model retraining.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.20378
