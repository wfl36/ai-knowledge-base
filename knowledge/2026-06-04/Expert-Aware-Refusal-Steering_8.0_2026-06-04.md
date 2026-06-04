# Expert-Aware Refusal Steering

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 安全对齐, MoE, 推理干预, 论文  
**更新日期：** 2026-06-04  
**来源：** rss  

## 项目描述
arXiv:2606.04160v1 Announce Type: new Abstract: Safety alignment in instruction-tuned large language models (LLMs) depends on a model's ability to reliably refuse to respond to harmful or disallowed requests. Recent work has shown that a steering vector can be applied to a dense LLM during inference to effectively suppress refusal behavior, inducing response to harmful requests. We extend this refusal steering method to three open-source Mixture-of-Experts (MoE) LLMs and find that steering performance is uninhibited by the complex routing patterns inherent to the MoE architecture. We then propose two expert-aware refusal steering methods that leverage refusal-specific expert routing patterns and expert-specific steering directions to suppress normal refusal behavior. We find that refusal behavior can be effectively steered based on the output of a single expert. Our results show that refusal signals captured by steering methods differ from expert routing behavior, suggesting a substantial role for attention in MoE refusal behavior.

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文将拒绝行为转向研究从密集型 LLM 扩展至 MoE 架构，创新性地提出了两种专家感知转向方法。研究发现 MoE 的复杂路由并未阻碍转向效果，且仅需单个专家输出即可有效控制拒绝行为。更重要的是，论文揭示了转向方法捕获的拒绝信号与专家路由行为存在差异，指出注意力机制在 MoE 拒绝行为中扮演关键角色，具有深刻的技术洞见。

### 实用性 (评分: 7.5/10)
研究结果对大模型安全防护和红蓝对抗具有直接指导意义。揭示了 MoE 模型在安全对齐上的脆弱性（单专家即可被操纵绕过安全限制），为后续设计更鲁棒的 MoE 安全对齐机制和防御策略提供了明确的方向，但工程化应用需进一步开发。

### 社区活跃度 (评分: 8.0/10)
随着 MoE 架构在主流开源大模型中的广泛应用，其安全性成为社区关注焦点。该论文紧贴 MoE 安全对齐的前沿痛点，来源为 arXiv 学术预印本，对 AI 安全研究社区具有较高的时效性和参考价值。

## 项目链接
https://arxiv.org/abs/2606.04160
