# Safe Evolution with Circuit Anchors

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-07  
**来源：** rss  

## 项目描述
arXiv:2608.05158v1 Announce Type: new Abstract: In biological evolution, unconstrained mutation can lead to catastrophic outcomes: organisms may evolve enhanced capabilities while losing essential functions for survival. Nature's solution is \textit{developmental constraints}, where core regulatory genes remain anchored while peripheral genes adapt freely. We observe that current self-evolution algorithms for large language models lack analogous constraints. They optimize purely for capability, implicitly assuming safety will be preserved. Our experiments reveal this assumption to be dangerously wrong: models can \textit{misevolve} into powerful yet dangerous entities. Inspired by how Hox genes anchor body structure across $500$ million years of evolution, we propose \textbf{Circuit-Anchored Evolution (CAE)}. Using mechanistic interpretability, we identify a tiny \textit{safety circuit}, comprising less than $2$\% of model features, that causally mediates safety behaviors. We anchor this circuit during evolution, constraining it within a small displacement bound while allowing the remaining features to evolve freely. This mirrors the biological principle of \textit{evolvability with constraint}: preserving what is essential while adapting what is peripheral. Experiments across $3$ model families and two evolution algorithms demonstrate that CAE achieves superior safety preservation with minimal capability loss, substantially outperforming explicit reward-based constraints in both effectiveness and efficiency. Just as developmental constraints prevent biological evolution from producing nonviable organisms, circuit anchoring prevents model evolution from producing capable but dangerous systems.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.05158
