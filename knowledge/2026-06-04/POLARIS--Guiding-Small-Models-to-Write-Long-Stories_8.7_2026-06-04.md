# POLARIS: Guiding Small Models to Write Long Stories

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 强化学习, 长文本生成, 创意写作, GRPO, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04095v1 Announce Type: new Abstract: Small open-weight models struggle at long-form creative writing: their generated stories either fall far short of the requested length, or their quality significantly degrades as length increases, especially when compared to frontier models. We present POLARIS (Policy Optimization with LLM-as-a-judge rewards and Anchored-Reference Injection for Storywriting), a lower-compute GRPO recipe with two key ingredients: a frontier LLM judge with a structured Story Quality rubric as the online reward, and human-reference injection (HRI), where a teacher-forced human-written story serves as a high-reward anchor within each GRPO group. By applying our training recipe to Qwen3.5-9B, using a dataset of approximately 1.4K prompt-story pairs derived from 100 short-story anthologies and 4 A100 GPUs, we obtain POLARIS-9B. Across five benchmarks spanning in-distribution and out-of-distribution prompts and rubrics, POLARIS-9B is competitive with much larger open-weight models while following length instructions more closely. A blinded human evaluation confirms that POLARIS-9B is preferred to the base Qwen3.5-9B and on par with Qwen3.5-27B. Despite training only on stories up to 4k words, POLARIS-9B preserves quality on prompts requesting stories up to 3 times the training length, a regime where most open-weight models degrade substantially in quality, length adherence, or both. More broadly, our results suggest that length generalization is a meaningful stress test for creative-writing models and a useful lens for distinguishing otherwise close models.

## 综合总结
本文提出POLARIS，一种针对小模型长篇创意写作的低算力GRPO训练配方。通过结合LLM评判奖励和人类参考注入（HRI），仅需1.4K数据和4张A100，POLARIS-9B在写作质量上媲美Qwen3.5-27B，并在3倍于训练长度的提示下仍保持出色的长度遵循度与质量，突破了小模型长文本生成易退化的瓶颈。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了POLARIS方法，创新性地将LLM-as-a-judge（带结构化评分标准）作为在线奖励，并引入人类参考注入（HRI）作为GRPO组内的高奖励锚点。该方法有效解决了小模型在长文本生成中质量退化和长度不足的痛点，且实验论证严谨，通过5个基准测试和盲评证实了其有效性。此外，论文提出'长度泛化'是评估创意写作模型的有效压力测试视角，具有较高的研究深度和洞见。

### 实用性 (评分: 9.0/10)
极高的工程落地价值。该方法仅需约1.4K数据和4张A100 GPU，即可将9B小模型的写作能力提升至媲美27B模型的水平，极大降低了长文本生成模型的算力与部署门槛。其HRI和LLM评判的RLHF配方不仅适用于创意写作，也可迁移至长代码、长报告等其他长文本生成场景，对从业者指导意义显著。

### 社区活跃度 (评分: 8.5/10)
长文本生成和小模型能力提升是当前AI社区的核心痛点与热点。作者团队包含知名NLP学者Mohit Iyyer，学术背景可靠。该工作以极低算力成本实现小模型对大模型的追赶，且具备出色的长度泛化性，对开源模型生态和RLHF技术发展具有较强的影响力和推动作用。

## 项目链接
https://arxiv.org/abs/2606.04095
