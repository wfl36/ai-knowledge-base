# Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, MCP, 推理, 大模型, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12674v1 Announce Type: new Abstract: Compact language models (LMs) reduce cost, latency, and deployment risk for tool agents. Yet MCP-style tool use requires more than isolated function calling: an agent must discover tools from live catalogs, satisfy schemas, preserve dependencies across intermediate outputs, and ground final responses in executed evidence. Small planners often generate plausible workflow graphs that fail under tool resolution, parameter validation, dependency tracking, or execution. We argue that this failure mode is poorly handled by small-corpus distillation. A few hundred teacher traces can teach workflow format, but rarely cover the recovery behavior needed to repair failed plans over changing tool catalogs. We introduce Evoflux, an inference-time evolutionary search method that treats compact tool use as the repair of executable tool workflows. It evolves typed workflow graphs through structured edits, execution feedback, adaptive intensity, meta-guided redesign, and diversity pruning. On held-out MCP-Bench tasks spanning live MCP servers and 250 tools, Evoflux raises execution feasibility from roughly 3% to 17-24% across small planners. In contrast, SFT and SFT+DPO on the same search-mined data match, underperform, or collapse below zero-shot performance; ReAct reaches higher peaks, but with higher variance and token cost. These results show that execution-grounded search is more reliable under scarce teacher-trace budgets.

## 综合总结
本文提出Evoflux，一种针对紧凑型Agent的推理时进化搜索方法，解决小模型在MCP工具调用中工作流易失败的问题。通过在推理时对工作流进行结构化编辑和执行反馈修复，Evoflux在MCP-Bench上将执行可行性从3%提升至17-24%，显著优于SFT、DPO及ReAct等基线，证明了在稀缺数据下推理时搜索优于传统微调范式，为低成本Agent部署提供了新思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对紧凑型语言模型在MCP风格工具调用中易生成不可执行工作流的痛点，创新性地提出了Evoflux推理时进化搜索方法。该方法摒弃了传统的微调范式，将工具使用视为对可执行工作流的修复，通过结构化编辑、执行反馈、自适应强度和元引导等机制演化类型化工作流图，技术路径新颖且论证严谨。

### 实用性 (评分: 9.0/10)
对工业界部署轻量级Agent具有极高的参考价值。传统SFT/DPO在工具动态变化和稀缺教师轨迹下表现不佳甚至崩溃，而Evoflux通过推理时搜索修复工作流，无需大量训练数据即可显著提升执行可行性，为低成本、低延迟的紧凑模型Agent落地提供了切实可行的工程实践指导。

### 社区活跃度 (评分: 9.0/10)
紧密结合当前AI Agent领域最热门的MCP协议，时效性极强。作者团队包含IBM等知名机构研究员，权威性高。在包含250个工具的MCP-Bench上取得的显著性能提升（3%至17-24%），对社区探索小模型Agent能力和推理时计算具有较大影响力。

## 项目链接
https://arxiv.org/abs/2606.12674
