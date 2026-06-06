# Uncertainty Aware Functional Behavior Prediction and Material Fatigue Assessment for Circular Factory

**评分：** 8.0  
**状态：** 正常  
**标签：** 预测性维护, 不确定性量化, 循环制造, 物理信息融合, 时序预测, 论文, 工程实践  
**更新日期：** 2026-06-06  
**来源：** rss  

## 项目描述
arXiv:2606.05334v1 Announce Type: new Abstract: Returned products in circular factories re-enter production with heterogeneous degradation states, usage histories, and remaining capability. Reuse cannot be decided from the current inspection alone, because future function fulfillment and component integrity may evolve differently under the next service scenario. Existing PHM approaches support degradation prediction, but often target fixed operating conditions or isolated component benchmarks, while material-fatigue assessment is rarely linked to system-level functional prognosis. This paper addresses this gap for an angle grinder by combining uncertainty-aware functional prediction with component-level fatigue assessment in an instance-specific reliability workflow. The proposed framework combines the current tool state with recent force--torque usage windows. A convolutional encoder extracts loading patterns from spindle forces and shaft torque, and an LSTM backbone predicts nine functional variables as Gaussian mean and variance estimates. In parallel, the same loading history is translated into output-shaft fatigue information through finite-element-supported stress reconstruction, S--N/Miner damage evaluation with Haibach extension, and Paris-law crack-growth analysis. A streaming replay algorithm consolidates both branches into functional, material, and system reliability trajectories. Held-out tests show mean \(2\%\)-tolerance accuracy of 0.9652 across nine outputs. Thermal variables are predicted near-perfectly, while drive motor current and load speed remain the most demanding dynamic outputs, with \(R^2\) values of 0.9750 and 0.9924. Torque history is especially important for these variables, and the conventional LSTM outperforms GRU and xLSTM in the short-history setting. Reliability calibration is most informative for drive motor current, where predicted and observed exceedance probabilities ...

## 综合总结
本文针对循环工厂中回收产品再利用的可靠性评估问题，提出了一种融合不确定性感知功能预测与材料疲劳评估的实例化框架。该框架利用CNN和LSTM从力-扭矩历史中预测功能变量的高斯分布，同时结合有限元应力重构与疲劳裂纹分析，最终通过流式回放算法生成系统级可靠性轨迹。实验在角磨机上验证了其高精度（2%容差精度0.9652），并发现传统LSTM在短历史设定下优于GRU/xLSTM，为工业设备的预测性维护和循环再利用提供了极具价值的工程实践指导。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.0/10)
论文提出了一种结合不确定性感知的深度学习与物理有限元分析的创新框架，解决了循环工厂中系统级功能预测与组件级材料疲劳评估脱节的问题。技术深度体现在将CNN+LSTM提取的力-扭矩特征与高斯分布预测（均值与方差）相结合，并平行引入S-N/Miner损伤评估及Paris-law裂纹生长分析，最后通过流式回放算法融合双分支轨迹。论证严谨，实验结果详实（9个输出变量平均2%容差精度达0.9652），且对比了LSTM、GRU与xLSTM在短历史设定下的表现，证明了方法的有效性。

### 实用性 (评分: 8.5/10)
对工业界和制造业从业者具有极高的落地参考价值。该框架为旋转机械（如角磨机）在异质退化状态下的实例化可靠性评估提供了端到端的工作流，直接指导了“如何判断回收产品能否再次投入使用”的实际痛点。方法可复用性强，物理模型与数据驱动模型的结合方式可推广至其他工业设备的预测性维护与寿命评估中，适用范围明确且落地路径清晰。

### 社区活跃度 (评分: 7.5/10)
话题契合当前循环经济与可持续制造的时效性热点，来源为arXiv预印本，作者团队背景扎实（涉及卡尔斯鲁厄理工学院等知名机构）。虽然在主流AI社区（如大模型）中关注度有限，但在工业AI、PHM（故障预测与健康管理）及智能制造细分领域具有较高的权威性和潜在影响力。

## 项目链接
https://arxiv.org/abs/2606.05334
