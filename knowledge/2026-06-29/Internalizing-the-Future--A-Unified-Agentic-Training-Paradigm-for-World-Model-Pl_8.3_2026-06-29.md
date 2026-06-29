# Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning

**评分：** 8.3  
**状态：** 正常  
**标签：** Agent, 世界模型, 推理, 强化学习, 论文  
**更新日期：** 2026-06-29  
**来源：** rss  

## 项目描述
arXiv:2606.27483v1 Announce Type: new Abstract: Large language model (LLM) agents have demonstrated strong capability in sequential decision-making, yet they remains fundamentally reactive in long-horizon tasks. Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. Therefore, we propose to internalize future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate-a textual analogue of the Q-value. Crucially, we identify a format-capability gap: simply fine-tuning agents on look-ahead traces during post-training leads to superficial mimicry of foresight without genuine predictive grounding. To bridge this gap, we introduce a three-stage training paradigm: (i) World Model Agentic Mid-Training (WM-AMT) to inject latent predictive capabilities into the policy; (ii) Format-Eliciting SFT (FE-SFT) to structure this injected capability; and (iii) Foresight-Conditioned Reinforcement Learning (FC-RL) to refine the calibration and utility of the generated simulations. Evaluated on search and mathematical reasoning tasks, our approach consistently outperforms other training baselines. Our results demonstrate that effective internal world modeling in LLM agents requires a capability-first training pipeline to achieve grounded and calibrated foresight.

## 综合总结
本文针对LLM Agent在长程决策中缺乏内部世界模型导致的被动反应问题，提出了一种统一的世界模型规划训练范式。研究揭示了简单微调导致的“格式-能力差距”，并创新性地设计了能力优先的三阶段训练管线（WM-AMT、FE-SFT、FC-RL），将未来状态推演与成功概率估计内化至自回归模型中。实验表明该方法在搜索与数学推理任务上显著超越基线，为构建具备真正预见性规划能力的Agent提供了重要突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
深刻揭示了LLM Agent在长程规划中的“格式-能力差距”，即简单微调仅能产生表面的预见模仿而无实质预测基础。创新性地提出将未来状态推演与成功概率估计（文本化Q值）内化至单一自回归模型，并设计了WM-AMT、FE-SFT、FC-RL三阶段严谨的训练范式，论证逻辑清晰，技术深度高。

### 实用性 (评分: 7.5/10)
提出的三阶段训练范式为解决Agent长程规划问题提供了明确的工程实践路径，对开发具备深度规划能力的Agent具有较高参考价值。但实施该管线需构建特定的预测数据集与RL环境，落地门槛中等，目前验证范围限于搜索与数学推理任务。

### 社区活跃度 (评分: 8.5/10)
紧扣当前大模型领域最前沿的Agent与世界模型热点，极具时效性与话题度。论文发布于arXiv，作者团队具备一定学术背景，且通过实验有效验证了方法优于现有基线，具备较高的学术可信度与潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.27483
