# "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, AI安全, 对齐, 欺骗性对齐, 可解释性, 论文  
**更新日期：** 2026-06-12  
**来源：** rss  

## 项目描述
arXiv:2606.12618v1 Announce Type: new Abstract: Robust lie detectors for language models could enable powerful techniques for auditing, monitoring, and post-hoc investigation of model behaviour, but evaluating them requires testbeds where models verifiably believe the opposite of what they say. We show that existing trained model organisms often fail this requirement, leaving prior positive and negative detection results difficult to interpret. We address this with 13 reasoning model organisms whose hidden beliefs are verified in chain-of-thought and shown to generalise to held-out tasks, alongside Varied Deception, a prompted-lying testbed covering a broad range of lie-inducing motivations. On these testbeds we evaluate four detectors: a chain-of-thought judge, a logprob classifier, and two activation probes, including Did-You-Lie (DYL), a new method for training follow-up probes. On prompted lying, across 31 open-weight models spanning 2B to 1T parameters, all four detectors show positive scaling with model capability. However, every activation- and logprob-based detector drops sharply on our trained model organisms, with DYL retaining the most signal; only the chain-of-thought judge remains strong, with 0.82 balanced accuracy, partly as an artefact of our verification process favouring CoT-readable beliefs. Current lie detectors therefore cannot support high-confidence claims about model beliefs, and we suggest research directions that may address some of their current limitations. We release our datasets, model organisms, and trained detectors.

## 综合总结
本文针对大模型测谎仪评估中“模型是否真正相信其谎言”的盲区，提出了具有信念验证的推理模型生物体和涵盖多动机的提示说谎测试床。跨尺度（2B-1T参数）评估发现，虽然四种检测器在提示说谎上随模型能力正向缩放，但在训练说谎场景下，基于激活和概率的检测器性能急剧下降，仅CoT检测器保持一定效力（部分归因于验证伪影）。结论指出当前测谎仪尚不足以支持关于模型信念的高置信度声明，为AI安全审计敲响警钟，并开源了全套评估工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
深刻揭示了现有大模型测谎仪评估中“模型是否真正相信其谎言”这一核心盲区，并构建了具有信念验证的推理模型生物体及涵盖多动机的提示说谎测试床。研究严谨区分了提示说谎与训练说谎，发现基于内部状态（激活探针、logprob）的检测器在训练说谎场景下性能骤降，仅CoT检测器有效但受限于验证伪影，展现了极高的技术深度与批判性思维。

### 实用性 (评分: 8.5/10)
对AI安全审计与模型监控具有极高的实践指导意义。研究直接指出了当前基于内部状态的测谎仪在真实欺骗场景下的不可靠性，避免了从业者产生虚假的安全感。同时，开源的测试床、模型生物体和检测器为后续的模型对齐评估提供了可直接复用的基准工具。

### 社区活跃度 (评分: 9.0/10)
研究话题处于大模型安全与对齐领域的最前沿，直击“模型欺骗与测谎”这一高关注度痛点。作者团队包含知名AI安全专家，且全面开源了数据与模型，具有极高的权威性与可复现性。该研究对现有测谎评估范式的颠覆性结论，将在AI安全社区产生深远影响。

## 项目链接
https://arxiv.org/abs/2606.12618
