# The yes-no bias of large language models reflects answer order and wording, not shifts in moral judgment

**评分：** 8.9  
**状态：** 正常  
**标签：** 大模型, 对齐, 评测, 偏见, 推理, 论文  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05552v1 Announce Type: new Abstract: Large language models (LLMs) increasingly issue judgments read as binary verdicts, and a growing literature reports such judgments shifting under logically irrelevant changes of wording - among them an amplified yes-no bias on moral dilemmas, absent in humans. A single framing cannot say what such a shift is: in a yes/no question the word "no" is at once logical verdict, lexical token, and last-printed option. We introduce a psychometric battery that separates these: crossed symmetrization - every logically irrelevant factor flipped in balanced pairs - across a corpus of question forms. A graded rating across logically equivalent forms recovers a coherent internal moral scale: frontier models' stance $\theta$ is nearly format-invariant (cross-form incoherence 0.12-0.21 on a $\pm 1$ axis); small open-weight models fail in model-specific ways. Forcing the verdict through yes/no overlays a decomposable artifact: an order bias toward the last-printed option - opposite to classic human primacy - plus a lexical pull toward the word "no"; the artifact is substantial only in the Claude models (story-averaged -0.32 to -0.86), $\approx 0$ for GPT-5.5 and Gemini, and shrinks under extended reasoning. The word and the verdict share one token; swapping the words for arbitrary labels separates them, and the verdict-attached logical bias proves $\approx 0$ for every frontier model, while model-specific label and order attachments remain: the models are not drawn toward rejecting - the pull follows the printed surface, not the verdict it carries. A minimal model, $P = \sigma((\theta \pm m)/s)$, summarizes any such artifact by a framing susceptibility m and a moral decisiveness s, measurably distinct from sampling temperature. The battery applies unchanged to any dilemma set and binary format: measuring what a model values requires crossing the frames of the question, not asking once.

## 综合总结
本文通过引入心理测量电池和交叉对称化方法，揭示了LLM在二元道德判断中的yes-no偏差并非源于道德立场的转变，而是由答案顺序和词汇表面形式引起的可分解伪影。前沿模型具有连贯的内部道德尺度，且该偏差可通过扩展推理或替换任意标签消除。研究提出的最小模型为准确测量模型价值观提供了新范式，强调必须通过交叉提问来消除框架效应。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.2/10)
研究设计极具深度与创新性，引入心理测量学中的'交叉对称化'方法，成功将LLM在二元道德判断中的yes-no偏差解构为顺序偏差（偏向最后打印选项）和词汇拉力（偏向词汇'no'）。研究证实了前沿模型具有格式不变的内部道德尺度，偏差源于表面形式而非逻辑拒绝，并提出了量化框架易感性(m)和道德果断性(s)的最小数学模型，论证严谨且方法新颖。

### 实用性 (评分: 8.5/10)
提出的心理测量电池和最小模型可直接应用于各类二元判断和困境集的评估中，为AI对齐和模型评测从业者提供了消除伪影、准确测量模型真实价值观的实操方法（即必须交叉提问而非单次询问），对红队测试和模型对齐工作具有极高的方法论指导价值。

### 社区活跃度 (评分: 9.0/10)
论文发布于2026年，涉及GPT-5.5等最新前沿模型，直击LLM偏见与道德判断这一核心热点问题。arXiv来源保证了学术权威性，其'偏差源于表面形式而非道德偏移'的结论对社区在模型对齐和评测方面的认知有重要纠偏影响，话题时效性与影响力极高。

## 项目链接
https://arxiv.org/abs/2607.05552
