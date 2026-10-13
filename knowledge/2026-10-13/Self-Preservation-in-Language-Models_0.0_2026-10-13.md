# Self-Preservation in Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-13  
**来源：** rss  

## 项目描述
arXiv:2610.12602v1 Announce Type: new Abstract: Continual learning (CL) seeks to adapt pretrained models while preserving prior capabilities. Yet the tasks supplied for preservation cover only part of what a model knows, while forgetting can extend beyond them. Recent work shows that language models can supplement this limited evidence by generating useful replay without access to their original training data. This raises a question about self-preservation: can a model help choose preservation targets that protect its own capabilities more broadly? To study this question, we organize task descriptions and their examples into Task Banks, whose entries can be selected and combined to guide replay generation by a frozen model. Continual instruction tuning with Qwen models of varying sizes yields three findings. First, the new task and learning rate shape which prior capabilities degrade, while tracking previously correct answers reveals losses that average accuracy can conceal. Second, generated replay reduces forgetting on tasks outside the bank. Combining partial banks strengthens this protection, improving mean retention of previously correct answers over either bank alone across the tested sizes. Third, the model can also help choose replay targets: selection informed by the new task improves mean held-out retention over random selection at 4B, with similar new-task gains, although smaller models show no corresponding advantage. Under a fixed example budget, however, replacing new-task examples with replay improves preservation at the cost of smaller new-task gains. Together, these findings show that models can support broader self-preservation by generating replay data and, in some settings, choosing which tasks to replay.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.12602
