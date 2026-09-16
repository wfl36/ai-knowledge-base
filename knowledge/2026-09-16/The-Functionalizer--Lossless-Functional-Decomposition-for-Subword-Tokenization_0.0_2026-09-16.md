# The Functionalizer: Lossless Functional Decomposition for Subword Tokenization

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-16  
**来源：** rss  

## 项目描述
arXiv:2609.15991v1 Announce Type: new Abstract: Standard subword tokenizers either treat every orthographic variation of a word (such as hello, Hello, HELLO, and H\'ello) as unrelated vocabulary entries, which fragments the embedding space, or discard this variation through lossy normalization. We present the Functionalizer, a lossless pre-tokenizer framework that factors orthographic and structural variations into a compositional opcode/operand prefix stream before tokenization: a canonical base token (operand) prefixed by parametric transformation operators (opcodes) encoded in the Unicode Private Use Area. We introduce operators covering casing (CAPITALIZE), diacritics (13 dedicated opcodes), and character repetition (REPEAT, MULTIREPEAT), which are fully reversible. Across six natural language and code corpora, the Functionalizer enables complete corpus coverage with significantly smaller vocabularies under unconstrained conditions, reducing actual vocabulary slot requirements by up to 16%. When looking at sequence lengths, we observe a sharp domain-dependent tradeoff: it compresses indentation-heavy code sequences but inflates natural-language prose sequences. Preliminary downstream evaluations on 25M parameter GPT-2 scale models show that at this scale, the Functionalizer drastically improves code syntax validity and improves code character perplexity while maintaining similar text coherence on prose. These findings demonstrate that functional decomposition can be an effective mechanism for vocabulary-efficient, structurally aware language modeling, and motivate further validation at production scale.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.15991
