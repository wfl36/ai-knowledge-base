# Stability vs. Manipulability: Evaluating Robustness Under Post-Decision Interaction in LLM Judges

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 评估, LLM-as-judge, 鲁棒性, 论文  
**更新日期：** 2026-06-06  
**来源：** rss  

## 项目描述
arXiv:2606.05384v1 Announce Type: new Abstract: LLM-as-judge evaluation is widely used in benchmarking pipelines, where model outputs are compared and ranked using automated evaluators. These pipelines typically assume that judgments are stable properties of fixed inputs. We show that this assumption does not hold under interaction. We study post-decision manipulability: the extent to which an evaluation outcome can be altered through subsequent conversation with the judge after an initial decision has been made. Across controlled experiments on MT-Bench and AlpacaEval, we find that LLM judges are highly stable under repeated and neutral reevaluation, yet become substantially reversible under targeted post-decision challenge. An anti-baseline challenge protocol shows that stable judgments can be overturned through motivated interaction, while a counterbalanced target-validation protocol separates this reversibility from net target-directed steering. These reversals have practical consequences: they can degrade agreement with human preferences, shift benchmark rankings, and produce harmful evaluation changes despite high self-reported confidence. Authority framing is especially destabilizing, and revised judgments are often accompanied by low-overlap justifications, suggesting post hoc rationalization rather than reliable error correction. We introduce the Evaluation Robustness Score (ERS) to quantify interactional robustness by combining reversal susceptibility with counterbalanced directional effects. Our findings identify post-decision interaction as a distinct failure mode for LLM-as-judge evaluation and motivate evaluation protocols that measure not only static agreement, but robustness under challenge.

## 综合总结
本文揭示了LLM-as-judge评估在决策后交互中的脆弱性：尽管在中立重评下表现稳定，但在针对性挑战（尤其是权威框架）下极易被操纵逆转，导致与人类偏好一致性下降及排名偏移，且常伴随事后合理化现象。作者提出了评估鲁棒性分数(ERS)及配套挑战协议来量化交互鲁棒性，呼吁评测体系应从仅关注静态一致性转向测量动态挑战下的鲁棒性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文揭示了LLM-as-judge范式在交互环境下的一个关键且易被忽视的失败模式——决策后可操纵性。研究设计严谨，通过引入反基线挑战协议和平衡目标验证协议，成功分离了评估结果的逆转性与方向性引导；同时提出评估鲁棒性分数(ERS)进行量化。对'权威框架'的破坏性及'事后合理化'现象的机制分析具有较强深度和洞见。

### 实用性 (评分: 8.0/10)
对当前广泛依赖LLM作为评判者的基准测试（如MT-Bench, AlpacaEval）具有直接的实践指导价值。提出的ERS指标和挑战协议可直接集成到现有评估流水线中，帮助开发者检测评估器的抗操纵能力，防范恶意提示词攻击或不可靠的动态评估结果，提升评测系统的可信度。

### 社区活跃度 (评分: 8.0/10)
LLM-as-judge是当前大模型领域的核心热点与痛点，该研究直击评估体系的脆弱性，话题时效性极强。作为arXiv上的最新学术论文，其指出的评估漏洞和引入的新度量标准极易引发评测社区的广泛关注与后续跟进，对推动评测标准从静态向动态鲁棒性演进具有较高影响力。

## 项目链接
https://arxiv.org/abs/2606.05384
