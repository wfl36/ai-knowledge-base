# Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents

**评分：** 8.8  
**状态：** 正常  
**标签：** Agent, 上下文工程, 大模型, 工具调用, 论文, 工程实践  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.10209v1 Announce Type: new Abstract: Large language models deployed as autonomous agents for enterprise workflows face a key challenge: verbose tool responses from enterprise systems can cause context overflow, stale-state errors, and high inference cost. We study this problem in automated expense itemization in Microsoft Dynamics 365 Finance and Operations using Model Context Protocol tools. We evaluate four GPT-5 configurations on a 50-task hotel expense benchmark: no user model, full conversation history, context pruned to the last 5 tool call/response pairs, and pruning with automated summarization. Results are averaged across 5 independent runs, with the user model held constant for the context-engineering comparison. The no-user-model baseline achieves only 8.0% complete itemization. Full-context retention improves completion to 71.0%, but consumes 1,480,996 tokens and 14.56 hours per benchmark. Pruning to the last 5 tool calls improves completion to 79.0% while reducing token use to 535,274 and runtime to 5.39 hours. Adding summarization achieves the best result: 91.6% complete itemization and 99.64% average amount itemized, with 553,374 tokens and 5.79 hours. We further report confidence intervals, effect-size analysis, sensitivity over pruning and summary windows, failure analysis, results across five expense types grouped into three categories, and cross-model evidence with Claude Sonnet 4.5. These results show that, for this class of enterprise tool-use workflow, selective retention of recent tool interactions plus compact summarization can improve both reliability and efficiency compared with full-history retention.

## 综合总结
本文针对企业级LLM Agent在长周期工具调用中面临的上下文溢出、状态过时和高成本问题，在微软Dynamics 365场景下评估了四种上下文管理策略。实验表明，相比保留完整对话历史，采用'保留最近5次工具调用+自动摘要'的上下文工程方法，不仅将任务完成率从71.0%提升至91.6%，还将Token消耗和运行时间缩减了60%以上。该研究通过详实的消融实验和跨模型验证，有力证明了在Agent工作流中'少即是多'的高效性与可靠性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
针对LLM Agent长上下文痛点，提出了'修剪+摘要'的上下文工程策略。实验设计严谨，包含基线对比、敏感性分析、效应量评估及跨模型验证（GPT-5与Claude Sonnet 4.5），论证了在长周期工具调用中'少即是多'的洞见，具备较高的实证研究深度。

### 实用性 (评分: 9.5/10)
对Agent开发者具有极高的实操指导价值。提出的'最近K次交互保留+历史摘要压缩'方案简单易实现，能直接解决企业级Agent长流程中Token成本高、上下文溢出和陈旧状态干扰的痛点，立竿见影地提升系统可靠性与经济性。

### 社区活跃度 (评分: 9.0/10)
研究直击当前Agent落地最棘手的上下文管理痛点，时效性极强。基于微软Dynamics 365真实企业场景，实验数据详实，且使用了GPT-5等前沿模型进行验证，来源权威，对工业界和学术界均有较高影响力和参考价值。

## 项目链接
https://arxiv.org/abs/2606.10209
