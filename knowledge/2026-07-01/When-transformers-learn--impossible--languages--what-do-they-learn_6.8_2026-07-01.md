# When transformers learn "impossible" languages, what do they learn?

**评分：** 6.8  
**状态：** 正常  
**标签：** 大模型, 语言学, 认知科学, 生成, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30815v1 Announce Type: new Abstract: Recent work suggests that transformer language models show a bias towards human languages over unnatural ("impossible") languages argued to be unacquirable by humans. However, this literature has largely based these claims on differences in sample efficiency and test-set perplexity, rather than on direct evaluations of the linguistic capacities that could plausibly explain non-attestation in human languages. We evaluate two theoretically motivated linking hypotheses: impossibility arising from deficiencies in grammatical sensitivity or generative production. Using GPT-2 style models trained on perturbed "impossible" variants of English, we measure sensitivity to grammaticality using BLiMP minimal pairs, finding that model performance exhibits only gradual degradation, mediated by the language's information locality. In contrast, these models exhibited pronounced failures in generation, producing substantially fewer high-quality sentences at longer lengths. Together, these results suggest generative deficiency and transmission failures as a plausible linking hypothesis between language model behaviour and non-attestation of impossible languages.

## 综合总结
本文研究了Transformer模型在学习人类无法习得的'不可能'语言时的内在机制。不同于以往基于困惑度的宏观评估，作者使用GPT-2模型结合BLiMP测试，从语法敏感性和生成能力两个微观维度进行探究。实验发现，模型对语法规则的敏感性仅受信息局部性影响而缓慢下降，但在长句生成上却表现出严重的结构性失败。该研究提出'生成缺陷与传递失败'是解释不可能语言在人类中不存在的核心假设，为理解大模型的语言处理边界及人类语言的演化提供了深刻的理论洞见。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
文章在研究深度上表现出色，超越了以往仅依赖样本效率和测试集困惑度的表面评估，深入到语法敏感性与生成能力这两个理论驱动的语言学维度。通过严谨的实验设计（使用GPT-2与BLiMP最小对测试），揭示了模型在处理'不可能'语言时，语法敏感性仅受信息局部性影响而缓慢退化，但生成能力在长序列上出现显著崩溃。这一发现提出了'生成缺陷与传递失败'作为连接模型行为与人类语言非存在性的关键假设，论证严密且具有理论创新性。

### 实用性 (评分: 4.5/10)
本文偏向基础研究与认知科学理论探讨，对工业界AI从业者的直接工程落地参考价值有限。然而，其关于'信息局部性'影响模型语法敏感性的结论，对大模型训练数据的构建与长文本生成能力的优化具有间接启示，提醒从业者关注语言结构局部依赖对模型表现的影响。

### 社区活跃度 (评分: 7.5/10)
探讨大模型与人类语言认知机制的对比是当前AI与认知科学交叉领域的热点话题，时效性强。作者包含计算语言学领域知名学者Sharon Goldwater，学术背景权威，研究结论对语言演化、认知科学及AI基础理论社区具有较高影响力和可信度。

## 项目链接
https://arxiv.org/abs/2606.30815
