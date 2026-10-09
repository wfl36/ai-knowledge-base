# Wieszcz-XIX: A 3.1-Billion-Word Corpus of Pre-1918 Polish and Temporally Bounded Language Models Trained From Scratch

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-09  
**来源：** rss  

## 项目描述
arXiv:2610.10592v1 Announce Type: new Abstract: Historical Polish is well documented as a language but annotated in machine-readable form only to about a million words for the period this paper covers; the rest sits behind optical character recognition of variable quality. We present Wieszcz-XIX, a corpus of 6.75 billion tokens (about 3.1 billion words) in 294,369 documents, most of them periodical issues, of Polish published from 1800 to 1918, assembled from Wolne Lektury and the Internet Archive by a pipeline that filters, deduplicates, audits for post-1918 leakage and splits at the document level. It is over three orders of magnitude larger than the annotated corpus of the same period, and we quantify its defects: recognition corruption against a false-positive floor, near-identical duplication, which is removed, and post-1918 leakage, which is excluded from the training corpus itself down to a known residue of 0.04 to 0.38% of its bytes, found in the transcribed source, so the published corpus is the trained one document for document. On a hand-corrected sample the character error rate is 0.68% where the text is legible, and 45% of the sampled passages cannot be corrected. On it we train a ladder of decoder-only models from 47M to 349M parameters from scratch, and measure their temporal boundedness. Against two modern Polish base models, one far larger, the 349M shows a crossover, as does the 107M against the comparator of its size: post-1918 vocabulary costs them about 3.1 bits per byte more than period vocabulary, a gap the comparators do not show, and period vocabulary costs them fewer bits than it costs the comparators. Shown period text, the models keep its spelling and the comparators only partly. Adding parameters gains about twice as much as a second pass over the data. We release the corpus, code and weights. Content warning: the models reproduce period prejudice, including antisemitic statements.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.10592
