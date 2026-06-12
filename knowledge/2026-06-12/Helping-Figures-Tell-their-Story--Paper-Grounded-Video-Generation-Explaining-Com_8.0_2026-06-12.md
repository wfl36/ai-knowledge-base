# Helping Figures Tell their Story! Paper-Grounded Video Generation Explaining Complex Scientific Figures

**评分：** 8.0  
**状态：** 正常  
**标签：** 多模态, 视频生成, 科学图表理解, 基准评测, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12576v1 Announce Type: new Abstract: Scientific figures compress complex pipelines into a single canvas, yet understanding them requires paper-grounded, step-by-step narration aligned with visual highlights a capability missing from current video generation systems and benchmarks. To address this, we introduce paper-grounded figure-to-video generation: generating narrated, region-grounded walkthrough videos from a figure and its paper. We propose MINARD (Multimodal Interpretation of Narrated Architecture via Region Decomposition), a pipeline that generates paper-grounded narrations and sequentially grounds them to figure regions. We also release FigTalk, a benchmark with new sequential and component-level grounding metrics derived. On FigTalk, MINARD generates humanlike, paper-faithful narrations and outperforms narration-conditioned figure spatial grounding compared to existing approaches in both automatic and human evaluation

## 综合总结
本文提出全新任务“基于论文的图表到视频生成”，解决现有系统无法对科学图表进行逐步视觉高亮与旁白对齐解释的问题。作者提出MINARD流水线实现忠于论文的旁白生成与区域定位，并发布FigTalk基准及新评估指标。实验表明MINARD在自动与人工评估中均优于现有方法，生成效果接近人类水平。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了新颖的“基于论文的图表到视频生成”任务，填补了现有系统在科学图表细粒度解释与视觉高亮对齐上的空白。设计了MINARD流水线实现旁白生成与区域顺序定位，并构建了FigTalk基准及全新的组件级/顺序定位评估指标，技术深度与创新性兼备，实验论证严谨。

### 实用性 (评分: 7.5/10)
对学术教育、论文辅助阅读和科普视频自动化制作具有较高参考价值。MINARD流水线可直接指导多模态系统开发，但受限于科学图表的复杂性和专业门槛，当前落地范围主要聚焦于科研与教育垂直领域。

### 社区活跃度 (评分: 8.0/10)
视频生成与多模态理解是当前AI热点，结合科学文献解释具有很强的时效性。作者团队包含NLP领域知名学者，arXiv首发可信度高。该任务定义新颖，有望在学术多媒体处理社区引发关注和后续研究。

## 项目链接
https://arxiv.org/abs/2606.12576
