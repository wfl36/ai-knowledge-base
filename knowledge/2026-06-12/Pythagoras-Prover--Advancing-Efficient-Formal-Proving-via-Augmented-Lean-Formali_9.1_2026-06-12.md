# Pythagoras-Prover: Advancing Efficient Formal Proving via Augmented Lean Formalisation

**评分：** 9.1  
**状态：** 正常  
**标签：** 定理证明, 大模型, 推理, 形式化验证, 数据增强, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12594v1 Announce Type: new Abstract: Modern Lean theorem provers achieve strong performance only with substantial training and inference compute, driven in part by scarce verified proof data and the long reasoning traces of formal proof search, making both supervised fine-tuning (SFT) and sampling expensive. We introduce Pythagoras-Prover, a compute-efficient open-source family of Lean theorem provers built for practical compute budgets. The family spans two generation paradigms: autoregressive models at 4B and 32B parameters, and a first proof-of-concept diffusion-based prover (4B) that iteratively refines Lean proofs at inference time. For training efficiency, we build a Lean-verified corpus stratified into easy, medium, and hard problems for curriculum SFT, so models acquire proof skills progressively from shorter, simpler proofs to longer, harder ones. During SFT, a dynamic proof-reasoning filtering scheme preserves informative proof traces while keeping each instance within an 8k-token context budget. We also introduce Augmented Lean Formalisation (ALF), which expands scarce verified corpora into variants of formal statements, populated via self-distillation for extra training signal without formally verifying every mutated instance. By perturbing known problems while preserving their formal character, ALF reduces reliance on any statement's surface form. Empirically, Pythagoras-Prover-4B surpasses DeepSeek-Prover-V2-671B at pass@32 on MiniF2F-Test (86.1% vs 82.4%) with ~167x fewer parameters, while Pythagoras-Prover-32B sets the open-source state of the art at 93.0% on MiniF2F-Test and solves 93 of 672 PutnamBench problems. We release MiniF2F-ALF, an ALF-mutated contamination-sensitive benchmark on which every evaluated model loses accuracy; here our 32B remains strongest and our 4B matches the prior state of the art, Goedel-Prover-V2-32B.

## 综合总结
本文提出了Pythagoras-Prover，一个计算高效的开源Lean定理证明器家族。针对形式证明数据稀缺和搜索成本高昂的问题，本文创新性地提出了ALF数据增强方法，通过自蒸馏生成形式陈述变体以扩充训练语料，并结合课程学习SFT与动态过滤机制提升训练效率。模型家族包含4B/32B自回归模型及首个4B扩散证明模型。实验表明，其4B模型在MiniF2F-Test上以167倍更少的参数超越DeepSeek-Prover-V2-671B，32B模型则创下93.0%的开源SOTA记录。此外，团队还发布了防污染基准MiniF2F-ALF，进一步验证了模型的泛化能力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.2/10)
论文在方法上具有显著新颖性与深度，首次将扩散模型引入Lean形式证明领域进行迭代精炼；提出的ALF（Augmented Lean Formalisation）数据增强方法通过自蒸馏扰动生成变体，有效缓解了形式化验证数据稀缺问题，并减少模型对题目表面形式的过拟合；结合课程学习与动态过滤机制，技术栈完整且论证严谨，4B模型超越671B模型的结果极具说服力。

### 实用性 (评分: 8.8/10)
对从业者具有极高的实践指导价值。ALF数据增强策略、课程学习SFT及动态推理过滤方案可直接迁移至其他形式化语言（如Coq、Isabelle）或长推理轨迹的代码生成任务中；开源的4B和32B模型大幅降低了Lean自动证明的算力门槛，可直接集成到数学研究或形式化验证的IDE辅助工具中；发布的MiniF2F-ALF基准为社区提供了更可靠的防污染评估手段。

### 社区活跃度 (评分: 9.3/10)
紧扣当前大模型推理与形式化数学的前沿热点，在DeepSeek-Prover等巨量参数模型发布后迅速给出了极高参数效率的开源替代方案，时效性极强；作者团队包含知名NLP/形式化验证学者，来源权威可信；4B参数量超越671B的极致对比及开源SOTA成绩极具传播力，将引发AI for Math社区的广泛关注与跟进。

## 项目链接
https://arxiv.org/abs/2606.12594
