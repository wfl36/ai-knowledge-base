# On Improving Faithfulness of Podcasts from Documents

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 幻觉/忠实度, 播客生成, 评估框架, 论文  
**更新日期：** 2026-07-27  
**来源：** rss  

## 项目描述
arXiv:2607.21961v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used to generate long-form conversational content such as podcasts from textual sources. While these systems produce fluent and engaging narratives, they often introduce ungrounded information. In this work, we present the first systematic study of faithfulness in document-grounded podcast generation, where grounding must be maintained across conversational turns in long-form, multi-speaker transcripts. We construct a dataset of over 1500 documents spanning five domains and generate podcast transcripts using multiple LLMs. We introduce a turn-level LLM-as-a-judge framework for evaluating whether conversational turns are supported by the source document, and validate its reliability through human studies. Our analysis shows that even state-of-the-art models, including GPT-4o, frequently generate ungrounded content. To mitigate this issue, we propose catch-n-repair, a model-agnostic framework that detects and rewrites unfaithful conversational turns while preserving conversational flow. Experiments demonstrate consistent improvements in faithfulness across both in-domain and out-of-domain settings.

## 综合总结
本文针对大模型生成长篇播客内容时易产生不忠实信息的问题，进行了首次系统性研究。作者构建了跨5个领域的1500+文档数据集，发现即使GPT-4o也频繁生成无根据内容。为此，提出了经人类研究验证的turn-level LLM-as-a-judge评估框架，以及模型无关的catch-n-repair修复框架，通过检测并重写不忠实轮次来提升忠实度。实验证明该方法在域内外均能持续提升生成内容的忠实度，对当前热门的播客生成类应用具有极高的工程落地价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文首次系统性研究了文档驱动的长篇播客生成中的忠实度问题，填补了多轮对话长文本生成评估与优化的空白。技术上，提出了turn-level LLM-as-a-judge评估框架并通过人类研究验证了其可靠性；同时设计了模型无关的catch-n-repair框架，通过'检测-重写'机制在保持对话流畅性的同时修复幻觉。论证严谨，构建了跨5个领域的1500+文档数据集，并揭示了GPT-4o等SOTA模型在此任务上的高频幻觉现象。虽'检测-重写'范式并非全新，但在长对话场景的应用具有显著创新性。

### 实用性 (评分: 9.0/10)
对从业者具有极高的落地参考价值。当前基于文档生成播客（如NotebookLM）是大模型热门应用，但幻觉问题严重制约了其实用性。本文提出的catch-n-repair框架是模型无关的，可直接作为即插即用的后处理模块集成到现有生成管线中，在不更换底层模型的前提下显著提升内容可信度，适用于各类长文本对话生成、有声内容制作及RAG应用场景。

### 社区活跃度 (评分: 8.5/10)
话题时效性极强，紧贴当前AI播客生成应用爆发的热点，直击核心痛点。研究基于GPT-4o等最前沿模型进行实验，且发布于arXiv，具备较高的学术规范和可信度。针对工业界急需解决的幻觉问题，该研究有望在AI工程和产品社区产生广泛影响和讨论。

## 项目链接
https://arxiv.org/abs/2607.21961
