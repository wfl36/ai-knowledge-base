# SpeakPay: Domain-Adaptive LoRA Fine-Tuning of Whisper for Low-Resource Nepali Financial Speech Recognition

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-03  
**来源：** rss  

## 项目描述
arXiv:2609.01737v1 Announce Type: new Abstract: Mobile payment applications in Nepal are graphically mediated and largely inaccessible to visually impaired users. This paper presents SpeakPay, a voice-first digital wallet, and documents the central technical contribution: a controlled study of domain adaptation for low-resource financial speech recognition. We introduce NepFinSpeech-403, a 403-utterance dataset of Nepali financial voice commands (send, load, and balance operations spanning 237 unique numerals), and fine-tune Whisper large-v2 with LoRA. On the held-out test set, the domain-adapted model reduces Word Error Rate from 129.95% (zero-shot baseline) to 42.58% --- a 67.2% relative reduction --- and improves Devanagari numeral recognition accuracy from 0.0% to 73.9%. We find that word-level metrics understate the practical task-level impact: domain adaptation improves the Transaction Success Rate from 1.67% to 33.33%, a roughly 20x gain. The improvement is consistent at the individual-utterance level (sign test, $p < 10^{-17}$) and across all command types. A data efficiency analysis shows that as few as 100 domain-specific utterances are sufficient to halve the zero-shot WER, with performance plateauing around 300 examples. Error analysis reveals systematic numeral confusion patterns (zero insertion/deletion, prefix hallucination) that account for the majority of remaining transaction failures. The trained system is deployed as a publicly accessible voice-first web application. All code, dataset, model weights, and this paper are released at https://github.com/subedibiraj/speakpay.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.01737
