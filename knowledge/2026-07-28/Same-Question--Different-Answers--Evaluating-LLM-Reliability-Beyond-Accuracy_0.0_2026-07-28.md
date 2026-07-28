# Same Question, Different Answers: Evaluating LLM Reliability Beyond Accuracy

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-28  
**来源：** rss  

## 项目描述
arXiv:2607.22554v1 Announce Type: new Abstract: Large language models (LLMs) often achieve strong accuracy on benchmarks, yet it remains unclear how reliably they apply this knowledge when the same question is phrased in different but equivalent ways. In this work, we study how model answers change under meaning-preserving paraphrases across factual question answering and mathematical reasoning tasks. Across four benchmarks and 13 models, we find that model outputs frequently depend on the exact wording of the prompt. While overall accuracy typically changes only modestly across paraphrases, instance-level behavior is far less stable: for many questions, models alternate between correct and incorrect answers depending on phrasing, with mismatch rates reaching more than 23%. Conditioning on questions that are answered correctly in their original form reveals even larger failures measured by answer flip rates, showing that single-prompt correctness is often a poor indicator of reliability. At the same time, we find that models often produce a correct answer for at least one paraphrase of a question, suggesting that the underlying knowledge is present but inconsistently retrieved. Building on this observation, we show that a simple self-paraphrasing strategy can partially recover this latent knowledge and improve performance at inference time. Together, these findings suggest that standard accuracy metrics can mask substantial instability, and that evaluating consistency across equivalent inputs provides a clearer picture of LLM reliability.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.22554
