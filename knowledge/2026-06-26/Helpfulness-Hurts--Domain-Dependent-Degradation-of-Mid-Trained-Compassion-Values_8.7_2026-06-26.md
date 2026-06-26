# Helpfulness Hurts: Domain-Dependent Degradation of Mid-Trained Compassion Values Under Post-Training

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 对齐, 价值观, 后训练, 道德推理, 论文  
**更新日期：** 2026-06-26  
**来源：** rss  

## 项目描述
arXiv:2606.26102v1 Announce Type: new Abstract: Standard post-training pipelines apply supervised fine-tuning (SFT) and reinforcement learning (RL) to make language models helpful, but these processes may inadvertently degrade values instilled during pre-training. We investigate whether the domain of post-training data differentially affects the retention of animal compassion values in a Llama 3.1 8B model mid-trained on compassion-oriented synthetic data, using both SFT (helpfulness via Dolly-15k vs. coding via Magicoder-110K) and GRPO (helpfulness via RLHFlow vs. coding via Magicoder), evaluated on the Animal Harm Benchmark (AHB 2.2) and MORU benchmark (Moral Reasoning Under Uncertainty). Helpfulness training significantly degrades animal compassion relative to coding training on AHB (SFT: 35.7% vs. 65.2%; GRPO: 18.7% vs. 32.0%), replicating across two independent helpfulness datasets and two training paradigms. On English MORU items, helpfulness training degrades general moral reasoning by 25.5 percentage points (46.4% vs. 71.9%), a striking gap that rivals the compassion effect in magnitude. However, this effect does not transfer cross-lingually: on the multilingual MORU benchmark, the domain effect disappears (SFT: 52.3% vs. 51.2%). In contrast, the animal compassion effect transfers consistently across languages, with Magicoder's AHB percentage-point gain over the base model 4.5 times larger on non-English items than English items. This divergence suggests that values instilled through mid-training are encoded more deeply and cross-lingually than reasoning improvements from domain-specific post-training. These results suggest that, for labs building on value-laden mid-training, coding-domain post-training may better preserve mid-trained values than helpfulness post-training without harming general reasoning capabilities.

## 综合总结
本文探讨了后训练对大模型中训练阶段注入价值观的退化影响。研究发现，旨在提升'有用性'的SFT和RL训练会显著降低模型的动物同情心和通用道德推理能力，且退化程度远超代码领域训练。跨语言实验进一步表明，中训练价值观的编码比后训练的推理改进更深层且可跨语言迁移。据此，作者建议在价值观导向的中训练后，采用代码数据进行后训练能更好地保留价值观。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
研究揭示了后训练中'有用性'对齐对模型中训练阶段注入价值观的侵蚀作用，通过对比代码训练与有用性训练、SFT与GRPO范式，以及跨语言迁移实验，深入剖析了价值观与推理能力在模型内部编码深度的差异。实验设计严谨，控制变量合理，结论具有较强的新颖性和理论深度。

### 实用性 (评分: 8.5/10)
对大模型对齐和后训练流程具有高度实践指导意义。明确建议在具有价值观导向的中训练后，采用代码领域数据进行后训练比有用性数据更能保留既有价值观且不损害推理能力，为AI实验室的SFT/RL数据配比和训练策略提供了直接、可操作的参考。

### 社区活跃度 (评分: 8.5/10)
话题切中当前大模型对齐领域的核心痛点（对齐税/价值观遗忘），实验覆盖多种范式和基准，来源可信。其反直觉的结论（代码训练比有用性训练更保价值观）极易引发社区关注和讨论，具有较高的影响力和时效性。

## 项目链接
https://arxiv.org/abs/2606.26102
