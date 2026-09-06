# Launch HN: Chonkie (YC X25) – Open-Source Library for Advanced Chunking

**评分：** 7.5  
**状态：** 正常  
**标签：** RAG, chunking, embedding, 开源工具, Launch HN, YC X25, 向量检索  
**更新日期：** 2026-09-06  
**来源：** hackernews  

## 项目描述
Hey HN! We&#x27;re Shreyash and Bhavnick. We&#x27;re building Chonkie (<a href="https:&#x2F;&#x2F;chonkie.ai">https:&#x2F;&#x2F;chonkie.ai</a>), an open-source library for chunking and embedding data.<p>Python: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie</a><p>TypeScript: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie-ts</a><p>Here&#x27;s a video showing our code chunker: <a href="https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0" rel="nofollow">https:&#x2F;&#x2F;youtu.be&#x2F;Xclkh6bU1P0</a>.<p>Bhavnick and I have been building personal projects with LLMs for a few years. For much of this time, we found ourselves writing our own chunking logic to support RAG applications. We often hesitated to use existing libraries because they either had only basic features or felt too bloated (some are 80MB+).<p>We built Chonkie to be lightweight, fast, extensible, and easy. The space is evolving rapidly, and we wanted Chonkie to be able to quickly support the newest strategies. We currently support: Token Chunking, Sentence Chunking, Recursive Chunking, Semantic Chunking, plus:<p>-  Semantic Double Pass Chunking: Chunks text semantically first, then merges closely related chunks.<p>-  Code Chunking: Chunks code files by creating an AST and finding ideal split points.<p>-  Late Chunking: Based on the paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2409.04701</a>), where chunk embeddings are derived from embedding a longer document.<p>-  Slumber Chunking: Based on the &quot;Lumber Chunking&quot; paper (<a href="https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526" rel="nofollow">https:&#x2F;&#x2F;arxiv.org&#x2F;abs&#x2F;2406.17526</a>). It uses recursive chunking, then an LLM verifies split points, aiming for high-quality chunks with reduced token usage and LLM costs.<p>You can see how Chonkie compares to LangChain and LlamaIndex in our benchmarks: <a href="https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS.md">https:&#x2F;&#x2F;github.com&#x2F;chonkie-inc&#x2F;chonkie&#x2F;blob&#x2F;main&#x2F;BENCHMARKS....</a><p>Some technical details about the Chonkie package:  - ~15MB default install vs. ~80-170MB for some alternatives. - Up to 33x faster token chunking compared to LangChain and LlamaIndex in our tests. - Works with major tokenizers (transformers, tokenizers, tiktoken). - Zero external dependencies for basic functionality. - Implements aggressive caching and precomputation. - Uses running mean pooling for efficient semantic chunking. - Modular dependency system (install only what you need).<p>In addition to chunking, Chonkie also provides an easy way to create embeddings. For supported providers (SentenceTransformer, Model2Vec, OpenAI), you just specify the model name as a string. You can also create custom embedding handlers for other providers.<p>RAG is still the most common use case currently. However, Chonkie makes chunks that are optimized for creating high quality embeddings and vector retrieval, so it is not really tied to the &quot;generation&quot; part of RAG. In fact, We&#x27;re seeing more and more people use Chonkie for implementing semantic search and&#x2F;or setting context for agents.<p>We are currently focused on building integrations to simplify the retrieval process. We&#x27;ve created &quot;handshakes&quot; – thin functions that interact with vector DBs like pgVector, Chroma, TurboPuffer, and Qdrant, allowing you to interact with storage easily. If there&#x27;s an integration you&#x27;d like to see (vector DB or otherwise), please let us know.<p>We also offer hosted and on-premise versions with OCR, extra metadata, all embedding providers, and managed vector databases for teams that want a fully managed pipeline. If you&#x27;re interested, reach out at shreyash@chonkie.ai or book a demo: <a href="https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo" rel="nofollow">https:&#x2F;&#x2F;cal.com&#x2F;shreyashn&#x2F;chonkie-demo</a>.<p>We&#x27;re eager to hear your feedback and comments! Thanks!

## 综合总结
Chonkie 是 YC X25 孵化的轻量级开源文本分块库，主打 RAG 场景下的 chunking 和 embedding 需求。相比 LangChain、LlamaIndex 等综合框架，它以更小体积、更高速度和模块化设计为差异化卖点，支持包括代码分块、Late Chunking、Lumber Chunking 在内的多种前沿策略，并提供托管和本地部署方案。作为 RAG 工具链的基础组件，对构建自定义检索管道的开发者具有实际参考价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.0/10)
Chonkie 实现了多种 chunking 策略，包括基于 AST 的代码分块、Semantic Double Pass、Late Chunking（基于论文 2409.04701）和 Slumber/Lumber Chunking（基于论文 2406.17526），技术深度集中在分块策略的工程化实现上。技术亮点包括模块化依赖系统、aggressive caching、running mean pooling 等性能优化，以及与多种 tokenizer 的兼容性。但整体属于工程实现而非算法创新层面。

### 实用性 (评分: 8.0/10)
对 RAG 从业者有较高实用价值：相比 LangChain/LlamaIndex 体积更小（~15MB vs 80-170MB）、速度更快（声称最高 33x）、零依赖基础功能可用，且支持代码分块、语义检索、agent 上下文构建等多种 RAG 相关场景。提供 Python 和 TypeScript 双版本，托管版与本地版兼顾个人和团队需求。handshakes 集成降低了向量数据库对接成本。

### 社区活跃度 (评分: 7.5/10)
作为 YC X25 的 Launch HN，获得 151 points 和 42 条评论，属于中等偏上关注度。讨论集中在分块策略的实际效果、性能对比、与现有方案的差异化定位等实用话题，社区参与度和讨论质量尚可，但未达到爆款级别。

## 项目链接
https://news.ycombinator.com/item?id=44225930
