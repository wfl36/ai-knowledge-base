# UP-NRPA: User Portrait based Nested Rollout Policy Adaptation for Planning with Large Language Models in Goal-oriented Dialogue Systems

**评分：** 7.8  
**状态：** 正常  
**标签：** 大模型, 对话系统, 用户画像, 规划, 论文  
**更新日期：** 2026-06-15  
**来源：** rss  

## 项目描述
arXiv:2606.13683v1 Announce Type: new Abstract: To address the challenge that current dialogue policy planning methods struggle to dynamically adapt to diverse user characteristics, this paper proposes a User Portrait based Nested Rollout Policy Adaptation (UP-NRPA) online framework with Large Language Models. In contrast to conventional approaches dependent on model training and require offline reinforcement learning policy models for user groups, UP-NRPA enables dynamic customization of dialogue strategies through an adaptive mechanism. This is achieved by leveraging real-time user feedback alongside personality, preferences, and objectives mapped from the current user portrait, thereby adapting to user characteristics without offline reinforcement learning. In collaborative and non-collaborative dialogue benchmarks, UP-NRPA demonstrated considerable benefits, achieving an impressive 100% success rate in multiple dialogue tasks. Particularly in negotiation tasks, the sale-to-list ratio (SL) increased by 56.41%. This demonstrates that UP-NRPA can adapt to diverse user needs without requiring a training mechanism, enabling the dialogue system to adapt to user characteristics.

## 综合总结
本文提出了一种基于用户画像的嵌套滚动策略适应（UP-NRPA）在线框架，结合大语言模型解决目标导向对话系统中的策略规划问题。该方法摒弃了传统的离线强化学习训练依赖，通过实时用户反馈和用户画像动态调整对话策略。实验表明，该方法在多项对话任务中达到100%成功率，并在谈判任务中显著提升了56.41%的SL比率，展现了无需训练即可适应多样化用户需求的强大能力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文提出了UP-NRPA框架，创新性地将嵌套滚动策略适应（NRPA）搜索算法与大语言模型结合，并引入用户画像作为启发式信息。该方法摆脱了传统对话策略对离线强化学习训练的依赖，通过在线自适应机制动态调整策略，技术路径新颖且论证严谨，在协作与非协作场景下均取得了显著的效果提升。

### 实用性 (评分: 8.5/10)
该框架无需离线RL训练，极大降低了对话策略定制的工程门槛和计算成本。通过实时反馈和用户画像即可动态适应用户特征，对目标导向的对话系统（如智能客服、谈判机器人等）具有极高的落地参考价值，适用范围广泛。

### 社区活跃度 (评分: 7.0/10)
结合LLM进行对话策略规划是当前学术界与工业界的热点话题。该论文来源于arXiv，提出的免训练在线适应方案及在基准测试中取得的高指标（100%成功率、SL提升56.41%）具有较强的吸引力和讨论度，但极端数据表现仍需社区进一步验证其泛化性。

## 项目链接
https://arxiv.org/abs/2606.13683
