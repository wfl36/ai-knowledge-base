# Learning Evidence Sufficiency Boundaries for Selective Answering in Grounded Multi-Hop QA

**评分：** 6.5  
**状态：** 正常  
**标签：** RAG, Grounded QA, 多跳推理, 选择性回答, 论文  
**更新日期：** 2026-09-03  
**来源：** rss  

## 项目描述
arXiv:2609.01687v1 Announce Type: new Abstract: Grounded question answering systems should answer only when the supplied evidence supports the answer. In multi-hop QA, this requirement is difficult because partial evidence can make an unsupported answer appear plausible. We study selective answering through evidence sufficiency boundaries: for the same question, a model should abstain under unsupported or partially supported context, answer when the context first becomes sufficient, and keep the answer stable when redundant evidence is added. We introduce Evidence Sufficiency Boundary Training, a generation-native training framework that constructs ordered evidence chains and supervises the abstain-to-answer transition directly. The method combines level supervision, a boundary flip margin, post-boundary stability, and answer recall protection. We build evidence chains from HotpotQA, 2WikiMultiHopQA, and MuSiQue, then evaluate models with chain metrics, raw QA utility, and unsupported-answer rates on external non-answerable sets. With Qwen2.5-3B-Instruct and LoRA adaptation, Evidence Sufficiency Boundary Training gives the strongest boundary localization among the tested systems, with flip accuracy of 0.807 compared with 0.781 for a token-level abstention baseline. It also achieves the lowest overall unsupported-answer rate on external non-answerable evaluation, 0.095 compared with 0.101 for the same baseline, while retaining competitive raw QA F1. The results show that grounded selective answering improves when training marks the evidence level where refusal should give way to answering.

## 综合总结
本文针对多跳Grounded QA中证据不足导致的错误回答问题，提出Evidence Sufficiency Boundary Training框架，通过有序证据链构造和边界监督信号训练模型精确识别从拒绝到回答的转换点。方法在三个标准数据集上验证，相比token-level abstention基线在边界定位和不可回答集上的未支持回答率上取得小幅提升。该工作为RQA系统的可靠性提供了有意义的探索，但技术新颖性和结果改进幅度均属渐进式，适合关注Grounded QA鲁棒性的研究者参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.2/10)
论文提出了Evidence Sufficiency Boundary Training框架，针对多跳QA中选择性回答问题，通过构造有序证据链并直接监督从abstain到answer的转换。方法包含level supervision、boundary flip margin、post-boundary stability和answer recall protection等多个组件，设计上有一定新颖性。但整体思路偏向于工程化组合训练目标，理论深度有限。在Qwen2.5-3B-Instruct上flip accuracy仅从0.781提升到0.807，绝对改进幅度较小，技术贡献属于渐进式改进而非突破。

### 实用性 (评分: 6.8/10)
对从事RAG/Grounded QA系统开发的从业者有一定参考价值，提供了在多跳场景下处理evidence sufficiency的实用训练框架。在HotpotQA、2WikiMultiHopQA、MuSiQue三个常用基准上验证，且包含外部不可回答集的评估，实验设计相对完整。方法使用LoRA适配，可在中等规模模型上实践。但实际部署中证据链构造成本、边界定位的可靠性等问题还需进一步验证，对工业级系统的直接指导性中等。

### 社区活跃度 (评分: 5.5/10)
话题聚焦于Grounded QA中的evidence sufficiency，属于RAG和QA领域的细分方向，时效性中等。来源为arXiv论文，作者为非知名机构研究人员，缺少知名学者背书。发布时间为2026年9月（可能是预印本时间戳），尚未经过同行评审。实验结果改进幅度有限，社区关注度预计不高。

## 项目链接
https://arxiv.org/abs/2609.01687
