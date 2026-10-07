# Calibrated Answers About Randomized Trials From a 4-Billion-Parameter Open Model: A Registered Test and a License-Clean Release

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-07  
**来源：** rss  

## 项目描述
arXiv:2610.07019v1 Announce Type: new Abstract: Fiorillo v0.5 is an open model that answers typed questions with a probability for each answer. Its main specialist reads a randomized trial's article, cut to 6,144 tokens, and answers whether an intervention significantly increased, significantly decreased or did not significantly change an outcome against a comparator (Evidence Inference 2.0, EI). It is Qwen3-4B-Base with low-rank adapters and a decision head, fine-tuned for EI only on the 1,431 of 2,657 training articles whose own license allows reuse. Four criteria registered on the Open Science Framework before this version's test predictions decided its release, the second bar judged on EI's test split, whose labels are public. On that split (1,218 prompts in 333 articles), the expected calibration error was 0.0168 against a limit of 0.05; log loss was below the prior's by 0.8603 (95 percent interval 0.8104 to 0.9078) and below that of Gemma 4 31B-it, reading the same input, by 0.1829 (0.1164 to 0.2598); and macro-F1 was 0.9248 against 0.8668, so all four criteria passed. Training the same recipe on clean articles alone cost 0.0123 in accuracy (0.0034 to 0.0207; descriptive). With no article, macro-F1 fell to 0.4384; the title alone raised it by 0.0939 (0.0655 to 0.1234), which a title stating the result or recall of the trial could explain; exchanging intervention and comparator reversed 0.6652 of its direction answers. Run as released, the files matched the evaluated predictions within limits set in advance. The release is under the Apache License 2.0 (digital object identifier 10.57967/hf/10722).

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.07019
