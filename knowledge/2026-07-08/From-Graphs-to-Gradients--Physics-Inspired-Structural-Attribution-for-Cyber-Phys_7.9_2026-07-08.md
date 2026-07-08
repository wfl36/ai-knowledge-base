# From Graphs to Gradients: Physics-Inspired Structural Attribution for Cyber-Physical IoT Systems and Beyond

**评分：** 7.9  
**状态：** 正常  
**标签：** 可解释AI, 因果推断, 信息物理系统, 物联网, 统计力学, 论文  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05563v1 Announce Type: new Abstract: Interpretable explanation methods in Artificial Intelligence aim to uncover the underlying causes and their effects, enabling a deeper understanding of why a system behaves in a certain way under different inputs. Unlike traditional explainability methods, which mainly highlight correlations between input and output variables, causal explanation focuses on interventional questions. By doing so, it provides more robust insights, helping users understand automated decisions, especially in high-risk domains. Recovering an explicit directed causal structure, however, is often impractical in large-scale, hybrid cyber-physical systems with feedback loops and partial observability. This paper introduces a novel framework inspired by statistical mechanics that instead models variable dependencies through an undirected, energy-based representation of cyber-physical IoT systems. Our approach enables rigorous dependency-aware attribution by analysing how variations in the energy landscape reflect the influence of individual components, without recovering a directed causal graph. It also supports reasoning about perturbation effects across hybrid interactions, providing reliable explanations of abnormal behaviours. We empirically examined our framework through simulations on an industrial IoT testbed with hybrid continuous and discrete variables, demonstrating higher attribution accuracy, improved robustness and better scalability than state-of-the-art graph-based approaches. While the attributions are not intended to fully recover the system's generative dynamics, they provide valuable, dependency-aware explanations supporting both human interpretation and downstream predictive and diagnostic tasks. Although demonstrated in industrial IoT security, our framework also applies to other high-dimensional cyber-physical and socio-technical systems requiring principled, structural explanations.

## 综合总结
本文提出了一种受统计力学启发的无向能量表示框架，用于解决信息物理IoT系统中难以恢复有向因果图的结构归因问题。该框架通过分析能量景观变化实现依赖感知归因，在工业物联网测试床中表现出优于现有图方法的准确性、鲁棒性和可扩展性，为高维混合系统的异常解释与诊断提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
论文提出了一种基于统计力学的新型框架，通过无向能量表示法对信息物理IoT系统进行结构归因，巧妙地绕过了在混合反馈系统中恢复有向因果图的难题，方法新颖且论证严谨。

### 实用性 (评分: 7.5/10)
该框架在工业物联网测试床上验证了其在混合变量系统中的归因准确性、鲁棒性和可扩展性，对安全诊断和预测任务有直接指导意义，但能量景观分析对工程落地有一定门槛。

### 社区活跃度 (评分: 7.5/10)
因果可解释性是当前AI领域的前沿热点，该文针对信息物理系统这一高风险领域提出创新解法，具备较高的时效性和学术权威性，有望在复杂系统归因领域产生广泛影响。

## 项目链接
https://arxiv.org/abs/2607.05563
