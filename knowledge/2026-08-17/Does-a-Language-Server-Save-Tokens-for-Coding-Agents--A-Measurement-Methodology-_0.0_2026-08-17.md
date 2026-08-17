# Does a Language Server Save Tokens for Coding Agents? A Measurement Methodology and Preliminary Study

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-17  
**来源：** rss  

## 项目描述
arXiv:2608.13568v1 Announce Type: new Abstract: Coding agents spend most of their context budget on retrieval. Lexical retrieval (grep) is universal, instant, and zero-setup, but noisy: it cannot tell a definition from a call from a comment. Semantic retrieval via the Language Server Protocol (LSP) is precise and typed, but needs a running, indexed server and pays a per-symbol round-trip. The claim that semantic retrieval is more token-efficient is, we find, asserted almost everywhere and measured almost nowhere: no public source isolates the LSP-vs-lexical token delta for an agent at equal task-success. This paper formalizes the question with one metric (tokens-to-success), specifies a five-arm ablation isolating semantic retrieval from confounds, maps three pre-stated failure modes onto measurable variables, and reports a preliminary study (Python and TypeScript repos; Claude Opus 4.8, Sonnet 4.6, Haiku 4.5). The answer is conditional and usually negative. On symbol-named localization the LSP costs tokens (+6% to +118%) and the agent ignores it when free. On reference-completeness it buys precision but not token savings and cannot raise the recall ceiling set by agent thoroughness; it saves tokens only for the weakest model. Tool choice is task-dependent: models default to grep on localization (0-6% semantic use) but reach for the LSP about half the time on reference tasks, unprompted. On edits scored by real test execution the gap is starkest: grep solves multi-file renames perfectly, a location-only LSP fails three-quarters of them by missing a call site, and even a complete, index-warmed, text-enriched LSP (each reference's line inline, as production LSP-MCP servers do) recovers most of the gap but cannot close it, since a rename must touch comments and strings that semantic references exclude. The implication is not LSP-always but an adaptive router keyed on task class, model capability, and lexical noise.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.13568
