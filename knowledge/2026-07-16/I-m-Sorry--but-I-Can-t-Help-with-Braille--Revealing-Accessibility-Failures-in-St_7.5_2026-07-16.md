# I'm Sorry, but I Can't Help with Braille: Revealing Accessibility Failures in State-of-the-Art LLMs

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 无障碍, 盲文, 评估, 微调, 论文  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.11893v1 Announce Type: new Abstract: Large Language Models (LLMs) perform strongly on many language tasks, but their capability in structurally constrained, accessibility-critical modalities such as Braille remains unclear. We evaluate state-of-the-art LLMs on bidirectional Korean-Braille translation using a human-annotated dataset. Despite expectations that multilingual, instruction-tuned models can generalize to Braille via text representations, we find consistently poor, unstable outputs and substantial disagreement with human judgments. These results point to missing Braille-aware tokenization and weak alignment between Korean and Braille patterns. In contrast, supervised fine-tuning of a small model (T5-small) on the same data yields large and stable gains over zero-shot and prompted LLM baselines across standard metrics (SacreBLEU, ChrF++, CER, BLEU, ROUGE-L, METEOR, CIDEr). Our findings reveal a systematic limitation of current LLMs and demonstrate the effectiveness of modest task-specific supervision.

## 综合总结
本文评估了SOTA大模型在韩语-盲文双向翻译任务上的表现，发现其存在严重的系统性局限，输出质量差且不稳定，原因在于缺乏盲文感知的tokenization和模式对齐。相比之下，对T5-small等小模型进行监督微调能取得显著且稳定的提升。该研究为AI无障碍领域敲响了警钟，并为盲文翻译提供了切实可行的工程实践方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文揭示了当前SOTA LLMs在结构受限的无障碍模态（如盲文）翻译上的系统性局限。通过严谨的对比实验，指出大模型在韩语-盲文双向翻译中表现极差且不稳定，根本原因在于缺乏盲文感知的tokenization及语言与盲文模式的弱对齐，同时证明了小模型通过特定任务SFT能显著超越大模型的zero-shot表现，论证扎实且切中痛点。

### 实用性 (评分: 7.5/10)
对致力于无障碍技术的AI从业者具有极高的实践指导意义。明确警告了直接依赖大模型处理盲文的风险，并提供了低成本、高收益的替代方案（使用T5-small等小模型进行SFT），可直接应用于多语言盲文翻译系统的工程开发中。

### 社区活跃度 (评分: 7.0/10)
无障碍是AI伦理与应用的前沿关注点，该研究话题时效性强，arXiv来源具备基础可信度。尽管盲文翻译相对小众可能限制其广泛影响力，但其揭示的大模型在特定模态下的“系统性失效”对社区具有重要警示作用。

## 项目链接
https://arxiv.org/abs/2607.11893
