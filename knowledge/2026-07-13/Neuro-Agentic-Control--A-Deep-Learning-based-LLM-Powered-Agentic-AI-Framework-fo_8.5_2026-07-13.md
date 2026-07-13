# Neuro-Agentic Control: A Deep Learning-based LLM-Powered Agentic AI Framework for Controlling Security Controls

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, Agent, 工控安全, 时间序列基础模型, 论文  
**更新日期：** 2026-07-13  
**来源：** rss  

## 项目描述
arXiv:2607.09076v1 Announce Type: new Abstract: Cyberattacks on operational technology are increasingly causing costly downtime and physical damage, exposing the limitations of traditional rule-based monitoring in industrial IoT environments. While Large Language Models (LLMs) have strong semantic reasoning abilities to assist in decision support, their hallucinatory nature presents unacceptable safety liabilities for closed-loop control. This paper introduces a neuro-agentic control framework, a novel architecture that couples an LLM-based planner (i.e., such as Gemini 2.5 Flash-Lite) with a pre-trained Time-Series Foundation Model (TimesFM), to achieve physics-grounded autonomous defense. The paper introduces a ``Counterfactual Physics Injection'' mechanism that simulates the impact of LLM-proposed interventions within the numerical latent space of the foundation model before actuation, while allowing the system to reject hallucinatory or unsafe actions. Evaluated on an industrial dataset (e.g., the Secure Water Treatment (SWaT)) in the context of stochastic attack scenarios, the framework exhibited better performance compared to LSTM and TCN baselines. The Neuro-Agentic Loop prevented five breaches (33.3%) below the threshold versus LSTM (26.7%) and TCN (13.3%), with zero physically invalid (hallucinated) actions executed. These results demonstrate the efficacy of using foundation models as deterministic ``Sentinels'' to safeguard agentic AI in critical infrastructure.

## 综合总结
本文提出了一种神经代理控制框架，通过结合LLM规划器与时间序列基础模型，并引入“反事实物理注入”机制，有效解决了LLM在工业物联网闭环控制中的幻觉问题。在SWaT数据集上的实验表明，该框架在阻止安全违规方面优于LSTM和TCN基线，且实现了零物理无效动作，为关键基础设施的自主防御提供了安全可靠的AI Agent架构。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
提出了一种新颖的神经代理控制框架，将LLM（如Gemini 2.5 Flash-Lite）与时间序列基础模型相结合，解决LLM在闭环控制中的幻觉问题。引入了“反事实物理注入”机制，在执行前于基础模型的潜在空间中模拟LLM提议的干预措施，从而过滤不安全或幻觉动作，技术深度与创新性兼备。

### 实用性 (评分: 8.2/10)
对工业物联网和关键基础设施的安全防护具有极高的参考价值。通过在SWaT数据集上的验证，该框架实现了零物理无效动作，证明了其在安全关键场景下的可靠性，能够指导工业控制系统的自动化防御实践，但实际部署需考虑LLM的实时推理延迟。

### 社区活跃度 (评分: 8.5/10)
话题极具时效性，结合了当前热门的Agent、大模型与时间序列基础模型。针对LLM在关键基础设施控制中的安全痛点提出了解决方案，来源为arXiv预印本，具有较高的学术探讨价值和潜在的行业影响力。

## 项目链接
https://arxiv.org/abs/2607.09076
