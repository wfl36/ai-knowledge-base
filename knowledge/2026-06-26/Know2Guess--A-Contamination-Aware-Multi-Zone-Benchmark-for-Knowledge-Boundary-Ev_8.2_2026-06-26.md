# Know2Guess: A Contamination-Aware Multi-Zone Benchmark for Knowledge-Boundary Evaluation in Large Language Models

**评分：** 8.2  
**状态：** 正常  
**标签：** 大模型, 评估基准, 知识边界, 数据污染, 拒答, 论文  
**更新日期：** 2026-06-26  
**来源：** rss  

## 项目描述
arXiv:2606.26101v1 Announce Type: new Abstract: Reliable evaluation of large language models should separate supported answering from unsupported guessing without conflating either with data contamination, prompt idiosyncrasy, or generic refusal behavior. We present a contamination-aware, multi-zone benchmark for measuring the transition from answerable knowledge to abstention-expected unknowns under frozen build-time labels. The benchmark contains 1,200 items across five domains, explicit abstention expectations, contamination-risk metadata, and dual parsing with an official strict parser plus a normalized robustness parser. We evaluate FLAN-T5, Qwen2.5-Instruct, and Llama-3-Instruct models under locked answer-or-abstain prompts, answer-only controls, and prompt-template variants. The benchmark is not solved by generic non-answer behavior: FLAN baselines remain weak on productive abstention, while stronger instruction-tuned models expose a selective but incomplete transition from answering to abstaining. Qwen2.5-3B-Instruct achieves the best overall reliability, but answer-expected zones remain difficult, calibration remains poor, and benign-item refusal persists. Prompt and parser robustness analyses preserve the main ranking and qualitative conclusions. The benchmark therefore provides a reproducible protocol for auditing answerability, abstention, refusal, and contamination as distinct but interacting dimensions of LLM reliability.The dataset is publicly available at https://github.com/renweimeng/Know2Guess-A-Contamination-Aware-Multi-Zone-Benchmark.

## 综合总结
本文提出了Know2Guess，一个感知数据污染的多区域基准测试，旨在解耦评估大语言模型的可回答性、预期弃权、拒绝行为与数据污染问题。该基准包含1200个跨五个领域的条目，配备污染风险元数据和双重解析器。对多个主流模型的实验表明，现有模型在主动弃权上表现不佳，校准较差且存在良性拒绝现象，其中Qwen2.5-3B-Instruct整体可靠性最佳。该工作为审计LLM可靠性和知识边界提供了可复现的评估协议与开源工具。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究在LLM评估方法论上具有较高深度，创新性地将‘可回答知识’与‘预期弃权未知’的过渡进行解耦，并严格区分了数据污染、提示特异性和通用拒绝行为的干扰。提出的多区域基准与双重解析器（严格+鲁棒）设计严谨，实验充分揭示了当前指令微调模型在‘主动弃权’上的选择性缺陷及校准问题。

### 实用性 (评分: 8.0/10)
对LLM开发者和评估者具有极高的实操参考价值。基准测试及代码已开源，提供了一套可复现的评估协议，能直接用于审计模型的‘知识边界’、‘拒答能力’及‘数据污染’情况，有效指导模型对齐和安全微调实践，帮助解决模型‘幻觉’与‘过度拒绝’的平衡难题。

### 社区活跃度 (评分: 8.0/10)
话题高度契合当前大模型社区对‘知识边界’、‘幻觉’及‘诚实性’的关注热点。论文来源于arXiv且附带开源数据集，增强了其权威性与可验证性。评估对象涵盖FLAN-T5、Qwen2.5与Llama-3等主流模型，结论对社区具有广泛的参考和警示意义。

## 项目链接
https://arxiv.org/abs/2606.26101
