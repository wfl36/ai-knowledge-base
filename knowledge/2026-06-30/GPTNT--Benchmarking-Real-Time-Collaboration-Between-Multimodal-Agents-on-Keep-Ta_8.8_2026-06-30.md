# GPTNT: Benchmarking Real-Time Collaboration Between Multimodal Agents on Keep Talking And Nobody Explodes

**评分：** 8.8  
**状态：** 正常  
**标签：** 多模态, Agent, 多智能体协作, 实时交互, 基准测试, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28514v1 Announce Type: new Abstract: Multimodal models are increasingly deployed to solve tasks collaboratively with humans or other artificial agents. Existing benchmarks show that these models possess many of the required component capabilities, but the conditions that coincide in collaboration, including time pressure, information asymmetry, and imperfect communication, are usually studied in isolation. We introduce GPTNT, a benchmark built on the cooperative video game Keep Talking and Nobody Explodes, in which two agents must coordinate to defuse procedurally generated bomb puzzles against a live countdown. One agent can see and manipulate the bomb but does not have the defusal instructions; the other has the instructions but cannot see or manipulate the bomb. Neither agent can succeed alone: success requires effective and efficient communication. Unlike turn-based proxies, GPTNT requires agents to act asynchronously and communicate in real time. GPTNT is designed to separate collaboration from reliance on memorized solutions: the instruction manual, the partner, or both can be withheld to isolate what a model derives in the moment from what it already knows. We show that GPTNT poses a substantial challenge for state-of-the-art systems: none of the closed- or open-source models we test defuses a single bomb in real time, a bar that human players clear. Through controlled experiments, we identify critical weaknesses in state tracking, efficient action under time pressure, ambiguity handling, and error recovery. We release GPTNT as a benchmark for collaborative performance that current evaluations leave unmeasured. Because it runs on the real game, GPTNT benefits from procedural generation and inherits a living modding community, allowing the benchmark to evolve as models improve rather than being solved once and retired.

## 综合总结
本文提出了GPTNT基准，基于合作游戏《保持通话，没人爆炸》评估多模态智能体在实时、异步、信息不对称及时间压力下的协作能力。实验表明，当前所有SOTA模型在实时条件下均无法完成拆弹任务，暴露了它们在状态跟踪、高压行动和错误恢复等方面的严重不足。该基准通过控制变量有效分离了模型的记忆与推理能力，且基于真实游戏支持持续演进，为多智能体实时协作研究提供了极具挑战性和前瞻性的评估标准。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
创新性地基于《保持通话，没人爆炸》游戏构建了GPTNT基准，将多智能体协作置于实时、异步、信息不对称和时间压力的复合极端条件下。通过控制变量（隐藏手册或搭档）有效分离了模型的记忆依赖与即时推理能力，深刻揭示了当前SOTA模型在状态跟踪、高压行动、歧义处理及错误恢复等维度的根本性缺陷，论证严谨且极具研究深度。

### 实用性 (评分: 8.5/10)
对开发实时交互Agent和多智能体系统的从业者具有极高的参考价值。明确指出了当前模型在“实时协作”这一关键场景下的短板，为后续Agent的优化（如提升状态跟踪和错误恢复能力）提供了清晰的指引。基准基于真实游戏且支持Mod社区，具备长期演进的工程落地潜力，不易被静态解决后废弃。

### 社区活跃度 (评分: 9.0/10)
紧扣当前AI Agent与多模态协作的前沿热点，时效性极强。论文揭示的“所有SOTA模型在实时条件下均无法拆弹，而人类可以”的结论极具冲击力与话题性。来源为arXiv学术论文，可信度高，且基准设计具备可持续演进特性，有望在AI社区产生深远影响并引发广泛讨论。

## 项目链接
https://arxiv.org/abs/2606.28514
