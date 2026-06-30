# Data and Evaluation Closed-Loop for Model Capability Enhancement

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 预训练, 数据工程, 评估, 闭环优化, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28471v1 Announce Type: new Abstract: Model capability is the central variable in LLM pre-training, yet is never observed directly: data shapes it prospectively, while evaluation reveals it only retrospectively, compressing samples, prompts, decoding, and scoring rules into one noisy score. Practical optimization runs this backward: a failure is observed first, and the engineer must infer the corpus fix. The two sides speak incompatible vocabularies -- benchmark names and per-sample correctness versus data sources, domains, and quality labels -- so this inference is usually intuition, not method. We close this gap with the \emph{capability slice}: a group of evaluation samples sharing background condition, task type, solving operation, and output constraint -- precise enough to localize a single weakness yet stable enough to survive aggregation, unlike a benchmark name, too coarse, or a single sample, too noisy. Built around this unit, an evaluation taxonomy, a non-instruction data taxonomy, and mapping rules form a closed loop turning a benchmark-level failure into a targeted, testable data intervention. We test this loop on two case studies pulling in opposite directions. First, the loop rules the data out: continued pre-training drives BBH down by $-46.82\%$, but diagnosis traces this to a single masked \texttt{\textless EOS\textgreater} loss rather than weakened reasoning; restoring it recovers BBH to $66.44$, above the original checkpoint, without changing the data. Second, the loop rules the data in: a persistent math-reasoning weakness is decomposed by solving operation into specific failing combinations, and a weakness-targeted sampling procedure built from it lifts AIME2025/AIME2026 Pass@128 from $6.67$/$0.00$ to $26.67$ each. The same unmodified loop reaches opposite, correct verdicts in both cases, showing the evaluation-to-data inference can be routine, auditable, and experimentally validated rather than intuitive.

## 综合总结
该论文针对大模型预训练中评估与数据词汇不兼容、导致数据修复依赖直觉的痛点，提出了“能力切片”概念，构建了从评估失败到数据干预的闭环系统。通过两个案例验证了该框架的双向有效性：一是发现BBH性能下降实为masked EOS loss所致而非推理退化，恢复后性能反超；二是通过针对性数据采样显著提升AIME数学推理成绩。该研究将数据修复从直觉驱动转变为系统化、可审计的方法，对大模型数据工程具有重要指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
提出了“能力切片”这一新颖概念，精准刻画了评估样本与数据干预之间的映射关系，解决了大模型训练中评估与数据'词汇不兼容'的核心痛点。论证严谨，通过两个反向案例（排除数据问题与引入数据干预）闭环验证了方法的有效性，特别是发现BBH下降源于EOS loss而非推理退化的洞察极具深度，将传统的直觉驱动转化为系统化、可审计的工程方法。

### 实用性 (评分: 8.5/10)
对大模型预训练和持续预训练的从业者具有极高的实操参考价值。构建的评估分类法、数据分类法及映射规则，可直接指导工程师进行错误归因与针对性数据补充，大幅降低试错成本。无论是排查性能退化还是强化特定能力（如数学推理），该闭环框架都提供了清晰、可落地的操作路径。

### 社区活跃度 (评分: 8.0/10)
聚焦大模型数据工程与评估对齐的前沿痛点，话题时效性极强。arXiv论文形式发布，且实验涉及AIME2025/2026等高难度基准并取得显著提升，若结果可靠将在AI工程与研发社区产生较大影响力。但作者相对小众，且发布时间标注为未来（2026年），可信度需后续同行评议验证，故适度保守给分。

## 项目链接
https://arxiv.org/abs/2606.28471
