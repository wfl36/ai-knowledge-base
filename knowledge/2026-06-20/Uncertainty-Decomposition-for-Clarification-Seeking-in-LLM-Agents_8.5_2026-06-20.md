# Uncertainty Decomposition for Clarification Seeking in LLM Agents

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 大模型, 不确定性, 推理, 论文  
**更新日期：** 2026-06-20  
**来源：** rss  

## 项目描述
arXiv:2606.19559v1 Announce Type: new Abstract: Recent position papers argue that the classical aleatoric/epistemic uncertainty framework is insufficient for interactive large language model (LLM) agents and call for underspecification-aware, decomposed, and communicable uncertainty representations that can unlock new agent capabilities such as proactive clarification seeking and shared mental-model building. Practical deployment constraints -- black-box APIs, interactive latency budgets, and the absence of labeled trajectories -- rule out logprob-based, multi-sampling, and training-based methods, leaving prompt-based estimation as the most viable family for surfacing such signals at deployment time. We answer this call with a simple prompt-based decomposition that separates action confidence from request uncertainty (u), enabling the agent to ask for clarification when the task specification is ambiguous. To evaluate it, we introduce two clarification-augmented benchmarks (WebShop-Clarification and ALFWorld-Clarification) in which 50% of tasks are deliberately underspecified, and systematically compare the proposed decomposition against ReAct+UE and Uncertainty-Aware Memory (UAM) across five LLM backbones (GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B, GPT-OSS-120B) on these variants together with the standard WebShop, ALFWorld, and REAL benchmarks for fault detection. Averaged across the five backbones, the proposed decomposition improves clarification F1 on ALFWorld-Clarification by 73% over ReAct+UE and by 36% over UAM, and leads clarification F1 on every backbone on WebShop-Clarification and on four of five backbones on ALFWorld-Clarification, indicating that the gains generalize beyond a single LLM.

## 综合总结
本文提出了一种面向LLM Agent的基于提示词的不确定性分解方法，将动作置信度与请求不确定性解耦，使Agent能在任务欠规范时主动寻求澄清。该方法无需模型内部概率或微调，完美适配黑盒API部署。通过构建两个新的澄清增强基准并在五个主流大模型上测试，证明该方法在澄清F1上显著优于现有基线，为构建高可靠性交互式Agent提供了简单高效的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对交互式LLM Agent的不确定性表达问题，指出了经典偶然/认知不确定性框架的不足，创新性地提出了一种基于提示词的不确定性分解方法，将动作置信度与请求不确定性分离。该方法有效规避了黑盒API、延迟预算和无标签轨迹等实际部署限制，无需logprob或多次采样。实验设计严谨，构建了两个含50%欠规范任务的基准，并在5个不同量级和架构的SOTA模型上验证了泛化性，澄清F1指标提升显著（最高达73%）。

### 实用性 (评分: 9.0/10)
极高的工程落地价值。采用纯提示词方案实现不确定性估计和主动澄清，完全兼容当前主流的黑盒API调用模式，无需额外训练或复杂的采样策略，接入成本极低。该方案直接解决了Agent在模糊指令下盲目执行导致失败的核心痛点，对构建鲁棒的客服、自动化操作等交互式Agent系统具有直接的指导意义。

### 社区活跃度 (评分: 8.0/10)
研究话题极具时效性和前瞻性，触及了当前Agent构建中可靠性不足的关键痛点。虽然文中涉及的未来模型版本（如GPT-5.1等）带有假设性质，但其提出的基准测试和跨模型验证框架符合学术界高标准，来源为arXiv预印本，预计将在Agent和不确定性量化社区引发较高关注和讨论。

## 项目链接
https://arxiv.org/abs/2606.19559
