# Can Spectral-Clipping Enable Better Learning While Forgetting Less for Low-Rank Adaptation?

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-14  
**来源：** rss  

## 项目描述
arXiv:2608.12332v1 Announce Type: new Abstract: In recent years, low-rank adaptation (LoRA) has emerged as a significant paradigm that freezes pre-trained weights and introduces small, learnable adapters instead of fine-tuning the full set of parameters. In this work, we uncover several key insights regarding the singular components of network parameters based on Singular Value Decomposition (SVD). Firstly, the principal singular components with large singular values in pre-trained network parameters can be effectively reused during fine-tuning, whereas the minor components with smaller singular values are more task-specific and require substantial adaptation. Secondly, we first establish the theoretical connection that the uncontrolled growth of singular values in LoRA adapters leads to the forgetting of pre-trained knowledge -- a well-known issue referred to as catastrophic forgetting. Building on these observations, we propose SCLoRA, which injects parameterized singular components with spectral clipping into the pre-trained model in a way that is aware of the spectral distribution of the pre-trained model. SCLoRA effectively adapts to new tasks by focusing updates on components that require adaptation, while simultaneously alleviating catastrophic forgetting. We conduct extensive experiments and demonstrate that SCLoRA not only improves downstream performance but also effectively retains pre-trained knowledge.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.12332
