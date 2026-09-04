# BharatGather: A Culturally-Informed Benchmark Dataset for Misinformation and Fake News Detection in Indian Public Events

**评分：** 4.7  
**状态：** 待复核  
**标签：** 假新闻检测, 数据集, 多模态, LLM, 社会文化, 基准测试, 工程实践  
**更新日期：** 2026-09-04  
**来源：** rss  

## 项目描述
arXiv:2609.02895v1 Announce Type: new Abstract: Large-scale public events, such as religious festivals, political rallies, and cultural gatherings, are increasingly vulnerable to the rapid dissemination of misinformation, posing substantial risks to public safety and social cohesion. While automated fake news detection has seen significant methodological progress, existing benchmarks frequently fail to capture the socio-cultural nuances and event-specific dynamics characteristic of the Indian context. This paper introduces BharatGather, a curated, multi-source dataset specifically engineered for binary misinformation classification within the ecosystem of Indian mass gatherings. The corpus comprises 14,646 records constructed through a hybrid pipeline involving systematic web scraping of prominent fact-checking platforms, multimedia transcript extraction, and Large Language Model (LLM)-mediated synthetic augmentation to ensure narrative diversity. By providing a resource tailored to the unique complexities of event-aware misinformation in India, this work facilitates the development of culturally informed detection systems and establishes a rigorous benchmark for evaluating their performance in high-stakes public environments.

## 综合总结
BharatGather是一个针对印度大规模公共事件（如宗教节日、政治集会等）中虚假信息检测的基准数据集，包含14,646条通过混合管道（网络爬取、多媒体转录、LLM合成增强）构建的记录。该工作的核心贡献在于填补现有假新闻检测基准在印度社会文化语境方面的空白，为开发文化感知的检测系统提供了资源。然而，方法论新颖性有限，缺乏深入的偏差分析、跨文化泛化研究和充分的基准实验，整体影响力受限。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 4.5/10)
技术层面，该工作主要贡献在于构建了一个针对印度特定社会文化背景的虚假信息检测数据集，方法上采用网页爬取、多媒体转录提取与LLM介导的合成数据增强的混合流程。方法论本身并不具备显著的新颖性，LLM合成数据增强已在多个领域广泛使用，缺乏在数据质量控制、偏差评估、跨文化泛化等方面的深入分析，技术深度有限。

### 实用性 (评分: 5.5/10)
该数据集对从事印度地区假新闻检测、文化敏感型NLP系统开发的研究者和从业者具有直接参考价值。14,646条记录的规模适中，且针对宗教节日、政治集会等高风险场景的标注具有实际应用意义。但数据集的语言覆盖范围、标注质量细节、基准实验结果等关键信息缺失，限制了其作为通用基准的实用性。

### 社区活跃度 (评分: 4.0/10)
话题涉及假新闻检测这一持续受关注的研究方向，针对特定地区文化背景的数据集建设有一定需求。然而发布时间标注为2026年9月（arXiv编号2609.02895），属于预印本，且未见顶会或期刊的发表信息。作者来自印度研究机构，来源可信度一般，社区影响力尚待验证。缺乏实验对比和性能基准数据，限制了话题的传播广度。

## 项目链接
https://arxiv.org/abs/2609.02895
