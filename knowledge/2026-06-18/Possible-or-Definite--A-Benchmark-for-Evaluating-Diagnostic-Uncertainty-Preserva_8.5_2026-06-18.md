# Possible or Definite? A Benchmark for Evaluating Diagnostic Uncertainty Preservation in Clinical Text

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 医疗AI, 安全评估, 临床文本, 不确定性, 论文, 基准测试  
**更新日期：** 2026-06-18  
**来源：** rss  

## 项目描述
arXiv:2606.18471v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly used for clinical text tasks such as summarization and revision. While most studies evaluate the fluency and coherence of LLM-generated text, whether LLMs correctly preserve diagnostic uncertainty remains underexplored. In clinical practice, phrases such as ``possible pneumonia'' communicate the strength of available evidence and directly guide decisions about follow-up testing and treatment. Altering these uncertainty expressions can change the clinical meaning entirely. In this paper, we systematically evaluated this problem in two steps. First, we constructed a benchmark of 1,200 clinical documents with 9,184 uncertainty annotations across five levels. Second, we evaluated three LLMs on this benchmark. Our results show that (1) LLMs preserve the original uncertainty cues poorly, often less than half the time; (2) LLMs struggle with nuanced distinctions between adjacent levels. This work reveals a failure mode not captured by standard evaluation metrics and provides implications for the safe deployment of LLMs in clinical workflows.

## 综合总结
本文针对大语言模型在临床文本任务中容易改变诊断不确定性的问题，构建了一个包含5级不确定性标注的基准测试（1200份文档，9184个注释）。通过对三个LLM的评估，发现模型保留原始不确定性提示的能力极差（不足一半），且难以区分相邻级别的细微差异。该研究揭示了传统评估指标未覆盖的严重失败模式，对LLM在临床工作流中的安全部署具有重要警示与指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文具有显著的研究深度与新颖性。传统LLM评估多聚焦于文本的流畅性与连贯性，而本文敏锐捕捉到了临床文本中'诊断不确定性'（如'可能肺炎'与'肺炎'的区分）这一极具专业门槛且至关重要的语义特征。研究不仅系统性地定义了5级不确定性标注体系，还构建了包含9,184个注释的基准测试，论证过程严谨扎实，揭示了LLM在细微语义级别区分上的结构性缺陷。

### 实用性 (评分: 9.0/10)
对医疗AI从业者具有极高的落地指导价值。在临床实践中，不确定性表达直接关联后续的检查与治疗方案，误判可能导致过度医疗或延误治疗。本文指出的LLM'不确定性保留率不足一半'的失败模式，为医疗大模型的安全部署敲响了警钟，可直接指导临床文本生成系统的评估指标设计、微调数据构建及安全护栏的开发。

### 社区活跃度 (评分: 8.0/10)
话题时效性强，切中当前大模型在垂直领域（尤其是高风险的医疗领域）安全落地的核心痛点。虽然作者团队相对新锐，但该研究指出的'标准评估指标未捕捉到的失败模式'极具启发性，对医疗NLP社区和AI安全对齐领域具有较强的影响力潜力，有望引发对专业领域语义保真度评估的广泛关注。

## 项目链接
https://arxiv.org/abs/2606.18471
