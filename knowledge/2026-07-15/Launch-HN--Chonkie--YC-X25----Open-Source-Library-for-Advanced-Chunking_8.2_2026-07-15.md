# Launch HN: Chonkie (YC X25) – Open-Source Library for Advanced Chunking

**评分：** 8.2  
**状态：** 正常  
**标签：** RAG, Chunking, Open-Source, 发布  
**更新日期：** 2026-07-15  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Shreyash and Bhavnick. We&#x27;re building Chonkie (<a href="https:&#x2F;&#x2F;chonkie.ai">https:&#x2F;&#x2F;chonkie.ai</a>), an open-source library for chunking and embedding data.<p>Python: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie</a><p>TypeScript: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts</a><p>Here&#x27;s a video showing our code chunker: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0</a>.<p>Bhavnick and I have been building personal projects with LLMs for a few years. For much of this time, we found ourselves writing our own chunking logic to support RAG applications. We often hesitated to use existing libraries because they either had only basic features or felt too bloated (some are 80MB+).<p>We built Chonkie to be lightweight, fast, extensible, and easy. The space is evolving rapidly, and we wanted Chonkie to be able to quickly support the newest strategies. We currently support: Token Chunking, Sentence Chunking, Recursive Chunking, Semantic Chunking, plus:<p>-  Semantic Double Pass Chunking: Chunks text semantically first, then merges closely related chunks.<p>-  Code Chunking: Chunks code files by creating an AST and finding ideal split points.<p>-  Late Chunking: Based on the paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701</a>), where chunk embeddings are derived from embedding a longer document.<p>-  Slumber Chunking: Based on the &quot;Lumber Chunking&quot; paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526</a>). It uses recursive chunking, then an LLM verifies split points, aiming for high-quality chunks with reduced token usage and LLM costs.<p>You can see how Chonkie compares to LangChain and LlamaIndex in our benchmarks: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS.md">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS....</a><p>Some technical details about the Chonkie package:  - ~15MB default install vs. ~80-170MB for some alternatives. - Up to 33x faster token chunking compared to LangChain and LlamaIndex in our tests. - Works with major tokenizers (transformers, tokenizers, tiktoken). - Zero external dependencies for basic functionality. - Implements aggressive caching and precomputation. - Uses running mean pooling for efficient semantic chunking. - Modular dependency system (install only what you need).<p>In addition to chunking, Chonkie also provides an easy way to create embeddings. For supported providers (SentenceTransformer, Model2Vec, OpenAI), you just specify the model name as a string. You can also create custom embedding handlers for other providers.<p>RAG is still the most common use case currently. However, Chonkie makes chunks that are optimized for creating high quality embeddings and vector retrieval, so it is not really tied to the &quot;generation&quot; part of RAG. In fact, We&#x27;re seeing more and more people use Chonkie for implementing semantic search and&#x2F;or setting context for agents.<p>We are currently focused on building integrations to simplify the retrieval process. We&#x27;ve created &quot;handshakes&quot; – thin functions that interact with vector DBs like pgVector, Chroma, TurboPuffer, and Qdrant, allowing you to interact with storage easily. If there&#x27;s an integration you&#x27;d like to see (vector DB or otherwise), please let us know.<p>We also offer hosted and on-premise versions with OCR, extra metadata, all embedding providers, and managed vector databases for teams that want a fully managed pipeline. If you&#x27;re interested, reach out at shreyash@chonkie.ai or book a demo: <a href="https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo" rel="nofollow">https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo</a>.<p>We&#x27;re eager to hear your feedback and comments! Thanks!

## 综合总结
Chonkie 是一个开源的轻量级高级文本分块与嵌入库，旨在替代 LangChain 等臃肿方案。它集成了包括 Late Chunking、AST 代码分块和 LLM 验证分块在内的多种前沿策略，通过极致的工程优化实现了极小的体积和极高的处理速度，为 RAG 和语义搜索开发者提供了高实用价值的工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目实现了多种高级分块算法，包括基于 AST 的代码分块、基于最新论文的 Late Chunking 和 Slumber Chunking（LLM 验证分割点）。在工程优化上，通过零外部基础依赖、激进缓存和预计算、running mean pooling 等技术，实现了约 15MB 的轻量体积和最高 33 倍的速度提升。

### 实用性 (评分: 9.0/10)
直击 RAG 开发中现有分块库（如 LangChain）体积臃肿、速度慢的痛点，为从业者提供了轻量、高效的替代方案。支持 Python/TS 双语言，并内置与主流向量数据库的集成，能显著降低 RAG、Agent 及语义搜索管线的开发与部署成本。

### 社区活跃度 (评分: 8.0/10)
获得了 151 个点赞和 42 条评论，在 Launch HN 中表现良好。社区对轻量级替代方案和 RAG 基础设施优化展现出浓厚兴趣，讨论多集中于与现有工具的对比、具体技术实现细节及商业化模式。

## 项目链接
https://news.ycombinator.com/item?id=44225930
