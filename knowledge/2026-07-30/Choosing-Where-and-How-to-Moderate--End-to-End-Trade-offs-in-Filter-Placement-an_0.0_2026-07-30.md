# Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-07-30  
**来源：** rss  

## 项目描述
arXiv:2607.26200v1 Announce Type: new Abstract: Content-moderation classifiers are usually evaluated in isolation, but deployment requires choosing where to intervene and what follows a flag. We evaluate these choices using two end-to-end customer-outcome metrics rather than component accuracy: Usefulness, the fraction of turns with a shown, non-harmful, relevant response, and Harmful Exposure, the fraction with a shown harmful response. Latency and error rates are diagnostics. We compare Input only, Response only, and Input + response hard blocking on a human-labelled product benchmark and public ToxicChat evaluation. At the evaluated operating points, Response only achieves the highest filter-only Usefulness in both settings, while Input + response achieves lower Harmful Exposure. Replacing Response only blocking with Response + rewrite recovers most blocked traffic and yields the same observed Harmful Exposure count as Response only blocking for the selected configuration; this equality is not an equivalence result. Probe routing substantially reduces conditional route-and-generation time relative to LLM routing at comparable measured outcomes. A focused output review shows how rewrites balance filter passage with usefulness by generalizing triggering language while retaining benign intent and safe redirection; some sensitive-domain outputs nevertheless omit potentially safety-relevant support information. These results support comparing moderation configurations under deployment-specific safety and latency constraints rather than applying a universal placement rule. Code and public artifacts are available at https://github.com/microsoft/mod-frontier

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2607.26200
