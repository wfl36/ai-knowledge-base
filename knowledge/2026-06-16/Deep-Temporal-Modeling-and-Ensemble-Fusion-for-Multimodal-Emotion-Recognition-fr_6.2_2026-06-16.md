# Deep Temporal Modeling and Ensemble Fusion for Multimodal Emotion Recognition from Physiological Signals

**评分：** 6.2  
**状态：** 正常  
**标签：** 多模态, 情感计算, 生理信号, 时序模型, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.15026v1 Announce Type: new Abstract: Physiological stress and emotion recognition are important for health monitoring and affective computing. In this work, we present a comprehensive evaluation of deep learning models such as Long Short-Term Memory (LSTM), Temporal Convolutional Networks (TCN), and Transformer on the WESAD dataset for multimodal affect recognition using wrist and chest sensor signals. We perform ablation studies to assess the individual contributions of each modality by training models on wrist-only and chest-only inputs. In addition, we implement a late-fusion ensemble strategy that combines predictions from all three architectures trained on multimodal input. We also employ early fusion at the sensor level by concatenating wrist and chest signals before feeding them into each model. Our results show that Transformer models consistently achieve the highest accuracy in multimodal settings, while TCN models perform best in the wrist-only configuration. The ensemble method yields the highest overall accuracy (98.91 +/- 0.13%) and macro-F1 score (98.56 +/- 0.17%). These findings demonstrate the effectiveness of sensor fusion and ensemble-based fusion in developing robust systems for physiological emotion recognition.

## 综合总结
本文在WESAD数据集上对比了LSTM、TCN和Transformer在生理信号情感识别中的表现，并引入早期传感器融合与晚期集成融合策略。结果显示Transformer在多模态设置下表现最佳，TCN在单手腕传感器下领先，而结合三种模型的晚期集成方法达到了98.91%的最高准确率和98.56%的宏F1分数，证明了多模态融合与模型集成的有效性。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 6.0/10)
本文系统评估了LSTM、TCN和Transformer三种主流时序模型在生理信号情感识别中的表现，并对比了早期传感器融合与晚期集成融合策略，实验设计完整且消融研究详尽。但在模型架构和融合机制上缺乏根本性创新，属于现有成熟方法的组合与基准测试，且在WESAD这一较小规模数据集上达到98.91%的准确率，存在过拟合的嫌疑。

### 实用性 (评分: 6.5/10)
为可穿戴设备与情感计算领域的从业者提供了不同模型与融合策略在WESAD数据集上的详尽基准对比，对工程选型（如手腕端轻量化模型选TCN，多模态选Transformer）具有实际参考价值。但实验室受控环境下的极高指标在真实复杂场景中的泛化能力仍有待验证。

### 社区活跃度 (评分: 6.0/10)
生理信号情感识别是数字健康和情感计算的持续热点。本文作为arXiv预印本，作者团队具有一定学术背景，但所用方法较为常规，且在经典小数据集上刷得极高指标，虽能引起一定关注，但整体学术影响力和颠覆性有限。

## 项目链接
https://arxiv.org/abs/2606.15026
