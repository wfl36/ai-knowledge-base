# A decodability criterion predicts when hidden-state selection beats majority voting in large language models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-19  
**来源：** rss  

## 项目描述
arXiv:2608.17124v1 Announce Type: new Abstract: Combining the answers a large language model (LLM) samples for a question into one decision is a test-time information fusion problem, usually solved by majority voting. Voting is unreliable on difficult questions, where the sampled answers share correlated errors, so the wrong answer can win and drawing more samples makes the decision worse. Selecting a candidate by reading a correctness signal from the model's hidden states is a promising alternative, but its accuracy varies across models and tasks, and no measure indicates when it can be trusted. In this paper, we propose CASE (Correctness-Axis SElection), a dynamic selection combiner that trains a linear gate on the answer-token hidden state and selects the highest-scoring candidate. Its main contribution is decodability, a leakage-free measure of how well the gate ranks a question's correct candidates above its incorrect ones, which predicts whether hidden-state selection will outperform voting. A conventional probe appears accurate only because of question-identity leakage, which vanishes under question-grouped evaluation. On held-out data, decodability predicts the accuracy gain of selection over voting with a Pearson correlation r=0.75 and a decision threshold near AUC=0.60. Across general and medical LLMs, CASE improves over voting by up to 19 points on medium-difficulty questions and 16.8 points on hard questions. Decodability depends on the aligned knowledge a model must recall, not on its scale, and its prediction transfers to an unseen scientific domain within 3.8 points. It thus provides a practical criterion, measurable in advance for a given model and task, for choosing between learned selection and majority voting.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.17124
