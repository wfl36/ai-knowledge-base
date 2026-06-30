# COMPASS: Grounding Composition-Intent Guidance in Unified Multimodal Models

**评分：** 8.2  
**状态：** 正常  
**标签：** 多模态, 图像生成, 组合控制, MoE, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28696v1 Announce Type: new Abstract: Composition is a high-level visual intent that governs where subjects are placed and how a scene is organized, yet current unified multimodal models remain unreliable at fine-grained composition recognition and struggle to turn such intent into controllable generation. We present COMPASS, the first unified multimodal framework that grounds composition-intent control in a single system spanning both composition perception and composition-guided generation, with a shared expert token $\tau_c$ as the central intent anchor. On the perception side, COMPASS injects composition expertise into an MoE backbone in a minimally invasive manner and distills the inferred intent into $\tau_c$. On the generation side, COMPASS reuses $\tau_c$ as a global conditioning signal that steers the denoising trajectory, effectively converting passive composition analysis into explicit layout control. To support systematic instruction-following composition learning and evaluation at scale, we construct Comp-11, a large-scale dataset with an 11-class taxonomy and reasoning-augmented annotations. Extensive experiments show that COMPASS substantially improves category-level composition understanding and delivers more composition-consistent, prompt-faithful generation than strong baselines.

## 综合总结
本文提出COMPASS框架，首次在单一多模态系统中统一组合感知与组合引导生成。通过共享专家token $\tau_c$ 桥接两端，感知端将组合知识注入MoE并蒸馏意图，生成端复用该token引导去噪实现显式布局控制。同时构建了大规模推理增强数据集Comp-11。实验证明该框架显著提升了类别级组合理解与生成的一致性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文提出了首个统一组合感知与生成的多模态框架COMPASS，核心创新在于使用共享专家token $\tau_c$ 作为意图锚点桥接理解与生成。技术上，感知端采用最小侵入方式将组合知识注入MoE骨干并蒸馏意图，生成端复用该token引导去噪轨迹，将被动的组合分析转化为显式的布局控制。论证严谨，并构建了Comp-11数据集支撑系统性评估，技术深度和新颖性较高。

### 实用性 (评分: 8.0/10)
对多模态大模型从业者在解决“空间组合性差/布局控制弱”痛点上具有高参考价值。MoE的最小侵入式注入方案易于在现有架构上进行改造和扩展，Comp-11数据集可直接用于模型的训练和评测。适用于文生图、视觉问答、图像编辑等需要细粒度空间控制的场景，但统一多模态模型的训练与推理成本可能构成一定的工程落地门槛。

### 社区活跃度 (评分: 8.0/10)
发布于2026年6月，时效性极强，直击当前多模态大模型在细粒度组合意图控制上的前沿痛点。作者团队在图像生成与计算机视觉领域具有一定知名度，来源可信。解决多模态模型“理解易、控制难”的痛点极易引发学术界和工业界的广泛关注与讨论。

## 项目链接
https://arxiv.org/abs/2606.28696
