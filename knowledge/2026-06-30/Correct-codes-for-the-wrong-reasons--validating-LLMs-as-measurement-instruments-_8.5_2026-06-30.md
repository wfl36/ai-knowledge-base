# Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs

**评分：** 8.5  
**状态：** 正常  
**标签：** 大模型, 评估, 构念效度, 可解释性, 测量工具, 论文  
**更新日期：** 2026-06-30  
**来源：** rss  

## 项目描述
arXiv:2606.28574v1 Announce Type: new Abstract: When a large language model (LLM) codes a construct in text as a human annotator would, that agreement makes the LLM a reliable coder. Yet reliability leaves construct validity untouched. The instrument may be theory-naive, reaching the code through a correlate that meets none of the demands the construct's theory makes, and no current method tells that apart from genuine measurement. We propose grain calibration as a method that closes the gap. It decomposes a construct into clause-level components, tests each against the text with extractive evidence, and combines the results through an explicit, theory-derived rule. Because the rule is stated rather than lodged in one opaque pass, its structure is evidence about the process rather than the output. It shows which components settled a code, and, when the code is wrong, whether a component was missed or an adjacent construct mistaken for it. Validation shifts from scoring an instrument's outputs against an annotator to showing that the instrument runs on the construct its theory specifies.

## 综合总结
本文指出了大语言模型（LLM）作为测量工具时存在的“正确编码但原因错误”的问题，即高标注一致性（可靠性）掩盖了缺乏构念效度的本质。为解决此问题，作者提出“粒度校准”方法，将理论构念分解为子句级组件，结合提取式证据与显式理论规则进行验证，使评估从单纯的输出结果比对转向对推理过程的透明化检验，为LLM在严谨测量场景下的应用提供了重要的方法论突破。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
论文深刻指出了当前LLM作为测量工具时“可靠性不等于构念效度”的盲区，即模型可能通过虚假关联得出正确结果而缺乏理论支撑。提出的“粒度校准”方法通过将构念分解为子句级组件、提取证据并使用显式规则组合，实现了从黑盒输出验证到白盒过程验证的转变，理论深度和方法新颖性极高。

### 实用性 (评分: 8.0/10)
该方法为使用LLM进行文本编码、社会科学测量或自动标注的从业者提供了极具价值的实践指导。通过显式规则和组件分解，开发者可以精准定位LLM的错误来源（是遗漏组件还是构念混淆），从而有针对性地优化Prompt或系统设计，尽管实施需要一定的理论拆解成本。

### 社区活跃度 (评分: 8.5/10)
论文切中了当前LLM评估领域的核心痛点，对盲目依赖LLM标注一致性的现状提出了有力质疑。来源为arXiv预印本，话题在AI对齐、评估和社科计算领域具有高度时效性和潜在影响力，易引发学术界广泛讨论。

## 项目链接
https://arxiv.org/abs/2606.28574
