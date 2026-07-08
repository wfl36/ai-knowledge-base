# Revisiting the Relation Between Language Model Perplexity and ASR Word Error Rate for Modern End-to-End Speech Recognition

**评分：** 9.0  
**状态：** 正常  
**标签：** ASR, LLM, 语言模型, 困惑度, 论文  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05612v1 Announce Type: new Abstract: Language model (LM) perplexity (PPL) has historically been used as a proxy for automatic speech recognition (ASR) word error rate (WER), with prior work reporting an approximately linear relation in log-log space. Modern end-to-end ASR systems challenge this assumption because they already contain internal language modeling capacity, are often evaluated without external language models, and can now be combined with neural LMs and large language models (LLMs) through different recognition strategies. This paper revisits the relation between PPL and WER for modern ASR systems. We study whether external LMs still improve current end-to-end ASR systems, whether the PPL-WER relation remains linear in log-log space, how encoder context length affects this relation, and how LLM perplexities fit into the trend observed for standard neural LMs. We further investigate internal language modeling (ILM) in attention-based encoder-decoder systems and show that ILM subtraction changes the observed PPL-WER relation, indicating that the decoder's internal LM must be considered when interpreting the effect of external LM quality.

## 综合总结
本文由语音识别权威Hermann Ney团队撰写，重新审视了现代端到端ASR系统中语言模型困惑度(PPL)与词错率(WER)的经典关系。研究发现，由于E2E系统内部语言模型(ILM)的存在，传统对数-对数线性假设不再完全适用；特别是在引入LLM和外部LM融合时，ILM减法会显著改变PPL-WER关系。该成果对理解现代ASR机制及指导LLM与语音系统的融合具有重要理论和实践价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
重新审视了现代端到端ASR系统中语言模型困惑度(PPL)与词错率(WER)的关系。研究指出，由于E2E系统自带内部语言模型(ILM)能力，传统的对数-对数线性关系受到挑战。论文深入探讨了外部LM的有效性、编码器上下文长度的影响以及LLM的PPL表现，并重点论证了ILM减法会改变观察到的PPL-WER关系，揭示了在评估外部LM效果时必须考虑解码器内部LM的影响，具有深刻的理论洞见与严谨的论证。

### 实用性 (评分: 8.5/10)
对现代ASR系统的开发和优化具有直接指导意义。研究结论（特别是关于ILM减法的影响）能帮助工程师在将外部神经LM或LLM与E2E ASR融合（如shallow fusion）时，更准确地评估和选择语言模型，调整融合策略，从而有效降低WER，提升语音识别系统的性能。

### 社区活跃度 (评分: 9.5/10)
话题极具时效性，切中当前E2E ASR与LLM融合的技术热点。作者团队包含语音识别领域泰斗Hermann Ney，权威性极高。该研究对ASR领域长期依赖的经典PPL-WER线性假设提出了现代视角的修正，预计将对学术界和工业界产生重要影响。

## 项目链接
https://arxiv.org/abs/2607.05612
