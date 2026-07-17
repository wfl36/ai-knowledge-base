# Token Time Continuous Diffusion for Language Modeling

**评分：** 7.5  
**状态：** 正常  
**标签：** 大模型, 扩散模型, 语言建模, 非自回归生成, 条件生成, 论文  
**更新日期：** 2026-07-17  
**来源：** rss  

## 项目描述
arXiv:2607.14106v1 Announce Type: new Abstract: In this paper we introduce token time continuous diffusion (TTCD), a new diffusion language model which (a) operates in continuous space, deterministically mapping Gaussian noise to a final token canvas with no further sampling, and crucially (b) incorporates a new notion of per-token times, with some tokens proceeding from noise to token at a faster rate than others. Continuous space modeling helps TTCD avoid the parallel sampling of multiple tokens, which is a key source of inaccuracy at high speedups for models that iterate purely in discrete space. The notion of per-token times helps TTCD to better model conditional generation, allows for more sure tokens to proceed at a faster rate, and allows for differentiated inter-token influences during refinement. TTCD outperforms discrete models at high speedups. We train a 160M parameter TTCD model on OpenWebText, and then self-distill it; we find that at high speedups we are comparable in unconditional generation quality, and outperform in conditional generation, several existing models of similar size trained, on the same data, and self-distilled. We achieve similar gains in Sudoku solving as well.

## 综合总结
本文提出了TTCD扩散语言模型，通过在连续空间操作并引入per-token times机制，解决了离散扩散模型在高加速比下的精度问题，提升了条件生成质量。在160M参数模型和数独任务上的实验表明，该方法在高加速比下优于同类离散模型，为非自回归语言建模提供了新的突破性思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了Token Time Continuous Diffusion (TTCD)模型，创新性地在连续空间进行扩散建模，并引入per-token times机制，允许不同token以不同速率去噪。这有效避免了离散空间模型在高加速比下的采样不准确性，增强了条件生成能力和token间差异化影响，理论和方法具有显著新颖性与严谨性。

### 实用性 (评分: 6.0/10)
在160M参数规模上验证了有效性，特别是在高加速比的条件生成（如数独求解）上优于同类离散扩散模型。但对于工业界大模型应用的直接指导意义尚需更大规模的验证，工程落地仍需克服连续空间映射和自蒸馏的成本问题，目前更偏向学术探索。

### 社区活跃度 (评分: 8.0/10)
扩散语言模型是当前非自回归生成的前沿探索方向，该论文发布于arXiv，作者为知名学者，具有较高的学术权威性和时效性。尽管扩散语言模型在工业界尚未成为主流，但该工作为突破自回归模型推理瓶颈提供了有价值的学术参考，易引发学术界关注与讨论。

## 项目链接
https://arxiv.org/abs/2607.14106
