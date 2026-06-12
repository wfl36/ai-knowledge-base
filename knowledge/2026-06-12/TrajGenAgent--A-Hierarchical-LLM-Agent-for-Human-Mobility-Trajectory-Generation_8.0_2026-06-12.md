# TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, Agent, 时空计算, 轨迹生成, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12657v1 Announce Type: new Abstract: Human mobility data is important for transportation, urban planning, and epidemic control, but large-scale trajectory collection is often costly and privacy-constrained, motivating realistic synthetic trajectory generation. Existing LLM-based generators typically rely on either prompt engineering, which preserves zero-shot reasoning but lacks fine-grained spatiotemporal grounding, or trajectory-level fine-tuning, which improves statistical precision but incurs substantial computational cost and may weaken general reasoning. We propose TrajGenAgent, a semantic-aware hierarchical LLM-agent framework for human mobility trajectory generation without model fine-tuning. TrajGenAgent uses a two-stage orchestrator-worker design: an LLM first synthesizes an individual- and weekday-conditioned activity chain from historical evidence via in-context learning, and a deterministic workflow then grounds each activity into a complete visit using personalized POI retrieval, distance-aware location selection, kinematics-aware travel-time propagation, and LLM-based duration estimation. To evaluate realism beyond aggregate spatiotemporal statistics, we introduce an anomaly-detection-based evaluation framework using two complementary detectors to assess behavioral and semantic plausibility. Experiments on benchmark and large-scale simulation datasets show that TrajGenAgent improves spatiotemporal fidelity, semantic coherence, and individual-specific behavioral realism over representative neural and LLM-based baselines, while avoiding parameter updates.

## 综合总结
本文提出了TrajGenAgent，一个免微调的分层LLM代理框架，用于生成人类移动轨迹。该框架采用两阶段设计：LLM通过上下文学习生成个性化活动链，确定性工作流负责时空落地，有效兼顾了语义连贯性与时空物理约束。同时引入了基于异常检测的新颖评估框架。实验表明，该方法在多项指标上优于现有基线，且无需高昂的微调成本，为交通规划与城市计算等领域的轨迹合成提供了高保真、低门槛的实用解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该论文提出了TrajGenAgent，一个无需微调的分层LLM代理框架，巧妙解决了现有LLM轨迹生成中提示工程缺乏细粒度时空基础与微调导致计算成本高及通用推理削弱之间的矛盾。其两阶段orchestrator-worker设计（LLM上下文学习生成活动链+确定性工作流进行时空落地）逻辑严谨，兼顾了语义推理与物理约束。此外，引入基于异常检测的评估框架，超越了传统的聚合统计指标，从行为和语义合理性双重维度评估，研究深度与方法新颖性俱佳。

### 实用性 (评分: 8.0/10)
该框架无需模型参数更新，极大降低了计算成本和部署门槛，使得从业者能够直接利用现成LLM进行大规模轨迹生成。其生成的轨迹在时空保真度、语义连贯性和个体行为真实性上表现优异，可直接应用于交通仿真、城市规划、疫情控制等缺乏真实数据或存在隐私限制的实际场景，具有极高的工程落地与应用价值。

### 社区活跃度 (评分: 7.5/10)
论文聚焦于LLM在空间计算与轨迹生成领域的交叉应用，属于当前AI Agent和智慧城市的热点方向。arXiv预印本发布，作者团队在相关领域具有一定研究基础。虽然轨迹生成相对通用大模型属于垂直领域，但其在Agent工作流设计和免微调方案上的探索，对LLM落地应用社区有较好的启发性和参考价值，具备一定的影响力和时效性。

## 项目链接
https://arxiv.org/abs/2606.12657
