# RepSelect: Robust LLM Unlearning via Representation Selectivity

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 机器遗忘, 模型安全, 对齐, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17168v1 Announce Type: new Abstract: Making large language models (LLMs) deeply forget specific knowledge and values without sacrificing general capabilities remains a central challenge in unlearning. However, current methods are easily reversed by fine-tuning or few-shot prompting, suggesting their forgetting is only shallow. We identify the root cause. Existing methods target representations shared with both the retain set and the subspace recovered by a fine-tuning attacker, making unlearning both disruptive to general capabilities and easy to reverse. We propose RepSelect (Representation Selectivity), isolates forget-set-specific representations by collapsing top principal components of weight gradients before each update, leaving general capabilities intact while limiting what fine-tuning can recover. We evaluate across two forget categories, biohazardous knowledge and abusive tendencies, and four model families spanning dense and Mixture-of-Experts architectures (Llama 3, Qwen 3.5, Gemma 4 E4B, DeepSeek V2 Lite). Compared to five popular baselines (GradDiff, NPO, SimNPO, RMU, UNDIAL), RepSelect achieves a 4-50x larger reduction in post-relearning answer accuracy than the strongest baseline, and is near-perfectly robust to few-shot prompting attacks. Targeting selective representations is thus an important step towards deep and robust LLM forgetting.

## 综合总结
本文针对大模型遗忘易被微调和少样本提示逆转的“浅层遗忘”问题，指出其根源在于现有方法针对的表征与保留集共享。为此提出RepSelect方法，通过折叠权重梯度的顶部主成分来隔离遗忘集特有的表征，从而在保持通用能力的同时限制微调恢复。实验表明，RepSelect在多个主流模型架构上，抗重学能力比最强基线提升4-50倍，且对少样本攻击近乎免疫，是实现深度鲁棒LLM遗忘的重要突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文深刻揭示了当前LLM遗忘方法易被微调或少样本提示逆转的根源：现有方法针对的表征与保留集及微调恢复子空间存在重叠。基于此洞见，提出RepSelect方法，通过在每次更新前折叠权重梯度的顶部主成分，精准隔离遗忘集特有的表征。该方法理论分析深入，且在4个主流模型家族（含Dense和MoE架构）和5个强基线上的实验论证严谨，抗重学能力提升显著（4-50倍），技术深度与新颖性极高。

### 实用性 (评分: 8.0/10)
LLM遗忘在隐私保护、版权合规和安全对齐等工业场景中需求迫切。RepSelect解决了实际部署中模型易被恶意微调或提示词攻击恢复有害知识的痛点，对从业者构建安全鲁棒的模型具有极高的参考和指导价值。不过，梯度主成分折叠操作在实际大规模模型训练中的计算开销与工程适配性仍需进一步验证，整体可落地性强。

### 社区活跃度 (评分: 8.5/10)
机器遗忘是当前大模型安全与对齐领域的热点话题。该论文发布于arXiv（标注为2026年新文），探讨了前沿模型（如Llama 3, Qwen 3.5, Gemma 4, DeepSeek V2 Lite），时效性极强。作者来自学术机构，实验规模大且对比充分，具备较高的权威性与潜在影响力，但作为预印本尚未经过正式同行评审，可信度留有少许余地。

## 项目链接
https://arxiv.org/abs/2606.17168
