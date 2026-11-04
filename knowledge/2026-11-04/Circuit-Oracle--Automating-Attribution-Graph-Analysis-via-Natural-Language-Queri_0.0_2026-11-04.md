# Circuit Oracle: Automating Attribution Graph Analysis via Natural-Language Queries

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-04  
**来源：** rss  

## 项目描述
arXiv:2611.00420v1 Announce Type: new Abstract: Attribution graphs, an emerging tool in mechanistic interpretability, use transcoders to decompose language model computations into sparse interpretable features connected by causal edges. However, turning a graph into a safety-relevant insight requires hours of manual analysis by experts. We introduce Circuit Oracle, an off-the-shelf LLM equipped with a multi-agent harness and task-specific authored skills, which answers natural-language questions about a target model by reading the attribution graph through tool calls. We evaluate it on three safety-relevant proxy tasks: detecting spurious features in probe circuits, eliciting hidden knowledge from taboo-finetuned models, and suppression jailbreaking via feature-level interventions. Beyond task scores, the oracle produces pruned subgraphs and context-specific feature explanations that we assess qualitatively. Results are mixed. On spurious-feature detection, Circuit Oracle reaches 78.2 $\pm$ 2.4% accuracy, outperforming single-layer feature-ranking baselines. On secret elicitation, trained self-explainers like Activation Oracles remain the stronger baseline. On refusal suppression over 50 prompts, its single committed intervention is slightly below a diff-in-means baseline, and only exceeds it when allowed the best of five attempts. Results are stable across five runs and across model choices for the agents. We also release the pruned subgraphs and context-specific feature readings that revise existing global labels, and invite future work to develop evaluations that can measure their usefulness directly.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.00420
