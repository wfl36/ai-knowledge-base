# Automatic Extraction of Structured Information from Brain MRI Reports Using an Open-Weight Large Language Model

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 医疗AI, 信息提取, 神经放射学, 论文, 应用评估  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.07721v1 Announce Type: new Abstract: Objectives: Automatic data extraction from free-text radiology reports enables large-scale research, but few studies assessed the performance of large language models (LLMs) on Dutch neuroradiology reports. Methods: We analyzed 947 brain MRI reports from a tertiary memory clinic (2016-2021), authored by consultant neuroradiologists. Trained medical students annotated thirty variables; 100 reports were double-annotated to assess inter-rater reliability. We evaluated the performance of the open-weight LLM LLaMA 3.1 using different languages (Dutch vs. English translation) and few-shot prompting with different example selection strategies. Performance was evaluated using balanced accuracy for categorical variables, accuracy and mean absolute error for counts, and text similarity for free-text. Metrics were computed across 10 random splits of the 947 reports. Results: LLaMA 3.1 demonstrated high zero-shot performance for visual rating scores (mean [95%-CI]): Medial Temporal Atrophy: 90% [77-100%] on the left and 96% [94-99%] on the right, Global Cortical Atrophy: 87% [83-91%], and Fazekas: 94% [93-96%]. Microbleed mentions were detected with 93% accuracy [92-95%] and infarct mentions with 82% [80-84%]. Text similarity for lesion location reached 0.95 [0.95-0.96]. Performance was lower for numerical variables: 80% [78-82%] for the number of microbleeds and 66% [63-68%] for infarcts. English translation yielded comparable results. Few-shot prompting improved performance for numerical variables, achieving 92% [90-93%] for microbleeds and 81% [77-85%] for infarcts using structural similarity-based selection. Conclusion: LLaMA 3.1 shows strong potential for extracting data from Dutch neuroradiology reports. Few-shot prompting enhances performance for numerical variables, whereas challenges remain for location-specific variables.

## 综合总结
本研究评估了开源大模型LLaMA 3.1从荷兰语脑部MRI报告中自动提取结构化信息的能力。基于947份临床报告的实验表明，模型在零样本设置下对视觉评分和病灶检测等分类变量表现出色，但在提取微出血和梗死等数值变量时表现较弱。研究进一步发现，英语翻译对性能影响不大，而基于结构相似性的少样本提示策略能显著提升数值变量的提取准确率。该工作证实了开源LLM在非英语医疗报告结构化提取中的巨大潜力及优化方向。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
该研究属于应用型评估，技术方法上未提出新型架构或算法，主要基于开源LLaMA 3.1模型进行零样本和少样本提示工程测试。但其研究设计严谨，针对荷兰语神经放射学报告这一特定垂直领域，细致区分了分类变量、数值变量和自由文本变量，并引入了基于结构相似性的少样本示例选择策略，有效解决了数值提取的短板，论证过程扎实且具有针对性。

### 实用性 (评分: 8.5/10)
对医疗AI从业者及临床科研人员具有极高的落地参考价值。从自由文本放射学报告中提取结构化数据是医疗信息学的刚需，本研究验证了使用开源模型（LLaMA 3.1）替代人工标注或昂贵闭源模型的可行性。给出的少样本提示优化策略（如结构相似性选择）可直接复用于其他语种或病种的医疗报告信息抽取任务，适用范围广，工程落地成本低。

### 社区活跃度 (评分: 8.0/10)
大语言模型在医疗领域的应用是当前学术界和工业界的热点。本研究聚焦于非英语（荷兰语）医疗数据的评估，填补了开源大模型在多语种神经放射学报告提取领域的空白。作者团队具备专业医学背景，数据来源于真实的三级记忆诊所，且评估指标全面，来源权威性与可信度高，对推动开源大模型在医疗垂直领域的应用具有积极影响力。

## 项目链接
https://arxiv.org/abs/2606.07721
