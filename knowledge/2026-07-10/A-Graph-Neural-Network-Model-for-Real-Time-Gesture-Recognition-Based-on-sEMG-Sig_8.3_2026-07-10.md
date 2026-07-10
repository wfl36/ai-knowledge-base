# A Graph Neural Network Model for Real-Time Gesture Recognition Based on sEMG Signals

**评分：** 8.3  
**状态：** 正常  
**标签：** 图神经网络, sEMG, 手势识别, 人机交互, 信号处理, 论文  
**更新日期：** 2026-07-10  
**来源：** rss  

## 项目描述
arXiv:2607.07850v1 Announce Type: new Abstract: For seemless control of advanced hand prostheses and augmented reality, accurate and immediate hand gestures recognition is essential. Surface electromyography (sEMG) signals obtained from the forearm are commonly employed for this purpose. In this paper, we present a novel approach for sEMG representation that utilizes graph networks which contain information about muscle activation patterns in the forearm. Based on these graph networks, we have developed a machine learning algorithm capable of real-time hand gesture recognition using a graph neural network. The algorithm's performance was evaluated using sEMG signals acquired from myoband, which has 8 electrodes placed around the forearm, involving 8 healthy subjects. The proposed method demonstrated an average classification accuracy of 99\%, surpassing the performance of state-of-the-art techniques. The average time for both graph construction and prediction stood at 48ms utilizing a M1 pro CPU, rendering the approach well-suited for real-time applications.

## 综合总结
本文提出了一种基于图神经网络（GNN）的sEMG信号实时手势识别方法，通过图结构表征肌肉激活模式。该方法在8名健康受试者测试中达到99%的平均准确率，超越现有SOTA，且在M1 Pro CPU上端到端延迟仅48ms，具备极强的实时性和落地潜力，非常适用于假肢控制与AR等人机交互场景。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
将图神经网络（GNN）引入sEMG信号处理，通过图结构表征前臂肌肉激活模式，方法具有新颖性；在8名受试者上达到99%准确率，技术论证较为扎实，但未明确说明是否为跨受试者泛化测试，这在sEMG领域是关键的严谨性考量。

### 实用性 (评分: 9.0/10)
算法在M1 Pro CPU上端到端延迟仅48ms，满足实时应用严苛要求；对假肢控制、AR等人机交互领域的从业者具有极高的工程参考价值，硬件门槛低，落地路径清晰。

### 社区活跃度 (评分: 7.5/10)
sEMG与GNN结合是生物电信号处理的前沿探索方向，话题具有时效性；但99%的极高准确率在sEMG领域常受跨受试者泛化性质疑，来源为arXiv预印本，权威性有待同行评审进一步确认。

## 项目链接
https://arxiv.org/abs/2607.07850
