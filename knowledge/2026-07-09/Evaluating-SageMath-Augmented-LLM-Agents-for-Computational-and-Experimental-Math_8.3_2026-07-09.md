# Evaluating SageMath-Augmented LLM Agents for Computational and Experimental Mathematics

**评分：** 8.3  
**状态：** 正常  
**标签：** 大模型, Agent, AI4Math, 推理, 计算数学, 论文, 评估基准  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.06820v1 Announce Type: new Abstract: Recent advances in AI for Mathematics have focused largely on autoformalization and theorem proving, leaving the role of Computer Algebra Systems (CAS) in agentic LLM workflows underexplored. We propose a ReAct-style agentic setup that combines LLM reasoning with verifiable feedback from SageMath, together with Context7 for the up-to-date documentation. We evaluate this agentic setup across frontier models for solving research-level mathematical problems from the RealMath benchmark in a setting that emulates a computational-mathematics research loop. We also propose a refinement to the RealMath benchmark by introducing a multi-step post-processing procedure and a multi-stage validation pipeline, both of which improve the quality and reliability of the extracted problem set. Our experiments reveal substantial performance gains from SageMath access across all evaluated models on +9.7~pp on average, the gains range from 1.5~pp to 27.8~pp and narrow the gap between open-weight and closed models. Qwen~3.7-Max benefits from SageMath the most, while GPT-5.5 achieves the highest solve rate of $75.2\%$ and the lowest token usage among tool-enabled configurations. Our findings suggest that CAS-augmented agents represent a promising direction for assisting mathematicians in computational exploration, and we believe that this work is a step towards automated conjecture discovery. The project repository is available online.

## 综合总结
本文提出了一种结合LLM与SageMath计算机代数系统的ReAct风格Agent框架，用于解决计算与实验数学问题。研究改进了RealMath基准的提取与验证流程，实验表明CAS接入使各前沿模型性能平均提升9.7pp，其中Qwen 3.7-Max受益最大，GPT-5.5达到75.2%的最高解决率。该工作验证了CAS增强Agent在辅助数学计算探索和自动化猜想发现方面的有效性，为AI4Math提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文在AI for Math领域提出了重要的视角转换，从主流的自动形式化和定理证明转向计算与实验数学，填补了CAS在Agent工作流中作用的探索空白。技术方案上采用ReAct风格结合SageMath与Context7（提供最新文档），并针对RealMath基准提出了多步后处理和多阶段验证管道，增强了评估的严谨性。实验论证扎实，揭示了CAS接入对不同前沿模型带来的显著性能提升（平均+9.7pp），技术深度和新颖性较高。

### 实用性 (评分: 8.0/10)
对计算数学研究者和AI4Math工程师具有极高的实践指导价值。SageMath作为成熟的开源CAS工具，与LLM结合的框架已开源，从业者可直接复现或借鉴此范式构建数学计算Agent。该框架不仅适用于学术研究中的计算探索，也为自动化猜想发现提供了可落地的工程路径，适用范围明确且工具链成熟。

### 社区活跃度 (评分: 8.5/10)
AI4Math是当前大模型推理能力突破的核心赛道之一，本文切入的'计算代数系统增强Agent'方向极具时效性。评估涵盖了GPT-5.5、Qwen 3.7-Max等最新前沿模型，紧跟社区发展脉搏。论文开源了项目仓库，增强了结果的可信度与社区影响力，其揭示的'缩小开源与闭源模型差距'的现象也将引发广泛讨论。

## 项目链接
https://arxiv.org/abs/2607.06820
