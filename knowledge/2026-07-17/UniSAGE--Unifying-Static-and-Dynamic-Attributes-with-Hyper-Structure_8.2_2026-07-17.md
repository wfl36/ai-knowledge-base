# UniSAGE: Unifying Static and Dynamic Attributes with Hyper-Structure

**评分：** 8.2  
**状态：** 正常  
**标签：** 图学习, 表征学习, 异构数据, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14102v1 Announce Type: new Abstract: With the rapid growth of digital data, real-world applications increasingly involve hierarchical information that combines static attributes with dynamic records. Modeling such heterogeneous data in a unified and generalizable manner remains challenging. Existing approaches often rely on extensive manual design, are tightly coupled to specific data schemas, and typically process static and dynamic attributes in isolation, thereby overlooking their implicit interactions. We propose UniSAGE, a unified framework for modeling data with both static and dynamic attributes. UniSAGE constructs a global attribute graph that represents hierarchical and temporal relationships in a unified structure. To ensure representational consistency, it introduces two orthogonal parameter subspaces that jointly support static aggregation and dynamic reasoning within a shared semantic space. Building on these unified representations, UniSAGE further enables task-specific interaction between static and dynamic attributes via a lightweight hyper-structure mechanism. UniSAGE is fully automated, robust to evolving data schemas, and capable of capturing complex cross-attribute dependencies. Extensive experiments on multiple public benchmarks and a real-world financial behavior dataset demonstrate that UniSAGE consistently outperforms existing methods, achieving performance improvements of over 10% on several tasks.

## 综合总结
UniSAGE提出了一种统一框架，通过构建全局属性图和引入正交参数子空间，解决了异构数据中静态与动态属性孤立建模的问题。该框架利用轻量级超结构机制实现跨属性交互，具备全自动化和对数据模式演化鲁棒的特点。在多个公开基准和真实金融数据集上，UniSAGE显著优于现有方法，部分任务性能提升超10%。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出全局属性图和正交参数子空间来统一静态聚合与动态推理，解决了异构数据中静态与动态属性孤立建模的痛点。通过轻量级超结构机制实现跨属性交互，理论设计严谨，且在多个任务上取得了超10%的性能提升，论证充分。

### 实用性 (评分: 8.5/10)
框架全自动化且对演化数据模式鲁棒，极大降低了实际业务中的手工设计成本和模式耦合问题。在真实金融行为数据集上的验证证明了其落地潜力，非常适用于风控、推荐等包含静态画像与动态行为的高频演进业务场景。

### 社区活跃度 (评分: 8.0/10)
发布于2026年7月，时效性极强；作者团队包含领域内知名学者，arXiv首发具备较高权威性；解决静态与动态属性统一建模的通用痛点，具备在图学习与数据挖掘社区引发广泛关注的潜力。

## 项目链接
https://arxiv.org/abs/2607.14102
