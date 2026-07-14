# Robust, Scalable Detection of Text Containment in Large Web-Crawled Corpora

**评分：** 8.3  
**状态：** 正常  
**标签：** 数据清洗, 版权检测, 大模型, 语料库, 论文, 开源工具  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.10020v1 Announce Type: new Abstract: We present FindMyText, an open-source Python package designed to efficiently assess whether a given text appears, in part or in full, within a text corpus. The tool builds on prior techniques for document fingerprinting, but extends them with a novel mechanism to explicitly capture sequences of matching fingerprints. By identifying such chains, the tool can more reliably detect near-verbatim copies of a given text rather than mere textual similarities. This makes FindMyText particularly suited for verifying the presence of copyrighted material in a corpus. Leveraging a distributed, disk-based indexing framework, the system scales to large web-crawled datasets. Using a new benchmark for evaluating text containment methods, we show that FindMyText outperforms alternative approaches across three datasets (ArXiv papers, Wikipedia, and generic web content).

## 综合总结
本文介绍了 FindMyText，一个用于检测大规模语料库中文本包含关系的开源 Python 工具。该工具在传统文档指纹技术基础上，创新性地引入了匹配指纹序列捕获机制，以更可靠地识别近逐字拷贝，特别适用于验证语料库中是否存在版权材料。结合分布式磁盘索引，系统具备大规模数据处理能力，并在新基准的三个数据集上表现出优于替代方法的性能，对大模型数据合规与清洗具有重要实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
提出了一种基于文档指纹序列匹配的新机制，能够显式捕获匹配指纹链，从而更可靠地检测近逐字拷贝而非仅依赖文本相似度；结合分布式磁盘索引框架，解决了大规模语料库的扩展性问题，并构建了新基准进行验证，技术与工程深度结合较好。

### 实用性 (评分: 9.0/10)
以开源 Python 包形式发布，直接针对大模型训练数据中的版权合规与数据溯源痛点，支持大规模网络爬取数据集，对数据清洗、版权审查和合规评估具有极高的实操指导价值。

### 社区活跃度 (评分: 8.5/10)
直击当前大模型训练数据版权争议的热点问题，arXiv 论文来源权威，开源工具具备良好的传播潜力和社区影响力。

## 项目链接
https://arxiv.org/abs/2607.10020
