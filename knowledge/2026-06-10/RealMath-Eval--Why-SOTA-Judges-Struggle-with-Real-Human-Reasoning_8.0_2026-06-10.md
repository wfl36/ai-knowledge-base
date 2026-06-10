# RealMath-Eval: Why SOTA Judges Struggle with Real Human Reasoning

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 评估基准, 数学推理, AI教育, LLM-as-a-Judge, 论文  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.10254v1 Announce Type: new Abstract: While Large Language Models (LLMs) have achieved near-perfect performance in \emph{solving} high-school mathematics, their ability to \emph{evaluate} the diverse reasoning processes of real human students remains under-examined. To bridge this gap, we introduce \textbf{RealMath-Eval}, a rigorously annotated benchmark of 224 real-world exam responses from high schools. Our initial evaluation reveals that even state-of-the-art LLM judges struggle significantly on this task, exhibiting a high Mean Squared Error ($\sim$2.96) against expert human grading. To probe a plausible explanation, we contrast this performance with a control setting where the same judges evaluate synthetic LLM-generated solutions. We identify a stark ``Evaluation Gap'': judges are considerably more accurate and consistent on synthetic text (MSE $\sim$1.17) but struggle to generalize to authentic student reasoning. Through semantic embedding analysis, we find that synthetic errors suffer from a ``structural collapse'' into predictable, low-dimensional linear subspaces, whereas human errors form a more diverse error space. Furthermore, generative probability probes suggest that human reasoning involves significantly higher information-theoretic surprisal, indicating that student reasoning transitions are more out-of-distribution for current models. Finally, we find that surface-level style transfer fails to close this gap. Our findings suggest that current LLM evaluation pipelines relying heavily on synthetic data may not adequately capture the diversity of authentic student mathematical reasoning.

## 综合总结
本文提出RealMath-Eval基准，揭示了当前SOTA LLM评委在评估真实人类数学推理时存在显著的'评估鸿沟'：对合成解答评估准确（MSE~1.17），但对真实学生解答表现糟糕（MSE~2.96）。深入分析表明，合成错误存在'结构坍塌'且惊奇度低，而人类错误空间更多样、更分布外（OOD），表面风格迁移无法弥合此差距。研究警示，依赖合成数据的评估管线无法有效捕捉真实人类推理的复杂性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文具有很高的研究深度与新颖性，精准切中了LLM作为评判者的盲区。通过构建真实学生数学推理数据集与合成数据的对照实验，创新性地提出了'评估鸿沟'（Evaluation Gap）概念。论证过程严谨，结合语义嵌入分析（揭示合成错误的'结构坍塌'）和信息论探针（揭示人类推理的高惊奇度与OOD特性），从几何结构和概率分布双重维度深刻剖析了SOTA模型评估人类真实推理失败的根本原因。

### 实用性 (评分: 7.5/10)
对AI教育、自动评分和LLM-as-a-Judge领域的从业者具有极高的警示和参考价值。研究明确指出依赖合成数据训练或验证的评估管线在真实场景中存在严重泛化问题，甚至表面风格迁移也无法弥补，这指导开发者在构建教育类评估系统时必须引入真实人类数据进行对齐。但受限于基准规模（224条）且未提出具体的解决方案，实际落地指导略受局限。

### 社区活跃度 (评分: 8.0/10)
话题具有极强的时效性，LLM-as-a-Judge是当前大模型社区的核心痛点与热点，而将其应用于数学推理评估更是极具挑战的焦点。论文发布于arXiv，作者团队来自知名学术机构，数据来源基于真实高中考试，具有很高的权威性与可信度。该发现对当前过度依赖模型合成数据的评估范式构成了有力挑战，有望在AI教育及评测社区产生广泛影响。

## 项目链接
https://arxiv.org/abs/2606.10254
