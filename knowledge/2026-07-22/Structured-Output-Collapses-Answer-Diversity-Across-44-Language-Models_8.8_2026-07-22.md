# Structured Output Collapses Answer Diversity Across 44 Language Models

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 结构化输出, 多样性, 工具调用, 评估, 论文, 实证研究  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18476v1 Announce Type: new Abstract: When a language model must choose one answer from a large space of equally valid options, a format clause -- "Reply with JSON only" -- changes which answer it chooses. We re-run the One-Word Census (arXiv:2607.12796): 31 wide-answer-space category prompts asked of 44 models, now with the reply requested in JSON -- no schema enforcement, no constrained decoding, only the request. Convergence deepens sharply: on the unconstrained "Pick a word" prompt the modal answer rises from 41% to 64% of the pool and distinct answers fall from 52 to 36; mean answer-choice surprisal drops from 1.80 to 1.58 bits. The tax is progressive: six of 44 models move individually (BH-FDR q=.10), all toward the mode, led by the most distinctive models, while the conformist floor is immobile. It is a sharpener, not a re-indexer -- the plain-chat modal answer survives in 28 of 31 categories. Defaults are register-indexed: a within-run re-sample (n=20) finds JSON shifts 53% of a model's stable chat defaults, mostly back to the crowd, and installs defaults absent from chat (Claude Fable 5 answers "cerulean" for colour 0% of the time in chat, 100% in JSON). Full-battery controls reveal a register gradient: compression is significant and specific to the answer-delivery formats models are trained to speak (JSON -0.22 bits, p=.0002; XML -0.19, p=.002), absent for YAML and CSV, and reversed for an arbitrary bracket wrapper (+0.13, p=.009) -- weighing the mechanism toward tool-use post-training. Enforcing the schema at the decoder (response_format) compresses no further than the request (-0.03 bits): the collapse lives in the model's response to the register, not the decoder. Structured output is how software consumes language models, and that surface is served by a measurably more homogeneous model than the chat surface on which models are evaluated, compared, and chosen.

## 综合总结
本文通过44个大模型的实证研究发现，仅要求大模型以JSON等格式输出（无需强制解码），就会显著降低其回答的多样性，使模型趋同于最常见的答案。这种“同质化税”源于模型在工具调用后训练中形成的语域偏好（JSON/XML显著，YAML/CSV无此效应），且解码器强制无法进一步压缩多样性。这表明，当前基于结构化输出的软件应用所面对的模型，比Chat评估环境下的模型更加同质化，对AI工程实践和模型评估具有深远影响。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
研究深度极高，通过大规模（44个模型）实证与严谨的统计控制，揭示了“要求JSON输出”这一看似中性的格式指令会显著压缩大模型回答的多样性（信息量下降，趋同于众数）。研究精妙地区分了“格式请求”与“解码器强制约束”的作用，并通过对照实验（JSON/XML压缩多样性，YAML/CSV无影响，任意括号反向影响）证实了这是模型在工具调用后训练中形成的“语域”效应，而非单纯的解码约束，机制剖析深刻且逻辑严密。

### 实用性 (评分: 8.5/10)
对AI工程实践具有重要指导意义。当前基于大模型的Agent和软件系统高度依赖JSON等结构化输出进行通信，该研究提醒开发者：生产环境中的模型比Chat评估环境下的模型更加同质化和保守。在设计需要多样性或长尾回答的AI应用时，开发者需警惕结构化输出的“同质化税”，并考虑通过调整提示词或选择特定格式来缓解这一偏差。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，直击当前大模型应用落地的核心范式（Function Calling/结构化输出）。来源为arXiv权威预印本，实验规模大、论证扎实，结论颠覆了业界对“结构化输出仅为格式转换层”的常规认知，极易在AI工程与对齐社区引发广泛关注与讨论，具有较高影响力。

## 项目链接
https://arxiv.org/abs/2607.18476
