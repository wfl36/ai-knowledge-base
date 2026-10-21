# H2DF: Calibrated Target Bands for Controllable Language-Model Unlearning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-21  
**来源：** rss  

## 项目描述
arXiv:2610.26864v1 Announce Type: new Abstract: Gradient ascent (GA) is a simple language-model unlearning baseline, but it continues increasing forget loss after useful forgetting has occurred. This unbounded pressure can damage retained utility and make forgotten examples abnormally high-loss. We introduce H2DF, a calibrated target-band objective that applies GA-like pressure below a data-dependent lower target and suppresses, or reverses, that pressure after the target region is reached. The targets are estimated from matched non-member examples before training, so the base objective requires one forget-batch forward/backward pass per optimization step; our reported TOFU variant adds sparse retain replay every tenth step. We instantiate a one-sided objective for TOFU question answering and a two-sided objective for MUSE-News language modeling. Across three TOFU seeds, H2DF obtains a forget NLL of 1.528 with margin 0.049 and retain NLL of 1.165 with margin 0.047, matching GradDiff while using retain replay only every tenth step and showing substantially lower variability than GA. On MUSE-News, H2DF improves retention over GA and NPO and is competitive with SimNPO, but does not dominate it. Ablations show that the upper target reduces overshoot and that validation-based checkpoint selection is important. These results support calibrated target bands as a practical mechanism for controlling forgetting strength, while also exposing sensitivity to random seed and calibration quality.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.26864
