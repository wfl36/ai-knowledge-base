# Expert-Aware Refusal Steering

**评分：** 7.8  
**状态：** 正常  
**标签：** 大模型, MoE, 安全对齐, 机制可解释性, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04160v1 Announce Type: new Abstract: Safety alignment in instruction-tuned large language models (LLMs) depends on a model's ability to reliably refuse to respond to harmful or disallowed requests. Recent work has shown that a steering vector can be applied to a dense LLM during inference to effectively suppress refusal behavior, inducing response to harmful requests. We extend this refusal steering method to three open-source Mixture-of-Experts (MoE) LLMs and find that steering performance is uninhibited by the complex routing patterns inherent to the MoE architecture. We then propose two expert-aware refusal steering methods that leverage refusal-specific expert routing patterns and expert-specific steering directions to suppress normal refusal behavior. We find that refusal behavior can be effectively steered based on the output of a single expert. Our results show that refusal signals captured by steering methods differ from expert routing behavior, suggesting a substantial role for attention in MoE refusal behavior.

## 综合总结
本文将大模型的拒绝行为引导技术扩展至MoE架构，提出了两种专家感知的拒绝引导方法。研究发现MoE的路由模式并未阻碍引导效果，且拒绝行为可由单一专家输出控制，同时揭示了注意力机制在MoE拒绝行为中的关键作用，为MoE模型的安全对齐与红队测试提供了重要洞见。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
将拒绝引导方法从稠密大模型扩展至MoE架构，提出了两种利用拒绝特定路由模式和专家特定引导方向的专家感知方法。研究发现MoE复杂的路由模式并未阻碍引导效果，且拒绝行为可基于单一专家输出被有效引导，揭示了注意力机制而非路由在MoE拒绝行为中的重要作用，具有较高的机制可解释性研究深度。

### 实用性 (评分: 7.0/10)
对AI安全红队测试和MoE模型的对齐加固具有直接参考价值。通过揭示单一专家即可控制拒绝行为以及注意力机制的作用，为开发更鲁棒的MoE安全对齐策略提供了明确的切入点，但主要面向安全研究人员，普通开发者落地场景较窄。

### 社区活跃度 (评分: 8.5/10)
紧扣当前大模型领域的两大热点：MoE架构与安全对齐。随着MoE模型的广泛普及，其特有的安全漏洞与机制研究极具时效性和关注度。arXiv论文来源可信，对社区理解并防御MoE模型的安全风险有较好的启发意义和影响力。

## 项目链接
https://arxiv.org/abs/2606.04160
