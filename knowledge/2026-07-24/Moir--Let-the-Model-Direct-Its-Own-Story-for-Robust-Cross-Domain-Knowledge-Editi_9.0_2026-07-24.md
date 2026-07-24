# Moir: Let the Model Direct Its Own Story for Robust Cross-Domain Knowledge Editing

**评分：** 9.0  
**状态：** 正常  
**标签：** 大模型, 知识编辑, 推理, 协方差估计, 论文  
**更新日期：** 2026-07-24  
**来源：** rss  

## 项目描述
arXiv:2607.20433v1 Announce Type: new Abstract: While language models remain frozen at their training state, the world evolves continuously. Knowledge editing has emerged as a key alternative to full retraining, but its deployment is bottlenecked by the erosion of core capabilities: mathematical and programmatic reasoning collapse while encyclopedic recall remains intact. We trace this asymmetric degradation to a distributional mismatch. Covariance-based editors preserve only the subspaces spanned by their reference corpus, but fail to capture the operative distribution shaped by post-training such as SFT and DPO. Static external corpora, including Wikipedia and even the original pretraining mixture, cannot recover this shifted manifold. We propose Moir, which estimates the preservation covariance $C$ directly from the model itself by sampling from its own decoding distribution. Seeding generation with a single random vocabulary token bypasses the instruction-following templates that otherwise dominate sampled outputs, exposing the broader subspaces the model has internalized. Moir requires no external data and serves as a drop-in component for any covariance-based editor, a practical advantage given that the pre- and post-training corpora of most modern LLMs are not publicly accessible. Across OLMo-2, Llama-3.1, and Qwen-3 (7-8B), under both MEMIT and AlphaEdit and in batch and sequential regimes, Moir consistently extends preservation in the most vulnerable domains, most strikingly on Qwen3-8B after 20,000 AlphaEdit batch edits, it retains 79.9% GSM8K accuracy compared to 10.9% with the Wikipedia baseline. These results suggest that aligning the preservation distribution with the model's operative distribution is a key factor in non-destructive editing, and that the model itself may be the most accessible source of that distribution for deployed systems.

## 综合总结
本文针对大模型知识编辑中导致数学和编程等推理能力崩溃的问题，指出其根源在于后训练引起的分布偏移使得基于静态外部语料的协方差编辑器失效。为此提出Moir方法，通过从模型自身的解码分布中采样（使用随机词元种子绕过指令模板）来估计保留协方差，无需任何外部数据。Moir可作为现有编辑器的即插即用组件，在多款主流大模型上显著缓解了推理能力的退化，如在Qwen3-8B经过2万次编辑后将GSM8K准确率从10.9%提升至79.9%，证明了模型自身是获取操作分布的最佳来源。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文深刻揭示了知识编辑导致大模型推理能力崩溃的根本原因：后训练（如SFT和DPO）造成的分布偏移使得静态外部语料库无法捕捉模型的实际操作流形。提出从模型自身的解码分布中采样来估计保留协方差，并巧妙地使用单个随机词元作为生成种子以绕过指令模板，方法新颖且理论自洽。在Qwen3-8B上将GSM8K准确率从10.9%提升至79.9%，论证极具说服力。

### 实用性 (评分: 9.5/10)
极具有实际应用价值。Moir无需任何外部训练数据，解决了现代LLM预训练和后训练语料难以获取的痛点。作为即插即用的组件，可无缝集成到MEMIT和AlphaEdit等现有主流协方差编辑器中，改造成本极低。对于需要频繁更新知识且对推理能力退化零容忍的商业大模型部署场景，提供了直接可行的解决方案。

### 社区活跃度 (评分: 8.5/10)
知识编辑是大模型迭代与维护的前沿热点话题。文章发布于arXiv，涉及Llama-3.1和Qwen-3等最新开源模型，时效性极强。实验结果惊人（准确率8倍提升），极大概率会引发社区对该研究方向的广泛关注与复现，对后续无损知识编辑研究具有重要的指导意义和影响力。

## 项目链接
https://arxiv.org/abs/2607.20433
