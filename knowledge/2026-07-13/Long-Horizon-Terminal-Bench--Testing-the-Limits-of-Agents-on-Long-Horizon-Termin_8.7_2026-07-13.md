# Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 评估基准, 长周期规划, 软件工程, 论文  
**更新日期：** 2026-07-13  
**来源：** rss  

## 项目描述
arXiv:2607.08964v1 Announce Type: new Abstract: AI agents have become capable of autonomously completing short, well-specified tasks. However, existing terminal benchmarks largely focus on simple problems that finish within minutes and are evaluated only by their final outcome. This setup overlooks intermediate progress and partial solutions, yielding sparse reward signals and an incomplete picture of agent capability. We introduce Long-Horizon-Terminal-Bench, a terminal benchmark of 46 long-horizon tasks spanning nine categories, including experiment reproduction, software engineering, multimodal analysis, interactive games, and scientific computing. Each task follows a Terminal-Bench-style setup with a reference solution or simulation engine, but is further decomposed into fine-grained graded subtasks. This design enables dense intermediate rewards and partial credit, allowing evaluation to capture not only whether an agent reaches the final goal, but also how far it progresses on open-ended workflows. Tasks in Long-Horizon-Terminal-Bench typically require hundreds of episodes and minutes to hours of execution, stressing long-horizon planning, long-context management, and iterative debugging rather than one-shot problem solving. We evaluate 15 frontier models and find that agents consume on average 9.9M tokens per task, with roughly 231 episodes and 85.3 minutes of execution time per run, making Long-Horizon-Terminal-Bench more demanding than prior terminal-based benchmarks. Even the strongest tested model achieves 15.2% pass@1 at a partial-reward threshold of 0.95 and 10.9% at a perfect-reward threshold of 1.0, while the mean pass rate across models is 4.3% and 1.7% under the two thresholds, respectively. These results reveal headroom for improvement. We further analyze failure modes and error patterns, and release Long-Horizon-Terminal-Bench to support future progress on long-horizon terminal agents.

## 综合总结
本文提出了Long-Horizon-Terminal-Bench，一个专注于长周期终端任务的Agent评估基准。针对现有基准稀疏奖励和忽略中间进度的问题，该研究通过分解46个跨9大类的复杂任务，引入了密集中间奖励和部分学分机制。对15个前沿模型的测试表明，当前Agent在长周期任务上表现堪忧（最强模型完美完成率仅10.9%），平均需消耗9.9M tokens和85.3分钟执行时间。该工作揭示了现有模型在长程规划和迭代调试上的巨大短板，为未来长周期Agent的研发与评估提供了关键工具和深刻见解。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究在Agent评估方法论上具有显著深度。针对现有终端基准测试仅关注短期任务和稀疏奖励（仅看最终结果）的局限，创新性地提出了基于密集中间奖励和部分学分的评估框架。通过将长周期、复杂工作流（如软件工程、科学计算等）分解为细粒度子任务，不仅评估最终目标达成率，更量化了Agent的中间进度。对15个前沿模型的大规模实验极具说服力，揭示了当前SOTA模型在长上下文管理和迭代调试中的严重不足（最强模型完美完成率仅10.9%），并深入分析了失败模式，技术论证严谨且富有洞见。

### 实用性 (评分: 9.0/10)
对AI Agent开发者和研究人员具有极高的实践指导价值。该基准填补了长周期、高复杂度终端任务评估的空白，其密集奖励机制能帮助开发者精准定位Agent在多步工作流中的崩溃点（如规划失败、上下文遗忘等），而非仅仅得到一个失败结果。9个类别46个任务的覆盖面广泛，贴近真实世界的复杂工程场景，可直接作为检验和优化Agent长程规划与纠错能力的标准化测试床。

### 社区活跃度 (评分: 8.5/10)
话题时效性极强，直击当前AI Agent领域从“短步长玩具任务”向“长周期真实任务”迈进的核心痛点。发布时间标注为2026年，处于Agent技术深水区探索的前沿。评估了15个前沿模型，数据详实（平均消耗9.9M tokens/任务），极具权威性和参考价值。该基准的发布有望引发社区对Agent长程规划与上下文管理能力的重新审视，推动评估标准从结果导向向过程导向演进。

## 项目链接
https://arxiv.org/abs/2607.08964
