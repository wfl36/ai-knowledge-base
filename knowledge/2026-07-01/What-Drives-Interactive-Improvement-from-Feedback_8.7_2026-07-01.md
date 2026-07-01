# What Drives Interactive Improvement from Feedback?

**评分：** 8.7  
**状态：** 正常  
**标签：** Agent, 推理, 评估, 多轮交互, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30774v1 Announce Type: new Abstract: We study when natural-language feedback produces improvement beyond the gains obtainable from repeated attempts alone. In multi-turn language agent setting, higher final accuracy can reflect useful feedback, but it can also arise from resampling, format correction, or additional test-time computation. To separate these effects, we introduce a controlled student-teacher protocol across Omni-MATH, Codeforces, BBEH Linguini, and ARC-AGI1, evaluating thirteen open-weight models in both student and teacher roles. We compare external feedback, self-feedback, and unguided self-refinement, while varying interaction history, task difficulty, and teacher access to privileged task information. Across settings, we find that multi-turn improvement is often not evidence of feedback use: self-generated feedback adds little beyond unguided self-refinement, whereas the strongest external teachers produce substantially larger feedback-specific gains, suggesting that useful feedback must provide guidance beyond generic retry. Dense student-teacher interaction matrices further show that interactive gains are driven more by the student's ability to use feedback than by the teacher's identity, although teacher choice remains important for a fixed student. These results suggest that feedback-based agents should be evaluated against repeated-attempt baselines, and that ability to act on feedback, not merely feedback availability, is a central bottleneck for interactive improvement. We release our controlled student-teacher evaluation framework at https://j-lojek.github.io/feedback-generation-is-a-bottleneck/.

## 综合总结
该论文研究了自然语言反馈在多轮语言智能体中产生真实改进的条件。通过引入受控的师生协议并在多个复杂数学、编程与推理基准上评估，发现多轮改进往往源于重复采样而非有效利用反馈。研究表明自我反馈几乎不优于无引导重试，而强外部教师能带来显著增益；且交互提升更取决于学生使用反馈的能力而非教师身份。论文建议反馈型Agent应基于重复尝试基线进行评估，并指出吸收反馈的能力是当前交互改进的核心瓶颈。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
研究深度极高，精准剥离了多轮交互中'重复采样/格式修正'与'真实反馈利用'带来的性能提升。通过严谨的受控师生协议，证实了自我反馈往往等同于无引导重试，而外部有效反馈和学生的吸收能力才是关键，对现有Self-Refine范式提出了有力挑战与澄清。

### 实用性 (评分: 8.5/10)
具有显著的工程指导价值，指出了当前Agent开发中易陷入的'虚假反思提升'陷阱，并提供了基于重复尝试的评估基线及开源框架，帮助开发者在设计多轮交互Agent时更科学地衡量反馈机制的真实收益。

### 社区活跃度 (评分: 8.5/10)
话题紧扣当前大模型Agent与自我反思的研究热点，采用了ARC-AGI1等极具关注度的前沿推理基准，结论对社区现有的评估惯例形成重要冲击，开源代码进一步增强了其影响力和可信度。

## 项目链接
https://arxiv.org/abs/2606.30774
