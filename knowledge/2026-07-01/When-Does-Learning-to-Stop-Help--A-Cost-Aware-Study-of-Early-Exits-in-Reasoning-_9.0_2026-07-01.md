# When Does Learning to Stop Help? A Cost-Aware Study of Early Exits in Reasoning Models

**评分：** 9.0  
**状态：** 正常  
**标签：** 推理模型, 推理优化, 早退机制, 成本感知, 论文, 实证研究  
**更新日期：** 2026-07-01  
**来源：** rss  

## 项目描述
arXiv:2606.30852v1 Announce Type: new Abstract: Reasoning models spend different amounts of useful computation across instances, but it remains unclear when a learned stopping rule improves over simple confidence or convergence thresholds. We study this question with LearnStop, a hidden-state-free checkpoint stopper for reasoning language models. At fixed budget checkpoints, LearnStop probes a short answer from the current reasoning prefix and predicts prefix correctness from online features such as answer confidence, entropy, prefix vote share, answer stability, and backtracking-marker density. Across 18 task-model settings spanning GSM8K, MATH-500, MMLU-Pro, AIME-90, GPQA, Qwen3, and DeepSeek-R1 distillations, the answer is task-dependent. On free-form math, learned multi-feature stopping improves the fixed-budget frontier and often beats scalar exits: on GSM8K with Qwen3-32B, the empirical frontier reaches a post-hoc peak adapt gain of +0.157, validation-selected operating points preserve positive gains, and the paired gain over the strongest scalar baseline is +0.028. On multiple-choice and very hard settings, scalar confidence, entropy, or stability rules are competitive or stronger. We therefore frame learned stopping not as a universal replacement for scalar exits, but as a tool whose value depends on trajectory structure. We further provide validation-selected operating points, paired bootstrap tests, finite-grid lost-correct risk calibration, cost accounting under KV-fork, prefix-cache, and black-box regimes, H100 serving profiles, checkpoint-schedule sweeps, transfer analyses, and robustness checks. The main practical finding is that learned stopping is useful when many questions become correct before full budget but do not exhibit a single reliable scalar stopping signal; its benefits largely disappear when confidence or answer convergence already solves the stopping problem.

## 综合总结
本文研究了推理模型中的早退机制，提出LearnStop检查点停止器，并在18个任务-模型设置下进行了全面评估。研究发现，学习停止规则并非标量规则的通用替代品：它在自由形式数学任务中能显著提升固定预算前沿，但在多选题和极难任务中不如简单的标量规则。该研究为推理模型降本提供了明确的工程指导，指出学习停止仅在缺乏单一可靠标量信号的场景下具有优势。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.8/10)
针对推理模型早退机制，提出LearnStop（基于在线特征的无隐藏状态检查点停止器）。研究深度体现在通过18个任务-模型设置的详尽实验，打破了学习停止规则普遍优于简单标量阈值的假设，明确界定了其适用边界：在自由形式数学任务中有效，但在多选题或极难任务中不如标量规则。论证严谨，包含大量校准、成本核算和鲁棒性检验。

### 实用性 (评分: 9.2/10)
对大模型推理降本具有极高的工程落地价值。不仅提供了具体的LearnStop实现方案，还给出了不同任务类型下的最佳实践指导（何时用学习停止，何时用标量规则），并附带了H100服务配置分析和不同KV缓存机制下的成本核算，直接指导工业界推理服务优化。

### 社区活跃度 (评分: 9.0/10)
话题紧扣当前大模型长推理成本高昂的痛点，时效性极强。作者团队包含顶尖学府研究者，实验规模庞大且分析客观，结论对社区纠正“通用学习停止”的盲目预期具有重要参考价值，可信度高。

## 项目链接
https://arxiv.org/abs/2606.30852
