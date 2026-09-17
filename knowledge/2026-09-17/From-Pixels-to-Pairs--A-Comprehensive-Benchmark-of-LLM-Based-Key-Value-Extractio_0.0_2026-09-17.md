# From Pixels to Pairs: A Comprehensive Benchmark of LLM-Based Key-Value Extraction in Noisy Document Settings

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-17  
**来源：** rss  

## 项目描述
arXiv:2609.17538v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used for structured information extraction from documents, yet their behavior under realistic OCR noise remains poorly understood. We present a systematic benchmark of open-source instruction-tuned LLMs for key-value pair (KVP) extraction under both clean-text and noisy OCR conditions. We evaluate representative decoder-only models (Gemma, Mistral, Qwen2.5, LLaMA 3, and DeepSeek) on the FUNSD, CORD, and SROIE benchmarks using both Gold-text annotations and OCR outputs from PaddleOCR, EasyOCR, and Tesseract. A unified evaluation protocol isolates the effects of input quality, model design, and prompting under consistent conditions. The results show that modern LLMs act as strong semantic extractors when high-quality text is available, in some cases approaching supervised layout-aware systems. Under OCR noise, however, performance degrades substantially and performance gaps between models narrow as input corruption increases. Across all datasets, extraction performance is governed by two factors: semantic reasoning over text and preservation of textual fidelity under OCR noise. While larger models improve results on clean text, these gains diminish under noisy inputs, where OCR quality becomes the dominant factor. We also identify recurring failure modes, including key-value misalignment, hallucination, and numeric corruption. Our findings highlight the gap between clean-text evaluation and real-world deployment, emphasizing the need to jointly improve OCR quality, structural reasoning, and LLM-based semantic modeling.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.17538
