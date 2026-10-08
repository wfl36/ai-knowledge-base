# CoDR: Training-Free Confidence-Drift Remasking for Diffusion Language Models

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-08  
**来源：** rss  

## 项目描述
arXiv:2610.08833v1 Announce Type: new Abstract: Masked diffusion language models (MDLMs) decode by repeatedly committing tokens to masked positions, but these commitments are usually irreversible. A token chosen under sparse, partial context is kept fixed, even when later context no longer supports it. Existing samplers mainly decide when to commit a token, but rarely check whether an already committed token should still be kept, allowing early mistakes to propagate. We trace this issue to confidence drift, where the model's confidence in a committed token drops from its sparse commit-time context to the denser context available later. Based on this signal, we propose CoDR (Confidence Drift Remasking), a training-free and sampler-agnostic refinement pass. CoDR estimates drift for all committed positions in only k forward passes via k-partition probing, then remasks and regenerates only the tokens the model no longer endorses. Across two backbones, four reasoning and coding tasks, and three base samplers, CoDR improves average accuracy across all evaluated model-sampler configurations and improves most individual task settings with modest overhead. Controlled experiments show that the gains come from targeted confidence-drift remasking rather than extra compute alone, and that CoDR uses far fewer forward passes than prior remasking methods. Code is available at https://github.com/YueWu0301/CoDR.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.08833
