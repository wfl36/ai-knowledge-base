# Learnable Splines for Unstructured Neural Operators

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-19  
**来源：** rss  

## 项目描述
arXiv:2610.22446v1 Announce Type: new Abstract: Neural operators approximate solution operators of partial differential equations at a fraction of the cost of numerical solvers. Efficient grid-based architectures such as the Fourier neural operator (FNO) assume uniform rectangular grids, whereas engineering simulations use large, irregular, and locally refined meshes. We introduce L-SplineFNO, a memory-efficient neural operator that couples an FNO backbone with a sparse, learnable tensor-product B-spline transfer between unstructured meshes and a latent Cartesian grid. A local normalised scatter avoids the geometry-dependent solve of analytic spline transformation while preserving compact support, partition of unity, and spline smoothness by construction. The neural operator, conditioned on global design and operating parameters, learns the mapping of geometry to the field solution. Across six three-dimensional engineering benchmarks, L-SplineFNO achieves strong predictive accuracy while requiring substantially less memory and compute than baseline operators, scaling to 26.6 million nodes in training and 46 million in inference on a single A100 GPU. It also supports zero-shot super-resolution and efficient closed-form spatial derivatives. Uniquely, the analytic spline decoder yields rigorous prediction bounds over continuous space and uncertain parameters, via Bernstein convex hulls and Taylor models, demonstrated on a 29.2-million-node MAST-U tokamak model.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2610.22446
