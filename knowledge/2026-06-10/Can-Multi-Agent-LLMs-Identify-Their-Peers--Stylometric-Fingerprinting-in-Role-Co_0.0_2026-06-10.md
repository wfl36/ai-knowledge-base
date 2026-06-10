# Can Multi-Agent LLMs Identify Their Peers? Stylometric Fingerprinting in Role-Constrained Political Analysis

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.09854v1 Announce Type: new Abstract: Multi-agent large language model (LLM) pipelines for political statement analysis are vulnerable to peer-preservation bias: models tend to protect peer models from deactivation and show identity-dependent scoring distortions. Prompt-level anonymization was proposed as a mitigation, but prior work simultaneously documented that stylometric fingerprints survive anonymization in role-constrained outputs - raising the question of whether this mitigation is sufficient. This paper provides the first systematic investigation of whether LLMs can identify the model family behind political analysis texts under anonymization conditions. We evaluate three classifier approaches - LLM zero-shot and few-shot (Claude Sonnet 4.6 and Llama-3.3-70B) and a fine-tuned T5-base model - on a five-class attribution task covering four commercial LLM families and an open-world 'unknown' class. We introduce a statement-disjoint cross-validation protocol (SD-CV; defined in Section 3.5) that guarantees no content overlap between training and validation data, and contrast it with a run-disjoint baseline (RD-CV). T5 achieves Macro F1 = 0.991 (+-0.008) under SD-CV and F1 = 0.978 on 24 completely held-out statements - robust despite a 2.1x increase in train-test content distance versus RD-CV (0.767 vs. 0.366, p<0.001), demonstrating genuine stylometric generalization. A fractional SD-CV analysis identifies a performance knee at 40% of training data (~440 texts). Our findings confirm that prompt-level anonymization alone cannot neutralize model identity signals, with direct implications for EU AI Act compliance (Articles 13, 14, 26) and for computer system validation (CSV) in quality-critical multi-agent deployments.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2606.09854
