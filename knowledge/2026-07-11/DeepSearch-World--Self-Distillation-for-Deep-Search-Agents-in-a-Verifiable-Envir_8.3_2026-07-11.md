# DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, 自进化, 自蒸馏, 搜索, 强化学习, 论文  
**更新日期：** 2026-07-11  
**来源：** rss  

## 项目描述
arXiv:2607.07820v1 Announce Type: new Abstract: Training tool-use agents to improve from their own experience remains challenging, as supervised fine-tuning relies on fixed teacher-distilled trajectories, while sparse-reward reinforcement learning provides weak supervision for long-horizon interactions. We present DeepSearch-Evolve, a self-distillation framework for web agents built on DeepSearch-World, a deterministic and verifiable environment with reproducible search and page-reading tools. DeepSearch-World contains 420K multi-hop QA tasks constructed from entity-level random walks and supports key agentic cognitive behaviors useful for self-evolving, including progress verification, grounded reflection, and failure recovery. DeepSearch-Evolve iteratively performs trajectory generation, filtering, data mixing, and fine-tuning to train stronger agents. Without distillation from more capable models, DeepSearch-World-9B achieves competitive performance compared with open-source agents, reaching 31.2% on BrowseComp, 61.5% on GAIA, and 93.4% on HotpotQA, showing that verifiable environments enable scalable self-evolution for long-horizon web agents. We will release the environment, 420K training pool, validation set, model, and code to facilitate future research on self-improving deep search agents.

## 综合总结
本文提出DeepSearch-Evolve自蒸馏框架及DeepSearch-World可验证环境，解决Web Agent依赖强模型蒸馏与长交互稀疏奖励的痛点。通过构建包含42万条多跳QA的确定性环境，支持进度验证、反思与失败恢复，实现Agent闭环自我进化。实验表明，无需更强模型蒸馏，9B模型在BrowseComp(31.2%)和GAIA(61.5%)等基准上达到开源领先水平，验证了可验证环境对Agent自进化的关键作用，项目将全栈开源。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文针对工具使用Agent依赖固定教师轨迹SFT和长交互稀疏奖励RL监督弱的痛点，提出了基于可验证环境的自蒸馏框架DeepSearch-Evolve。其创新点在于构建了确定性、可复现的DeepSearch-World环境，支持进度验证、基于事实的反思和失败恢复等核心认知行为，通过迭代式轨迹生成、过滤与混合微调实现自我进化。无需更强模型蒸馏即可在9B模型上取得优异表现，论证严谨且方法具有较高新颖性。

### 实用性 (评分: 8.0/10)
对从业者具有极高的实践指导价值。首先，完全摆脱了对昂贵闭源大模型（如GPT-4）蒸馏数据的依赖，大幅降低训练成本；其次，承诺开源环境、42万训练池、验证集、模型与代码，提供了开箱即用的自进化Web Agent基座；最后，其提出的'可验证环境+自蒸馏'范式可直接迁移至其他需要长交互的工具调用场景中。

### 社区活跃度 (评分: 8.5/10)
Agent自我进化与深度搜索是当前AI社区最前沿且备受关注的方向。论文在极具挑战性和权威性的GAIA、BrowseComp基准上取得了31.2%和61.5%的高分，显著超越了同量级开源模型，结果极具说服力。全栈开源的承诺将进一步放大其在开源社区和学术圈的影响力，有望成为Web Agent自进化研究的新基线。

## 项目链接
https://arxiv.org/abs/2607.07820
