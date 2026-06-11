# One Jailbreak, Many Tongues: Learning Language-Insensitive Intention Representations for Multilingual Jailbreak Detection

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型安全, 越狱检测, 多语言, 表示学习, 论文  
**更新日期：** 2026-06-11  
**来源：** rss  

## 项目描述
arXiv:2606.11202v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly deployed in applications for global multilingual users, yet safety training remains concentrated in dominant languages and has not progressed in parallel with multilingual capability, creating exploitable gaps for jailbreak attacks. Current jailbreak defenses are largely developed and evaluated in dominant languages, and their effectiveness is limited by the scarcity of aligned multilingual supervision and representations dispersion caused by language variation. To address this issue, we propose MLJailDe, a multilingual jailbreak detection framework designed to improve both multilingual robustness and cross-lingual generalization. MLJailDe first introduces a multilingual back-translation data augmentation algorithm to construct a semantically consistent and functionally effective dataset spanning 11 languages, consisting of 2,232 benign and 1,239 jailbreak samples. On this basis, MLJailDe employs relative-distance constraints to reduce cross-lingual representation dispersion and encourage jailbreak prompts with similar intent to form consistent clusters across languages, while an imbalance-aware classification objective is further used to alleviate class imbalance and learn more reliable multilingual decision boundaries. Experimental results show that MLJailDe outperforms state-of-the-art baselines across multiple languages, achieving an F1 score of 98.5\%, and obtains an average F1 score of 97.1\% on unseen languages, demonstrating strong effectiveness and cross-lingual generalization.

## 综合总结
本文针对大模型多语言安全训练滞后导致的越狱攻击漏洞，提出了一种多语言越狱检测框架MLJailDe。该框架通过多语言回译算法构建了涵盖11种语言的数据集，并利用相对距离约束减少跨语言表示分散，使相似意图的越狱提示跨语言聚类，同时结合不平衡感知分类目标优化决策边界。实验表明，MLJailDe在多语言越狱检测上达到98.5%的F1分数，在未见语言上平均F1达97.1%，显著提升了多语言鲁棒性和跨语言泛化能力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文深入剖析了多语言越狱防御中“对齐数据稀缺”和“语言差异导致的表示分散”两大核心痛点，创新性地提出学习语言无关的意图表示。通过回译数据增强、相对距离约束（跨语言表示对齐）与不平衡感知分类的有机结合，技术方案逻辑严密，且在11种语言及未见语言上的极高F1分数充分验证了其研究深度与论证严谨性。

### 实用性 (评分: 9.0/10)
该研究对大模型全球化部署的安全防护具有极高的实践指导价值。MLJailDe提供了一套从多语言数据构建到模型训练的完整工程方案，直接解决了出海产品面临的小语种安全防御薄弱问题。其出色的跨语言泛化能力（未见语言F1达97.1%）意味着可低成本扩展至更多语种，对AI安全从业者落地防御系统具有强参考性。

### 社区活跃度 (评分: 8.5/10)
大模型多语言安全是当前AI社区高度关注且亟待解决的痛点，该论文切中时弊，时效性极强。作者团队来自学术机构，发布于arXiv，具备较高的学术可信度。其在多语言越狱检测这一细分赛道上取得的显著性能提升，有望在AI安全与对齐社区产生较大影响力。

## 项目链接
https://arxiv.org/abs/2606.11202
