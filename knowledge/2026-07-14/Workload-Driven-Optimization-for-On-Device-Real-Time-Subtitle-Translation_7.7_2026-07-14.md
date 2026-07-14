# Workload-Driven Optimization for On-Device Real-Time Subtitle Translation

**评分：** 7.7  
**状态：** 正常  
**标签：** 端侧AI, 机器翻译, 模型优化, 词表裁剪, 论文, 工程实践  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09957v1 Announce Type: new Abstract: This report studies on-device English-to-Traditional-Chinese subtitle translation for Taiwan under short inputs, short outputs, batch-size-one inference, low latency, and privacy constraints. These conditions limit the value of optimizations designed for long-context or high-throughput language-model serving. Starting from LMT-60-0.6B, preliminary profiling suggests that vocabulary projection becomes a more important decode-time cost after GGUF quantization reduces the relative cost of Transformer blocks. We replace the original 151k-token vocabulary with a 64k-token subtitle-domain tokenizer, migrate the embedding space, and adapt the model through embedding calibration followed by full supervised fine-tuning. On a fixed 500-example subset of the OpenSubtitles2024 test set, the LocalSubs achieves a 59.2% tie-excluded win rate against Google Translate under GPT-4o pairwise judging. Performance is strongest on short cues and declines as cue length increases. Preliminary Apple M2 Metal measurements on a 64k-vocabulary model show a 1.63$\times$ speedup over a 151k-vocabulary profiling baseline. The raw benchmark configuration is incomplete, so the latency result is treated as preliminary.

## 综合总结
本文针对端侧实时英译中字幕翻译场景，发现GGUF量化后词表投影成为解码瓶颈。作者通过将原151k词表替换为64k领域专用分词器、迁移嵌入空间并进行校准与SFT，在短字幕上以59.2%的胜率击败Google Translate，并在Apple M2上实现1.63倍推理加速。该工作为端侧短上下文低延迟场景的模型轻量化与优化提供了极具实操价值的工程范式。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
针对端侧实时字幕翻译场景（短输入输出、batch-size-one、低延迟），深入剖析了GGUF量化后词表投影成为解码耗时瓶颈的现象。通过引入64k字幕领域专用分词器、迁移嵌入空间并结合嵌入校准与全量SFT，有效解决了长上下文/高吞吐优化方案在短上下文场景的失效问题。技术路径清晰且论证具有针对性，但作者也坦诚基准测试配置尚不完整，且模型在较长字幕上的性能有所衰减，深度和完备性略有局限。

### 实用性 (评分: 8.5/10)
对端侧大模型部署和实时翻译从业者具有极高的参考价值。提出的“量化分析瓶颈 -> 词表裁剪 -> 嵌入空间迁移与校准 -> 领域SFT”优化链路可直接复用于其他受限于算力、内存和延迟的端侧NLP任务。在Apple M2上实测获得的1.63倍推理加速以及超越Google Translate的胜率，证明了该方案在端侧短文本场景下的卓越落地潜力。

### 社区活跃度 (评分: 7.0/10)
端侧AI与实时翻译是当前AI社区持续关注的热点方向，结合Apple M2 Metal的实测数据具有较好的时效性和吸引力。来源为arXiv新论文，作者在文中坦诚指出了基准测试配置的不完整性，体现了较好的学术诚实度，但单一作者的预印本在权威性和广泛影响力上仍有待社区进一步验证。

## 项目链接
https://arxiv.org/abs/2607.09957
