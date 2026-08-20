# Persona-Guided LLM Agents for Task-Oriented Dialogue

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-20  
**来源：** rss  

## 项目描述
arXiv:2608.18085v1 Announce Type: new Abstract: Prior work has shown that large language models (LLMs) can express diverse personality traits in open-ended text generation. However, it remains unclear whether they can do so in a goal-directed dialogue without compromising task completion, and whether adapting to the user's personality improves the interaction quality. We study these questions in task-oriented dialogue (TOD), where a system helps a user accomplish a goal via multi-turn interaction. We build a training-free framework that simulates a TOD interaction between two LLMs: a user agent that exhibits a target personality and a system agent that adapts to the user while completing the task. To isolate the effect of adaptation, we vary how much the system knows about the user's personality across three conditions. In Neutral, the system receives no personality information. In Try, it infers the personality from dialogue cues. In Oracle, it is given the personality explicitly. We evaluate GPT-4o, Qwen3-Next-80B, and Gemini 2.0 Flash on Hotel and Restaurant dialogues from the Schema-Guided Dialogue (SGD) dataset, across the Big Five traits and their opposite poles. We find that the user agent can express personality while the system maintains strong task performance, although some traits are realized far less reliably than others. Adapting to the user's personality improves constraint satisfaction, inform rate, and user satisfaction, but lowers truthfulness, revealing a trade-off between personalization and task-grounding. Oracle's gains grow when the target trait is strongly expressed, whereas Try's gains are largely insensitive to realization strength. Overall, cue-based adaptation in Try best resolves this trade-off and offers a more reliable route to personality-aware TOD without fine-tuning.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.18085
