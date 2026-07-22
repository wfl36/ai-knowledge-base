# Calibrated Selective Fact-Checking via Evidence Chain Evaluation

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 事实验证, Agent, 校准, 论文  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18240v1 Announce Type: new Abstract: Large language models (LLMs) can achieve strong fact-checking accuracy, yet forced binary decisions conceal a critical reliability problem: systems may issue confident verdicts even when supporting evidence is weak, sparse, or internally inconsistent. We address this issue through Evidence Chain Evaluation (ECE), a selective fact-checking framework that permits abstention via an uncertain verdict instead of requiring a true/false decision for every claim. The evaluated system is a tool-using verification agent that gathers evidence through web search, scholarly search, and executable checks, and then returns a structured verdict with confidence and source-level metadata. On ECE-Bench, ECE achieves 91.6% standard accuracy, 93.7% coverage, and 97.8% selective accuracy on answered claims. Although ECE does not outperform the strongest retrieval baseline on aggregate calibration metrics such as Expected Calibration Error, Brier score, or AURC, it delivers a clear selective-prediction trade-off: the system maintains very high accuracy on answered claims while deferring 6 of 95 cases. These deferred cases are concentrated in lower-reliability evidence settings (5/6 at source level L4), supporting the view that abstention functions as a safety-oriented mechanism for handling epistemically weak evidence. Code is available at https://github.com/ cheshireyang/ECE.git

## 综合总结
本文针对大模型事实验证中强制二元决策掩盖证据不可靠的问题，提出了证据链评估（ECE）框架。该框架允许工具使用型验证Agent在证据弱、稀疏或矛盾时做出‘不确定’的弃权判决，而非强制输出真假。实验表明，ECE在保持91.6%标准准确率的同时，通过拒答6个低可靠性证据案例，将已回答声明的准确率提升至97.8%。尽管在总体校准指标上未超越最强基线，但ECE有效实现了准确率与覆盖率的权衡，验证了弃权机制作为处理认知弱证据安全手段的有效性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文敏锐地指出了大模型事实验证中‘强制二元决策’掩盖证据不可靠的隐患，创新性地提出了证据链评估（ECE）框架，允许系统在证据弱或矛盾时做出‘弃权’判决。引入工具使用验证Agent和结构化元数据分析，论证逻辑严谨。尽管在总体校准指标（如ECE、Brier score）上未超越最强检索基线，但对选择性预测权衡的深入剖析（拒答案例集中在低可靠性证据源）展现了扎实的研究深度与新颖视角。

### 实用性 (评分: 8.5/10)
对AI工程实践具有极高的参考价值。在RAG和Agent应用中，系统‘幻觉’或‘强行回答’是核心痛点，ECE框架提供的安全弃权机制可直接指导高要求场景（如医疗、法律、金融事实核查）的系统设计。通过置信度和源级元数据实现可解释的延迟决策，且项目已开源，从业者可快速将其集成至现有的验证流水线中，提升系统整体可靠性。

### 社区活跃度 (评分: 7.5/10)
事实验证与大模型可靠性是当前AI社区持续关注的热点，话题时效性强。文章发布于arXiv预印本平台，作者为独立研究者，权威性中等。虽然未在所有校准指标上实现全面超越，但其‘选择性预测’与‘安全弃权’的理念契合工业界对AI系统可控性的迫切需求，有望在Agent可信度评估细分领域引发关注与讨论。

## 项目链接
https://arxiv.org/abs/2607.18240
