# Validating the Comparison, Not Just the Scorer: Why Overall Accuracy Can Mislead in Interactive LLM Evaluation

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-26  
**来源：** rss  

## 项目描述
arXiv:2610.31678v1 Announce Type: new Abstract: Many LLM studies compare how models respond to different follow-up prompts. For example, one prompt may neutrally ask a model to reconsider, while another insists that an invented film really exists. The difference is used to measure the effect of conversational pressure. An automatic scorer then labels whether each response makes an unsupported factual claim. Researchers commonly validate the scorer with one overall accuracy or $F_1$ score. However, high overall performance can hide prompt-specific mistakes: if the scorer makes more errors after one prompt, the measured difference can be too large, too small, or point in the wrong direction. An audit containing mostly difficult responses can also misrepresent performance in the full study. We derive how such errors alter a prompt comparison and examine the problem using six models, 180 invented-entity questions, and six prompt conditions. In a balanced audit of 288 responses, overall $F_1$ was $.916$. Yet, depending on the prompt, the scorer flagged 2.6%-33.3% of responses that the primary LLM rater judged not to contain an unsupported claim; these prompt-specific estimates were uncertain. In a second audit, the scorer and two separate LLM raters evaluated the same 300 model-question cases under each prompt. An apparent 9.3-point increase from asserting certainty rather than neutrally asking the model to reconsider fell to 2.3 points under both raters. The primary-rater interval included zero, so it did not establish an increase. Two other prompt comparisons kept their direction under both raters, while an attempted prompt-specific correction remained too uncertain for a firm conclusion. Researchers should therefore validate the exact difference they plan to report, not just the scorer as a whole: audit both prompts on matching cases and include scorer and rater uncertainty in the final result.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.31678
