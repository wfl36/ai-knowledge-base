# Cost of Reasoning in non-English Languages: A Case Study on Japanese

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 推理, 多语言, GRPO, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.10114v1 Announce Type: new Abstract: Reasoning Language Models (RLMs) achieve their strongest performance when they reason in English, the language for which reasoning-oriented training data is most abundant. However, reasoning trace is a clue for model interpretability and safety, and useful in practice for both the model users and for model developers. Thus, it is desirable to be able to develop a model that reasons in a language of the user's choice, while still maintaining strong reasoning performance. To this end, we study the feasibility of training a model that reasons in Japanese. We develop a Japanese-reasoning variant of Qwen-3-Swallow-8B, which is a Japanese LLM continually pretrained from Qwen-3-8B, with GRPO and evaluate it across coding, math, and science benchmarks. The study shows that reasoning-language control is feasible by training a Japanese continually pretrained model with GRPO. However, its performance is at best on par with strong English-reasoning baselines on several benchmarks. We also evaluate the trained model on Japanese cultural benchmarks and observe that the model's performance is worse than the baseline models, suggesting that the reasoning in Japanese does not immediately improve performance on culturally relevant tasks for free.

## 综合总结
本文探讨了在非英语（日语）环境下训练推理语言模型的可行性与代价。基于Qwen-3-Swallow-8B和GRPO的实验表明，虽然可以通过训练控制模型使用日语进行推理，但其性能仅能与英语推理基线持平，且在日语文化基准上并未表现出预期优势。该研究为多语言RLM的开发提供了重要实证，揭示了推理语言本地化面临的性能与对齐挑战。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
研究深入探讨了非英语（日语）推理语言模型的可行性与性能代价。通过在Qwen-3-Swallow-8B上应用GRPO训练日语推理变体，证实了推理语言控制的可行性，但发现日语推理性能最多与英语推理基线持平。更有价值的发现是，日语推理并未在日语文化相关基准上带来预期增益，反而表现不如基线，揭示了推理语言与任务文化属性间非直觉的复杂关系，论证严谨且有反直觉洞见。

### 实用性 (评分: 7.5/10)
对非英语大模型（特别是中日韩等语言）的开发者具有较高参考价值。研究证实了GRPO可用于定制模型的推理语言，满足可解释性与本地化需求；但同时也给出了明确的工程警示：切换推理语言无法免费获得文化任务增益，且可能牺牲部分推理性能上限，指导从业者在实际应用中需在可解释性、安全性与性能间做出权衡。

### 社区活跃度 (评分: 8.5/10)
话题紧扣当前大模型推理能力爆发背景下的多语言痛点，时效性极强。arXiv论文来源权威可信，非英语推理的可控性与性能权衡是当前AI社区高度关注的议题，对于推动RLM在全球多语种场景的落地有较强的启发意义和影响力。

## 项目链接
https://arxiv.org/abs/2607.10114
