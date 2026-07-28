# CHiPS: Character Histograms and Positional Signals for Lightweight Authorship Attribution in Romanian Texts

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-28  
**来源：** rss  

## 项目描述
arXiv:2607.22884v1 Announce Type: new Abstract: We propose CHiPS, a lightweight character-level authorship attribution method for Romanian texts. All reported experiments are closed-set: the true author is one of the candidate authors in the training data. CHiPS studies two complementary fingerprints of writing style: CH-SVM, a character-histogram classifier based on one-character marginal distributions, and FFT12-LR, a positional-signal classifier that represents selected characters and punctuation classes as impulse trains (binary indicator sequences over character positions) and extracts Fourier/Welch spectral descriptors. We also report CHiPS-F, a leakage-safe decision-level fusion variant, and an optional top-5 listwise reranker trained only on out-of-fold predictions. The method requires no tokenization, syntactic analysis, pretrained language model, or transformer fine-tuning, and it avoids character $n$-gram features with $n \geq 2$ in the histogram component. On a locked grouped ROST split comprising 400 files from 392 source-text groups, written by 10 authors, with source-text-level evaluation and grouped five-fold model selection, CHiPS-F reaches 0.9310 accuracy and 0.9341 macro-F1. A matched but unrestricted character 2--5-gram TF--IDF SVM comparator reaches 1.0000 accuracy and macro-F1 on the same held-out groups, so the contribution is not a claim of best possible classification accuracy. Instead, the experiments ask how far restricted, transparent character evidence can go under strict leakage control. On ROSTories-cleaned, a secondary ROST-overlapping corpus comprising 1,248 files from 1,240 source-text groups, written by 19 authors, the same protocol gives 0.8919 accuracy and 0.8708 macro-F1 for CHiPS-R.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.22884
