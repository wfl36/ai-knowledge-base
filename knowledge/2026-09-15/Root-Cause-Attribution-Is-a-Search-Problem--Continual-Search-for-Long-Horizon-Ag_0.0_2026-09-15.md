# Root-Cause Attribution Is a Search Problem: Continual Search for Long-Horizon Agent Failures

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-15  
**来源：** rss  

## 项目描述
arXiv:2609.13463v1 Announce Type: new Abstract: The increasing deployment of AI agents in long-horizon tasks yields massive execution logs. Diagnosing failures within these records is crucial for reliability, as it transforms outcome-level signals into actionable interventions. The sheer scale of the data renders human review impractical, driving the need for automated root-cause attribution (RCA). However, automated RCA methods using LLMs suffer from low diagnostic accuracy, especially as execution traces grow larger. They struggle because relevant information is often sparse, distributed across distant actions, and disconnected from the visible failure, reducing root-cause attribution to a massive search problem. Existing RCA methods typically rely on one-shot LLM judgments to diagnose failures from execution traces. While effective for shorter trajectories, these judges tend to settle on a plausible diagnosis early, leaving critical evidence in longer traces unexamined. We introduce Continual Search, an iterative framework that nudges the judge, over successive turns, to keep searching for unresolved diagnostic evidence. We evaluate Continual Search across four existing RCA benchmarks. Recognizing the lack of massive execution traces in current benchmarks, we introduce MegaRCA-Mix to evaluate RCA at scale. MegaRCA-Mix provides a challenging testbed of 50 human-annotated failure trials spanning long-horizon, execution-heavy tasks. Across multiple benchmark suites and model families, Continual Search consistently improves attribution performance. On MegaRCA-Mix, for example, it improves GPT-5.5's F1 score by more than 40\%, from $0.349$ to $0.498$. More interestingly, within the same model family, lower-tier models can even surpass their higher-tier counterparts, demonstrating that effective search supersedes raw model scale.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.13463
