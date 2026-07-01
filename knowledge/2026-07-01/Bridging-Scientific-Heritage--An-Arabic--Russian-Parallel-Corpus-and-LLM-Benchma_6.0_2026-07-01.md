# Bridging Scientific Heritage: An Arabic--Russian Parallel Corpus and LLM Benchmark for Sustainable Knowledge Transfer

**评分：** 6.0  
**状态：** 正常  
**标签：** 大模型, 机器翻译, 多语言, 低资源语言, 数据集, 论文  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30943v1 Announce Type: new Abstract: Russian and Arabic are among the major languages of scientific communication. Language barriers impede the exchange of research results between these communities, which affects international collaboration and the progress of sustainability-related research. We present a benchmark for Arabic--Russian scientific translation. The benchmark includes a hybrid parallel corpus of about 27,000 sentence pairs, compiled from scientific abstracts and general-domain texts (religion, news, conversations). We fine-tune three multilingual language models -- mT5-base (580M parameters), NLLB-200-distilled-1.3B (1.3B), and Qwen2.5-7B-Instruct (7B) -- using LoRA with ranks 8, 16, 32, and 64. The Qwen2.5-7B model with QLoRA (rank 8) yields BLEU 23.15, chrF 43.89, BERTScore 0.906, and COMET 0.758. These are +4.36 BLEU and +0.051 COMET above the zero-shot baseline. Few-shot prompting with three examples does not improve performance, indicating that domain-specific fine-tuning is required. We release the models, the corpus, and the evaluation code. By lowering the language barrier for scientific texts, the work enables knowledge exchange between Arabic-speaking and Russian-speaking researchers. It contributes to sustainable partnerships (UN SDG 17) and innovation infrastructure (SDG 9), aligning with the conference's focus on technology-driven sustainable development.

## 综合总结
本文针对阿拉伯语-俄语科学翻译的痛点，构建了一个约2.7万句对的混合平行语料库及基准。通过在mT5、NLLB和Qwen2.5等模型上进行LoRA微调实验，证实了领域微调优于few-shot prompting，其中Qwen2.5-7B表现最佳。该工作开源了相关资源，有助于降低阿俄学术交流的语言障碍，促进可持续发展，但数据规模和技术方法创新性较为有限。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.0/10)
本文构建了一个包含约2.7万句对的阿拉伯语-俄语科学翻译平行语料库，并在mT5-base、NLLB-200和Qwen2.5-7B等模型上进行了不同LoRA rank的微调实验。研究发现QLoRA(rank 8)微调的Qwen2.5-7B效果最佳，且few-shot prompting无法替代领域微调。研究方法较为常规，技术深度有限，主要贡献在于基准和数据集的构建。

### 实用性 (评分: 7.0/10)
研究开源了语料库、模型和评估代码，对从事阿俄翻译或低资源语言对微调的从业者具有直接的参考和复用价值。但语料库规模较小且混合了通用领域文本，在纯科学领域的实际落地效果可能存在瓶颈，需进一步扩充数据。

### 社区活跃度 (评分: 6.0/10)
该研究聚焦于阿拉伯语与俄语之间的科学知识传递，结合了联合国可持续发展目标（SDG 9和17），具有较好的社会意义和跨文化交流价值。但作为单一作者的arXiv预印本，且属于相对冷门的语言对，在主流AI社区的短期影响力和关注度相对有限。

## 项目链接
https://arxiv.org/abs/2606.30943
