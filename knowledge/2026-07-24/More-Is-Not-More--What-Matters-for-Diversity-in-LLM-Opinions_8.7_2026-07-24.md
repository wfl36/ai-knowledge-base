# More Is Not More: What Matters for Diversity in LLM Opinions?

**评分：** 8.7  
**状态：** 正常  
**标签：** 大模型, 多样性, 角色模拟, 合成数据, 论文  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20429v1 Announce Type: new Abstract: Large language models are increasingly used to simulate diverse human opinions in open-ended tasks such as synthetic surveys, focus group modeling, and public opinion prediction. However, LLM outputs exhibit systematic opinion homogenization. Practitioners have explored various interventions to increase diversity, but the landscape remains fragmented: different methods are evaluated in isolation with incomparable metrics, and in practice they are typically deployed and upgraded simultaneously, making it difficult to attribute gains to specific components. To advance a more scientific understanding of LLM output diversity, we design a factorial experiment that separates two primary intervention dimensions: input conditioning (operationalized through persona depth) and interaction architecture. We evaluate all conditions on 100 real-user open-ended questions across 7 models, measuring diversity with multiple complementary metrics. Our findings challenge several common assumptions. First, more persona detail does not monotonically increase diversity. The initial step of persona conditioning already captures the majority of the gain, while further elaboration with demographic detail does not consistently improve and can reduce diversity on some models. Second, rather than seeking a single best interaction architecture, we find that different architectures explore largely non-overlapping opinion regions. Combining multiple architectures yields broader coverage than optimizing any one. Third, commonly attempted low-cost alternatives such as raising sampling temperature and adding diversity instructions produce negligible effects compared to structured interventions. Overall, our work demonstrates that diversity is not a product of scaling along any single dimension, but is highly sensitive to the structural form and combination of interventions.

## 综合总结
本文通过因子实验探究了提升LLM输出多样性的有效方法，挑战了三个常见假设：1) 角色细节并非越多越好，基础角色设定已能获取大部分多样性收益，过度增加细节甚至可能起反作用；2) 不存在单一最优的交互架构，不同架构覆盖不同的意见空间，组合使用效果更佳；3) 提高采样温度或添加多样性指令等低成本方法对提升实质性多样性几乎无效。研究表明，LLM多样性并非单维度的简单缩放，而是高度依赖于干预措施的结构形式与组合方式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
研究设计严谨，采用因子实验有效分离了输入条件化（角色深度）与交互架构两个维度的干预效果。结论具有高度反直觉性和理论价值，有力挑战了'角色细节越多越好'、'存在单一最优架构'以及'调高温度/加指令可提升多样性'等业界常见假设，揭示了多样性是干预结构组合的产物而非单维度的线性缩放。

### 实用性 (评分: 8.5/10)
对从事合成数据生成、焦点小组模拟和民意预测的从业者具有极高的实操指导价值。结论直接否定了低效的'堆砌角色细节'和'调温度/加指令'做法，指导从业者将资源集中在基础角色设定和组合多种交互架构上，从而以更低成本获得更广泛的真实意见覆盖。

### 社区活跃度 (评分: 8.5/10)
话题直击当前大模型应用中'输出同质化'的痛点，属于社区高度关注的合成数据与模拟方向。作为arXiv新发论文，其颠覆性结论极易引发广泛讨论，对纠正业界当前关于提升LLM多样性的错误认知具有重要影响力。

## 项目链接
https://arxiv.org/abs/2607.20429
