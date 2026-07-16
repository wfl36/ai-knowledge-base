# Interventional Grounding Audits: Black-Box Premise-Dependency Tests for LLM Chain-of-Thought via Predicate Substitution

**评分：** 8.0  
**状态：** 正常  
**标签：** 大模型, 推理, CoT, 可解释性, 评估, 论文  
**更新日期：** 2026-07-16  
**来源：** rss  

## 项目描述
arXiv:2607.13069v1 Announce Type: new Abstract: Large language models produce chain-of-thought (CoT) reasoning that appears logically sound yet may not genuinely depend on its stated premises. We introduce interventional grounding audits, a black-box, step-level test of premise dependency: we intervene on a single premise by substituting its target predicate with a fresh symbol, re-run the model, and check whether each reasoning step's normalized conclusion (canonical predicate form) changes. We evaluate on ProntoQA, a synthetic multi-hop deductive reasoning benchmark with gold proof trees, where step-level premise dependencies are known. Applied to 50 ProntoQA problems with GPT-4o, our method achieves F1 = 0.806 on detecting proof-tree dependencies (F1 = 0.885 on predicate-determining dependencies; Recall = 100%), significantly outperforming a self-consistency baseline (F1 = 0.343; 95% bootstrap CIs non-overlapping). We further identify that 66% of correctly-solved problems contain at least one aligned step insensitive to a direct proof-tree dependency under consistent substitution -- all involving entity-introduction premises, a documented blind spot of the consistent-substitution evaluator -- a "right answer, wrong reasoning" signal invisible to passive methods. All audit certificates, raw outputs, and reproduction scripts are available in a public GitHub repository, and we discuss scope limits beyond formal, parsable benchmarks.

## 综合总结
本文提出了一种名为“干预性基础审计”的黑盒测试方法，通过谓词替换干预前提来检测大模型思维链是否真正依赖其陈述的前提。实验证明该方法显著优于自洽性基线，并揭示了66%正确解决的问题存在“正确答案，错误推理”的现象，即推理步骤对实体引入前提不敏感，这是传统被动方法无法发现的盲点。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 8.5/10)
提出了一种新颖的黑盒干预方法（谓词替换）来测试LLM思维链的前提依赖性，论证严谨。实验表明其在检测证明树依赖性上显著优于自一致性基线（F1 0.806 vs 0.343），并深刻揭示了模型推理中66%的'正确答案，错误推理'现象（对实体引入前提不敏感），精准切中了CoT忠实度评估的技术痛点。

### 实用性 (评分: 7.5/10)
提供了无需访问模型内部权重的黑盒测试方案，且开源了审计证书与复现脚本，对从业者评估LLM推理可靠性具有较高实践指导价值；但目前方法主要局限于形式化、可解析的推理基准（如ProntoQA），在更广泛的自然语言复杂推理场景中的适用性仍需进一步探索与扩展。

### 社区活跃度 (评分: 8.0/10)
LLM推理的忠实度与幻觉是当前AI社区的核心热点，该研究直击'CoT看似合理实则未依赖前提'的痛点，开源代码增强了结果的可信度与影响力，对推动大模型可解释性与安全评估领域的发展具有较高时效价值和启示意义。

## 项目链接
https://arxiv.org/abs/2607.13069
