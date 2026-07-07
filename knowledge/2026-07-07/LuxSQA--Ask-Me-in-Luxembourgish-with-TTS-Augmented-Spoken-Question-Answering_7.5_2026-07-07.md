# LuxSQA: Ask Me in Luxembourgish with TTS-Augmented Spoken Question Answering

**评分：** 7.5  
**状态：** 正常  
**标签：** 语音大模型, 低资源语言, 语音问答, TTS, 数据增强, 论文  
**更新日期：** 2026-07-07  
**来源：** rss  

## 项目描述
arXiv:2607.02763v1 Announce Type: new Abstract: Spoken Question Answering (SQA) remains largely focused on high-resource languages and carefully recorded speech, limiting the reach of speech-LLM methods in low-resource settings. This paper investigates whether text-to-speech (TTS) can provide task-specific training data for Luxembourgish SQA without requiring a large human-recorded QA corpus. Starting from existing text-based QA resources, we translate questions into Luxembourgish, synthesize spoken questions with multiple TTS systems, and pair them with textual answers. We train a parameter-efficient SLAM-style architecture that connects a frozen Whisper encoder to frozen multilingual LLM backends through a learned projector and LoRA adapters. We compare MMS-TTS, Qwen3-TTS, and OmniVoice variants, including single-source corpora of about 48k questions and a 4TTS multi-source mix of approximately 230k questions. Evaluation on LLAMA-LB-Test with two real Luxembourgish speaker conditions shows that multi-source and voice-design-based synthetic training configurations yield the strongest SQA performance. The results also show that no-reference TTS quality scores do not monotonically predict downstream QA performance, indicating that synthetic speech must be evaluated as task-specific training data rather than only as natural-sounding audio.

## 综合总结
本论文提出了一种利用TTS合成数据增强低资源语言（卢森堡语）语音问答（SQA）的方法。通过将文本QA翻译并使用多种TTS系统合成语音，结合参数高效的SLAM架构（冻结Whisper+LLM+LoRA）进行训练。实验表明，多源TTS混合数据效果最佳，且发现TTS的音频质量分数与下游QA性能非单调相关，强调了需从任务导向角度评估合成语音数据。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
探讨了TTS合成数据在低资源语言SQA中的应用，采用主流SLAM架构（Whisper+LLM+LoRA）进行参数高效微调。核心洞见在于发现TTS的无参考质量分数与下游QA性能并非单调正相关，强调了必须从任务导向角度评估合成语音数据，打破了'越自然越好'的直觉，具有一定的研究深度和启发性。

### 实用性 (评分: 8.0/10)
提出了一套低成本、可复用的低资源语言SQA构建范式（文本翻译+多源TTS合成+PEFT训练），有效解决了人工录制语料匮乏的痛点。该方法可直接指导多语言语音大模型在长尾语言上的落地实践，对缺乏语音标注资源的语种具有很高的实际参考价值。

### 社区活跃度 (评分: 7.0/10)
研究切中当前Speech-LLM在低资源语言上的痛点，话题具有时效性。来源为arXiv预印本，实验设计包含多TTS系统对比和真实说话人条件评估，具备较高学术可信度。但受限于卢森堡语的受众规模，社区直接影响力相对有限，其方法论价值大于具体语种应用价值。

## 项目链接
https://arxiv.org/abs/2607.02763
