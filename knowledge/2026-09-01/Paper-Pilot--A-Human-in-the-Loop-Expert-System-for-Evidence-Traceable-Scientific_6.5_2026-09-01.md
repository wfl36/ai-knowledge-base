# Paper Pilot: A Human-in-the-Loop Expert System for Evidence-Traceable Scientific Manuscript Generation in Applied Sciences

**评分：** 6.5  
**状态：** 正常  
**标签：** LLM Agent, 科研写作, 人类在环, AI 治理, 引用接地, 幻觉抑制, 论文, 工程实践  
**更新日期：** 2026-09-01  
**来源：** rss  

## 项目描述
arXiv:2608.28596v1 Announce Type: new Abstract: Large language model (LLM) agents are increasingly embedded in scientific workflows for literature analysis, drafting, and review. Existing systems advance autonomous discovery and manuscript generation, but do not resolve the governance problem that arises when ideas, methods, results, and claims propagate through AI-assisted workflows without mandatory human approval or artifact-level traceability. This paper proposes Paper Pilot, a human-in-the-loop expert system for evidence-traceable scientific manuscript generation in applied sciences. It adapts the Collaborative Agent Reasoning Engineering (CARE) methodology to manuscript development through manuscript-owner approval gates, explicit no-pass criteria, claim classification, audit logging, advisory LLM review, and evidence-locked revision control. The framework defines eight approval gates across the idea-to-claim pipeline and distinguishes literature-grounded from artifact-grounded claims, requiring reported numbers and interpretations to remain traceable to approved evidence; its system prompt is openly released for deployment in ChatGPT, Gemini, Claude, or institutional LLM environments. As a first empirical validation, we evaluate the citation-grounding layer with a controlled, mechanically scored benchmark (two commercial LLMs, real arXiv papers, no LLM judge): under coverage pressure ungated drafters fabricated up to 25% of their citations and never flagged an evidence gap, whereas the same models under Paper Pilot's evidence-locked rules produced zero fabricated citations and surfaced the planted gaps as explicit placeholders. Preliminary results for result grounding, revision, and adversarial robustness point the same way; full evaluation is left to future work. Paper Pilot positions LLM-assisted writing as a controlled human-AI decision-support process rather than a fully autonomous authorship pipeline.

## 综合总结
Paper Pilot 是一个面向应用科学领域的人类在环证据可追溯论文写作专家系统，基于 CARE 方法论设计了包含八个审批门、声明分类与证据锁定版本控制的治理框架。其最有价值的实证贡献是揭示了无门控 LLM 在引用接地任务中高达 25% 的伪造率，并通过其证据锁定规则将伪造率降至 0%，验证了治理机制的有效性。然而论文在结果接地、对抗鲁棒性等方面的评估尚未完成，整体偏向系统性框架贡献而非方法论突破，对希望落地的学术写作场景从业者具有参考价值，但社区影响力与可信度受发布渠道异常影响需谨慎对待。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
论文提出 Paper Pilot 系统，将 CARE 方法论适配到科研论文生成流程，设计了八个审批门(approval gates)、声明分类(文献支撑 vs 事实支撑)、审计日志、证据锁定版本控制等机制，方法论框架相对系统化。核心实证仅针对引用接地(citation-grounding)一层，使用受控机械评分基准(无 LLM judge)，展示了 0% 伪造引用与显式占位符的效果，方法上有一定严谨性。但整体技术深度有限——大多数组件(审批门、声明分类、审计日志)属于工程化治理模式而非新颖算法创新，结果接地、对抗鲁棒性等仅给出初步方向，未做完整评估，学术贡献偏向系统框架而非方法突破。

### 实用性 (评分: 7.0/10)
对学术写作场景的从业者具有较高的实用参考价值：明确提出了 AI 辅助写作中引用伪造(高达 25%)这一真实痛点，提供的八审批门流程和证据锁定规则可直接应用于 ChatGPT/Gemini/Claude 等部署环境，系统提示词已开源。即时可用性较强，特别适合需要严谨文献支撑的研究者、学术期刊编辑、研究机构。局限性在于完整评估未完成，实际部署中的工程细节、可扩展性、多人协作场景等方面尚未充分验证。

### 社区活跃度 (评分: 6.0/10)
话题契合当前 AI 辅助科研写作与 AI 治理的热点议题——LLM 幻觉、引用伪造、人类在环决策等都是社区高度关注的问题。arXiv 预印本形式发布，作者来自学术界(三位作者署名)。但发布时间标为 2026-09-01 且 arXiv 编号 2608.28596 格式异常(疑似生成或虚构条目)，来源权威性存疑。尚未有完整实证结果，社区影响力有限。

## 项目链接
https://arxiv.org/abs/2608.28596
