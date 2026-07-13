# Launch HN: Chonkie (YC X25) – Open-Source Library for Advanced Chunking

**评分：** 7.8  
**状态：** 正常  
**标签：** RAG, Chunking, Open-Source, Launch  
**更新日期：** 2026-07-13  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Shreyash and Bhavnick. We&#x27;re building Chonkie (<a href="https:&#x2F;&#x2F;chonkie.ai">https:&#x2F;&#x2F;chonkie.ai</a>), an open-source library for chunking and embedding data.<p>Python: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie</a><p>TypeScript: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts</a><p>Here&#x27;s a video showing our code chunker: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0</a>.<p>Bhavnick and I have been building personal projects with LLMs for a few years. For much of this time, we found ourselves writing our own chunking logic to support RAG applications. We often hesitated to use existing libraries because they either had only basic features or felt too bloated (some are 80MB+).<p>We built Chonkie to be lightweight, fast, extensible, and easy. The space is evolving rapidly, and we wanted Chonkie to be able to quickly support the newest strategies. We currently support: Token Chunking, Sentence Chunking, Recursive Chunking, Semantic Chunking, plus:<p>-  Semantic Double Pass Chunking: Chunks text semantically first, then merges closely related chunks.<p>-  Code Chunking: Chunks code files by creating an AST and finding ideal split points.<p>-  Late Chunking: Based on the paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701</a>), where chunk embeddings are derived from embedding a longer document.<p>-  Slumber Chunking: Based on the &quot;Lumber Chunking&quot; paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526</a>). It uses recursive chunking, then an LLM verifies split points, aiming for high-quality chunks with reduced token usage and LLM costs.<p>You can see how Chonkie compares to LangChain and LlamaIndex in our benchmarks: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS.md">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS....</a><p>Some technical details about the Chonkie package:  - ~15MB default install vs. ~80-170MB for some alternatives. - Up to 33x faster token chunking compared to LangChain and LlamaIndex in our tests. - Works with major tokenizers (transformers, tokenizers, tiktoken). - Zero external dependencies for basic functionality. - Implements aggressive caching and precomputation. - Uses running mean pooling for efficient semantic chunking. - Modular dependency system (install only what you need).<p>In addition to chunking, Chonkie also provides an easy way to create embeddings. For supported providers (SentenceTransformer, Model2Vec, OpenAI), you just specify the model name as a string. You can also create custom embedding handlers for other providers.<p>RAG is still the most common use case currently. However, Chonkie makes chunks that are optimized for creating high quality embeddings and vector retrieval, so it is not really tied to the &quot;generation&quot; part of RAG. In fact, We&#x27;re seeing more and more people use Chonkie for implementing semantic search and&#x2F;or setting context for agents.<p>We are currently focused on building integrations to simplify the retrieval process. We&#x27;ve created &quot;handshakes&quot; – thin functions that interact with vector DBs like pgVector, Chroma, TurboPuffer, and Qdrant, allowing you to interact with storage easily. If there&#x27;s an integration you&#x27;d like to see (vector DB or otherwise), please let us know.<p>We also offer hosted and on-premise versions with OCR, extra metadata, all embedding providers, and managed vector databases for teams that want a fully managed pipeline. If you&#x27;re interested, reach out at shreyash@chonkie.ai or book a demo: <a href="https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo" rel="nofollow">https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo</a>.<p>We&#x27;re eager to hear your feedback and comments! Thanks!

## 综合总结
Chonkie是一个专为RAG和语义搜索设计的开源轻量级分块与嵌入库。它针对现有框架体积大、速度慢的痛点，提供了仅15MB的极简安装和最高达33倍的性能提升。项目支持多种分块策略，包括基于AST的代码分块及跟进最新论文的Late Chunking和Slumber Chunking，并提供了与主流向量数据库的无缝集成，对AI开发者构建高效RAG应用具有极高的实用价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
项目聚焦于RAG流程中的数据预处理环节，技术深度体现在对前沿论文（Late Chunking, Lumber Chunking）的快速工程实现，以及AST解析代码分块、running mean pooling优化语义分块等手段。虽非基础模型层面的突破，但在工程优化和算法应用上展现了较高的技术含金量。

### 实用性 (评分: 9.0/10)
对AI从业者（尤其是RAG和搜索方向）具有极高的实用价值。直击现有框架（如LangChain）体积庞大、速度慢的痛点，提供了轻量、高性能的替代方案。支持多种分块策略和主流向量数据库集成，可直接应用于生产环境，显著降低开发与运维成本。

### 社区活跃度 (评分: 7.5/10)
151个点赞和42条评论表明该项目在HN社区获得了不错的关注度。作为YC的Launch项目，其针对LangChain等主流框架的痛点进行优化，容易引发开发者关于RAG实践和框架选择的讨论，社区互动质量较高。

## 项目链接
https://news.ycombinator.com/item?id=44225930
