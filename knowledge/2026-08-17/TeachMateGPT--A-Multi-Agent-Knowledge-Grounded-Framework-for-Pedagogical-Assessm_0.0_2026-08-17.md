# TeachMateGPT: A Multi-Agent Knowledge-Grounded Framework for Pedagogical Assessment Generation from Science Curriculum Materials

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-08-17  
**来源：** rss  

## 项目描述
arXiv:2608.13708v1 Announce Type: new Abstract: Automatically generating textbook-grounded assessment items can reduce science teachers' workload, but existing retrieval-augmented generation (RAG) systems rely on flat retrieval, support only single-question generation, lack safeguards against weak evidence, and are ill-suited to low-resource, board-exam-structured curricula. We address these limitations with TeachMateGPT, a multi-agent system contributing four advances to curriculum-grounded science-assessment authoring. (i) COPE, a hierarchical knowledge base replacing token-window chunking with a multi-resolution index that segments documents along syllabus structure and links them at three granularities via a traversable graph-based lineage, matching evidence to each topic's instructional level. (ii) A staged, fail-closed agent pipeline replacing one-shot retrieve-then-generate: routing gates search, retrieval fuses dense and lexical evidence under a coverage gate that withholds generation on insufficient evidence, and specialist agents draft objective and constructed-response items. (iii) SAVER, a source-attributed verification protocol scoring faithfulness, relevance, and hallucination risk against retrieved evidence, applying stricter grounding checks across each creative question's four sub-parts, paired with teacher-in-the-loop evaluation rather than automatic filtering. (iv) NCTB-SciGen8, a curriculum-grounded dataset of 198 items (143 multiple-choice, 55 creative questions) spanning all 14 chapters of the NCTB Class 8 science textbook, produced by the pipeline and rated by three practicing teachers. TeachMateGPT raises faithfulness (0.68 $\rightarrow$ 0.96) and answer relevancy (0.60 $\rightarrow$ 0.89) over a vanilla RAG baseline.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2608.13708
