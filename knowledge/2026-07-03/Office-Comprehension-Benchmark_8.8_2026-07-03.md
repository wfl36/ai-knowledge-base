# Office Comprehension Benchmark

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, 文档理解, 基准测试, 多模态, 推理, 论文, 数据集  
**更新日期：** 2026-07-03  
**来源：** rss  

## 项目描述
arXiv:2607.01245v1 Announce Type: new Abstract: We introduce Office Comprehension Bench (OCB), the first public benchmark to jointly evaluate LLM systems on Word, Excel, and PowerPoint comprehension over native file formats (.docx, .xlsx, .pptx) and their variants. OCB consists of two tracks. File Fidelity Q&A tests structural and visual perception of office artifacts - tables, charts, embedded images, formulas, and app-specific elements such as headers, speaker notes, and named ranges. Domain Q&A tests expert-level reasoning grounded in real-world industry documents across 12 professional domains, with queries requiring multi-step analysis and synthesis across documents. Each reference answer is decomposed into atomic, binary-gradable claims, and an ensemble of LLM judges scores responses against each claim independently. Even the strongest frontier system in its default reasoning mode reaches only about 59.3% on Domain Q&A increasing thinking depth within a tier does not move performance materially, while moving to a higher product tier yields modest gains. We release the dataset, evaluation tooling, judge prompt, and a public leaderboard.

## 综合总结
本文发布了OCB（Office Comprehension Bench），首个针对Word、Excel和PowerPoint原生格式联合理解的公开基准。基准包含文件保真度问答和领域问答两个赛道，全面测试模型对文档结构视觉感知及跨领域多步推理能力。评测采用原子化声明与LLM评委机制，发现当前最强前沿模型在领域推理上仅达59.3%，且增加推理深度收益甚微，揭示了LLM在复杂办公文档理解上的显著瓶颈。项目已开源数据集与评测工具，对企业级文档理解应用具有极高的指导价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究提出了首个针对Word、Excel和PowerPoint原生格式联合理解的公开基准OCB，填补了当前LLM评估在复杂办公文档原生结构上的空白。技术设计上具有较高深度与创新性，分为文件保真度问答（测试结构、视觉感知及应用特定元素）和领域问答（测试跨12个专业领域的多步推理与综合分析）两个赛道。评估方法采用原子化二元声明结合LLM评委集成，严谨性高。实验揭示了当前最强前沿模型在领域推理上仅达59.3%，且单纯增加推理深度无法带来实质性提升，深刻指出了现有LLM在处理复杂结构化文档时的能力瓶颈。

### 实用性 (评分: 9.0/10)
对AI从业者具有极高的落地参考价值。办公文档（docx/xlsx/pptx）是企业级应用（如RAG、Agent）最核心的数据载体，该基准直接切中真实业务场景痛点。项目不仅提供了跨领域的复杂测试集，还开源了评估工具、评委提示词和排行榜，开发者可直接将其应用于自身文档解析与理解Pipeline的评测与优化，指导意义显著。

### 社区活跃度 (评分: 9.0/10)
话题时效性极强，直击当前大模型在企业级应用中“难以处理原生复杂办公文档”的普遍痛点。来源可信度高（作者群庞大且极大概率来自核心办公软件生态企业），具备成为该领域标准评测数据集的潜力。其揭示的“增加推理深度无济于事”的结论对社区后续模型训练和架构优化具有强烈的指引作用，影响力深远。

## 项目链接
https://arxiv.org/abs/2607.01245
