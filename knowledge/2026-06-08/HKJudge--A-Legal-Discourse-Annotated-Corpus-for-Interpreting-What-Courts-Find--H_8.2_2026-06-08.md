# HKJudge: A Legal Discourse-Annotated Corpus for Interpreting What Courts Find, How They Reason, and What They Rule

**评分：** 8.2  
**状态：** 正常  
**标签：** 法律NLP, 数据集, 大模型, 基准测试, 论文  
**更新日期：** 2026-06-08  
**来源：** rss  

## 项目描述
arXiv:2606.06679v1 Announce Type: new Abstract: Court judgments are central to legal practice and jurisprudence, yet discourse analysis of Hong Kong judgments has received limited attention, owing largely to the absence of expert-annotated corpora. We introduce the Hong Kong Judgment Discourse Dataset (HKJudge), the first sentence-level expert-annotated legal discourse corpus. HKJudge includes criminal judgments across all five levels of HK's court hierarchy, comprising $\sim$290k sentences and $\sim$6.5 million tokens, fully annotated by legal linguistics experts. We design a two-tier discourse schema that captures what facts a court finds, how it reasons, and what it rules. At the sentence level, each sentence is assigned one of 26 rhetorical roles. At the span level, sentences are further annotated with three sentencing elements (charge, imprisonment term, fine). Ten legal linguistics annotators produced the annotations with an inter-annotator agreement of $\kappa = 0.8$. We formulate two tasks on HKJudge, termed rhetorical role classification and legal element extraction, and provide the first benchmark evaluation of four BERT-based models, two open-source LLMs under zero-shot and fine-tuning settings, and four commercial LLMs on both tasks. Our work demonstrates the value of sentence-level discourse annotation for modeling the structure of HK judgments and provides a rich data foundation for future work on legal judgment prediction. The HKJudge dataset and code are available at https://github.com/xuanxixi/HKJudge.

## 综合总结
本文介绍了HKJudge，首个针对香港法院刑事判决的句子级专家标注法律话语语料库，包含约29万句子和650万token。研究设计了双层话语模式（句子级26个修辞角色+跨度级3个量刑元素），由10位法律语言学专家完成标注（kappa=0.8）。基于此数据集，作者提出了修辞角色分类和法律要素提取两个任务，并对BERT模型、开源及商业LLM进行了全面的基准评估。该工作填补了香港法律话语分析的空白，为法律判决预测等下游任务提供了高质量的数据基础，数据和代码已开源。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
首创香港判决句子级专家标注语料库，填补了该领域的话语分析空白。双层话语模式设计（26个修辞角色与3个量刑元素）精细且具创新性，标注一致性高(kappa=0.8)。基准测试涵盖BERT至各类LLM，论证严谨，但模型层面未提出突破性架构，主要为数据与任务定义的贡献。

### 实用性 (评分: 8.5/10)
对法律NLP从业者具有极高的落地参考价值。开源的高质量语料库及基准代码可直接用于训练和评估法律文本解析、判决预测及信息提取模型。虽主要针对香港普通法系，但其话语标注范式对其他法系的法律NLP任务亦有重要借鉴意义。

### 社区活跃度 (评分: 8.0/10)
话题契合当前LLM在垂直领域（法律）应用的热点趋势。来源可信度高，由法律语言学专家与NLP学者合作完成，且标注一致性优异。作为首个香港判决话语语料库，具备成为该领域基准数据集的潜力与影响力。

## 项目链接
https://arxiv.org/abs/2606.06679
