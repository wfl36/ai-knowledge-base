# IMCBench: A benchmark for multimodal LLMs in Image-grounded Medical Conversations

**评分：** 8.2  
**状态：** 正常  
**标签：** 多模态, 医疗AI, 评估基准, 大模型, 安全性, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28556v1 Announce Type: new Abstract: Recent advances in large language models and vision-language models have enabled reasoning over multimodal data, offering opportunities for clinical applications such as decision support and triaging. However, existing medical AI benchmarks are fragmented: some support multi-turn dialogues but lack images, while others provide multimodal inputs but focus on single-turn QA tasks. To address this gap, we introduce IMCBench, an image-grounded, multi-turn medical conversation benchmark that pairs real, publicly available clinical images with synthetic patient profiles to simulate realistic patient-clinician interactions. Each conversation is evaluated across three clinical dimensions: safety, accuracy, and appropriate use of uncertainty in diagnosis. We benchmark eight multimodal frontier models across four model families (Claude, GPT, Nova, and Llama), scoring each on a 1-5 scale using LLM-as-Jury scoring calibrated against expert clinician annotations. Our results show that Claude Opus 4.6 achieves the highest overall score (3.61), followed by Claude Sonnet 4.6 (3.30) and GPT-5.2 (3.29), though no model dominates all dimensions and safety degrades for both malignant and rare conditions ($\Delta$ = -0.27 each). Ablation studies further reveal that both visual input and EHR context contribute to safe guidance (safety drops of 0.18 and 0.23 on average when each is removed), with stronger models leveraging visual features more effectively. Together, these findings demonstrate that accurate clinical description does not guarantee safe patient guidance, motivating the need for multi-dimensional evaluation frameworks in medical AI.

## 综合总结
本文提出IMCBench，首个结合图像与多轮对话的医学AI基准，通过真实图像与合成档案模拟医患交互，从安全性、准确性和不确定性三个维度评估模型。对8个前沿多模态模型的测试表明，尽管Claude Opus 4.6领先，但所有模型在恶性和罕见疾病上安全性显著下降。消融实验证实视觉和EHR输入对安全指导至关重要，揭示了临床准确性与患者安全指导之间的脱节，强调了多维评估的必要性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
填补了医学AI评估中多轮对话与多模态输入割裂的空白，提出IMCBench基准。创新性地结合真实临床图像与合成患者档案，构建了包含安全性、准确性和不确定性三个维度的评估体系。采用LLM-as-Jury并经专家校准，消融实验严谨地验证了视觉输入和EHR上下文对安全性的贡献，揭示了'准确描述不等于安全指导'的重要洞见，研究深度与论证严谨度高。

### 实用性 (评分: 8.0/10)
对医疗AI模型开发者和临床应用者具有极高的实践指导意义。基准不仅提供评估工具，还明确指出了当前前沿模型在恶性和罕见疾病上的安全短板，以及多模态和上下文信息对提升安全性的关键作用，可直接指导医疗多模态大模型的安全对齐与能力迭代，落地参考价值显著。

### 社区活跃度 (评分: 8.0/10)
多模态大模型在医疗场景的落地是当前AI社区的核心关注点。该研究针对痛点提出多维评估框架，来源为arXiv预印本，作者团队包含业界资深研究者。其揭示的模型安全性隐患对社区具有较强警示作用，话题时效性强，预计将在医疗AI评估领域产生积极影响。

## 项目链接
https://arxiv.org/abs/2606.28556
