# Benchmarking Large Language Models for Safety Data Extraction

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 评估基准, 多模态, 信息抽取, 工业安全, 论文  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11204v1 Announce Type: new Abstract: Accurate extraction of structured information from Safety Data Sheets (SDS) remains challenging in industrial safety due to heterogeneous document formats and the limitations of traditional rule-based methods. This study benchmarks state-of-the-art Large Language Models (LLMs) for automated SDS data extraction, comparing text-based and multimodal processing pipelines. We systematically evaluate four models: Gemini 1.5 Pro, GPT-4o, Claude 3.7 Sonnet, and Llama 3.1-70B, across three prompting strategies: zero-shot, few-shot, and chain-of-thought. The evaluation framework assessed accuracy, latency, and cost across more than 50,000 extracted data fields. Results show that text-based extraction consistently outperforms multimodal processing across all metrics. Gemini 1.5 Pro combined with a Chain-of-Thought prompt achieved the highest accuracy (84%), outperforming GPT-4o (81%) and Claude 3.7 Sonnet (79%). However, no model surpassed the 90% accuracy threshold commonly required for reliable real-world deployment. These findings indicate that general-purpose LLMs are not yet robust enough for unsupervised industrial use, though performance suggests strong potential with task-specific fine-tuning. Future research should focus on domain-adapted training, model calibration, and the integration of Human-in-the-Loop verification to ensure safety-critical reliability.

## 综合总结
该论文系统评估了Gemini 1.5 Pro、GPT-4o等四个主流大模型在安全数据表(SDS)信息提取任务上的表现，对比了文本与多模态管道及三种提示策略。研究发现文本提取效果全面优于多模态，Gemini 1.5 Pro结合思维链提示达到了最高84%的准确率，但仍未达到工业可靠部署所需的90%阈值。结论指出通用大模型尚不足以进行无监督工业应用，需结合领域微调与人机协同验证来保障安全关键场景的可靠性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
研究系统性地评估了4个主流大语言模型在安全数据表(SDS)信息提取任务上的表现，对比了文本与多模态处理管道以及三种不同的提示策略（零样本、少样本、思维链），评估维度涵盖准确率、延迟和成本，数据量超过5万字段，实验设计严谨全面。但方法上属于常规的基准测试，未提出新的模型架构或算法，且结论（文本优于多模态、通用大模型未达工业级要求）符合当前领域认知，缺乏颠覆性技术洞见。

### 实用性 (评分: 8.0/10)
对工业安全、化工等垂直领域的从业者具有极高的参考价值。研究明确给出了当前SOTA模型在特定任务上的准确率上限（最高84%），指出了其与实际工业部署阈值（90%）的差距，并对比了不同模型的延迟与成本。同时，为工程落地指明了具体方向（领域微调、模型校准、人机协同HITL），能够直接指导企业在引入LLM处理复杂文档时的技术选型与预期管理。

### 社区活跃度 (评分: 7.5/10)
作为arXiv论文具备学术可信度，评估对象为当前最新的主流闭源与开源模型（如GPT-4o、Claude 3.7 Sonnet等），时效性强。虽然SDS数据提取属于相对垂直的工业应用场景，在泛AI社区的话题热度有限，但在大模型垂直领域落地和工业信息抽取的细分社群中具有较高的关注度和参考影响力。

## 项目链接
https://arxiv.org/abs/2606.11204
