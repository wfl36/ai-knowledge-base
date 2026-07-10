# DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, Web Agent, 自进化, 自蒸馏, 多跳问答, 论文  
**更新日期：** 2026-07-10  
**来源：** rss  

## 项目描述
arXiv:2607.07820v1 Announce Type: new Abstract: Training tool-use agents to improve from their own experience remains challenging, as supervised fine-tuning relies on fixed teacher-distilled trajectories, while sparse-reward reinforcement learning provides weak supervision for long-horizon interactions. We present DeepSearch-Evolve, a self-distillation framework for web agents built on DeepSearch-World, a deterministic and verifiable environment with reproducible search and page-reading tools. DeepSearch-World contains 420K multi-hop QA tasks constructed from entity-level random walks and supports key agentic cognitive behaviors useful for self-evolving, including progress verification, grounded reflection, and failure recovery. DeepSearch-Evolve iteratively performs trajectory generation, filtering, data mixing, and fine-tuning to train stronger agents. Without distillation from more capable models, DeepSearch-World-9B achieves competitive performance compared with open-source agents, reaching 31.2% on BrowseComp, 61.5% on GAIA, and 93.4% on HotpotQA, showing that verifiable environments enable scalable self-evolution for long-horizon web agents. We will release the environment, 420K training pool, validation set, model, and code to facilitate future research on self-improving deep search agents.

## 综合总结
本文提出了DeepSearch-World（一个包含42万任务的可验证确定性Web环境）和DeepSearch-Evolve（自蒸馏框架）。该框架通过迭代式的轨迹生成、过滤与微调，使Agent在无需强教师模型的情况下实现自我进化，并支持进度验证、反思和失败恢复。其9B模型在BrowseComp、GAIA和HotpotQA上取得了极具竞争力的表现，证明了可验证环境对长交互Agent自进化的关键作用，项目将完全开源。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对长交互Web Agent训练中SFT依赖固定轨迹和RL稀疏奖励监督弱的痛点，创新性地提出了基于可验证环境的自蒸馏框架DeepSearch-Evolve。构建了包含42万任务的DeepSearch-World环境，支持进度验证、基于事实的反思与失败恢复等关键认知行为，实现了无需强教师模型蒸馏的自我进化闭环，技术路径新颖且论证严谨。

### 实用性 (评分: 9.0/10)
框架的迭代进化流程（轨迹生成、过滤、数据混合、微调）对Agent工程实践具有极高的参考价值。可验证环境的构建思路可直接指导RAG和Web Agent的开发。项目承诺全开源（环境、数据池、模型和代码），大幅降低了从业者的复现与应用门槛，落地潜力极大。

### 社区活跃度 (评分: 8.5/10)
Web Agent的自我进化与工具使用是当前AI社区的核心前沿话题，时效性极强。论文在GAIA、BrowseComp等高难度基准上，仅用9B模型即取得了与开源领先模型竞争的表现，数据扎实，可信度高。该工作为自进化Agent提供了新范式，且全开源承诺将带来显著的社区影响力。

## 项目链接
https://arxiv.org/abs/2607.07820
