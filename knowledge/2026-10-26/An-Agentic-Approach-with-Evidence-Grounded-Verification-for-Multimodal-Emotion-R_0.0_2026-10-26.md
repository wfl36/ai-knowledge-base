# An Agentic Approach with Evidence-Grounded Verification for Multimodal Emotion Reasoning in Conversation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-26  
**来源：** rss  

## 项目描述
arXiv:2610.31685v1 Announce Type: new Abstract: LLM-based multimodal emotion reasoning systems perform well on standard benchmarks, but improving them through instruction tuning can be computationally expensive. Agentic pipelines built from frozen models avoid this cost, but introduce a different challenge: when a prediction is wrong, the system must identify which agent or stage caused the error. We address this problem with an agentic framework for traceable multimodal emotion reasoning and prompt-space adaptation. Modality-specific perception agents analyze visual, acoustic, and lexical inputs and post evidence-cited observations to a shared board. An integration agent combines these observations with retrieved multimodal examples to produce an emotion description, label set, and supporting citations, while an MLLM critic can request one revision before the output is finalized. For incorrect predictions, a separate evidence-grounded verification stage applies deterministic checks to verify that cited evidence and references are valid, and an entailment check to determine whether the final claims are supported by that evidence. Detected failures are then grouped by the responsible component and failure type, converted into targeted prompt patches, and accepted only after validation on a held-out set. This adapts the agent prompts without updating model weights. On the MER2025 dataset, targeted prompt adaptation outperforms the frozen static pipeline on all four MLLMs, ranging from 2B to 38B parameters, and matches or outperforms undifferentiated reflection baselines on each of them: VideoLLaMA3-2B, Phi-3.5-vision-instruct, Qwen2.5-VL-7B-Instruct, and InternVL2.5-38B. It improves F-score by 0.6--2.2 points depending on the backbone, including an increase from 52.3 to 54.5 on Qwen2.5-VL-7B.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.31685
