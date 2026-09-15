# Causal Analysis and Mitigation of Spurious Onsets in Full-Duplex Speech LLMs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-15  
**来源：** rss  

## 项目描述
arXiv:2609.13445v1 Announce Type: new Abstract: Speech-to-speech LLMs like Moshi, and its derivative PersonaPlex, can listen and speak concurrently through full-duplex generation. However, they can begin speaking inappropriately during prolonged user silence: under digital-zero input, Moshi and PersonaPlex initiate speech in 12/40 and 11/40 five-minute continuations, respectively. What causes this spurious speech? We investigate two hypotheses: either repeated sampling selects speech despite persistently low onset probabilities, or conditioning on the model's nonspeech outputs causes an abrupt spike in onset probability. We find that, at every observed onset, speech probability spikes by over nine orders of magnitude in one 80-ms frame, supporting the latter hypothesis. Then, to suppress these onsets without blocking genuine responses, we ask a causal counterfactual question: is the model responding to user speech, or would its next-token distribution remain similar if the preceding user input were muted? Accordingly, we suppress onsets whose distributions change little under this intervention. Across 40 held-out trials per model with realistic microphone noise, our method suppresses 13/13 Moshi and 9/9 PersonaPlex spurious onsets, while preserving 40/40 genuine responses per model. Our inference-time method requires no retraining and runs in real-time, with 95th-percentile decision time below 61 ms, within the 80-ms frame budget. Our code is available at https://github.com/KentoNishi/icassp27-spurious-onsets.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.13445
