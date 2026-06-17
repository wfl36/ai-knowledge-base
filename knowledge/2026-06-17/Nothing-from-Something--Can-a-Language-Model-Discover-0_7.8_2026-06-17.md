# Nothing from Something: Can a Language Model Discover 0?

**评分：** 7.8  
**状态：** 正常  
**标签：** 大模型, 推理, AI4Math, 认知科学, 泛化, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17289v1 Announce Type: new Abstract: AI systems based on artificial neural networks are being developed with aspirations of pushing the boundary of human mathematical knowledge. A key question for these systems is how much they can reach beyond their training data. Mathematical discovery requires a strong form of out of distribution generalization; the ability to hypothesize genuinely new - and potentially logically more powerful - mathematical structures. It has been hypothesized that language abilities support such generalizations in human cognition. In this work, we use simple arithmetic as a case study for examining how modern AI models could expand their mathematical horizons, evaluating whether these models can independently discover the concept of "zero". We show that We show that (1) language models of a GPT-2 size are unable to perform this generalization at test time regardless of language pretraining, but (2) models can improve substantially after training on tens or hundreds of examples of zero. Additionally, we find that language pretraining reduces the number of required examples by approximately $50\%$, showing that language abilities can scaffold mathematical discovery in neural models.

## 综合总结
本文探讨了语言模型能否超越训练数据独立发现新数学概念，以‘发现零’为案例进行实验。研究发现，GPT-2规模的模型在测试时无法自发泛化出‘零’的概念，但在接受少量包含零的样本训练后表现显著提升；同时，语言预训练可将所需样本数减少约50%。这表明语言能力能为神经网络的数学发现提供认知支架，揭示了当前模型在强OOD泛化上的局限以及语言与数学认知的深层联系。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究具有极高的认知科学与AI交叉领域的洞见深度。文章巧妙地将‘发现零’这一人类数学认知史上的关键飞跃作为强分布外（OOD）泛化能力的测试基准，探讨了语言模型能否真正实现‘从无到有’的概念发现。实验设计严谨，通过控制变量清晰剥离了语言预训练与少样本微调的作用，论证了语言能力作为数学发现‘脚手架’的认知机制。不足之处在于受限于GPT-2规模，对当前前沿大模型的推论可能存在一定局限。

### 实用性 (评分: 6.0/10)
对AI4Math和认知启发AI方向的研究者具有较高的理论参考价值，揭示了当前小规模模型在真正自主发现新概念上的局限性，并验证了‘语言预训练+少量示例’的有效范式，可为课程学习或数据设计提供启发。但该研究偏向基础认知与泛化机制探索，缺乏直接的工程落地指导，对普通从业者的实操价值有限。

### 社区活跃度 (评分: 9.0/10)
话题极具时效性与争议性，直击当前AI社区对‘大模型是随机鹦鹉还是具备真正推理/发现能力’的核心焦虑。作者Thomas L. Griffiths与Brenden M. Lake均为认知科学与AI领域的顶尖学者，权威性极高。‘模型能否发现0’这一命题兼具学术深度与传播属性，极易在学术圈与科技社区引发广泛讨论与影响力。

## 项目链接
https://arxiv.org/abs/2606.17289
