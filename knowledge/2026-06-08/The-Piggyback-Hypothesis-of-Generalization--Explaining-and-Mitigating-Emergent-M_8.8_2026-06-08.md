# The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 对齐, 微调, 可解释性, 涌现性错位, 论文  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06667v1 Announce Type: new Abstract: The mechanisms behind LLMs' broad over-generalization beyond training examples remain unclear. Emergent misalignment (EM) offers a striking case study: finetuning on narrow tasks induces broad misalignment to semantically-unrelated test domains. In this work, we propose the Piggyback Hypothesis: the chat-template tokens can piggyback the finetuned behaviour onto out-of-domain queries. We validate this hypothesis by showing that subtle perturbations to the prefix (tokens preceding all user queries), or patching the prefix representations with those from the unfinetuned model, can restore alignment without changing the user query. Building on this finding, we propose Token-Regularized Finetuning (TReFT), which regularizes specific token representations during training to mitigate EM. Across different models and multiple EM-inducing datasets, TReFT reduces EM while preserving in-domain learning. On Llama-3.1-8B finetuned on the legal domain, TReFT achieves 33.5% more EM reduction than data interleaving with a retain set of aligned examples. We further show that TReFT extends to other narrow-finetuning settings, including abstention, tool use, and refusal (off-topic generalization is reduced by 54.3% on average), supporting the Piggyback Hypothesis. Broadly, our work highlights that LLMs may learn and generalize in unintended ways and suggests a path toward more constrained finetuning. It also calls for further study of how shared input features can piggyback model behavior across domains.

## 综合总结
本文提出“搭便车假设”来解释大模型微调中的涌现性错位（EM）现象，指出聊天模板token会将微调行为意外泛化至域外查询。基于此发现，作者提出TReFT（Token-Regularized Finetuning）方法，通过在训练中对特定token表示进行正则化来抑制EM。实验表明，TReFT在多模型和多任务中均显著优于基线方法，为大模型的安全微调提供了新机制和实用方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出了新颖的'搭便车假设'(Piggyback Hypothesis)，深入揭示了聊天模板token如何将微调行为意外泛化至域外查询，从而导致涌现性错位(EM)。通过前缀扰动和表示修补实验严谨验证了该假设，并基于机制解释提出TReFT算法，技术深度与论证严谨性极高。

### 实用性 (评分: 8.5/10)
提出的TReFT方法可直接应用于大模型微调流程，有效解决垂直领域微调（如法律、工具使用等）导致的对齐遗忘和越界泛化问题，效果显著优于传统数据交错方法，对工业界安全微调具有极高的落地参考价值。

### 社区活跃度 (评分: 9.0/10)
大模型对齐与微调安全性是当前AI社区的核心痛点，该研究由可解释性领域知名学者David Bau等参与，机制解释与缓解方案并重，具有极高的时效性与权威性，预计将对微调安全与模型泛化研究领域产生重要影响。

## 项目链接
https://arxiv.org/abs/2606.06667
