# Self-Supervised Keyframe Discovery for Horizon-Invariant Behavior Cloning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-09  
**来源：** rss  

## 项目描述
arXiv:2610.10857v1 Announce Type: new Abstract: Behavior cloning (BC) in non-Markovian environments is a challenging problem because policies have to reason over contextual information over long horizons. Existing policy architectures rely on recurrent or attention-based mechanisms to capture long-term dependencies. However, recurrent models suffer from hidden-state collapse and gradient instability under backpropagation through time, while attention-based models are fundamentally limited by context length. To address these issues, we propose Keyframe Mnemonics, a novel self-supervised method that $\textit{discovers}$ a set of information-critical observations ($\textit{mnemonics}$) by learning an objective from randomly sampled past observations and using it as a reward for keyframe selection. We then train a BC policy that conditions on the discovered keyframes to model the action distribution. Under certain task-structure assumptions, our formulation provides context retention guarantees over an infinite horizon, while maintaining a small set of decision-relevant keyframes in the policy's working memory. We evaluate our method on synthetic memory domains, where mnemonic-conditioned BC policies achieve $100$% success rates (SR) and generalize to horizons orders of magnitude beyond training without performance degradation. Additionally, we evaluate on memory-intensive robot manipulation benchmark, achieving a $13.9$% average absolute SR improvement over the strongest baseline across $23$ tasks and retaining $80$% SR at $20\times$ longer horizons on a real robot. Code and videos are available at https://keyframe-mnemonics.github.io.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.10857
