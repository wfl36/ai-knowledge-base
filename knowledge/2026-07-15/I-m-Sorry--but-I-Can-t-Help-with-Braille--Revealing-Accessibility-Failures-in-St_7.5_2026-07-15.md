# I'm Sorry, but I Can't Help with Braille: Revealing Accessibility Failures in State-of-the-Art LLMs

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 无障碍, 盲文, 机器翻译, 评估, 论文  
**更新日期：** 2026-07-15  
**来源：** rss  

## 项目描述
arXiv:2607.11893v1 Announce Type: new Abstract: Large Language Models (LLMs) perform strongly on many language tasks, but their capability in structurally constrained, accessibility-critical modalities such as Braille remains unclear. We evaluate state-of-the-art LLMs on bidirectional Korean-Braille translation using a human-annotated dataset. Despite expectations that multilingual, instruction-tuned models can generalize to Braille via text representations, we find consistently poor, unstable outputs and substantial disagreement with human judgments. These results point to missing Braille-aware tokenization and weak alignment between Korean and Braille patterns. In contrast, supervised fine-tuning of a small model (T5-small) on the same data yields large and stable gains over zero-shot and prompted LLM baselines across standard metrics (SacreBLEU, ChrF++, CER, BLEU, ROUGE-L, METEOR, CIDEr). Our findings reveal a systematic limitation of current LLMs and demonstrate the effectiveness of modest task-specific supervision.

## 综合总结
该论文评估了SOTA大语言模型在韩语-盲文双向翻译上的表现，发现其存在严重的性能不足和不稳定性，揭示了当前LLM在结构受限模态（盲文）上的系统性局限，主要归因于缺乏盲文感知的分词机制和弱对齐问题。同时，研究表明通过小模型（T5-small）进行监督微调即可在该任务上取得显著优于大模型零样本/提示词基线的稳定表现，为无障碍AI的工程实践提供了重要参考。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
该论文切入点新颖，聚焦于大模型在结构受限且关乎无障碍的模态（盲文）上的能力盲区。研究设计严谨，通过人工标注数据集对SOTA LLMs进行韩语-盲文双向翻译评估，并深入剖析了性能低下的技术根源（缺乏盲文感知的分词器与韩盲模式弱对齐）。对比实验全面，采用多种主流指标验证了小模型监督微调（SFT）的有效性，论证扎实，揭示了当前LLM在特定符号体系下的系统性局限。

### 实用性 (评分: 7.5/10)
对AI无障碍领域的从业者具有直接的指导价值。研究明确指出在盲文等低资源、强结构化任务中，盲目依赖大模型的泛化能力不可靠，而采用小模型（如T5-small）进行特定任务的监督微调是更高效、稳定的落地路径。此外，结论对多语言LLM的分词器设计及垂直领域适配提供了重要的工程实践参考，适用范围可延伸至其他类似的结构受限模态翻译任务。

### 社区活跃度 (评分: 7.0/10)
话题具有显著的社会价值与时效性，无障碍AI是当前备受关注的重要议题。该研究揭示了先进LLMs在弱势群体需求上的系统性失败，对社区具有强烈的警示作用。来源为arXiv预印本，虽作者单一且需等待同行评审进一步确认权威性，但其指出的LLM能力边界问题极易引发学术界和工业界对无障碍功能评估的广泛讨论与关注。

## 项目链接
https://arxiv.org/abs/2607.11893
