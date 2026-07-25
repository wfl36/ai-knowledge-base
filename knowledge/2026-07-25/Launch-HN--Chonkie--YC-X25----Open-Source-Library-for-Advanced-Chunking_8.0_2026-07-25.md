# Launch HN: Chonkie (YC X25) – Open-Source Library for Advanced Chunking

**评分：** 8.0  
**状态：** 正常  
**标签：** RAG, Chunking, 开源项目, 发布  
**更新日期：** 2026-07-25  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Shreyash and Bhavnick. We&#x27;re building Chonkie (<a href="https:&#x2F;&#x2F;chonkie.ai">https:&#x2F;&#x2F;chonkie.ai</a>), an open-source library for chunking and embedding data.<p>Python: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie</a><p>TypeScript: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts</a><p>Here&#x27;s a video showing our code chunker: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0</a>.<p>Bhavnick and I have been building personal projects with LLMs for a few years. For much of this time, we found ourselves writing our own chunking logic to support RAG applications. We often hesitated to use existing libraries because they either had only basic features or felt too bloated (some are 80MB+).<p>We built Chonkie to be lightweight, fast, extensible, and easy. The space is evolving rapidly, and we wanted Chonkie to be able to quickly support the newest strategies. We currently support: Token Chunking, Sentence Chunking, Recursive Chunking, Semantic Chunking, plus:<p>-  Semantic Double Pass Chunking: Chunks text semantically first, then merges closely related chunks.<p>-  Code Chunking: Chunks code files by creating an AST and finding ideal split points.<p>-  Late Chunking: Based on the paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701</a>), where chunk embeddings are derived from embedding a longer document.<p>-  Slumber Chunking: Based on the &quot;Lumber Chunking&quot; paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526</a>). It uses recursive chunking, then an LLM verifies split points, aiming for high-quality chunks with reduced token usage and LLM costs.<p>You can see how Chonkie compares to LangChain and LlamaIndex in our benchmarks: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS.md">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS....</a><p>Some technical details about the Chonkie package:  - ~15MB default install vs. ~80-170MB for some alternatives. - Up to 33x faster token chunking compared to LangChain and LlamaIndex in our tests. - Works with major tokenizers (transformers, tokenizers, tiktoken). - Zero external dependencies for basic functionality. - Implements aggressive caching and precomputation. - Uses running mean pooling for efficient semantic chunking. - Modular dependency system (install only what you need).<p>In addition to chunking, Chonkie also provides an easy way to create embeddings. For supported providers (SentenceTransformer, Model2Vec, OpenAI), you just specify the model name as a string. You can also create custom embedding handlers for other providers.<p>RAG is still the most common use case currently. However, Chonkie makes chunks that are optimized for creating high quality embeddings and vector retrieval, so it is not really tied to the &quot;generation&quot; part of RAG. In fact, We&#x27;re seeing more and more people use Chonkie for implementing semantic search and&#x2F;or setting context for agents.<p>We are currently focused on building integrations to simplify the retrieval process. We&#x27;ve created &quot;handshakes&quot; – thin functions that interact with vector DBs like pgVector, Chroma, TurboPuffer, and Qdrant, allowing you to interact with storage easily. If there&#x27;s an integration you&#x27;d like to see (vector DB or otherwise), please let us know.<p>We also offer hosted and on-premise versions with OCR, extra metadata, all embedding providers, and managed vector databases for teams that want a fully managed pipeline. If you&#x27;re interested, reach out at shreyash@chonkie.ai or book a demo: <a href="https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo" rel="nofollow">https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo</a>.<p>We&#x27;re eager to hear your feedback and comments! Thanks!

## 综合总结
Chonkie是一个YC孵化的开源轻量级文本分块库，旨在解决现有RAG开发中分块工具臃肿、缓慢和策略单一的问题。项目通过极致的工程优化实现了极小的体积和极高的速度，并支持包括语义分块、AST代码分块及基于最新论文的Late/Slumber分块等高级策略，为构建RAG、语义搜索和Agent的AI从业者提供了极具价值的高效基础设施。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目在RAG前置处理环节展现了不错的技术深度与工程优化能力。不仅实现了基础的Token和递归分块，还深入支持了基于AST的代码分块、基于最新论文的Late Chunking和Slumber Chunking（LLM验证分割点）等高级策略。工程层面通过零外部基础依赖、激进缓存与预计算、running mean pooling等手段，实现了相比LangChain等竞品33倍的性能提升和极小的包体积（~15MB）。

### 实用性 (评分: 9.0/10)
对AI从业者（尤其是RAG、搜索和Agent方向的开发者）具有极高的实用价值。直接击中了现有主流框架（如LangChain/LlamaIndex）中分块模块臃肿、缓慢且策略单一的痛点。提供了Python和TS双端支持，开箱即用的多种分块策略，以及与主流向量数据库的轻量级集成，能够显著降低开发门槛并提升Pipeline效率。

### 社区活跃度 (评分: 7.5/10)
作为Launch HN项目，151个Points和42条评论展现了良好的社区关注度。开发者对轻量级、高性能替代重型框架的工具通常抱有极大兴趣，评论中大概率涉及与现有框架的对比、分块策略的实际效果探讨以及功能请求，讨论质量较高。

## 项目链接
https://news.ycombinator.com/item?id=44225930
