# Where Prefill Expert Reduction Hurts MoE Models: A Few Prompt Tokens Carry Most of the Short-Answer F1 Loss

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-19  
**来源：** rss  

## 项目描述
arXiv:2610.22454v1 Announce Type: new Abstract: Running prompt tokens through fewer routed experts during prefill is a simple way to make mixture-of-experts (MoE) serving cheaper, yet it is unclear what this damages. We locate the damage with token-, layer- and attention-path interventions on short-answer question answering in four MoE families. At half the experts the F1 loss of three families is mostly answer form: the model still finds the answer but stops answering briefly. In Qwen3-30B-A3B this loss is made at the two chat-template tokens before the answer, and in DeepSeek-V2-Lite at the first 8-32 prompt tokens, where its instruction sits; by answer likelihood these positions account for about half and a fifth of the damage. Reduction changes the first token's attention mass, norm and largest activation by less than 4%, and restoring super experts or massive activations recovers at most about a quarter of the loss, well below keeping the sensitive positions full. On real prompts with about 4% of tokens at full experts, placing them on the task interface keeps F1 within one point of the unmodified model, while placing them at random in the documents is about 3 points worse (two of five prespecified primary comparisons; the others were undecided or not run). Because the answer boundary always ends a single-turn prompt, and DeepSeek's loss was no longer detectable once its instruction moved away from the start, the sensitive tokens lay at the prompt ends in every sensitive layout we found, so rules that keep the ends are not distinguished from rules that read application marks. Time to first token falls about 14% on 11K-token prompts and not at 2K tokens.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.22454
