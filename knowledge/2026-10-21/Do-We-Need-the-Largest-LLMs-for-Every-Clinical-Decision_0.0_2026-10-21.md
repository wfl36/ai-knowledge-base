# Do We Need the Largest LLMs for Every Clinical Decision?

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-21  
**来源：** rss  

## 项目描述
arXiv:2610.26937v1 Announce Type: new Abstract: Large clinical language models often require multi-GPU infrastructure, limiting local deployment. We introduce CERTA, a decision-level statistical certificate that determines when a quantized model may substitute for its native BF16 reference and escalates decisions that cannot be certified to it. Across eleven instruction-tuned models, both general-purpose and domain-adapted, from three families (7-72B), we evaluated 2,500 clinical-verification decisions from de-identified patient contexts (2,484 patients), with patient-disjoint calibration and testing. In the higher-power operational analysis, round-to-nearest 8-bit quantization at BF16 storage served 99.8-100% of held-out decisions across all eleven models; formal finite-sample guarantees were assessed separately using the exact split-sample procedure. In the same operational analysis, the class-conditional 4-bit frontier reduced the amortized, BF16-equivalent deployment cost to 25.8% and 27.3% of the BF16 reference for Qwen2.5-72B and HuatuoGPT-o1-72B, respectively, with measured peak memory of 43.0 and 42.7 GB, below the nominal capacity of a single 48 GB accelerator. Deployment on that specific hardware was not directly tested. Under the exact split-sample certificate, which also accounts for configuration selection, these costs were 26.7% and 27.9%. On external disease named-entity benchmarks against human annotations, the frontier-selected NF4 configurations had a mean absolute F1 change of 0.045 on both datasets, with substantial model-specific variation. CERTA converts compression from a fixed precision choice into a risk-controlled deployment policy for this verification task.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.26937
