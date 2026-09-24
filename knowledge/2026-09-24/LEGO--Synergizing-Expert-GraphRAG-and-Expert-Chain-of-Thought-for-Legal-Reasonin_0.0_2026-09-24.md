# LEGO: Synergizing Expert GraphRAG and Expert Chain-of-Thought for Legal Reasoning

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-24  
**来源：** rss  

## 项目描述
arXiv:2609.27009v1 Announce Type: new Abstract: Large language models are increasingly applied to high-risk domains such as law, yet complex legal reasoning remains limited by two structural challenges. First, existing RAG and GraphRAG methods emphasize lexical or semantic similarity while overlooking normative relations among legal provisions. Second, vanilla Chain-of-Thought prompting may generate plausible rationales without enforcing the normative structure of legal reasoning. To deal with the bottleneck of pipelines in the legal reasoning domain, we propose LEGO, a dual-module framework that synergizes Legal Expert GraphRAG and expert Chain-of-thought for complex legal reasoning. ExpertGraphRAG uses an expert-annotated civil code graph encoding these normative relations with a greedy normative-coverage retrieval algorithm to dynamically extract instance-specific provision subgraphs, while ExpertCoT organizes the retrieved provisions and case facts into structured Provision-Fact-Conclusion reasoning. With a Qwen3-8B backbone, LEGO achieves 40.53% exact-match accuracy on LawExamQA_Civil, outperforming the evaluated RAG and CoT baselines and performing comparably to the evaluated larger models, while remaining robust on multi-hop questions. It also achieves the best results among the evaluated baselines on the open-ended benchmarks. Ablation studies confirm the individual and complementary contributions of both modules, demonstrating LEGO's effectiveness in improving LLMs' complex legal reasoning ability. Code and dataset can be found in the link: https://github.com/BLK-WHT/LEGO

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.27009
