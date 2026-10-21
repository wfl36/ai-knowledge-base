# Mixture of Phonetic Experts Based Low-Rank Adaptation of Conformer Models for Accented English Speech Recognition

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-21  
**来源：** rss  

## 项目描述
arXiv:2610.26888v1 Announce Type: new Abstract: We present Mixture of Phonetic Experts based Low-Rank Adaptation (MoPE-LoRA), a parameter-efficient adaptation framework for accented English speech recognition. Recent mixture-of-experts approaches typically allocate experts per accent, implicitly treating accent identity as the primary axis of variation. In contrast, we organize adaptation along phonetic categories, motivated by the observation that accent differences are often expressed as systematic distortions of phoneme realization. MoPE-LoRA introduces a fixed set of six low-rank experts aligned with manner-of-articulation classes and performs frame-level routing through a hybrid mechanism that combines phoneme supervision with learned acoustic gating. Because the expert set is shared across accents, the model does not require accent-specific modules and naturally extends to previously unseen accents. Experiments on L2-ARCTIC show that MoPE-LoRA consistently improves over single LoRA and full fine-tuning. In zero-shot evaluation where one accent is held out during training, the proposed method yields a 12.3% relative improvement over single LoRA. These results indicate that phonetic-category-based decomposition offers a scalable and transferable alternative to accent-level adaptation.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.26888
