# MedRealMM: A Real-World Multimodal Benchmark for Chinese Online Medical Consultation

**评分：** 9.1  
**状态：** 正常  
**标签：** 医疗AI, 多模态, 大模型评测, 线上问诊, 论文, 数据集/基准  
**更新日期：** 2026-07-13  
**来源：** rss  

## 项目描述
arXiv:2607.09142v1 Announce Type: new Abstract: Large language models (LLMs) are increasingly deployed in online medical consultation, yet existing benchmarks remain poorly aligned with real clinical practice. Many rely on synthetic conversations or patient simulators, omit patient-uploaded medical images, or evaluate open-ended clinical responses using multiple-choice or lexical-overlap metrics that poorly reflect clinical quality. We introduce \textbf{MedRealMM}, a large-scale benchmark for multimodal online medical consultation built from de-identified patient-doctor interactions collected from a nationwide Chinese internet hospital. MedRealMM uses a Multimodal Clinical Challenge Point (MCCP) extraction framework to identify clinically demanding moments in authentic consultation trajectories and converts each into a standardized next-response generation task while preserving the preceding text-image context. Each instance is paired with a case-specific rubric refined by physicians that rewards clinically desirable behaviors and penalizes unsafe, unsupported, or contradictory responses. The current release contains 5,620 real-world multimodal cases spanning 64 clinical departments. We evaluate 19 general-purpose and medical-specialized LLMs, including text-only and multimodal systems. Our results show that image information is critical for reliable clinical performance and that current frontier models remain below the online physician response. Although some frontier models satisfy as many or more positive clinical criteria than physicians, they trigger more negative criteria, indicating that safety-sensitive error avoidance remains a central bottleneck. MedRealMM offers a realistic and reproducible benchmark for evaluating multimodal medical reasoning in real-world online consultation. The dataset will be publicly available on Hugging Face at https://huggingface.co/datasets/jdh-algo/MedRealMM.

## 综合总结
MedRealMM是一个针对中文在线医疗问诊的真实世界多模态基准。该研究基于全国性互联网医院的真实脱敏数据，提出了MCCP提取框架和医生细化的病例特异性评分标准（区分正负向临床行为）。数据集包含5620个覆盖64科室的多模态病例。对19个LLM的评测表明，图像信息对临床可靠性至关重要，且当前前沿模型虽在正向标准上接近医生，但在安全敏感的负向错误规避上仍是核心瓶颈。该基准为多模态医疗推理提供了高真实度、可复现的评测标准。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
针对现有医疗评测脱离真实临床、缺乏图像及评估指标单一等痛点，创新性地提出了多模态临床挑战点（MCCP）提取框架，将真实问诊轨迹转化为标准化生成任务；设计了由医生细化的病例特异性评分标准，通过奖惩机制（奖励临床期望行为，惩罚不安全/矛盾回复）更精准地衡量临床质量，深刻揭示了当前模型在安全敏感错误规避上的核心瓶颈。

### 实用性 (评分: 9.2/10)
对医疗大模型研发团队具有极高的落地参考价值。基于真实互联网医院脱敏数据构建，覆盖64个科室的5620个多模态病例，且数据集已在Hugging Face开源，可直接作为线上问诊场景的标准化测试集；其MCCP框架和正负向评分体系也可被复用于构建其他垂直领域的专业评测基准。

### 社区活跃度 (评分: 9.3/10)
医疗多模态大模型是当前AI社区的核心热点，线上问诊需求迫切。该基准源自全国性互联网医院真实交互数据，由专业医生参与制定评分标准，来源权威、可信度极高；其揭示的“模型负向安全错误多于医生”的结论对行业具有强警示作用，开源数据集将显著推动医疗AI社区的发展。

## 项目链接
https://arxiv.org/abs/2607.09142
