# Most LLM Conformity Needs No Speaker: Measuring the Speaker-Free Floor in Peer-Pressure Benchmarks

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 评估基准, 从众性, 对齐, 论文  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05545v1 Announce Type: new Abstract: LLM conformity is often used to describe cases where a model changes a correct answer toward a peer or group response. We show that most of this apparent conformity survives even after the peer is removed. The reason is a confound: standard conformity prompts mix two cues at once, the presence of a speaker and the repeated wrong answer itself. Existing benchmarks vary these cues together, so they cannot tell how much of the revision actually depends on the speaker. We introduce a no-source condition: the same asserted answer with the explicit speaker removed. Across six open-weight LLMs and seven QA and reasoning datasets, this condition alone causes harmful revision in $66.5\%$ of initially correct cases, compared with $10.3\%$ under a plain re-ask. The effect also remains when the repeated answer is paraphrased and when answer options are hidden in an open-ended setting. Source framing mainly modulates this floor: expert-panel framing raises it, while minimal person labels do not reliably raise it. When models flip, they are usually confidently wrong, and simple recalibration does not recover the original answer. Source attribution still matters, but it should be measured as an increment above this speaker-free floor. The methodological lesson is that conformity benchmarks should first measure what remains after the speaker is removed; without this step, benchmarks may mistake repeated text for social influence.

## 综合总结
本文指出LLM的“从众性”大多并非源于社会影响，而是重复文本本身的锚定效应。研究通过引入“无来源条件”发现，仅重复错误答案即可导致66.5%的初始正确回答被有害修改，远高于单纯重问的10.3%。这一发现揭示了现有基准的缺陷，呼吁未来的从众性评估必须先测量移除说话者后的基线，以避免将文本重复效应误判为社会从众。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
观点极具洞见，精准识别出当前LLM从众性研究中的混杂变量（说话者存在与重复答案的混淆）。实验设计严谨，通过引入“无来源条件”有效剥离了社会影响与文本锚定效应，论证逻辑清晰且数据支撑有力，对现有理论形成了强有力的挑战与补充。

### 实用性 (评分: 8.5/10)
对LLM评估基准的设计具有直接的指导意义，未来的从众性测试必须包含“无来源基线”作为对照。同时，该发现对提示词工程和模型对齐也有重要参考价值，提醒开发者在处理重复上下文时需警惕模型的盲目翻转，而非仅关注社会压力因素。

### 社区活跃度 (评分: 8.5/10)
LLM的社会行为与对齐是当前学术界的热点话题，本文直接挑战了现有从众性基准的效度，具有很强的话题性和学术影响力。其揭示的“伪从众”现象触及了模型行为评估的根本方法，极易引发评估社区的广泛关注与标准重构。

## 项目链接
https://arxiv.org/abs/2607.05545
