# OpenRTLSet: A Fully Open-Source Dataset for Large Language Model-based Verilog Module Design

**评分：** 8.8  
**状态：** 正常  
**标签：** 大模型, EDA, Verilog, 硬件设计, 代码生成, 数据集, 论文, 开源项目  
**更新日期：** 2026-06-10  
**来源：** rss  

## 项目描述
arXiv:2606.10285v1 Announce Type: new Abstract: OpenRTLSet introduces the largest fully open-source dataset for hardware design, offering over 131,000 diverse Verilog code samples to the research community and industry. Our dataset uniquely combines Verilog code from GitHub repositories (102k modules), VHDL translations (5k modules), and synthesizable C/C++ translations (24k modules), all freely accessible without proprietary restrictions. Using the reasoning model DeepSeek-R1, we generated paired natural language descriptions for each code sample, enabling fine-tuning of various language model families (e.g., Qwen and Granite) for Verilog code generation. Our dataset explores multiple options, including Verilator-generated C++ files as additional context during labeling, quantization techniques (INT4 vs. BF16), and performance differences across model sizes (7B-32B parameters). OpenRTLSet demonstrates that open-source approaches can achieve superior performance in hardware design tasks, establishing a new foundation for accessible research and commercial use in this domain.

## 综合总结
OpenRTLSet 是目前最大的全开源硬件设计数据集，包含超13.1万个Verilog代码样本，涵盖GitHub原始代码、VHDL及C/C++翻译。该研究创新性地利用DeepSeek-R1为代码生成配对的自然语言描述，并系统探索了Verilator上下文辅助、模型量化及不同参数规模对Verilog代码生成性能的影响。此数据集无版权限制，为LLM在EDA和硬件设计领域的微调与落地提供了关键基础设施，证明了开源方案在该领域的巨大潜力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
该研究在LLM for EDA领域展现了较高的技术深度与创新性。首先，构建了目前最大规模（13.1万样本）的全开源Verilog数据集，并创新性地融合了多源异构数据（Verilog, VHDL, C/C++）；其次，引入推理模型DeepSeek-R1生成高质量的自然语言-代码对，提升了数据标注的语义深度；最后，系统性地探索了Verilator C++上下文辅助、量化技术（INT4 vs BF16）及不同参数规模（7B-32B）对生成性能的影响，实验设计严谨且全面。

### 实用性 (评分: 9.0/10)
对从业者具有极高的落地指导价值。数据集完全开源且无版权限制，直接解决了当前硬件设计领域训练数据匮乏和闭源的痛点。研究不仅提供了微调数据，还验证了Qwen、Granite等主流开源模型家族在Verilog生成任务上的适配性及量化部署方案，芯片设计公司和EDA研发人员可直接利用该数据集和实验结论进行模型微调和工业级应用探索。

### 社区活跃度 (评分: 9.0/10)
话题处于LLM代码生成与EDA交叉领域的前沿，时效性极强。作者团队包含UIUC Deming Chen等EDA领域知名学者，权威性与可信度高。作为目前该领域最大的开源数据集，OpenRTLSet填补了社区基础设施的空白，有望成为后续Verilog代码生成研究的标准Benchmark，对开源社区和商业界的影响力巨大。

## 项目链接
https://arxiv.org/abs/2606.10285
