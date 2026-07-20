# On the Structure of Address in Multi-Party Dialogue: From Discrete Labels to Continuous Levels

**评分：** 7.5  
**状态：** 正常  
**标签：** 多方对话, 对话系统, 话语指向, 多模态, 人机交互, 论文  
**更新日期：** 2026-07-20  
**来源：** rss  

## 项目描述
arXiv:2607.15648v1 Announce Type: new Abstract: In multi-party dialogues between a dialogue system and multiple users, identifying to whom an utterance is addressed is a key challenge. Prior work has typically treated addressee detection as a multi-class classification task, selecting a single label representing an individual participant or the group. This formulation assumes that address is inherently discrete and has primarily been used for predicting turn-taking. In this paper, we revisit this assumption by analyzing address as a continuous phenomenon. Using a multi-party human dialogue corpus annotated by multiple annotators, we construct both binary address labels derived from majority-vote addressee labels and continuous address levels inferred from annotator judgments using a latent-variable model. We then examine how these representations relate to turn-taking as well as listener behaviors, including gaze and backchannels. Our results show that, in addition to turn-taking, both gaze and backchannels are associated with address. Furthermore, models using continuous address levels achieve better predictive fit than those using discrete labels, suggesting that address may exhibit graded structure. Finally, we discuss the future directions of addressee detection research based on the findings of this study.

## 综合总结
本文挑战了多方对话中话语指向识别的传统离散分类假设，提出将其视为连续现象。通过潜在变量模型从多标注者判断中推断连续层级，并验证了其与话轮转换、注视及回应等听者行为的关联。实验证明连续层级模型比离散标签模型预测拟合度更好，表明话语指向具有分级结构，为未来多方对话系统的受话者检测与多模态交互研究提供了新方向。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
传统多方对话中的受话者检测被建模为离散的多分类问题，本文创新性地将其重新概念化为连续现象。通过引入潜在变量模型从多位标注者判断中推断连续的受话者层级，并结合注视和回应等多模态听者行为进行实证分析，论证严谨，揭示了话语指向的分级结构特征，具有较高的研究深度与新颖性。

### 实用性 (评分: 7.0/10)
研究成果对开发多方对话系统（如社交机器人、虚拟Agent、会议助手）具有直接参考价值。连续层级的话语指向表示能更精细地捕捉说话人对多参与者的注意力分配，有助于改进多模态对话系统中的话轮转换和反馈生成机制，但在大模型工程化落地方面仍需进一步适配与转化。

### 社区活跃度 (评分: 7.5/10)
论文来自京都大学知名语音与对话处理实验室，学术可信度高。多方对话与人机交互是当前AI Agent领域的前沿热点，话题时效性强。该研究对传统离散分类假设的修正，将在多模态对话和语用学细分领域产生积极影响。

## 项目链接
https://arxiv.org/abs/2607.15648
