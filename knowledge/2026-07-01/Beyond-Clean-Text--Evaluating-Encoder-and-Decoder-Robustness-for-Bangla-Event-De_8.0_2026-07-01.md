# Beyond Clean Text: Evaluating Encoder and Decoder Robustness for Bangla Event Detection in Noisy Text

**评分：** 8.0  
**状态：** 正常  
**标签：** 事件检测, 鲁棒性, 低资源语言, 大模型评估, 噪声文本, 论文, 基准测试  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30914v1 Announce Type: new Abstract: Event detection (ED) systems are typically evaluated on clean, curated text, leaving their robustness to real-world noise largely unexplored, particularly for low-resource languages such as Bangla. We introduce a generalized Bangla news event ontology and a benchmark comprising 9,979 annotated sentences across 40 event subtypes, spanning clean news text, real-world Automatic Speech Recognition (ASR) transcripts, and orthographically corrupted text. We systematically evaluate fine-tuned encoder-only models (BanglaBERT and XLM-R) alongside instruction-tuned decoder-only large language models (Llama 3 and Gemma 3). Our results reveal a clear architectural trade-off: encoder models achieve higher performance on clean text but degrade substantially under noise, whereas decoder-only LLMs are markedly more robust, particularly when event triggers are corrupted. We further show that embedding annotation guidelines during instruction tuning establishes a higher performance baseline on noisy text but yields inconsistent reductions in performance degradation across noisy conditions. Finally, model scaling consistently improves the robustness of decoder-only LLMs, while combined training on clean and noisy data serves as an effective regularization strategy that disproportionately benefits encoder architectures, significantly narrowing the robustness gap.

## 综合总结
本文针对孟加拉语事件检测在真实噪声下的鲁棒性进行了深入研究，构建了包含近万条标注句子的新基准。研究发现 encoder 模型在干净文本上性能占优但抗噪性差，而 decoder-only LLMs 在噪声下更鲁棒。模型缩放能提升 LLM 鲁棒性，而干净与噪声数据混合训练则显著提升了 encoder 的抗噪能力，有效缩小了架构间的鲁棒性差距。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
系统评估了 encoder-only 与 decoder-only 模型在孟加拉语事件检测任务中面对真实世界噪声（ASR转录、拼写错误）的鲁棒性。研究构建了包含40个子类型的孟加拉语事件本体及基准，揭示了明确的架构权衡：encoder 模型在干净文本上表现更优但抗噪性差，而 decoder-only LLMs 在噪声下更鲁棒。此外，深入探讨了指令微调嵌入指南、模型缩放及混合训练策略对鲁棒性的影响，论证严谨。

### 实用性 (评分: 8.0/10)
为处理低资源语言和噪声文本的 NLP 从业者提供了极具价值的实践指导。研究明确了模型选型策略：若追求干净文本极致性能可选 encoder，若需抗噪则选 decoder LLM。同时，验证了混合训练（干净+噪声数据）作为正则化手段能有效提升 encoder 鲁棒性，显著缩小与 decoder 的差距，该结论可直接应用于工程实践的模型训练与优化中。

### 社区活跃度 (评分: 7.5/10)
填补了低资源语言事件检测在噪声环境下评估的空白，构建的基准对相关社区具有较高的学术价值。对比当前主流 encoder 与 LLM (Llama 3, Gemma 3) 的鲁棒性差异，为社区理解大模型在非理想输入下的行为提供了重要实证。来源为 arXiv 论文，实验设计系统规范，结论可靠，但在更广泛的 AI 社区影响力受限于语种特定性。

## 项目链接
https://arxiv.org/abs/2606.30914
