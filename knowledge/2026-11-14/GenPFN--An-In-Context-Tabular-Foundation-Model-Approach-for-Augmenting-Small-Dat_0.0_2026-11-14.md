# GenPFN: An In-Context Tabular Foundation Model Approach for Augmenting Small Datasets in Engineering

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-14  
**来源：** rss  

## 项目描述
arXiv:2611.14804v1 Announce Type: new Abstract: Costly simulations and experiments limit the data available for engineering design. This paper proposes GenPFN, a training-free candidate generator guided by a pretrained tabular Prior-Data Fitted Network (TabPFN) classifier with fixed weights. The context contains evaluated designs labeled desired (Class 1) or undesired (Class 0). GenPFN interpolates between desired designs and refines candidates using gated classifier gradients and Gaussian noise. Each candidate is evaluated using the problem's constraints and objective functions. Evaluated desired designs and their objective values augment the context for regression training. Evaluation spans fourteen selected problems, including a two-parameter benchmark and a 44-parameter hull problem. In paired comparisons, GenPFN with TabPFN v1 achieves higher class satisfaction and lower realism distance than the tested adversarial, variational-autoencoder and diffusion generators. The variational-autoencoder generator provides greater coverage and diversity. Relative to the synthetic minority over-sampling technique (SMOTE), GenPFN provides lower coverage distance and greater diversity. Among observed paired regression fits, augmentation reduces estimated AutoGluon validation mean squared error by 62.1% relative to context-only training. A hull-stern case study yields 99.3% propeller-compatible candidates versus 1.4% among randomly sampled context designs. Generation followed by evaluation produces sample sets that augment limited datasets and support training more accurate predictive models.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.14804
