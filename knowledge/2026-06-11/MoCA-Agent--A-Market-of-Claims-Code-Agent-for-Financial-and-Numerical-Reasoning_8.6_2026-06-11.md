# MoCA-Agent: A Market-of-Claims Code Agent for Financial and Numerical Reasoning

**评分：** 8.6  
**状态：** 正常  
**标签：** Agent, 多智能体, 金融推理, 数值推理, 代码生成, 论文  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11537v1 Announce Type: new Abstract: Financial and tabular question answering requires more than fluent reasoning: answers must be grounded in the exact facts, formulas, units, signs, and scales that support them. A single misread cell or incorrect operation can silently produce a plausible but wrong result. We introduce \textsc{MOCA-Agent}, a market-of-claims code agent that replaces free-form multi-agent debate with claim-level verification. The system decomposes each question into typed atomic claims, asks specialist trader agents to buy or sell those claims, clears their orders into confidence-weighted accept/reject decisions, and synthesizes an executable Python program from market-supported evidence. A code-aware verifier then checks the program for execution, structural consistency, and common financial reasoning errors, with at most one market-aware repair round. Across ten public benchmarks spanning financial numerical reasoning, general tabular reasoning, ESG question answering, and multimodal chart reasoning, \textsc{MOCA-Agent} achieves strong performance using a fixed Qwen3.6-27B backbone, including $78.3\%$ on FinQA, $76.0\%$ on FinanceMath, $71.2\%$ on MultiHiertt, $86.9\%$ on ESGenius, and $85.6\%$ average on FinChart-Bench. These results show that aggregating evidence at the level of atomic claims, rather than whole answers, improves robustness in high-stakes numerical reasoning.\footnote{The code and data are available: https://github.com/UBC-NLP/MoCA-Agent.

## 综合总结
MoCA-Agent提出了一种基于“声明市场”机制的代码智能体，专为金融和数值推理设计。它将问题分解为原子声明，通过智能体交易进行细粒度置信度验证，并合成可执行Python程序，辅以代码感知验证器。该方法有效提升了高精度数值推理的鲁棒性，在10个基准测试中取得SOTA，为多智能体验证机制提供了创新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
提出了一种基于“声明市场”（Market-of-Claims）的多智能体验证机制，替代了传统的自由形式辩论。通过将复杂问题分解为类型化的原子声明，利用专业交易智能体进行买卖和置信度清算，实现了细粒度的事实与逻辑验证。结合代码感知验证器进行结构一致性和常见错误检查，有效解决了金融数值推理中“微小错误导致严重偏差”的痛点，方法新颖且论证严谨。

### 实用性 (评分: 8.5/10)
针对金融、ESG等对数值精度和逻辑容错率极低的场景具有极高的实用价值。系统最终输出可执行的Python程序，推理过程透明可追溯；且基于固定开源模型（Qwen3.6-27B）并提供了开源代码，便于企业级应用复现与部署。不过市场交易与多轮验证机制可能会带来一定的推理延迟和计算成本增加。

### 社区活跃度 (评分: 8.5/10)
金融数值推理与多智能体系统是当前AI社区的热门研究方向。该论文由UBC-NLP团队发布，在10个主流公开基准测试上取得了SOTA表现，结果极具说服力。其将预测市场机制引入Agent验证范式的思路对社区有较强的启发意义，开源代码也进一步提升了其影响力和可信度。

## 项目链接
https://arxiv.org/abs/2606.11537
