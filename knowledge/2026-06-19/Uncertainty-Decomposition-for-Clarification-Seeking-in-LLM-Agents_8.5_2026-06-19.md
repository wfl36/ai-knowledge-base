# Uncertainty Decomposition for Clarification Seeking in LLM Agents

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 大模型, 不确定性量化, 推理, 论文  
**更新日期：** 2026-06-19  
**来源：** rss  

## 项目描述
arXiv:2606.19559v1 Announce Type: new Abstract: Recent position papers argue that the classical aleatoric/epistemic uncertainty framework is insufficient for interactive large language model (LLM) agents and call for underspecification-aware, decomposed, and communicable uncertainty representations that can unlock new agent capabilities such as proactive clarification seeking and shared mental-model building. Practical deployment constraints -- black-box APIs, interactive latency budgets, and the absence of labeled trajectories -- rule out logprob-based, multi-sampling, and training-based methods, leaving prompt-based estimation as the most viable family for surfacing such signals at deployment time. We answer this call with a simple prompt-based decomposition that separates action confidence from request uncertainty (u), enabling the agent to ask for clarification when the task specification is ambiguous. To evaluate it, we introduce two clarification-augmented benchmarks (WebShop-Clarification and ALFWorld-Clarification) in which 50% of tasks are deliberately underspecified, and systematically compare the proposed decomposition against ReAct+UE and Uncertainty-Aware Memory (UAM) across five LLM backbones (GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B, GPT-OSS-120B) on these variants together with the standard WebShop, ALFWorld, and REAL benchmarks for fault detection. Averaged across the five backbones, the proposed decomposition improves clarification F1 on ALFWorld-Clarification by 73% over ReAct+UE and by 36% over UAM, and leads clarification F1 on every backbone on WebShop-Clarification and on four of five backbones on ALFWorld-Clarification, indicating that the gains generalize beyond a single LLM.

## 综合总结
本文针对交互式LLM Agent在任务模糊时缺乏主动澄清能力的问题，指出了经典不确定性框架的不足，提出了一种基于提示词的不确定性分解方法，将动作置信度与请求不确定性分离。该方法无需模型内部概率或多重采样，适合黑盒API部署。作者构建了两个包含故意欠定任务的基准，并在5个主流LLM上验证了该方法在澄清F1上的显著提升（如ALFWorld-Clarification上平均提升73%），证明了其跨模型的泛化性与有效性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文针对交互式LLM Agent的不确定性表达问题，指出了经典偶然/认知不确定性框架的局限性，创新性地提出了一种基于提示词的不确定性分解方法，将动作置信度与请求不确定性分离。该方法在理论定位上具有新颖性，且巧妙避开了黑盒API、延迟预算和无标注轨迹等实际部署限制，放弃了基于logprob或多重采样的传统路径。实验设计严谨，构建了两个专门的澄清增强基准，并在5个不同规模的LLM骨干网络上进行了系统对比，取得了显著的F1提升，论证具有很强的说服力。

### 实用性 (评分: 9.0/10)
该研究具有极高的落地指导价值。LLM Agent在实际应用中处理模糊指令是刚需痛点，而本文提出的基于提示词的估计方法无需模型训练或访问模型内部输出概率，极大降低了工程实现门槛，可直接应用于基于API调用的现有Agent架构中。其分离出的请求不确定性信号能够直接触发澄清机制，对开发高可靠性、强交互式的智能体系统具有直接的实践指导意义。

### 社区活跃度 (评分: 8.0/10)
LLM Agent的主动交互与不确定性量化是当前AI社区的前沿热点话题。本文紧扣这一趋势，提出的解决方案直击痛点，且实验中涉及的多个前沿大模型（如GPT-5.1、DeepSeek-v3.2-exp等）也显示了其研究的前瞻性。尽管部分模型版本信息带有未来属性，但其构建的基准和验证的泛化能力使其具备成为Agent交互领域重要参考的潜力，有望引发对Agent不确定性表达和共享心智模型构建的广泛讨论。

## 项目链接
https://arxiv.org/abs/2606.19559
