# Represented but Ignored: A Causal Account of Prosodic Underuse in Audio-Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-21  
**来源：** rss  

## 项目描述
arXiv:2608.19211v1 Announce Type: new Abstract: Human speech is richly expressive, with prosody carrying linguistic and emotional information beyond the lexical content. A capable large audio-language model (audio-LLM) should therefore support expressive speech understanding, not only transcribing what was said but also interpreting how it was said. Yet behavioral evaluations alone cannot reveal why a model fails on prosodic input. An error may reflect loss of acoustic information, incorrect internal interpretation, or failure to use a representation that is already available inside the model. We introduce a stage-specific probe ladder for localizing these failure modes in audio-LLMs. Across four understanding-only audio-LLMs, prosodic information is usually preserved in the audio path and decodable in late LLM states. Yet it is only partially expressed in the model's final response. We test the causal status of this latent representation with targeted hidden-state interventions. Every intervention shifts the answer distribution in the predicted direction, and in most model--task cells a single edit at the relevant layer is sufficient to drive the model toward the suppressed prosodic decision, though this recovery is directional rather than a selective restoration of the correct class. Feature-level analysis further suggests that this recoverable signal can be expressed through a small subspace. Some of the highest-attribution features in this analysis align with acoustic cues known to carry prosodic information. Within the matched-content contrasts we test, these results locate the recurring bottleneck not in perceiving prosody but in using it. Models that hear and correctly represent a prosodic cue can still fail to express it in their answers.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.19211
