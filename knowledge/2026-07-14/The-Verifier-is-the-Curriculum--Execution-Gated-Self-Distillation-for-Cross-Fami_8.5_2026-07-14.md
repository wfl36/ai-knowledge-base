# The Verifier is the Curriculum: Execution-Gated Self-Distillation for Cross-Family Game Generation

**评分：** 8.5  
**状态：** 正常  
**标签：** 代码生成, 强化学习/RLHF, 自蒸馏, 奖励欺骗, 游戏生成, 论文  
**更新日期：** 2026-07-14  
**来源：** rss  

## 项目描述
arXiv:2607.09709v1 Announce Type: new Abstract: Post-training a code generator against a learned judge can optimize proxy features that raise the score without improving the artifact. We study the opposite signal: a deterministic, judge-free, ungameable filter -- whether a generated project launches cleanly under a headless engine (strict-launch). Under this gate, rejection-sampling self-distillation compounds out-of-family generalization. On GameCraft-Bench (mapping a natural-language brief to a complete Godot project), a 14B model (Qwen3-14B+LoRA) distilled under strict-launch raises clean generation on four unseen game families from 8.8% to 42.2% per-candidate and best-of-K coverage from 18/25 to 25/25 (the gold ceiling) over three rounds, each a significant gain (p=0.0019, p<1e-4, p<1e-4). The gain is not from merely adding data: an exactly-matched gold-duplication control regresses below the base model (5.6% vs. 8.8%, p=0.019), while a count-matched decomposition splits the round-1-to-2 jump into comparable quality (+8.8pp) and quantity (+8.5pp) channels. Most directly, rerunning the loop with only the filter swapped -- the lenient BUILD check, which passes 99.9% of generations, in place of the launch gate -- erases the gain entirely (back to base, p=1e-3 vs. the launch-gated round), isolating verifier precision rather than the optimizer. A second ungameable signal, headless execution grounding, rises monotonically across rounds and yields far more grounded candidates than gold-duplication at a matched budget (16 vs. 5), confirming the gains are functional, not launch-but-empty. Game generation is a verifiable testbed for one lesson: the verifier is the curriculum -- what it certifies is what the model learns.

## 综合总结
本文针对代码生成后训练中学习型评判模型易导致reward hacking的问题，提出使用确定性、不可作弊的执行门控（strict-launch）进行拒绝采样自蒸馏。在GameCraft-Bench上的实验表明，该方法使14B模型在未见游戏家族上的干净生成率从8.8%提升至42.2%，达到金标准上限。严谨的消融实验证实增益源于验证器的精确度而非数据量，深刻揭示了'验证器即课程'的核心规律，为解决代码生成中的奖励欺骗问题提供了突破性思路。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.2/10)
论文针对代码生成后训练中学习型评判模型易导致reward hacking的问题，创新性地提出使用确定性、不可作弊的执行门控（strict-launch）作为过滤信号进行拒绝采样自蒸馏。其研究深度体现在极其严谨的消融实验设计上：通过金标准复制控制组证明增益非来自数据增加，通过数量/质量分解量化两者贡献，通过替换宽松检查器证明增益完全源于验证器精确度而非优化器，并引入无头执行接地信号证明生成内容的功能有效性。'The verifier is the curriculum'的论断深刻揭示了模型学习机制与验证标准的本质联系。

### 实用性 (评分: 7.5/10)
该方法对代码生成、游戏开发及Agent等具备确定性执行环境的领域具有极高的落地指导价值，能有效提升生成代码的可执行性和跨族泛化能力。但其强依赖于环境提供的确定性、无头执行反馈，对于缺乏客观可执行验证标准的开放性生成任务（如创意写作、开放式问答）适用性受限，落地场景具有一定门槛。

### 社区活跃度 (评分: 8.8/10)
话题紧扣当前大模型后训练中reward hacking和代码生成的核心痛点，极具时效性。实验数据详实、论证极具说服力，'The verifier is the curriculum'这一高度凝练的论断具有成为社区经典共识的潜力，对RLHF和代码生成社区的研究方向有重要的启发和纠偏作用。

## 项目链接
https://arxiv.org/abs/2607.09709
