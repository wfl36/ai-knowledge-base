# Small edits, large models: How Wikipedia advocacy shapes LLM values

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 数据归因, AI对齐, 数据安全, 论文  
**更新日期：** 2026-06-25  
**来源：** rss  

## 项目描述
arXiv:2606.24890v1 Announce Type: new Abstract: Can a small group of volunteers shape how AI systems discuss animal welfare, just by editing Wikipedia? We show that they can. Wikipedia appears in nearly every major language model training dataset and is weighted more heavily than web-crawled text. The Pro-Animal Wikipedians (PAW), a group of advocates who add sourced animal welfare content to relevant articles, have made 125 edits across 115 pages. Using gradient-based data attribution (Bergson; MAGIC), we traced how these edits influence language model behavior. TrackStar retrieval attribution on Llama 3.1 8B found that PAW-edited sections made up 68 percent of the highest-attributed documents for animal welfare queries (p < 0.0001) but only 52 percent for unrelated queries about the same companies (p = 0.53): the model links PAW content specifically to animal welfare topics, not to the entities in general. MAGIC counterfactual influence estimation on Llama-3.2-1B, run across five random training-order seeds, gave the same picture even more sharply: in every seed, the top-10 most influential documents on animal welfare queries were all PAW edits (10 of 10, 5 of 5 seeds), while on general queries the same top-10 sat at chance (4 to 6 of 10). Mean PAW influence exceeded mean control influence on animal welfare queries with p < 0.0001 in every seed, an effect 6 to 30 times larger than on general queries. Leave-subset-out validation gave Spearman rho = 1.00 for all 10 runs. When we fine-tuned separate models on PAW content versus control content, each model performed better specifically on the type of text it was trained on: the PAW-trained model cut perplexity on animal welfare text from 12.4 to 8.4, while the control-trained model cut perplexity on control text from 16.1 to 11.4. A small, coordinated Wikipedia editing campaign therefore measurably shapes how language models handle the topics those edits address.

## 综合总结
本研究探讨了少数志愿者是否能通过编辑维基百科来塑造AI系统在特定议题（如动物福利）上的价值观。通过追踪Pro-Animal Wikipedians (PAW)组织的125处编辑，研究利用TrackStar和MAGIC等数据归因技术在Llama模型上验证了这些编辑对动物福利查询的显著且特异性的影响（p < 0.0001），微调实验也证实了其对特定领域困惑度的改善。结果表明，小规模、有针对性的维基百科编辑活动能够切实改变大语言模型在相关话题上的行为表现，揭示了高权重训练数据对模型价值观的高杠杆效应与潜在安全风险。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
研究深度与论证严谨度极高。论文创新性地探讨了小规模、有针对性的维基百科编辑对大语言模型价值观的不成比例影响。技术层面，采用了多种先进的梯度数据归因方法（TrackStar检索归因、MAGIC反事实影响估计），在Llama 3.1 8B和Llama-3.2-1B上进行了跨随机种子的严格统计验证（p < 0.0001，Spearman rho = 1.00），并通过留一子集验证和微调困惑度对比实验，提供了坚实的因果证据，揭示了高权重数据源在LLM训练中的高杠杆效应。

### 实用性 (评分: 7.5/10)
对AI安全、对齐及数据治理从业者具有极高的实践参考价值。研究明确指出了LLM训练中维基百科等高权重数据源的脆弱性，为模型构建者防范数据投毒或进行定向价值观干预提供了明确的预警与指导；同时，该发现也为社会倡导团体提供了一条通过修改高质量公开数据源来影响AI系统输出的低成本、高收益的可操作路径。

### 社区活跃度 (评分: 8.0/10)
话题时效性与社会影响力极高。随着大模型对齐与数据治理成为焦点，'谁在塑造AI的价值观'是当前社区的核心议题。该论文直接证明了少数人可通过系统性编辑维基百科显著改变LLM在特定议题上的立场，这一结论极具话题性，极易在AI伦理、开源模型社区及公众媒体中引发关于数据可信度与AI价值观操控的广泛讨论。

## 项目链接
https://arxiv.org/abs/2606.24890
