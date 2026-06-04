# POLARIS: Guiding Small Models to Write Long Stories

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 强化学习, 长文本生成, 创意写作, GRPO, LLM-as-a-judge, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04095v1 Announce Type: new Abstract: Small open-weight models struggle at long-form creative writing: their generated stories either fall far short of the requested length, or their quality significantly degrades as length increases, especially when compared to frontier models. We present POLARIS (Policy Optimization with LLM-as-a-judge rewards and Anchored-Reference Injection for Storywriting), a lower-compute GRPO recipe with two key ingredients: a frontier LLM judge with a structured Story Quality rubric as the online reward, and human-reference injection (HRI), where a teacher-forced human-written story serves as a high-reward anchor within each GRPO group. By applying our training recipe to Qwen3.5-9B, using a dataset of approximately 1.4K prompt-story pairs derived from 100 short-story anthologies and 4 A100 GPUs, we obtain POLARIS-9B. Across five benchmarks spanning in-distribution and out-of-distribution prompts and rubrics, POLARIS-9B is competitive with much larger open-weight models while following length instructions more closely. A blinded human evaluation confirms that POLARIS-9B is preferred to the base Qwen3.5-9B and on par with Qwen3.5-27B. Despite training only on stories up to 4k words, POLARIS-9B preserves quality on prompts requesting stories up to 3 times the training length, a regime where most open-weight models degrade substantially in quality, length adherence, or both. More broadly, our results suggest that length generalization is a meaningful stress test for creative-writing models and a useful lens for distinguishing otherwise close models.

## 综合总结
本文提出POLARIS框架，通过结合LLM-as-a-judge结构化奖励与人类参考注入(HRI)的GRPO策略，有效解决了小模型长篇创意写作中质量随长度退化的问题。仅需1.4K数据和4张A100，POLARIS-9B在盲测中达到Qwen3.5-27B水平，且在3倍于训练长度的提示下仍保持高质量输出，证明了长度泛化是评估写作模型的有效压力测试，为低成本长文本对齐提供了极具价值的新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文在技术深度和新颖性上表现突出。针对小模型长文本生成质量退化及长度不达标的问题，创新性地提出了POLARIS框架，将LLM-as-a-judge与结构化评分标准结合作为在线奖励，并引入人类参考注入(HRI)作为GRPO的高奖励锚点，有效缓解了长文本强化学习中的奖励稀疏与偏移问题。此外，论文提出将‘长度泛化’作为创意写作模型的压力测试视角，具有深刻的学术洞见，实验论证严谨充分。

### 实用性 (评分: 9.0/10)
对从业者的实际参考价值极高。该方案仅需约1.4K数据和4张A100即可完成9B模型的训练，极大降低了长文本对齐的算力与数据门槛。其‘LLM-as-a-judge + HRI锚点’的强化学习配方不仅适用于创意写作，也可轻松迁移至代码生成、长文摘要等其他长输出场景，具有广泛的适用性和极强的可落地性。

### 社区活跃度 (评分: 8.5/10)
话题时效性强，紧扣当前开源小模型长文本生成与对齐的痛点。作者团队包含知名NLP学者Mohit Iyyer，来源权威性高。小模型以极低成本媲美大模型（9B对标27B）且具备3倍长度泛化能力的成果，极易在开源社区和AI工程界引发广泛关注与复现。

## 项目链接
https://arxiv.org/abs/2606.04095
