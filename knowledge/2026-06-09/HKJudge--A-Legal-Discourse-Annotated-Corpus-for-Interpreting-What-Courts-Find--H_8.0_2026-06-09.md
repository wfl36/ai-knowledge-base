# HKJudge: A Legal Discourse-Annotated Corpus for Interpreting What Courts Find, How They Reason, and What They Rule

**评分：** 8.0  
**状态：** 正常  
**标签：** 法律AI, NLP, 数据集, 基准测试, 判决预测, 论文  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.06679v1 Announce Type: new Abstract: Court judgments are central to legal practice and jurisprudence, yet discourse analysis of Hong Kong judgments has received limited attention, owing largely to the absence of expert-annotated corpora. We introduce the Hong Kong Judgment Discourse Dataset (HKJudge), the first sentence-level expert-annotated legal discourse corpus. HKJudge includes criminal judgments across all five levels of HK's court hierarchy, comprising $\sim$290k sentences and $\sim$6.5 million tokens, fully annotated by legal linguistics experts. We design a two-tier discourse schema that captures what facts a court finds, how it reasons, and what it rules. At the sentence level, each sentence is assigned one of 26 rhetorical roles. At the span level, sentences are further annotated with three sentencing elements (charge, imprisonment term, fine). Ten legal linguistics annotators produced the annotations with an inter-annotator agreement of $\kappa = 0.8$. We formulate two tasks on HKJudge, termed rhetorical role classification and legal element extraction, and provide the first benchmark evaluation of four BERT-based models, two open-source LLMs under zero-shot and fine-tuning settings, and four commercial LLMs on both tasks. Our work demonstrates the value of sentence-level discourse annotation for modeling the structure of HK judgments and provides a rich data foundation for future work on legal judgment prediction. The HKJudge dataset and code are available at https://github.com/xuanxixi/HKJudge.

## 综合总结
本文发布了HKJudge，首个香港法院判决的句子级专家标注法律话语语料库，包含约29万句子与650万词元。研究提出双层话语模式（26种修辞角色与3种量刑元素）进行标注，一致性达0.8。基于此定义了修辞角色分类与法律要素提取任务，并对多种模型进行了基准评估，为法律判决结构解析与预测提供了重要数据基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
首创香港判决句子级专家标注语料库，提出双层话语标注模式（句子级26种修辞角色+跨度级3种量刑元素），填补了普通法系下香港判决语料库的空白。基准测试涵盖BERT系列、开源及商业LLM，论证严谨（10名专家标注，Kappa=0.8），数据构建与任务设计具有较高研究深度。

### 实用性 (评分: 8.5/10)
提供高质量开源数据集与基准代码，对法律NLP从业者具有直接应用价值，可指导法律文本信息提取、判决预测等下游任务的模型训练与微调。其双层话语模式的方法论对其他法域的判决书解析亦有较强的借鉴与推广意义。

### 社区活跃度 (评分: 7.5/10)
法律AI与大模型垂直领域落地是当前社区热点。该研究来自学术机构，数据开源且标注规范，可信度高。作为首个香港判决话语语料库，在法律AI细分社区具有较强影响力和时效性，但受众相对垂直，整体大众影响力有限。

## 项目链接
https://arxiv.org/abs/2606.06679
