# Representational Simplicity and Circuit Size Dissociate in a Threshold-Dependent Way: A Controlled Test via Adversarial Training

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-30  
**来源：** rss  

## 项目描述
arXiv:2609.35890v1 Announce Type: new Abstract: Sparse-autoencoder decomposability and concentrated feature attribution are increasingly treated as evidence that a model's computation is easier to reverse-engineer. Whether this representational and attributional cleanliness actually predicts a smaller or more tractable causal circuit remains an open question. We test this directly using adversarial training as a controlled instrument: it reliably reshapes internal representations, but this alone does not constitute a test of circuit size. We investigate this question through reverse-engineering complexity: the causal structure required to recover a model's behavior at a fixed level of faithfulness. To our knowledge, this is the first controlled empirical test of whether representational or attributional simplicity translates into causal simplicity at the circuit level. Starting from the same pretrained GPT-2 Small checkpoint, we apply matched standard and adversarial continual training, requiring both conditions to retain competence on indirect object identification and pass independent robustness verification before comparing mechanisms. We then compare the models along three complementary axes: sparse-autoencoder decomposability, SAE feature engagement in task attribution, and the size of faithful circuits recovered from the raw computational graph. The robust model is more SAE-decomposable and engages fewer SAE features in task attribution. Circuit size is regime-dependent: on competence-matched IOI, standard leads or ties below 85% faithfulness, but robust needs substantially fewer edges at high faithfulness (90%, 95%), a pattern established on the primary pair while representational trends generalize across a seven-point sweep and a second corpus.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.35890
