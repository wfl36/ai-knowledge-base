# TurnNat: Automatic Evaluation of Turn-Taking Naturalness in Dyadic Spoken Dialogue

**评分：** 8.3  
**状态：** 正常  
**标签：** 语音交互, 全双工, 评估指标, 对话系统, 论文  
**更新日期：** 2026-07-03  
**来源：** rss  

## 项目描述
arXiv:2607.01345v1 Announce Type: new Abstract: Turn-taking naturalness is central to full-duplex spoken dialogue systems, yet its automatic evaluation remains limited. Existing evaluations often rely on human judgments or behavior-specific timing metrics, making it difficult to compare heterogeneous timing failures within a unified framework. We propose TurnNat, a likelihood-based framework for automatic turn-taking naturalness evaluation in two-channel spoken dialogue. A causal turn-taking prediction model trained on natural conversations estimates future two-speaker voice-activity states, and the negative log-likelihood (NLL) of the observed future activity measures timing atypicality. TurnNat pools frame-level NLLs over turn-taking boundary units (TBUs) extracted from utterance onsets and offsets, and aggregates mean and tail TBU scores into a dialogue-level naturalness score. We further construct a controlled perturbation benchmark of paired natural and perturbed dialogue clips, validated by human naturalness judgments. Experiments on this benchmark show that TurnNat successfully identifies unnatural turn-taking perturbations across heterogeneous timing failures.

## 综合总结
本文针对全双工口语对话系统中轮流发言自然度难以自动评估的问题，提出了TurnNat框架。该框架利用因果轮流发言预测模型计算未来语音活动的负对数似然(NLL)来衡量时序非典型性，并通过轮流发言边界单元(TBU)聚合得到对话级自然度分数。同时，作者构建了经人类验证的受控扰动基准，实验证明TurnNat能有效识别异构时序失败下的不自然轮流发言，为语音对话系统提供了统一且高效的自动评估方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
提出了基于似然的统一评估框架TurnNat，利用因果预测模型的负对数似然(NLL)衡量时序非典型性，并创新性地引入轮流发言边界单元(TBU)进行帧级到对话级的分数聚合（结合均值与尾部分数）。技术路线严谨完整，构建了经人类判断验证的受控扰动基准，有效解决了全双工对话中异构时序失败难以在统一框架下比较的痛点。

### 实用性 (评分: 8.5/10)
对全双工语音对话系统开发者具有极高的参考价值。自动化的自然度评估指标能够显著降低高昂的人工评估成本，加速模型迭代与优化。框架设计具备较强的可操作性，可直接集成到现有语音对话系统的评测流程中，适用范围覆盖双人全双工对话场景。

### 社区活跃度 (评分: 8.5/10)
全双工语音交互是当前大模型应用的前沿热点，该研究切中自然度评估缺失的痛点，时效性极强。作为arXiv发布的学术论文，构建了具有人类验证的基准，具备较高可信度。填补了语音对话自然度自动评估的空白，有望在语音交互与对话系统社区产生积极影响。

## 项目链接
https://arxiv.org/abs/2607.01345
