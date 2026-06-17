# Self-Generated Error Training for Token Editing in Diffusion Language Models

**评分：** 8.0  
**状态：** 正常  
**标签：** 扩散语言模型, Token编辑, 训练推理不匹配, LoRA, 解码优化, 论文  
**更新日期：** 2026-06-17  
**来源：** rss  

## 项目描述
arXiv:2606.17175v1 Announce Type: new Abstract: Token-to-token (T2T) editing lets LLaDA2.1 revise committed tokens during block-diffusion decoding. The released recipe trains this editor on random vocabulary corruptions, but at inference the editor sees the model's own fluent, high-confidence draft errors instead. We study this training-inference mismatch and propose self-generated T2T, which performs a no-gradient draft pass, fills masked positions with predicted tokens, and supervises recovery in a second pass under these self-generated corruptions. We implement the update as a short LoRA continued-pretraining pass on LLaDA2.1-mini and evaluate on several benchmarks under the official Q-Mode T2T procedure with unchanged inference parameters. The method generally improves accuracy while reducing T2T edit intensity, mitigating failure modes such as final-digit transcription errors after otherwise correct reasoning and excessive self-correction before short factual answers.

## 综合总结
本文针对扩散语言模型（如LLaDA2.1）中Token-to-Token (T2T) 编辑存在的训练与推理分布不匹配问题，提出了Self-generated T2T方法。该方法通过无梯度草稿推理生成模型自身的流畅错误，并在这些自生成错误上进行二次监督恢复训练。基于LLaDA2.1-mini的短LoRA微调实验表明，该方法在不改变推理参数的情况下，不仅提升了准确性、降低了编辑强度，还有效缓解了推理末尾数字转录错误和过度自我纠正等典型失败模式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
本文精准识别了扩散语言模型中T2T编辑任务的训练-推理分布不匹配问题（随机损坏训练 vs 模型自身流畅错误推理），并提出了Self-generated T2T方法。通过无梯度草稿生成自错误再进行二次监督恢复，方法逻辑严密、新颖，结合短LoRA微调实现，技术深度与论证严谨度较高。

### 实用性 (评分: 8.0/10)
提出的自生成错误训练方法可直接应用于LLaDA系列模型的解码优化，采用短LoRA继续预训练实现，计算成本低，易于复现。有效缓解了实际推理中的数字转录错误和过度自我纠正等痛点，对扩散语言模型从业者具有极高的实践指导价值，但适用范围目前受限于扩散架构模型。

### 社区活跃度 (评分: 7.5/10)
扩散语言模型是当前大模型前沿探索方向，LLaDA2.1作为较新模型，话题时效性强。arXiv论文来源具备一定权威性，但该细分领域社区影响力和普及度尚不及主流自回归大模型，整体关注范围相对垂直。

## 项目链接
https://arxiv.org/abs/2606.17175
