# Expert-validated STEM QA

**评分：** 6.7  
**状态：** 正常  
**标签：** 大模型评测, STEM, 数据集, AI for Science, 工程实践, 基准测试, 微调  
**更新日期：** 2026-09-01  
**来源：** rss  

## 项目描述
arXiv:2608.28591v1 Announce Type: new Abstract: Recent advancements in AI are helping scientists achieve breakthroughs in fields such as mathematics, medicine, and materials sciences. New evaluation datasets for AI models contribute to such advancement in AI. In the STEM domain, frontier models have consumed most of the available online data, creating the need for human-created datasets that codify the knowledge of leading experts in the domain. There are several STEM datasets available for the research community in this field. However, there are some gaps in these datasets, leaving room for improvement. Examples of gaps include (1) saturation in model performance on these datasets, leaving no head-room for meaningful evaluations, (2) skewed taxonomy distributions, (3) multiple choice question format that is misaligned with how scientists use AI in the real world, and (4) inaccurate answers and rationales partially led by a contest-based data collection and a time-bound review process. In this study, we present 'Expert-validated STEM QA', a high-quality, expert-validated STEM dataset (N=398) in Physics, Chemistry, Biology, and Mathematics, created by 241 domain experts. We (1) carefully designed a taxonomy with balanced distribution, (2) vetted question contributors with quality-driven incentive, (3) conducted multiple rounds of reviews with revisions validated by domain experts based on consensus, and (4) created the dataset in verifiable question and answer format. Our study demonstrated low performance ($<25\%$) of frontier AI models on the dataset as a benchmark. Post-training on a separate, private version of the dataset (N=2,000) increased performance of the open source model by $15\%$ relative to the baseline model (p=0.045) on the STEM subset of HLE-verified dataset, indicating potential utility of the dataset for model training. We have open-sourced a portion of our dataset for the AI research community.

## 综合总结
本文提出了'Expert-validated STEM QA'数据集，针对现有STEM评测数据集在饱和度、分类分布、问答格式和质量方面的四大缺陷，通过241位领域专家协作构建了包含398条（私有版2000条）物理、化学、生物、数学的高质量可验证QA数据集。前沿模型在该基准上表现低于25%，验证了其作为高难度未饱和评测基准的价值；后训练实验显示15%相对提升（p=0.045）证明了其训练用途。整体贡献以工程方法论和数据资源为主，技术新颖性中等，但对数据集构建实践和大模型STEM能力评估具有明确参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.5/10)
论文针对STEM领域QA数据集的现有缺陷（饱和度、分类偏斜、格式不匹配、答案不准确）提出了系统化的解决方案，包括平衡分类法设计、质量驱动激励、多轮专家评审共识机制以及可验证问答格式。方法论层面有一定的新颖性，特别是在数据集构建流程和质量控制方面提出了明确改进路径，但整体属于工程性贡献而非理论突破。私有数据集上后训练带来15%相对提升（p=0.045）的结果有一定说服力，但样本规模和统计显著性处于边际水平。

### 实用性 (评分: 7.0/10)
对AI研究社区和数据集构建者具有较高的实践参考价值。所提出的四个数据质量改进方向（去饱和、平衡分布、可验证格式、严格专家评审）可直接指导后续STEM数据集的设计。398条公开样本规模较小，但提供了完整的方法论模板。后训练实验表明该数据集可作为微调资源，对开源模型开发者有直接帮助。对模型评估从业者来说，该数据集作为'高难度未饱和'基准具有明确的使用场景。

### 社区活跃度 (评分: 6.5/10)
arXiv发布时间标注为2026年9月，URL编号2608.28591存在异常（格式可疑），需要核实真实发布状态。论文主题契合当前AI for Science和大模型评测领域的热点需求，回应了前沿模型在专业领域评测上的真实痛点。但作者团队机构背景未明确披露，影响力来源的权威性判断受限。数据集已开源部分内容，有利于社区复用和后续引用传播。

## 项目链接
https://arxiv.org/abs/2608.28591
