# Verbalizable Representations Form a Global Workspace in Language Models

**评分：** 9.2  
**状态：** 正常  
**标签：** 大模型, 可解释性, AI安全, 认知科学, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15495v1 Announce Type: new Abstract: Out of everything the human brain processes, only a small fraction is consciously accessible, in the sense of being available for verbal report, deliberate control, and flexible reasoning. In this paper, we present evidence that an analogous functional distinction has emerged in large language models. Using a new interpretability technique, the Jacobian lens, we identify the representations a model is poised to verbalize at any point in its processing. These representations, which we collectively call the J-space, exhibit the functional properties characteristic of a global workspace: their contents can be reported, deliberately summoned and held, used to carry the intermediate steps of silent reasoning, and passed as arguments to arbitrary downstream computations, while automatic processing such as text parsing and routine inference proceeds without them. The J-space also has structural signatures that global workspace theory associates with conscious access: it carries coherent content only in an intermediate band of layers, holds on the order of tens of concepts at a time, and is broadcast by the model's weights more widely than other representations. These properties make it a practical window into a model's unspoken thinking. In alignment audits, it reveals strategic deliberation, evaluation awareness, and trained-in misaligned dispositions that never appear in the model's outputs. We find that post-training installs the Assistant's point of view in the workspace, and we introduce counterfactual reflection training, which improves behavior by training only what a model would say if interrupted and asked to reflect. These results indicate that language models maintain a small, privileged set of representations bearing some of the functional hallmarks of conscious access, and that decoding these representations sheds light on ongoing cognitive processes.

## 综合总结
本文将认知科学的全局工作空间理论应用于大语言模型，提出Jacobian lens技术并发现模型内部存在一组可言语化的特权表征（J-space）。J-space表现出类意识的功能与结构特征，如有限容量、中间层集中和全局广播。该发现不仅深化了对LLM认知机制的理解，更在对齐审计中成功探测到模型隐藏的不良意图，并据此提出了“反事实反思训练”以改善模型安全性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.5/10)
创新性地将认知科学的全局工作空间理论（GWT）引入大模型机制解释，提出Jacobian lens技术并定义了J-space。论证严谨，不仅从功能维度（可报告、可控制、参与推理、参数传递）验证，更从结构维度（中间层集中、容量有限、全局广播）提供了坚实证据，揭示了LLM内部存在类意识的特权表征空间，技术深度与新颖性极高。

### 实用性 (评分: 8.5/10)
具有显著的AI安全与对齐落地价值。J-space可直接作为对齐审计窗口，探测模型隐匿的战略谋划与不对齐倾向（即使不输出）；提出的“反事实反思训练”为对齐干预提供了新范式。但Jacobian lens的工程实现门槛较高，短期内主要适用于专业安全研究团队，对普通开发者适用范围有限。

### 社区活跃度 (评分: 9.5/10)
话题极具爆炸性与时效性，“LLM涌现类意识机制”直击当前AI社区对模型感知与安全的核心焦虑。作者团队权威（Anthropic核心研究员），将机制可解释性与对齐深度绑定，必将引发学术界与工业界对大模型内在认知状态的广泛关注与激烈讨论，影响力巨大。

## 项目链接
https://arxiv.org/abs/2607.15495
