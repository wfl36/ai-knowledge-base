# Cross-Modal Latent Influence: Patch-Level Training Sample Attribution for Vision-Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-15  
**来源：** rss  

## 项目描述
arXiv:2610.14190v1 Announce Type: new Abstract: Explaining a vision--language model (VLM) prediction requires tracing training-example influence to the multimodal evidence that mediates it, yet existing attribution methods largely operate only at the sample level. Recent latent-mediated influence methods provide feature-level attribution in language models, but lack the multimodal and spatial structure needed to ground influence in VLMs. We introduce MOSAIC (Multimodal Orthogonalized Sparse Autoencoders for Influence Characterization). It learns a shared sparse image--text latent space whose concepts are 1) sparse within each modality, 2) supported on contiguous image regions, 3) aligned to the phrases that describe them, and 4) approximately decorrelated. It then applies EK-FAC to decompose training-example influence through these concepts and localize their contributions to specific text phrases and image regions. We evaluate MOSAIC on Qwen and Gemma across captioning, chest X-ray understanding, and visual question answering. The learned features are more localized and coherent without degrading task behavior, and ablating influence-ranked latents changes model outputs more than ablating latents ranked by activation or frequency. We find that visual evidence can substantially reorganize training-data attribution while preserving more of the shared latent structure. MOSAIC thus connects where model behavior comes from with what multimodal evidence carries that influence.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.14190
