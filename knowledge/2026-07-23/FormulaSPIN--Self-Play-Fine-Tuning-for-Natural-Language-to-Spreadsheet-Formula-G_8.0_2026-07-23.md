# FormulaSPIN: Self-Play Fine-Tuning for Natural Language to Spreadsheet Formula Generation

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 代码生成, 自博弈, 强化学习, 论文  
**更新日期：** 2026-07-23  
**来源：** rss  

## 项目描述
arXiv:2607.19354v1 Announce Type: new Abstract: Spreadsheet applications are used by hundreds of millions worldwide, yet writing formulas remains a significant barrier. Existing approaches rely on static supervised data, which quickly saturates on limited annotations. In this paper, we introduce FORMULASPIN, a self-play framework that breaks the ceiling of supervised fine-tuning by enabling iterative self-improvement without any additional data. Vanilla SPIN fails on this task: it uniformly penalizes every non-matching output, so execution-equivalent alternatives are punished as negatives in one example while serving as ground truth in another, producing contradictory gradients. Our framework resolves this by exploiting formula generation's unique advantage: binary executability provides implicit supervision that separates semantic errors from valid stylistic variants. We frame training as a two-player game in which the main player learns to prefer ground-truth formulas over those from its previous version, while execution feedback sorts outputs into distinct granularities-enabling an adaptive curriculum that shifts from semantic correctness to stylistic refinement. To further increase accuracy, we incorporate ExecVote, a semantic-level voting mechanism that naturally handles multiple valid formulations. Experiments on multiple benchmarks demonstrate that FORMULASPIN achieves state-of-the-art performance, with 74.9% exact match and 87.1% execution accuracy on NL2FORMULA, matching models trained with additional preference annotations while outperforming both traditional SFT and frontier proprietary models. These findings underscore self-play's potential to tackle scarce data tasks and open the door to extending it beyond executable domains.

## 综合总结
本文提出FORMULASPIN框架，针对自然语言到电子表格公式生成任务，解决了传统SPIN方法因惩罚执行等价变体而产生矛盾梯度的问题。通过利用公式的二进制可执行性提供隐式监督，将训练构建为自适应课程学习的双人博弈，并结合ExecVote机制处理多种有效表达。实验表明，该方法在无需额外偏好数据的情况下达到SOTA，为可执行代码/公式生成领域的自迭代训练提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文深入分析了传统SPIN在公式生成任务中的失败原因，即对执行等价但形式不同的输出施加矛盾梯度。通过引入二进制可执行性作为隐式监督，将语义错误与风格变体分离，并构建了从语义正确到风格优化的自适应课程学习，技术方案新颖且论证严谨。

### 实用性 (评分: 8.0/10)
针对数亿用户面临的电子表格公式编写痛点，提出无需额外偏好标注的自迭代框架。其利用执行反馈区分语义与风格的方法，不仅适用于Excel公式生成，还可广泛迁移至任何具备可执行验证机制的代码生成任务，对工业界落地极具参考价值。

### 社区活跃度 (评分: 7.5/10)
自博弈与自我改进是当前大模型后训练的热点方向。该论文在arXiv发布，来源具备权威性，且在NL2FORMULA基准上达到SOTA，超越传统SFT和闭源模型，对解决数据稀缺场景下的模型训练具有重要启示和影响力。

## 项目链接
https://arxiv.org/abs/2607.19354
