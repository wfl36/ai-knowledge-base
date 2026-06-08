# Launch HN: Chonkie (YC X25) – Open-Source Library for Advanced Chunking

**评分：** 8.0  
**状态：** 正常  
**标签：** RAG, 数据处理, 开源库, 发布  
**更新日期：** 2026-06-08  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Shreyash and Bhavnick. We&#x27;re building Chonkie (<a href="https:&#x2F;&#x2F;chonkie.ai">https:&#x2F;&#x2F;chonkie.ai</a>), an open-source library for chunking and embedding data.<p>Python: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie</a><p>TypeScript: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts</a><p>Here&#x27;s a video showing our code chunker: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0</a>.<p>Bhavnick and I have been building personal projects with LLMs for a few years. For much of this time, we found ourselves writing our own chunking logic to support RAG applications. We often hesitated to use existing libraries because they either had only basic features or felt too bloated (some are 80MB+).<p>We built Chonkie to be lightweight, fast, extensible, and easy. The space is evolving rapidly, and we wanted Chonkie to be able to quickly support the newest strategies. We currently support: Token Chunking, Sentence Chunking, Recursive Chunking, Semantic Chunking, plus:<p>-  Semantic Double Pass Chunking: Chunks text semantically first, then merges closely related chunks.<p>-  Code Chunking: Chunks code files by creating an AST and finding ideal split points.<p>-  Late Chunking: Based on the paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701</a>), where chunk embeddings are derived from embedding a longer document.<p>-  Slumber Chunking: Based on the &quot;Lumber Chunking&quot; paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526</a>). It uses recursive chunking, then an LLM verifies split points, aiming for high-quality chunks with reduced token usage and LLM costs.<p>You can see how Chonkie compares to LangChain and LlamaIndex in our benchmarks: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS.md">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS....</a><p>Some technical details about the Chonkie package:  - ~15MB default install vs. ~80-170MB for some alternatives. - Up to 33x faster token chunking compared to LangChain and LlamaIndex in our tests. - Works with major tokenizers (transformers, tokenizers, tiktoken). - Zero external dependencies for basic functionality. - Implements aggressive caching and precomputation. - Uses running mean pooling for efficient semantic chunking. - Modular dependency system (install only what you need).<p>In addition to chunking, Chonkie also provides an easy way to create embeddings. For supported providers (SentenceTransformer, Model2Vec, OpenAI), you just specify the model name as a string. You can also create custom embedding handlers for other providers.<p>RAG is still the most common use case currently. However, Chonkie makes chunks that are optimized for creating high quality embeddings and vector retrieval, so it is not really tied to the &quot;generation&quot; part of RAG. In fact, We&#x27;re seeing more and more people use Chonkie for implementing semantic search and&#x2F;or setting context for agents.<p>We are currently focused on building integrations to simplify the retrieval process. We&#x27;ve created &quot;handshakes&quot; – thin functions that interact with vector DBs like pgVector, Chroma, TurboPuffer, and Qdrant, allowing you to interact with storage easily. If there&#x27;s an integration you&#x27;d like to see (vector DB or otherwise), please let us know.<p>We also offer hosted and on-premise versions with OCR, extra metadata, all embedding providers, and managed vector databases for teams that want a fully managed pipeline. If you&#x27;re interested, reach out at shreyash@chonkie.ai or book a demo: <a href="https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo" rel="nofollow">https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo</a>.<p>We&#x27;re eager to hear your feedback and comments! Thanks!

## 综合总结
Chonkie是一个专为RAG和语义搜索设计的高性能开源Chunking库，旨在替代LangChain等笨重框架。它以轻量级（~15MB）、极速（快33倍）和零基础依赖为卖点，支持从基础Token切分到基于最新论文的Late Chunking、Slumber Chunking及AST代码切分等多种高级策略，并内置了主流Embedding模型支持和向量数据库快捷集成功能，对AI应用开发者极具工程参考与落地价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
项目聚焦RAG流程中的核心预处理环节Chunking，技术实现上不仅涵盖了基础的Token和Sentence切分，还深入集成了多篇最新学术论文的策略（如Late Chunking、Slumber Chunking），并采用AST进行代码切分。工程优化显著，通过激进缓存、预计算和Running Mean Pooling实现了比LangChain等主流框架快33倍的性能，且基础安装包仅约15MB，零外部依赖，体现了较高的工程含金量与技术深度。

### 实用性 (评分: 9.0/10)
对AI从业者（尤其是RAG和搜索开发者）具有极高的实用价值。Chunking质量直接决定RAG效果，该库提供了从基础到高级（语义、LLM验证）的一站式切分方案，且兼容主流Tokenizer和Embedding模型。此外，提供的Vector DB 'handshakes'功能极大简化了数据入向量库的流程，轻量级设计也使其极易集成到现有生产环境中，是构建AI应用的优质基础设施。

### 社区活跃度 (评分: 7.5/10)
作为YC X25的Launch HN项目，获得了151个点和42条评论，表现出较好的社区关注度。HN社区对替代LangChain等笨重框架的轻量级工具通常抱有极大热情，且该话题切中RAG开发者的痛点，容易引发关于切分策略优劣、性能对比及实际业务场景应用的深度讨论，整体热度与讨论质量处于中上水平。

## 项目链接
https://news.ycombinator.com/item?id=44225930
