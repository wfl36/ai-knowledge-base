# NAVER LABS System Re-implementation for the IWSLT 2026 Instruction-Following Task

**评分：** 5.5  
**状态：** 待复核  
**标签：** 语音翻译, 多模态, 指令微调, 工程实践, IWSLT  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05623v1 Announce Type: new Abstract: We re-implement the NAVER LABS IWSLT 2025 instruction-following pipeline for the IWSLT 2026 Shared Task (constrained condition, short audio track), adapting it to the mandated components: SeamlessM4T-v2-large as the speech encoder and Qwen3-4B-Instruct as the LLM backbone. The three-stage approach projector alignment, text-only LoRA pre-training, and multimodal merging is preserved from the original design. We additionally construct 100k synthetic instruction-following examples across ten speech-centric task types (10k per task) from the provided corpora, suitable for further Stage 3 fine-tuning. Our primary model achieves COMET 0.781 on EN-ZH speech translation and BERTScore-F1 0.346 on English SQA on the MCIF benchmark.

## 综合总结
本文复现并适配了NAVER LABS的IWSLT 2025指令跟随流水线以参加IWSLT 2026共享任务。作者将原有的三阶段训练方法迁移至官方指定的SeamlessM4T-v2-large语音编码器和Qwen3-4B-Instruct大模型，并额外构建了10万条涵盖10种语音任务的合成指令数据。最终模型在MCIF基准上的EN-ZH语音翻译和英语SQA任务上取得了0.781 COMET和0.346 BERTScore-F1的成绩。该工作主要为工程复现与基线适配，缺乏方法论上的突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 5.5/10)
该论文是对NAVER LABS在IWSLT 2025上提出的三阶段指令微调流水线的复现与适配，技术方案（投影对齐、纯文本LoRA预训练、多模态融合）沿用了已有设计，缺乏原创性方法。其贡献主要在于将流水线适配至新指定的组件（SeamlessM4T-v2-large与Qwen3-4B-Instruct），并构建了10万条跨10种语音任务的合成指令数据，技术深度和创新性有限，属于标准的工程复现与数据扩展。

### 实用性 (评分: 6.0/10)
对参与IWSLT 2026共享任务或从事语音-文本多模态大模型微调的从业者具有较高的参考价值。论文提供了明确的基线复现流程、组件适配方法以及大规模合成指令数据的构建策略，能够直接指导相关模型的训练与落地，但适用范围受限于特定的比赛规则和语音多模态场景。

### 社区活跃度 (评分: 5.0/10)
该论文针对IWSLT 2026共享任务发布，具有较强的时效性。但作为会议共享任务的系统复现报告，其权威性和广泛影响力较弱，主要受众为参赛者和特定领域的研究者，难以在更广泛的AI社区引起显著关注。

## 项目链接
https://arxiv.org/abs/2607.05623
