# DLawBench: Evaluating LLMs Through Multi-Turn Legal Consultation

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 评估基准, 法律AI, 多轮对话, 推理, 论文  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13931v1 Announce Type: new Abstract: Lawyer-client consultation is a critical starting point for legal services. Effective legal assistance hinges on eliciting sufficient and truthful information from clients in order to devise strategies that best protect their interests. This task requires Large Language Models (LLMs) not only to perform robust legal reasoning, but also to strategically elicit material facts through multi-turn interactions and effectively guide clients with diverse personalities. Yet existing legal benchmarks overlook this interactive capability. To fill this gap, we introduce DLawBench, a diagnostic benchmark for real-world legal consultation. Drawing on realistic client behavior, we characterize lawyer-client interactions into four types: Cooperative, Dependent, Withdrawn, and Adversarial. Using dialogues grounded in real cases, DLawBench evaluates whether LLMs can effectively conduct legal consultation under realistic conditions. DLawBench comprises 461 cases from Chinese and U.S. law, 5,532 paired fact entries, 3,411 inquiry rubrics, and 3,348 issue-resolution rubrics, and evaluates 26 representative LLMs. Systematic experiments show substantial headroom: the best-performing model, GPT-5.5, achieves only 0.562 on consultation-grounded legal reasoning. More importantly, DLawBench exposes both sycophancy in legal consultation and a paradox: models perform worse when clients need guidance most.

## 综合总结
本文提出了DLawBench，首个针对多轮法律咨询场景的LLM诊断基准。该基准创新性地将客户交互分为合作、依赖、退缩和对抗四种类型，并基于中美法律真实案例构建了详尽的评估体系。对26个代表性LLM的评估表明，当前最强模型（GPT-5.5）在法律推理上表现仍有限（得分0.562），且暴露出模型在法律咨询中的谄媚倾向及'越需要指导表现越差'的悖论，为法律AI的后续研发指明了关键改进方向。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
该研究具有显著的学术深度与新颖性，首次填补了多轮交互式法律咨询评估的空白。创新性地将客户行为分为合作、依赖、退缩和对抗四种类型，构建了包含事实条目、询问和问题解决评分标准的细粒度评估体系。更重要的是，研究揭示了LLM在法律咨询中的'谄媚现象'以及'越需要指导表现越差'的悖论，这一深刻洞见对理解大模型在高风险领域的推理与交互机制具有重要价值。

### 实用性 (评分: 8.5/10)
对法律AI领域的从业者具有极高的实践指导意义。基准测试明确指出了当前LLM在应对不同性格客户及多轮信息诱导时的缺陷，为法律Agent的系统设计（如抗谄媚机制、主动引导策略）提供了明确的优化方向。其基于真实案例的评分标准也可直接用于法律大模型的能力诊断与迭代评估。

### 社区活跃度 (评分: 9.0/10)
论文发布于2026年，评估了包括GPT-5.5在内的26个最新前沿模型，具有极强的时效性。法律大模型是当前AI落地的核心赛道之一，而该基准暴露出的模型交互缺陷与悖论直击行业痛点，预计将在法律科技与AI安全社区引发广泛关注与讨论，具备很高的影响力和权威性。

## 项目链接
https://arxiv.org/abs/2606.13931
