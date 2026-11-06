# Interactive Backdoor Attacks in LLM-Based Proactive Dialogue Systems

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-06  
**来源：** rss  

## 项目描述
arXiv:2611.06969v1 Announce Type: new Abstract: LLM-based proactive dialogue systems provide goal-directed support through sustained interaction. Fine-tuning their underlying models on externally supplied dialogue data introduces backdoor risks. Existing LLM backdoor studies primarily focus on eliciting an attacker-specified response upon trigger activation. We present an interactive backdoor attack framework that uses training-data poisoning to steer post-trigger, multi-turn interactions toward an attacker-specified objective. Poisoned fine-tuning dialogues implant a trigger-conditioned guidance-policy bias that ordinary user utterances can activate, without deployment-time prompt modification or further attacker intervention. Specifically, we instantiate three complementary attacks under progressively expanded post-trigger interaction settings: (1) Direct Attack, which targets an immediate response deviation upon trigger activation, retaining the conventional trigger--response setting; (2) Constrained Progressive Attack, which progressively advances the attack objective along a predefined multi-turn trajectory; and (3) Unconstrained Progressive Attack, which extends target-directed steering to open-ended interactions with varied user continuations. Using psychological counseling as a representative setting, experiments on two LLM backbones and two dialogue datasets show that all three attacks effectively achieve their objectives under their respective interaction settings while largely preserving normal utility. Separate defense evaluations show that the tested training-data filters retain nearly all poisoned dialogues, while three post-admission baselines leave substantial residual attack-specific success.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.06969
