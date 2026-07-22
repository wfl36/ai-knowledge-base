# A Classifier That Teaches Itself: Self-Improving, Frozen-gate Training (SIFT) for Dynamic Document Classification

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 文档分类, 持续学习, 弱监督学习, 模型安全, 论文, 工程实践, 系统架构  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18358v1 Announce Type: new Abstract: Document classification is a solved problem in the laboratory and an unsolved one in the enterprise. The blocker is rarely model architecture; it is the labeling project that must precede a model and the institutional fear of letting a model retrain itself once one exists. We present SIFT (Self-Improving, Frozen-gate Training), a dynamic classifier service, which attacks both. SIFT serves classification from a deliberately cheap, CPU-bound pipeline, a SPLADE sparse encoder feeding a LightGBM head, and escalates only the low-confidence minority of pages to an LLM judge. The judge's verdicts are written back into a labeled corpus, so the expensive model continuously teaches the cheap one: the escalation rate falls, the corpus grows from production traffic rather than from an up-front annotation effort, and accuracy compounds with use. Onboarding a new document family requires only a declarative bundle, label space, anchor phrases, and a judge glossary, not a labeling project. The harder problem is safety: an autonomously retraining classifier can silently regress. SIFT resolves this with a two-part promote gate, a critical-label F1 regression check plus a frozen golden regression set the model is never trained on, either of which vetoes promotion. This turns "retrain monthly without a human" from reckless into routine. We describe the architecture, the self-feeding corpus loop, the frozen-gate promotion mechanism, and an illustrative multi-domain deployment, and we discuss the economics of a classifier whose marginal labeling cost trends toward zero.

## 综合总结
本文提出SIFT（自改进、冻结门训练）动态文档分类系统，解决企业级分类中标注成本高和自动重训风险大的痛点。系统采用SPLADE+LightGBM的轻量级CPU管线处理大部分请求，仅将低置信度样本升级给LLM裁判，裁判结果回写语料库实现'强教弱'的自改进闭环。为保障安全，设计了包含关键标签F1检查和冻结黄金集否决的'冻结门'机制，防止模型静默回归。该方案使边际标注成本趋于零，让无人值守的自动重训变得安全可靠。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出SIFT（自改进、冻结门训练）架构，创新性地结合SPLADE稀疏编码器与LightGBM作为轻量级基座，将低置信度样本交由LLM裁判进行弱标注并回写语料库，实现'强教弱'的自改进闭环。针对自动重训可能导致模型静默回归的安全痛点，设计了双保险的'冻结门'机制（关键标签F1回归检查+冻结黄金回归集否决权），论证严谨，系统设计巧妙，在系统架构层面具有显著的新颖性。

### 实用性 (评分: 9.5/10)
极具落地价值。直击企业级文档分类的两大痛点：高昂的前期标注成本与对模型自动重训练的安全担忧。架构基于CPU友好的成熟组件，通过LLM裁判实现生产流量的自动标注，使边际标注成本趋于零；声明式接入新文档类型极大降低了业务接入门槛；'冻结门'机制让无人值守的自动重训成为安全可靠的常规操作，对工业界从业者具有极强的实践指导意义。

### 社区活跃度 (评分: 8.0/10)
话题时效性强，契合当前业界利用大模型降低数据标注成本及实现模型持续进化的热点。来源为arXiv，针对企业级AI落地的核心痛点，提出的'零边际标注成本'与'安全自动重训'理念对工程和算法社区具有很高的参考价值和潜在影响力。

## 项目链接
https://arxiv.org/abs/2607.18358
