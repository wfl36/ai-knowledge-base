# Speaking in Self-Assessing Tongues: On the Verbalized Confidence of LLMs in Machine Translation

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 机器翻译, 置信度评估, 模型校准, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17234v1 Announce Type: new Abstract: The rapid rise in popularity of large language models (LLMs) for translation calls for a thorough study of the reliability of their confidence in their own outputs. Unlike many generation tasks, translation errors and confidence levels can be useful at different levels of granularity (tokens, words, or spans). Unsupervised approaches based on internal signals like predicted probabilities can be misleading because they reflect certainty among alternatives rather than correctness. In addition, they require access to such internal signals. Here, we devise five verbalized methods of extracting an LLM's per-token confidence without those shortcomings and compare their reliability with that of the model's internal signals of certainty. We evaluate reliability using two forms of alignment: fine-grained error detection and calibration. For both, internal and verbalized methods perform similarly, although results vary by model. Interestingly, we find little to no correlation between internal and verbalized methods.

## 综合总结
本文研究了LLM在机器翻译任务中的自我评估能力，针对内部概率信号难以获取且可能存在误导的问题，提出了五种基于verbalized的token级置信度提取方法。评估表明，verbalized方法在细粒度错误检测和校准上与内部信号表现相当，但两者之间几乎无相关性。该发现对理解LLM置信度来源及黑盒场景下的翻译质量评估具有重要指导意义。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
论文针对LLM在机器翻译中的置信度评估进行了深入研究，提出了五种基于verbalized（语言化）的token级置信度提取方法。研究论证严谨，不仅对比了内部信号与verbalized方法的可靠性，更揭示了两者之间缺乏相关性的反直觉现象，为理解LLM自我评估机制与内部概率表征的差异提供了深刻洞见。

### 实用性 (评分: 8.0/10)
对于无法获取模型内部logprob的黑盒API调用场景，本文提出的verbalized置信度提取方法具有极高的落地价值。研究证明其效果与内部信号相当，可直接指导从业者在机器翻译及其他生成任务中实现低成本的质量监控与幻觉检测，适用范围广泛。

### 社区活跃度 (评分: 8.0/10)
LLM的置信度与自我评估是当前AI社区关注的热点问题，尤其在机器翻译等高可靠性要求场景下。该研究来自arXiv，紧扣行业痛点，其关于内部与外部置信度不相关的发现挑战了既有认知，具有较强的话题性和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.17234
