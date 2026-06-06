# What Should Agents Say? Action-state Communication for Efficient Multi-Agent Systems

**评分：** 8.7  
**状态：** 正常  
**标签：** 多智能体, Agent, 推理成本优化, 通信协议, 论文  
**更新日期：** 2026-06-06  
**来源：** rss  

## 项目描述
arXiv:2606.05304v1 Announce Type: new Abstract: Multi-agent systems (MAS) built on large language models are typically organized around roles, pipelines, and turn schedules, while the content that agents pass to one another is often left as unconstrained natural language. However, this free-form communication can rapidly inflate token usage, consume the shared context window, and ultimately affect both system performance and inference cost. We analyze five common inter-agent communication strategies across two MAS topologies, finding that no fixed strategy is universally optimal. Instead, effective inter-agent messages consistently preserve action-centered information needed by downstream agents. Building on this, we propose the PACT (Protocolized Action-state Communication and Transmission), which treats inter-agent communication as a public state-update problem and projects each raw agent output into a compact action-state record before it enters shared history. Across different MAS topologies, PACT consistently improves the performance-cost trade-off, achieving comparable or stronger task performance with substantially fewer tokens. The gains extend to production coding harnesses: PACT lifts OpenHands' resolve rate at -10% tokens-per-resolved, and is resolve-neutral on SWE-agent while halving input tokens. Our code is publicly available at https://github.com/iNLP-Lab/PACT.

## 综合总结
本文针对大模型多智能体系统（MAS）中自由格式通信导致的Token浪费与性能下降问题，提出PACT框架。该框架将智能体间通信视为公共状态更新问题，通过将原始输出投影为紧凑的动作状态记录，有效压缩了通信体积。实验证明，PACT在多种MAS拓扑结构中均能显著提升性能-成本权衡，在OpenHands和SWE-agent等生产环境中实现了以更少Token达到同等甚至更优的任务解决率，为高效MAS通信提供了重要的工程与理论指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文深入剖析了多智能体系统（MAS）中无约束自然语言通信导致的Token膨胀与上下文污染问题，提出'有效通信应保留以动作为中心的信息'这一核心洞见。基于此设计的PACT框架，将智能体间通信重构为公共状态更新问题，通过投影机制将原始输出压缩为紧凑的动作状态记录，理论依据充分，实验论证严谨。

### 实用性 (评分: 9.0/10)
极具工程落地价值。PACT直接击中当前LLM MAS开发中'推理成本高昂'与'上下文窗口溢出'的核心痛点。在OpenHands和SWE-agent等主流生产级代码框架上的验证表明，该方法能在大幅削减输入Token（甚至减半）的同时保持或提升任务解决率，为从业者提供了可直接复用的通信优化范式。

### 社区活跃度 (评分: 8.5/10)
话题时效性极强，多智能体协作与推理成本控制是当前AI社区的核心关注点。论文在arXiv发布并开源代码，基于业界广泛认可的SWE-bench基准进行测试，结果具有高度说服力，预计将对下一代Agent框架的底层通信设计产生显著影响。

## 项目链接
https://arxiv.org/abs/2606.05304
