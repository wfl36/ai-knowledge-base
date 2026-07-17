# Just Keep Prompting: Evaluating Repetitive Socratic Prompting in VLMs

**评分：** 8.2  
**状态：** 正常  
**标签：** VLM, 评估, 多轮对话, 鲁棒性, 认知稳定性, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14099v1 Announce Type: new Abstract: Deploying Vision-Language Models (VLMs) in real-world settings requires not only strong visual reasoning but also stability under sustained conversational pressure. We introduce Just Keep Prompting (JKP), a multi-turn evaluation framework that measures VLM epistemic stability when users repeatedly challenge, question, or contradict a model's answer. JKP probes models for up to 10 follow-up turns using three strategies: Adversarial Negation (repeated rejection), Pure Socratic Interrogation (repeated calls to reassess certainty), and Context-Aware Socratic Summarization (reflecting the model's prior rationale back before asking for reconsideration). We evaluate GPT-4o, Gemini 2.5 Pro, and Qwen3-VL-30B on a subset of the STAR benchmark across 720 multi-turn runs. Aggregate accuracy changes modestly from Turn 0 to Turn 10, but trajectory-level analysis reveals substantial instability: correct answers regress, wrong answers recover, and many runs exhibit repeated answer flipping. Repeated prompting has bounded upside and often acts as a destabilizer rather than a reasoning aid. The effect is strongly model-dependent: Qwen3-VL-30B achieves the highest final accuracy but becomes confidently wrong under direct contradiction; Gemini 2.5 Pro is comparatively stable but token-expensive; GPT-4o is the most brittle and oscillatory. These findings reveal that multi-turn VLM evaluation captures not just additional reasoning but pressure-response profiles: how models trade off visual grounding, calibration, and conversational compliance under repeated challenge.

## 综合总结
本文提出了Just Keep Prompting (JKP)多轮评估框架，用于测试视觉语言模型(VLM)在反复被用户质疑或反驳时的认知稳定性。通过对GPT-4o、Gemini 2.5 Pro和Qwen3-VL-30B的测试发现，虽然总体准确率变化不大，但模型在轨迹层面表现出显著的不稳定性（如正确答案退步、错误答案恢复及反复翻转）。研究指出反复提示往往起破坏作用，且不同模型展现出各异的'压力响应特征'：Qwen3易受直接反驳影响而自信犯错，Gemini较稳定但成本高，GPT-4o则最脆弱易震荡。该研究为VLM的多轮交互鲁棒性评估提供了新视角。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文提出了新颖的Just Keep Prompting (JKP)多轮评估框架，突破了传统单轮视觉问答评估的局限，聚焦于VLM在持续对话压力下的'认知稳定性'。研究设计了三种递进的追问策略（对抗性否定、纯苏格拉底式审问、上下文感知苏格拉底式总结），并深入到轨迹层面进行分析，揭示了'正确答案退步、错误答案恢复、反复翻转'等被总体准确率掩盖的细粒度不稳定现象，论证严谨且具有深度。

### 实用性 (评分: 8.0/10)
对VLM开发者和应用工程师具有极高的参考价值。研究明确指出'反复提示往往是破坏者而非推理辅助'，这为多轮对话系统的交互设计敲响了警钟。JKP框架可直接复用于评估自家模型的鲁棒性和对齐稳定性，同时揭示的不同模型'压力响应特征'（如Qwen3易受反驳影响、GPT-4o易震荡、Gemini较稳定但昂贵）为实际业务中的模型选型提供了重要实践指导。

### 社区活跃度 (评分: 8.0/10)
研究聚焦VLM的多轮交互鲁棒性，切中当前大模型社区关于'阿谀奉承'和'自我纠正'能力的热点议题。评估对象涵盖了GPT-4o、Gemini 2.5 Pro、Qwen3-VL-30B等前沿模型，时效性极强。论文来源为arXiv，实验设计扎实，结论对理解大模型在对抗性或长程对话中的行为模式具有较高影响力和可信度。

## 项目链接
https://arxiv.org/abs/2607.14099
