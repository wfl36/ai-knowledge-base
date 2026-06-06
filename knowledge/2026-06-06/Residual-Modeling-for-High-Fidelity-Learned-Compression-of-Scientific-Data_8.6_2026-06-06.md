# Residual Modeling for High-Fidelity Learned Compression of Scientific Data

**评分：** 8.6  
**状态：** 正常  
**标签：** 科学数据压缩, 有损压缩, 残差建模, 高保真, 论文  
**更新日期：** 2026-06-06  
**来源：** rss  

## 项目描述
arXiv:2606.05389v1 Announce Type: new Abstract: Lossy compression is essential for massive spatiotemporal data from scientific simulations. Learned compressors can achieve high compression ratios at moderate accuracy targets, but their aggregate reconstruction losses do not guarantee accuracy for each block. Existing Guaranteed Autoencoder (GAE) methods add a per-block residual correction by retaining SVD/PCA-style coefficients until the target is met. This works at moderate tolerances, but in the high-fidelity regime with block-level NRMSE from 10^-6 to 10^-4, the number of retained coefficients grows quickly and the correction stream dominates the total rate. We propose a residual-centric view: the learned residual is structurally different from the original scientific field and should be coded with a representation designed for that residual. We introduce two residual coders. LBRC is a deterministic, training-free pipeline that adaptively quantizes the learned residual to the target NRMSE and losslessly encodes the resulting integer residual using 3D Lorenzo differencing, zigzag mapping, bit-plane coding, and entropy coding. NGLR adds a causal neural predictor that outputs a normalized bias for an integer-rounded Lorenzo prediction in the same deterministic integer pipeline, reducing the entropy of the remaining residual code while preserving deterministic decoding. The predictor weights are serialized and counted in the bitstream. Across E3SM, JHTDB, and ERA5 at block-level NRMSE targets from 10^-6 to 10^-4, LBRC improves compression ratio over GAE by 30-60% and is broadly competitive with SZ. NGLR adds a further 10-40% over LBRC and outperforms SZ in the evaluated high-fidelity regime. These results show that residual representations tailored to learned-compressor residuals can preserve the advantage of learned compression when global residual correction becomes rate-dominant.

## 综合总结
本文针对高保真科学数据有损压缩中残差校正流码率过高的问题，提出以残差为中心的建模视角，并设计了LBRC和NGLR两种残差编码器。LBRC通过确定性整数流水线编码学习残差，NGLR进一步引入因果神经预测器降低残差熵。实验表明，在E3SM、JHTDB和ERA5数据集的高保真区间，LBRC比GAE提升30-60%，NGLR再提升10-40%并超越传统SZ算法，有效解决了学习型压缩器在高保真区间的性能瓶颈。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文针对学习型压缩器在高保真度（NRMSE 10^-6~10^-4）科学数据压缩中残差校正流码率过高的问题，创新性地提出了以残差为中心的视角。研究指出学习残差的结构异于原始数据，需采用专用表示编码。据此提出了LBRC（基于3D Lorenzo差分和位平面编码的无训练确定性流水线）和NGLR（引入因果神经预测器降低残差熵）两种残差编码器，在保证确定性解码的同时，有效突破了高保真区间学习型压缩的性能瓶颈，论证严谨且技术深度高。

### 实用性 (评分: 8.5/10)
该研究对处理大规模科学模拟数据（如气候、流体力学）的从业者具有极高的参考价值。LBRC作为无需训练的确定性流水线，易于在现有HPC存储系统中集成；NGLR通过序列化预测器权重保证了解码端的便捷性。在E3SM、ERA5等真实数据集上的显著压缩率提升，证明了其在实际科学计算数据归档与传输中的落地潜力。

### 社区活跃度 (评分: 8.2/10)
随着AI for Science和超算的发展，海量科学数据的高保真存储成为迫切需求。本文针对传统学习型压缩器在高保真区间不敌传统算法（如SZ）的痛点，提出了有效的解决方案，在特定区间超越了SZ，具有较高的学术权威性和领域影响力，为科学数据压缩提供了新的研究范式。

## 项目链接
https://arxiv.org/abs/2606.05389
