# TOUMAII: A 4.5M-Pair Tool-Calling Preference Dataset and Its Source-Agnostic Generator

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-24  
**来源：** rss  

## 项目描述
arXiv:2611.26722v1 Announce Type: new Abstract: To autonomously execute multi-step tasks, enterprise agents must reliably interact with tools, call APIs, or query databases, making tool-calling a fundamental capability of AI models. Supervised fine-tuning (SFT) optimises for producing the correct call, but never contrasts it with a plausible incorrect one. In an environment where even a minor formatting error can invalidate a call and an incorrect decision can derail the interaction, direct preference optimisation (DPO) targets exactly this contrast. DPO, therefore, requires preference pairs rather than plain demonstrations. For tool-calling, such data, especially in realistic multi-turn settings, remains extremely scarce. To address this scarcity, we introduce TOUMAII, a large-scale tool-calling preference dataset containing ~4.5M validated preference pairs, derived from Agent-Ark/Toucan-1.5M (apache-2.0) conversations. The dataset consists of multi- and single-turn interactions and includes parallel and sequential function calls. Additionally, we release TOUMAII-Gen, a synthetic data generation pipeline that consumes tool-calling SFT datasets and generates a preference dataset with naturally occurring model-generated tool-calling failure modes. To validate the effectiveness of our DPO data, we fine-tune a 3-billion-parameter model, achieving performance parity with other high-quality tool-calling preference datasets. Furthermore, we release a second small preference dataset derived from ToolACE (apache-2.0), showcasing the source-agnostic nature of our pipeline. We release the complete code and datasets: https://github.com/tum-ai/toumaii-gen and https://huggingface.co/collections/tum-ai/toumaii-generated-datasets

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.26722
