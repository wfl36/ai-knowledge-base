# XHotpotQA: A Benchmark for Cross-Lingual Knowledge Composition in Multi-Hop Question Answering

**评分：** 7.0  
**状态：** 正常  
**标签：** 多语言, 多跳问答, RAG, 基准测试, 知识组合, 论文  
**更新日期：** 2026-08-31  
**来源：** rss  

## 项目描述
arXiv:2608.27481v1 Announce Type: new Abstract: Knowledge-intensive multi-hop question answering requires systems to select evidence and compose dependent facts, yet multilingual benchmarks usually translate an entire example into one language. This hides failures at language boundaries inside the reasoning chain. We introduce XHotpotQA, a controlled benchmark for cross-lingual knowledge composition over mixed-language evidence. Each instance is modeled as an evidence-dependency graph whose question, bridge evidence, answer-bearing evidence, and distractors have explicit language assignments. The audited resource contains 15,661 training and 7,405 validation instances, with sentence-level support supervision and supplied distractors. In validation, 99.81% of items cross the question-to-gold-evidence language interface and 95.60% use gold paragraphs in different languages. Across three reader artifacts, full question-evidence mismatch is associated with 10.25 to 15.79 lower Unicode-aware answer F1 than partial alignment, and different-script evidence with deficits of 11.98 to 23.70 points; the corresponding adapted-selector contrasts are 1.71 and 1.78 points. Under this supplied-candidate design, the evaluated readers therefore show substantially larger condition-associated deficits than the selector. XHotpotQA provides role-aware diagnostics, modular evaluation, and an audited test bed for knowledge-based systems that must integrate evidence across languages.

## 综合总结
XHotpotQA 是一个面向跨语言知识组合的多跳问答基准，通过证据依赖图与显式语言标签设计，揭示了传统翻译基准中隐藏的语言边界推理失败。论文在受控实验设计和诊断分析上具备一定深度，提供模块化评估方案和审计过的数据集，对跨语言 RAG/多跳推理研究有参考价值。但作为基准类工作，方法论创新集中在数据构造而非理论突破，且受众相对小众。需注意 arXiv 编号异常可能影响可信度判断。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
论文提出了 XHotpotQA，一个针对跨语言知识组合的多跳问答基准。其核心方法创新在于将每个实例建模为证据依赖图，并对问题、桥接证据、答案证据及干扰项显式分配语言标签，这一设计有效暴露了传统翻译基准隐藏的语言边界推理失败。文中通过三种 reader artifact 量化了全语言失配、部分对齐与不同文字间的 F1 差距，分析层次较深。但作为基准工作，方法论本身偏向数据工程与受控实验设计，理论贡献有限，论证虽严谨但深度一般。

### 实用性 (评分: 7.0/10)
该基准为多跳问答与跨语言检索增强系统提供了可复用的诊断工具，包含句子级支持监督与可插拔的模块化评估方案，对研究 RAG/多跳推理在跨语言场景下的研究者具有较高参考价值。提供 15,661 训练和 7,405 验证实例，规模适中且经过审计，便于直接使用。但适用场景集中在跨语言多跳 QA 这一细分方向，对更广泛的从业者落地指导有限。

### 社区活跃度 (评分: 6.5/10)
跨语言多跳问答与知识组合是当前多语言 RAG 与多模态推理领域的活跃方向，话题具有较强时效性。arXiv 来源可信，作者机构背景尚需进一步验证。arXiv 编号格式（2608.27481）疑似未来时间戳，真实性存疑，影响了整体可信度评估。话题影响力集中于学术圈，工业界关注度相对有限。

## 项目链接
https://arxiv.org/abs/2608.27481
