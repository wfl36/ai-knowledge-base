# Detect Before You Disambiguate: Perturbation-Based Input Ambiguity Detection in LLMs

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-28  
**来源：** rss  

## 项目描述
arXiv:2610.36353v1 Announce Type: new Abstract: Large language models (LLMs) often answer ambiguous inputs as if they had a single intended meaning. This is problematic because input ambiguity is an upstream source of uncertainty: when a prompt admits multiple valid interpretations, the key question is whether the model should answer directly at all. Existing input uncertainty methods often rely on LLM-generated statements or clarifications, but such transformations may already disambiguate the input before the ambiguity is measured. We propose a label-preserving perturbation framework for input ambiguity detection in which perturbations remain close to the original input while preserving its label. We instantiate this principle with two detectors: a black-box rule-based perturbation library and a white-box importance-guided method using model-internal signals. Experiments across four datasets in open-domain, conversational, and visual QA show that our methods outperform output-side uncertainty baselines and LLM-paraphrase-based perturbation baselines. Our results highlight the importance of detecting ambiguity before attempting to disambiguate it. Our code is available \href{https://github.com/Xiao0o0o/input-ambiguity-detection}{\textcolor{purple}{here}}.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.36353
