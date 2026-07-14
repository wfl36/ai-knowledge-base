# Faithful, Not Corrective: Message-Format Effects in Multi-Hop Agent Relays Are Tier-Dependent

**评分：** 8.5  
**状态：** 正常  
**标签：** Agent, 多智能体, 大模型, 通信协议, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09678v1 Announce Type: new Abstract: When LLM agents hand off information to one another, does the message format matter? Two literatures disagree: format-optimization work reports that structured messages cut cost without hurting accuracy, while format-restriction work finds that imposing structure degrades generation -- and neither measures what happens when a message traverses multiple hops, where copy fidelity, not one-shot generation, dominates. We introduce a controlled relay testbed: briefs of twelve programmatically generated atomic facts are re-encoded hop-by-hop in five formats (free NL, precision-instructed NL, JSON, triples, key-value) over six hops, scored by a fixed strong grader against programmatic ground truth, across two relay-capability tiers, a cognitive-load condition, and a paired-fork error injection. We find that message-format effects are tier-dependent. (i) Under faithful-relay instructions a strong relay is nearly lossless -- the documented "telephone-game" collapse does not occur -- and adding per-hop cognitive load leaves format-level fidelity unchanged (within +/-1.8 points) while raising generation cost by 24-53%. (ii) Under a weak (1.5B) relay the across-format spread of six-hop recall grows by a factor of 8.7 (from 2.3 to 20.5 points), driven by two opposing mechanisms -- an encoding toll paid by the rigid formats and drift resistance specific to the fixed-key JSON schema -- that flip the format ranking in transit. (iii) In a paired-fork injection, an injected wrong value, once present, persists to the final hop in 83-100% of chains in every format, closely matching each format's retention of the true value, with no detectable collateral damage to neighboring facts. Structure buys a faithful, error-localizing channel -- not an error-correcting code -- and format choice should follow the weakest relay in the pipeline.

## 综合总结
本论文研究了多智能体多跳信息传递中消息格式的影响，解决了现有文献在格式优化与限制上的分歧。通过构建受控中继测试平台，作者发现格式效应高度依赖于智能体的能力层级：强模型几乎无损且不受认知负荷影响；弱模型下格式差异显著放大，JSON因抗漂移能力排名翻转。更重要的是，研究揭示结构化格式仅提供'保真与错误局部化'通道，而非纠错机制，注入的错误会高度持续。最终提出工程指导：格式选择应匹配管道中最弱的节点。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文精准定位了多智能体多跳通信中格式影响的争议盲区，实验设计严谨，通过5种格式、6跳传递、强弱层级对比及错误注入机制，量化了格式效应。核心洞见'结构化是保真通道而非纠错码'深刻且反直觉，揭示了强弱模型下格式排名翻转的底层机制（编码代价 vs 漂移抵抗），研究深度与新颖性极高。

### 实用性 (评分: 8.5/10)
对多Agent系统开发者具有直接指导意义。明确了'格式选择取决于最弱环节'的工程原则，打破了'结构化能自动纠错'的误区，为Agent间通信协议设计、消息格式选型（NL vs JSON等）及错误传播控制提供了可操作的实践依据，适用范围覆盖各类多智能体编排框架。

### 社区活跃度 (评分: 8.0/10)
多智能体协作是当前大模型领域的核心热点，消息传递格式是工程落地痛点，时效性极强。虽作者权威度尚待社区进一步验证，但严谨的实验设计和反直觉的结论极易引发工程界与学术界的关注与讨论，具备较高潜在影响力。

## 项目链接
https://arxiv.org/abs/2607.09678
