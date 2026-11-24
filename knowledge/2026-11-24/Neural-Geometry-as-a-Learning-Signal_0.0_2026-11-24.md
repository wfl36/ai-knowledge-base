# Neural Geometry as a Learning Signal

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-11-24  
**来源：** rss  

## 项目描述
arXiv:2611.26832v1 Announce Type: new Abstract: We investigate whether the geometric structure of neural representations can provide a sufficient learning signal for improving model behavior without any supervision on model outputs. First, we fine-tune Llama-3.1-8B to answer questions such as "What month is four months after June?" by supervising internal representations of the input month (June = 6) and offset (4), which are encoded with Fourier harmonics. Second, we fine-tune the model to predict line breaks in text wrapped to a fixed width by supervising an internal representation of the number of characters since the preceding newline, which is represented by a low-dimensional helical structure. In both tasks, we supervise a low-dimensional subspace of the residual stream using an idealized target structure, and find that internal geometric supervision achieves similar performance to standard fine-tuning (despite no supervision on outputs). Moreover, we find that simply patching in an ideal geometry is not sufficient to recover fine-tuning performance, and thus demonstrate geometric supervision provides beneficial effects beyond the representations it targets. Together, these findings show how mechanistic understanding of neural geometry can be leveraged to shape the behavior of neural networks.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2611.26832
