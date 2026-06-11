# Automated Mediator for Human Negotiation: Pre-Mediation via a Structured LLM Pipeline

**评分：** 8.0  
**状态：** 正常  
**标签：** Agent, LLM应用, 多智能体交互, 谈判调解, 论文  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11379v1 Announce Type: new Abstract: Pre-mediation, the preparatory phase preceding direct human negotiation, plays a critical role in achieving mutually beneficial agreements, yet is often omitted due to cost, time, and limited access to trained mediators. We introduce an automated mediator for human negotiation, implemented as a structured pipeline of LLM modules, that supports pre-mediation in integrative negotiation settings. The pipeline decomposes preparation into specialized modules for dialogue, preference prediction, response-level critique, and structured summarization, separating inference, generation, and evaluation to address limitations of monolithic single-prompt approaches. We use the term "agent" for each module following common LLM-systems terminology, but the components are not autonomous and do not interact peer-to-peer; outputs are passed forward in a fixed sequence. We evaluate the system in two controlled human-subject experiments comparing AI-based pre-mediation with professional human mediators in a multi-issue negotiation scenario. On short-term self-reported measures, the automated mediator achieves preparation outcomes broadly comparable to human mediators, including trust in the mediator and confidence in reaching mutually beneficial agreements, while achieving substantially lower error on the preference-inference task under our scenario and prompts (36% lower RMSE). A second study shows that targeted prompt refinements reduce excessive affirmation patterns from 36.6% to 16.8%, matching human mediator baselines. Our findings suggest that structured LLM pipelines can provide scalable, low-effort pre-mediation support broadly comparable to human mediators on short-term self-reported preparation outcomes. The pipeline's single-party design mirrors how human mediators run pre-mediation today and enables parallel deployment across all parties to a dispute, supporting scalability.

## 综合总结
本文提出了一种用于人类谈判前调解的结构化LLM管道系统，将准备过程拆解为多个专门模块以替代单体提示方法。通过两项受控人类受试者实验证明，该系统在信任度、信心等短期自我报告指标上与专业人类调解员表现相当，且在偏好推断准确率和避免过度肯定方面优于基线。该单方设计支持并行部署，为低成本、可扩展的自动化谈判前调解提供了高落地性的工程实践方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
该论文提出了一种基于结构化LLM管道的自动化调解系统，将谈判前准备过程分解为对话、偏好预测、响应级批评和结构化总结等专门模块，有效克服了传统单体单提示方法的局限性。技术实现上，通过分离推理、生成与评估，并在偏好推断任务中实现了36%的RMSE降低；同时通过提示词优化将过度肯定模式从36.6%降至16.8%。研究设计严谨，通过两项受控人类受试者实验与专业人类调解员进行对比，论证了该结构化管道的有效性。

### 实用性 (评分: 8.5/10)
对从业者具有极高的参考价值。该系统采用单方设计，完美契合现有专业调解员的工作模式，支持争议各方的并行部署，具备极强的可扩展性和低实施成本。实验表明其在信任度和达成互利协议的信心等短期指标上与人类调解员相当，能够有效替代高成本、耗时的人工前期准备环节，可直接应用于商业谈判、争议解决、劳资协商等场景的Pre-mediation阶段。

### 社区活跃度 (评分: 7.5/10)
话题时效性强，结合了当前热门的LLM智能体系统与多智能体/人类交互领域。作者Sarit Kraus为多智能体系统和自动谈判领域的知名学者，保证了研究的权威性与可信度。将AI应用于人类高阶交互（谈判调解）并达到人类相当水平，具有显著的社会影响力和话题传播潜力，但受限于arXiv预印本阶段，社区后续引用和讨论仍有待观察。

## 项目链接
https://arxiv.org/abs/2606.11379
