# How Language Models Fail: Token-Level Signatures of Committed and Persistent Reasoning Failures

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 推理, 不确定性, 可解释性, 论文  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.06635v1 Announce Type: new Abstract: Failures in language model reasoning emerge through distinct processes that leave identifiable signatures in the reasoning trace. We characterize these failures using token-level uncertainty signals, finding they arise through two empirically distinguishable processes. The first is committed failure, in which a model locks onto an incorrect reasoning path early in its trace. A central diagnostic signature is the commitment point, beyond which considering additional tokens hurt rather than help failure detection. In the second, persistent uncertainty, uncertainty instead accumulates throughout, and the full trace is needed to best distinguish failing from successful completions. These signatures reproduce across 23 model-dataset configurations, with the framework's falsifiable predictions holding in 20 of 23 cases, well above chance across both failure modes. Finally, we demonstrate our failure mode framework has direct implications for self-consistency, identifying when uncertainty signals complement it and when it can be selectively skipped. These results offer a foundation for understanding when LLM reasoning failures become detectable and for adapting detection strategies accordingly.

## 综合总结
该论文揭示了语言模型推理失败的两种token级机制：过早锁定错误路径的'执迷型失败'和不确定性持续累积的'持续不确定型'。研究通过23个模型-数据集配置验证了这些特征及'承诺点'的存在，其可证伪预测在绝大多数情况下成立。此外，该框架为优化自一致性策略提供了理论依据，指明了不确定性信号与投票机制的互补关系，为理解和检测LLM推理失败奠定了重要基础。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文在LLM推理失败的研究上展现了极高的洞见与深度，创新性地从token级别的不确定性信号出发，将推理失败解构为两种截然不同的机制：过早锁定错误路径的'执迷型失败'（Committed failure）和不确定性持续累积的'持续不确定型'（Persistent uncertainty）。提出了'承诺点'（Commitment point）这一核心诊断特征，并在23个模型-数据集配置中通过可证伪预测进行了严谨的实证验证（20/23成立），论证极其扎实。

### 实用性 (评分: 8.0/10)
尽管具有较强理论色彩，但该框架对工程实践有直接的指导意义。基于'承诺点'的发现，开发者可以设计更高效的早停机制或动态推理策略，避免在模型已锁定错误路径时浪费算力；同时，框架明确指出了不确定性信号何时能补充自一致性（Self-consistency）投票、何时可以选择性跳过，为降低推理成本和提升输出可靠性提供了可落地的策略。

### 社区活跃度 (评分: 8.5/10)
随着大模型推理能力（如o1等模型）的爆发，如何检测和理解其推理失败成为社区的核心痛点。该论文由斯坦福知名学者Mykel J. Kochenderfer等参与，发表时间新颖，直击当前LLM可信AI与可解释性研究的前沿，其提出的可证伪预测与跨配置泛化性极具说服力，有望在LLM可靠性评估与对齐领域产生广泛影响。

## 项目链接
https://arxiv.org/abs/2606.06635
