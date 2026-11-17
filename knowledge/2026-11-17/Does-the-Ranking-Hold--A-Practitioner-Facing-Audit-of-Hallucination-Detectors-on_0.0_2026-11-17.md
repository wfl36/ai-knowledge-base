# Does the Ranking Hold? A Practitioner-Facing Audit of Hallucination Detectors on Small, Quantized, On-Device LLMs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-17  
**来源：** rss  

## 项目描述
arXiv:2611.17339v1 Announce Type: new Abstract: Hallucination detection for large language models is dominated by methods evaluated on 7B-70B research models with abundant sampling budgets and exact-match or ROUGE correctness labels. The small models practitioners actually ship on-device, Phi-3-mini, Llama-3.2-3B-Instruct, Qwen2.5-3B-Instruct, and Gemma-2-2B-Instruct, typically at 4-bit precision, sit outside this evidence base. We present a reproducible one-GPU audit of four detectors spanning three paradigms: length-normalized token-margin calibration, a lexical n-gram baseline, and two sampling-based consistency methods (semantic entropy and SelfCheckGPT-NLI) on two small open instruction-tuned models (Llama-3.2-3B-Instruct and Qwen2.5-3B-Instruct) loaded at 4-bit NF4 quantization on a single Colab T4 GPU, evaluated on closed-book TriviaQA. Cross-model ranking transfer is poor: Spearman rho is -0.80 and Kendall tau-b is -0.667, meaning the detector ranking actively inverts between the two models, and the cheap lexical baseline is statistically indistinguishable from the sampling-based consistency detectors on both models under bootstrap 95 percent confidence intervals. As a second, methodological contribution, we show that the standard token-overlap-to-multiple-choice correctness labeler for TruthfulQA-Generation produces near-chance AUROC (0.46-0.59) for all four detectors on both models, a labeler failure, not a detector failure, since the same detectors reach 0.69-0.89 AUROC on TriviaQA under the identical pipeline. We release the harness, prompts, and per-item scores and frame the detector choice explicitly as a fairness-of-error-rates allocation problem for practitioners deploying on resource-constrained, on-device hardware.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.17339
