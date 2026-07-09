# Healthier LLMs: Retrieval-Augmented Generation for Public Health Question Answering

**评分：** 8.5  
**状态：** 正常  
**标签：** RAG, 医疗健康, LLM, 评估, 论文  
**更新日期：** 2026-07-09  
**来源：** rss  

## 项目描述
arXiv:2607.06641v1 Announce Type: new Abstract: Large language models (LLMs) achieve promising results on medical question answering benchmarks, yet their use in public health is constrained by hallucinations and the rapid evolution of official guidance. Retrieval-Augmented Generation (RAG) mitigates these risks by grounding responses in an explicitly maintained corpus, but end-to-end performance depends critically on retrieval configuration and on evaluation beyond multiple-choice formats. We extend PubHealthBench, a question answering (QA) benchmark of 7,929 questions derived from UK Government public health guidance, into a retrieval-augmented setting and systematically evaluate retrieval and generation choices. We compare dense, sparse, and hybrid retrieval across multiple embedding models and corpus variants, and show that hybrid retrieval consistently improves recall and ranking quality, with chunk length and topic interacting with ranking performance. Providing retrieved context substantially increases multiple-choice accuracy across a diverse set of LLMs, enabling smaller open-weight models to match or outperform larger models used without retrieval, with gains primarily driven by retrieval quality and careful context selection. To assess realistic free-form answering, we introduce a rubric-based LLM-as-a-judge covering faithfulness, completeness, clarity, and factual consistency, and validate it against dual human annotations. Judge-human agreement is strongest for faithfulness and completeness, while factual consistency and clarity are less reliably reproduced, motivating caution when interpreting those dimensions at scale. Overall, our results highlight retrieval as a primary lever for reliable public health QA and provide practical guidance for building and evaluating RAG systems grounded in official guidance.

## 综合总结
该论文将PubHealthBench扩展至检索增强生成（RAG）设置，系统评估了公共卫生问答中的检索与生成策略。研究表明，混合检索显著提升召回与排序，且RAG使小模型性能超越无检索大模型。同时，论文提出基于准则的LLM-as-a-judge评估自由回答，发现其在忠实度和完整性上与人高度一致，但在事实一致性和清晰度上存在不足。该研究为构建基于官方指南的可靠公共卫生RAG系统提供了关键的实践与评估指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文系统性地评估了RAG在公共卫生问答中的端到端表现，对比了稠密、稀疏及混合检索策略，并深入分析了分块长度与主题对排序性能的影响。在生成评估方面，创新性地提出了基于评分准则的LLM-as-a-judge方法来评估自由形式回答，并通过双人工标注验证，严谨地揭示了LLM在评估事实一致性和清晰度时的不可靠性，研究深度与论证严谨性俱佳。

### 实用性 (评分: 9.0/10)
对医疗健康等高风险场景的AI落地具有极高的实践指导价值。研究证明了通过高质量的检索与上下文选择，较小的开源模型即可媲美甚至超越无检索的大模型，显著降低了部署成本。文中关于混合检索配置、分块策略及LLM-as-a-judge评估维度的发现，可直接转化为构建和优化垂直领域RAG系统的工程指南。

### 社区活跃度 (评分: 8.5/10)
公共卫生与大模型的结合是当前极具社会价值与影响力的前沿方向。论文基于英国政府官方指南构建的PubHealthBench基准具有很高的权威性和时效性，有效回应了业内对大模型医疗幻觉和指南频繁更新的担忧，对推动安全可信的医疗AI发展具有积极的社区影响力。

## 项目链接
https://arxiv.org/abs/2607.06641
