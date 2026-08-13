# Backtrader-Bench: Benchmarking LLM Agents on Algorithmic Trading with Self-Generated MCQs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-13  
**来源：** rss  

## 项目描述
arXiv:2608.11232v1 Announce Type: new Abstract: Evaluating LLM coding agents in algorithmic trading is difficult because static benchmarks risk data contamination and numerical backtest outputs require ground truth from actual code execution. We present Backtrader-Bench, a framework with two complementary pipelines. A deterministic multiple-choice question (MCQ) pipeline generates questions from backtest configurations across five trading strategies, 33 templates, and three difficulty tiers, with an independent checker that re-derives every answer. A generator-solver filtering pipeline autonomously mines harder questions: a generator writes questions verified by executable code, converts them to MCQs, and discards any that a no-tool solver can answer without code execution. We evaluate 11 models without tools (10 runs each) and four with-tools configurations on a 30-question curated set. Tool-augmented agents reach 90.0% accuracy in a single pass (GPT-5.5 and Opus 4.7), outperforming the best no-tools baselines (73.0%, averaged over 10 runs) by 17 percentage points. On 38 separately mined questions, no-tools accuracy drops further, with half the models falling to roughly random-chance level (25%). Beyond evaluation, the scalable MCQ infrastructure is designed to produce a training corpus for reinforcement learning, with the ultimate goal of building a specialized agent for quantitative trading workflows.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.11232
