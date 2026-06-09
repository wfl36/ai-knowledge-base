# Reconstructing and forecasting disease trajectories of patients with Alzheimer's disease using routine data in resource-constrained settings

**评分：** 8.2  
**状态：** 正常  
**标签：** 医疗AI, 时间序列, 神经ODE, 阿尔茨海默病, 疾病轨迹预测, 论文  
**更新日期：** 2026-06-09  
**来源：** rss  

## 项目描述
arXiv:2606.07798v1 Announce Type: new Abstract: Alzheimer's disease is a progressive neurodegenerative disorder, and its progression varies substantially across patients. Existing work aims to forecast patients' future cognitive state, with minimal focus on reconstructing the state from past visits. Furthermore, in current research, quantifying predictive uncertainty remains underexplored and relies on costly modalities such as MRI, PET, and CSF, limiting their deployment in resource-limited settings. In this research, our primary objectives are: First, bidirectional prediction of cognitive scores from irregular visits to present the complete disease trajectory. Second, to enable interpolation and extrapolation capabilities to assist clinicians in informed prognostic decision making, and third, to provide a well-calibrated uncertainty estimate for all predictions, and finally, to achieve the objectives using the modalities available during routine visits. We propose a unified framework, GNOVA: A GRU-Neural ODE Variational Autoencoder. The architecture combines a Gated Recurrent Unit encoder and a Neural ODE decoder within a variational autoencoder framework. In our work, we forecast the CDR-SB and MMSE Scores. The GRU encoder allows for any number of inputs at any time point. The Neural-ODE decoder performs continuous estimation, allowing interpolation and extrapolation at any desired time point. The Variational autoencoder allows for uncertainty estimation in predictions. We worked with 1,727 patients from the ADNI dataset over 10 years; the model achieved mean absolute errors of 1.35 and 2.28 for CDR-SB and MMSE scores, respectively, without requiring any neuroimaging or biomarker data. Feature-ablation studies revealed that age, BMI, and APOE4 status were strong predictors. The proposed framework enables the reconstruction of incomplete patient histories and the anticipation of future cognitive states.

## 综合总结
本文提出GNOVA框架，结合GRU、Neural ODE与VAE，实现对阿尔茨海默病认知评分的双向预测与不确定性量化。该研究最大亮点在于摆脱了对昂贵神经影像和生物标志物的依赖，仅使用常规临床数据即可在ADNI数据集上取得优异表现，为资源受限环境下的AD临床辅助决策提供了高可落地的解决方案。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
创新性地将GRU、Neural ODE与变分自编码器(VAE)结合，提出GNOVA框架。GRU编码器处理不规则离散时间序列输入，Neural ODE解码器实现连续时间维度上的任意时刻插值与外推，VAE则提供预测的不确定性量化。技术组合巧妙且契合医疗时序数据痛点，消融实验也严谨地揭示了关键预测特征。

### 实用性 (评分: 9.0/10)
极具临床落地价值。打破了AD预测对昂贵MRI/PET/CSF数据的依赖，仅依赖常规随访数据（如年龄、BMI、APOE4）即可实现疾病轨迹的重建与预测，特别适用于基层和资源受限的医疗环境，为AD筛查和预后决策提供了低成本、高可用的辅助工具。

### 社区活跃度 (评分: 7.5/10)
阿尔茨海默病轨迹预测是医疗AI的持续热点，本文针对低成本预测和不确定性量化等前沿需求，具有较高时效性。基于权威ADNI数据集验证，结果可信度高，但作为arXiv预印本尚未经过同行评审，权威性有待进一步提升。

## 项目链接
https://arxiv.org/abs/2606.07798
