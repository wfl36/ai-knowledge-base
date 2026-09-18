# Closed-World Resolution Against Tool Hallucination in LLM Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-18  
**来源：** rss  

## 项目描述
arXiv:2609.19425v1 Announce Type: new Abstract: Tool-augmented large language model (LLM) agents fail in a way no tool-selection or tool-security method addresses: they call tools that do not exist and pass arguments no schema declares. Existing defenses either pick the right tool (selection) or constrain what an agent may do with real tools (gating), both of which presuppose the emitted call refers to a real tool at all. We show this is a structural blind spot: a hallucinated call is by construction not a decision any gate made, so no gate can reject it. This paper is primarily a measurement and benchmark study. We give a five-class taxonomy of tool hallucination (H1-H5) and, as a reference point, the Resolution Rung: a training-free, closed-world resolver (registry membership plus a signature check) whose interest is where it must sit, not what it computes. We prove hallucination defense must precede any causal gate, and characterize the one irreducible residue (borrowed arguments schema-indistinguishable from a valid call). Across ten hosted models under two invocation surfaces we measure 322 genuine hallucinations; fabricated-tool calls concentrate on the unconstrained raw-JSON surface (34 vs. 3), and model scale does not help (a 675B model matches a 7-8B one). We then extend to the Model Context Protocol, where merging several servers into one namespace creates hallucination surfaces a single registry cannot express (a second taxonomy, M1-M5); on the live MCP surface we measure 154 hallucinations, including from frontier models that were clean on the single-registry surface, because collisions and shadowing are structural to the merge. We release the versioned Hallucinated-Tools Benchmark (HTB) so any resolver is comparable across submissions.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.19425
