# VisKG-LM: Compiling Knowledge Graphs into Visual Memory for Multiple-Choice Question Answering

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-09-18  
**来源：** rss  

## 项目描述
arXiv:2609.19158v1 Announce Type: new Abstract: Knowledge graphs are usually integrated into question answering by encoding a retrieved subgraph with a graph neural network and fusing it with the language model in the online inference path. The same subgraph is therefore re-encoded from scratch every time a pair is scored, across training epochs, seeds, and evaluation runs, even though the knowledge graph never changes. We ask whether the retrieved knowledge graphs can instead be compiled once, offline, and then accessed as read-only memory. VisKG-LM shows that it can, by decoupling graph encoding from language reasoning. It serializes each retrieved candidate-specific subgraph as Relation-Labeled Paths and renders the result as an image whose two-dimensional layout preserves the branching structure of the paths. Each image is encoded once, offline, and cached for reuse. At inference, the language model contextualizes the question and candidate from text alone, and only its final layer consults the cached visual memory, reading both its global layout and its local relational detail. The graph information thus enters only after the text has been understood. On the test sets of CommonsenseQA, OpenBookQA, and MedQA-USMLE, VisKG-LMimproves over GreaseLM by $1.2$, $0.8$, and $4.3$ points, respectively, while matching or surpassing GraphVis, a $7$B vision-language model, with only about $400$M online parameters. Against a matched text-only control that receives the identical Relation-Labeled Paths, it gains $4.2$, $6.5$, and $5.1$ points across the three benchmarks. These gains show that the complete visual-memory interface adds value beyond path textualization alone and support compiled visual memory as an alternative to online graph propagation.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.19158
