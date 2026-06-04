# POLARIS: Guiding Small Models to Write Long Stories

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 强化学习, 长文本生成, 创意写作, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04095v1 Announce Type: new Abstract: Small open-weight models struggle at long-form creative writing: their generated stories either fall far short of the requested length, or their quality significantly degrades as length increases, especially when compared to frontier models. We present POLARIS (Policy Optimization with LLM-as-a-judge rewards and Anchored-Reference Injection for Storywriting), a lower-compute GRPO recipe with two key ingredients: a frontier LLM judge with a structured Story Quality rubric as the online reward, and human-reference injection (HRI), where a teacher-forced human-written story serves as a high-reward anchor within each GRPO group. By applying our training recipe to Qwen3.5-9B, using a dataset of approximately 1.4K prompt-story pairs derived from 100 short-story anthologies and 4 A100 GPUs, we obtain POLARIS-9B. Across five benchmarks spanning in-distribution and out-of-distribution prompts and rubrics, POLARIS-9B is competitive with much larger open-weight models while following length instructions more closely. A blinded human evaluation confirms that POLARIS-9B is preferred to the base Qwen3.5-9B and on par with Qwen3.5-27B. Despite training only on stories up to 4k words, POLARIS-9B preserves quality on prompts requesting stories up to 3 times the training length, a regime where most open-weight models degrade substantially in quality, length adherence, or both. More broadly, our results suggest that length generalization is a meaningful stress test for creative-writing models and a useful lens for distinguishing otherwise close models.

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了POLARIS方法，基于低算力GRPO算法，创新性地引入了基于前沿大模型和结构化评分标准的在线奖励机制，以及人类参考注入（HRI）作为高奖励锚点。研究不仅有效缓解了小模型在长文本创作中质量退化的问题，还提出并验证了'长度泛化'作为创作模型压力测试的有效性，论证严谨，实验设计包含5个基准测试与人类盲测，研究深度较高。

### 实用性 (评分: 9.0/10)
极具落地指导价值。该方法仅需4张A100 GPU和约1.4K数据即可将9B参数模型的创作能力提升至媲美27B模型的水平，大幅降低了长文本生成模型的训练算力与数据门槛。其HRI技巧和LLM-as-a-judge奖励机制具有高度可复用性，可轻松迁移至其他受限于算力的生成任务中，对工业界和开源社区开发者极其友好。

### 社区活跃度 (评分: 8.5/10)
选题精准切中当前开源小模型长文本生成能力不足的痛点，且GRPO与小模型强化学习对齐是当前AI社区的热点方向。作者团队包含知名NLP学者，实验包含人类盲测，结果可信度高。其'小模型媲美大三倍模型'的成果极具话题性，在开源社区和长文本应用领域将产生显著影响力。

## 项目链接
https://arxiv.org/abs/2606.04095
