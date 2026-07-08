# Memory in the Loop: In-Process Retrieval as ExtendedWorking Memory for Language Agents

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, 大模型, 记忆机制, 工程实践, 推理  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05690v1 Announce Type: new Abstract: Language agents run a loop - observe, reason, act - but the memory they reason over sits outside it: a store queried at most once per turn. We study the regime where memory moves inside the loop, read and written on every step. The obstacle has always been latency: networked stores answer in tens to hundreds of milliseconds, and in-loop retrieval can inflate end-to-end latency by up to 83x when retrieval is expensive. Prior work manages that cost rather than questioning it: serving-layer scheduling hides it, "memory-first" designs ration retrieval to once per turn. We argue latency is a property of where the store lives, not the in-loop pattern: an in-process store answers in ~100us, three orders of magnitude below the network regime, and at that speed the per-step tax collapses. By the extended-mind thesis's parity principle, a store fast enough to be constantly and directly available becomes extended working memory, not a tool the agent merely consults. The premise is causal: holding a fixed per-turn memory-latency budget and varying only the store's answer speed, redundant actions rise monotonically with latency - 0.0 of 12 at in-process speed, 7.2 of 12 at a 110ms cloud round trip (gpt-5-nano, gpt-5-mini; exact permutation p=0.0079). We demonstrate the regime end-to-end: across four GPT-5-class models under a bounded window, recall improves from 0/5 to 3.6-4.8/5 with in-loop memory, store ops at p50 80-165us - though an instructed restate-every-reply baseline also solves it perfectly, at a token cost that grows with the working set. The store never lost a fact in any run (244 of 244 writes kept); every miss traces to the agent's read policy, not the store. Our measurements also relocate the bottleneck: the dominant per-step cost is embedding (~200-400ms over the network); pairing the in-process store with a small local embedder returns the complete operation to a measured ~40us.

## 综合总结
本文针对语言智能体中记忆检索延迟过高的痛点，提出将记忆移入执行循环内部的'进程内检索'机制。研究发现，传统网络存储的延迟会导致智能体产生大量冗余动作，而采用进程内存储（延迟约100us）可消除冗余动作并显著提升召回率（从0/5提升至3.6-4.8/5）。结合本地嵌入模型，系统整体操作延迟可降至约40us，使记忆真正成为智能体的'扩展工作记忆'，为下一代高性能Agent架构提供了重要的工程与理论参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了将记忆检索移入语言智能体的观察-推理-行动循环内部的新颖视角，打破了传统每轮仅查询一次记忆的范式。通过引入'进程内存储'（in-process store），将检索延迟从网络级别的百毫秒级降至微秒级（约100us），论证严谨且具有深度。基于扩展心智理论的奇偶性原则，证明了足够快的存储可转化为智能体的扩展工作记忆。因果实验设计精巧，清晰揭示了延迟与冗余动作的单调递增关系（0/12 vs 7.2/12），并精准定位了瓶颈在于网络嵌入而非存储本身，技术洞见深刻。

### 实用性 (评分: 7.5/10)
对AI智能体架构设计具有极高的工程指导价值。指出了当前Agent架构中隐藏的性能瓶颈，并提供了可落地的解决方案：使用进程内存储替代网络存储，配合本地小型嵌入模型，可将完整操作延迟降至约40us。这为构建低延迟、高可靠性的Agent记忆系统提供了明确的技术路径，尤其适用于需要高频记忆访问和严格延迟限制的复杂任务场景。

### 社区活跃度 (评分: 8.0/10)
话题时效性极强，触及当前大模型智能体（Agent）研发的核心痛点——记忆机制与延迟问题。虽然摘要中提及的'gpt-5-nano/mini'及'2026年发布时间'可能为前瞻性测试或版本标识，但其揭示的架构优化方向符合行业发展趋势。将记忆从'外部工具'重新定义为'扩展工作记忆'的观点，对Agent开发社区具有启发性和较高的讨论热度。

## 项目链接
https://arxiv.org/abs/2607.05690
