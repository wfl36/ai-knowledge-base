# Heavy-Tailed Memory Traces in Long-Horizon Language Agents

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-02  
**来源：** rss  

## 项目描述
arXiv:2610.00010v1 Announce Type: new Abstract: Long-horizon language agents increasingly rely on external memory as a frozen world model, yet current memory systems are usually judged only by task success or token cost. We argue that the missing object is the shape of memory use: under finite context and repeated retrieval, agent memory can concentrate on a small core while leaving rare states in a long tail where prediction errors accumulate. We study this effect through a conservative tail audit and find that concentration is reproducible but policy-dependent. Random-walk agents produce log-normal-compatible retrieval artifacts, whereas semantic LLM policies yield the strongest truncated-power-law-compatible core--tail traces. Motivated by this audit, we propose Core--Tail World Model (CTWM), a rank-based memory controller that allocates prompt budget with a single exponent $\tau$ while retaining a summarized tail. On Synthetic Graph World, CTWM preserves full state and transition coverage, reduces prompt tokens by 5.9%, and lowers bottom-half tail prediction error by 13.6% relative to a graph-memory baseline. The same paired comparison gives consistent token savings on ALFWorld and a 24.48% token reduction on LongMemEval with aggregate accuracy parity. These results suggest that heavy-tailed memory traces are not only a diagnostic of finite retrieval, but also a practical control signal for token-efficient agent world models.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.00010
