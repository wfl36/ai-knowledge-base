# Design and Validation of a Lightweight 1D CNN for Affective Touch Classification in Soft Plush Companions

**评分：** 7.7  
**状态：** 正常  
**标签：** 边缘AI, 情感计算, 人机交互, 轻量级模型, 触觉感知, 论文, 工程实践  
**更新日期：** 2026-07-21  
**来源：** rss  

## 项目描述
arXiv:2607.16196v1 Announce Type: new Abstract: Soft, sensorized companions offer a physically safe and emotionally intuitive interface for socially assistive technologies, yet their deformability and multichannel tactile sensing complicate the robust interpretation of human affect. This study presents a complete open-source MATLAB-based framework for the development and validation of compact deep learning models for affective touch recognition in soft interactive companions. As a primary contribution, a diverse FAIR-compliant dataset of 1326 labelled gesture sequences collected from 25 participants spanning children, teenagers, and adults is made publicly available, providing a reusable resource for future research in affective touch recognition. Through systematic architecture and hyperparameter exploration across 468 CNN models, the study identifies compact dilated one-dimensional convolutional neural networks (1D CNNs) as the most effective solution, with a 13.2k-parameter model achieving 75% test accuracy and 85% mean leave-one-subject-out cross-validation accuracy. Theoretical inference-time analysis shows that quantized deployment requires 3.2 MMAC per window, compatible with 20 Hz real-time operation on the target microcontroller. PC-based real-time simulation with the physical toy streaming sensor data demonstrates that the CNN resolves subtle social touches that the previous heuristic system failed to detect, whereas high-force negative interactions are captured more reliably by trivial threshold-based logic. The resulting hybrid inference pipeline - instantaneous heuristic filtering followed by CNN-based nuanced gesture classification - is proposed as the embedded deployment strategy. The study demonstrates that emotionally meaningful, privacy-preserving touch interpretation is computationally feasible for direct embedding within soft therapeutic companions, with hardware integration addressed in a forthcoming study.

## 综合总结
本文提出了一种面向软体交互伴侣情感触摸识别的轻量级1D CNN及开源MATLAB框架。研究构建了包含25名参与者的1326个手势序列的FAIR合规数据集，通过系统化架构探索，确定了13.2k参数的扩张1D CNN模型（测试准确率75%，LOSOCV准确率85%）。该模型量化部署仅需3.2 MMAC/窗口，支持微控制器实时运行。研究进一步提出‘启发式过滤+CNN分类’的混合推理流水线，有效弥补了传统启发式系统在微妙社会触摸检测上的不足，验证了隐私保护下情感触摸识别在边缘设备端直接嵌入的计算可行性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 7.5/10)
研究在技术深度和严谨性上表现扎实，通过468个CNN模型的系统化超参数与架构探索，确定了紧凑型扩张1D CNN为最优解。虽然1D CNN和模型量化本身是成熟技术，但将其与启发式逻辑结合提出混合推理流水线，有效解决了高力度与微妙触摸的分类边界问题，在边缘计算约束下实现了情感触摸的细粒度识别，论证过程完整且具有工程深度。

### 实用性 (评分: 8.5/10)
对从业者的实际落地指导价值极高。研究不仅开源了MATLAB框架和包含多年龄段的FAIR合规触摸数据集，还给出了明确的微控制器部署指标（3.2 MMAC/窗口，20Hz实时运行）。提出的‘启发式过滤+CNN细粒度分类’混合部署策略，为软体机器人、智能玩具和社交辅助设备的边缘AI开发提供了可直接复用的工程范式。

### 社区活跃度 (评分: 7.0/10)
情感计算与人机交互（HRI）是当前AI落地的重要细分领域，该研究针对软体伴侣的触觉感知这一具体痛点，具有较好的时效性。论文提供了详实的数据集和开源承诺，来源可信度高；但由于其应用场景相对垂直，且未涉及大模型等当前广泛热点，在更广泛的AI社区中影响力可能受限，主要受众为边缘AI与交互系统开发者。

## 项目链接
https://arxiv.org/abs/2607.16196
