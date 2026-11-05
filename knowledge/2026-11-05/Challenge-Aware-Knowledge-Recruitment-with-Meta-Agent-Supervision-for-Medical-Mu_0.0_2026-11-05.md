# Challenge-Aware Knowledge Recruitment with Meta-Agent Supervision for Medical Multi-Agent Reasoning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-05  
**来源：** rss  

## 项目描述
arXiv:2611.05393v1 Announce Type: new Abstract: Large language models perform strongly on standard medical QA but degrade on harder reasoning tasks, where multi-agent debate often fails to beat strong single-model prompting. We argue that a key limitation is that existing systems select experts and retrieve knowledge from the question alone, rather than from gaps that emerge during reasoning. We propose challenge-aware adaptive recruitment: an external CHALLENGER inspects the evolving reasoning trace and identifies specific factual or expertise gaps. These signals trigger targeted knowledge retrieval or mid-discussion specialist recruitment. On the MEDAGENTSBENCH hard subset (862 questions across nine biomedical datasets), upfront retrieval provides little benefit, while challenge-aware in-between retrieval performs better; on a multi-specialist backbone it improves accuracy on 8 of 9 datasets and adds 6 percentage points over Challenger Only. Ablations indicate benefits from both retrieval timing and gap-specific query signals, and a live web-search experiment shows that the timing advantage persists across retrieval backends. For specialist recruitment, self-triggered adaptation is unreliable, whereas Challenger-triggered recruitment raises GPT-4.1-mini MedQA accuracy from 46% to 54%, with positive direction on all tested generalization datasets. Naively combining retrieval and specialist recruitment degrades performance, highlighting the need to coordinate adaptive intervention channels. These results show that when and why external resources are recruited is a key design choice in multi-agent medical reasoning.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.05393
