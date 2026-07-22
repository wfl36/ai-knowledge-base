# MILP-Evo: Closed-Loop Fully Automatic Design of MILP Solvers

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 运筹优化, MILP, 求解器, 代码生成, 论文  
**更新日期：** 2026-07-22  
**来源：** rss  

## 项目描述
arXiv:2607.18252v1 Announce Type: new Abstract: Machine learning methods have shown that data-driven policies can accelerate mixed-integer linear programming (MILP) solvers, but many such approaches remain difficult to inspect, adapt, and deploy because the learned policy is represented as an external predictor or other opaque model. By contrast, explicit solver logic is easier to understand and integrate, but is usually hand-designed rather than learned from solver feedback. We study whether the automatic design of MILP solver logic can instead be cast as LLM-guided closed-loop search over executable white-box components evaluated directly by end-to-end solver behavior. To this end, we propose a closed-loop program evolution framework for MILP solver auto-design, implemented through PySCIPOpt, and instantiate it on the joint design of a cut selector and a branching rule. Candidate programs are iteratively generated, loaded into SCIP, and evaluated by direct execution on MILP instances, with the resulting feedback guiding performance-based selection, targeted repair, diagnostic reflection, and diversity-aware population maintenance. The method outputs explicit solver components that can be inspected, modified, and deployed within standard solver workflows. Across four benchmark families, we find that LLM-guided program evolution can discover competitive domain-specialized policies in several settings.

## 综合总结
本文提出MILP-Evo框架，利用LLM引导的闭环程序演化自动设计MILP求解器的白盒组件。区别于传统黑盒ML策略，该方法通过PySCIPOpt迭代生成、评估和优化割平面选择器与分支规则代码，结合性能反馈、定向修复和多样性维护机制，最终输出可直接部署且可解释的求解器逻辑。实验表明，该方法能在多个基准测试中发现具有竞争力的领域专用策略，为求解器自动设计提供了新范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
将LLM与演化搜索结合，用于自动设计MILP求解器的白盒组件，打破了传统ML方法依赖黑盒预测模型的局限，实现了从数据驱动到代码生成的范式转换。通过闭环反馈（性能选择、定向修复、诊断反思与多样性维护）迭代优化割平面选择器和分支规则，技术深度与新颖性较高。

### 实用性 (评分: 8.0/10)
输出为可读、可修改的白盒代码，可直接部署在标准求解器（如SCIP）工作流中，无需额外的模型推理开销，对运筹优化工程师具有极高的落地吸引力。但方法的适用性依赖于特定MILP实例分布的定制化需求，泛化到通用场景仍需验证。

### 社区活跃度 (评分: 8.0/10)
结合了LLM与运筹优化两大热门领域，针对MILP求解器自动设计这一重要痛点问题。作者团队在相关领域有一定积累，预印本发布时间极新，若能切实提升求解器性能，将在运筹优化与AI交叉社区引起广泛关注。

## 项目链接
https://arxiv.org/abs/2607.18252
