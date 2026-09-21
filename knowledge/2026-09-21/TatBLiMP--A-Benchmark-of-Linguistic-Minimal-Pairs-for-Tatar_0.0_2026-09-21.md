# TatBLiMP: A Benchmark of Linguistic Minimal Pairs for Tatar

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-21  
**来源：** rss  

## 项目描述
arXiv:2609.20832v1 Announce Type: new Abstract: We introduce TatBLiMP, the first benchmark of linguistic minimal pairs for Tatar (tt, ISO 639-3 tat), a Qypchaq Turkic language written in Cyrillic. To our knowledge it is the first grammaticality evaluation for Tatar language models of any kind, since even the 101-language MultiBLiMP does not include Tatar. TatBLiMP covers 16 morphosyntactic phenomena in 1248 sentence pairs. Each pair differs by a single morpheme, one grammatical and one ungrammatical. A model passes a pair when it assigns higher probability to the grammatical member. Scoring compares probabilities the model already assigns, so the benchmark needs no text generation and no parser, and it runs on base models and on mid-training checkpoints. TatBLiMP adapts the phenomenon inventory and single-morpheme breaking operations of TurBLiMP to Tatar and adds one phenomenon specific to Tatar, bare-noun number after numerals and quantifiers. The grammatical member of every pair is an attested sentence from Tatar literary prose. The ungrammatical member is produced by a deterministic single-morpheme perturbation with the apertium-tat transducer. Every pair is ratified by a native speaker. A plausibility principle governs construction, so the ungrammatical member is a plausible real-world error rather than an arbitrary corruption. Across from-scratch Tatar models, cross-lingual adaptations, and frontier multilingual LLMs, the benchmark tracks focused Tatar training rather than parameter scale. A 478M from-scratch model and a 125M monolingual model lead near 0.97, a 7B adaptation trails, frontier LLMs of 30-120B parameters fall to 0.80-0.92, and a lightly tuned multilingual model is weakest. We close with the benchmark's main limitation. Its inherited taxonomy omits the morphophonology, vowel harmony and consonant assimilation, that is most salient to native speakers, and we sketch a native second layer that would add it.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.20832
