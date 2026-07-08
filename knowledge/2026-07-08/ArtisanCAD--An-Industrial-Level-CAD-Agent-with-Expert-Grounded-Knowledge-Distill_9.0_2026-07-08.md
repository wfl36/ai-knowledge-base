# ArtisanCAD: An Industrial-Level CAD Agent with Expert-Grounded Knowledge Distillation

**评分：** 9.0  
**状态：** 正常  
**标签：** Agent, CAD, 知识蒸馏, 工业设计, MCP, 论文  
**更新日期：** 2026-07-08  
**来源：** rss  

## 项目描述
arXiv:2607.05750v1 Announce Type: new Abstract: Computer-aided design (CAD) for industrial components requires long-horizon procedural modeling, robust feature dependencies, editable parametric geometry, and production-grade B-Rep execution. Existing text-to-CAD methods have made promising progress in generating CAD programs from natural-language descriptions, but they still struggle when user prompts are ambiguous, underspecified, or only describe high-level design intent. They also rarely exploit expert procedural knowledge naturally available in industrial workflows, such as CATIA operation recordings, macro logs, drawing notes, and engineering descriptions. We present \algname, a skill-guided industrial CAD agent with expert-grounded knowledge distillation. The core of \algname is CAD intermediate representation (CAD-IR), an executable procedural representation that encodes parameters, ordered operations, MCP tool bindings, dependencies, generated entities, and verification rules. CAD-IR plays two key roles: it first serves as the carrier for distilling expert CAD procedures into reusable parameterized skills; then it provides a procedural scaffold that turns vague or intermediate-level prompts into complete executable CAD operations. \algname retrieves expert-derived skills, instantiates and revises CAD-IR, executes the resulting procedure through a dedicated CATIA-MCP backend, and uses multi-view visual feedback for iterative refinement, and finally generates production-ready B-Rep models. On the Text2CAD benchmark, CAD-IR improves generation from intermediate prompts by reducing mean Chamfer Distance from $14.83$ to $9.88$, showing its ability to bridge ambiguous textual intent and executable CAD construction. On four complex automotive components, CAD-IR enables expert CATIA recordings to be distilled into reusable skills, allowing \algname to generate editable CATIA-native B-Rep models for new variant requests.

## 综合总结
本文提出ArtisanCAD，一种基于专家知识蒸馏的工业级CAD Agent。针对现有Text-to-CAD方法难以处理模糊提示且缺乏工业专家知识的问题，核心引入了CAD中间表示(CAD-IR)，不仅作为蒸馏专家操作记录为可复用技能的载体，还作为将模糊意图转化为可执行操作的过程脚手架。结合CATIA-MCP后端执行与多视角视觉反馈迭代，ArtisanCAD在Text2CAD基准上显著降低了Chamfer Distance（14.83降至9.88），并在复杂汽车部件上成功生成了可编辑的生产级B-Rep模型，展现了极强的工业落地潜力。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
本文在技术深度与新颖性上表现突出。针对现有Text-to-CAD方法难以处理模糊/高层意图及缺乏工业专家知识的痛点，创新性地提出了CAD中间表示(CAD-IR)，它不仅编码了参数和操作顺序，还整合了MCP工具绑定与验证规则。CAD-IR的双重角色设计（先作为知识蒸馏载体，后作为执行脚手架）极具洞见，有效弥合了自然语言模糊性与CAD建模严谨性之间的鸿沟。结合多视角视觉反馈的迭代优化机制，论证严谨，实验数据支撑有力（Chamfer Distance显著降低）。

### 实用性 (评分: 9.5/10)
对从业者的实际参考价值极高。该工作直接对接工业级软件CATIA，利用企业自然沉淀的操作记录和宏日志进行知识蒸馏，非常契合工业界现状。生成的模型为生产级、可编辑的B-Rep原生模型，能够直接响应变体设计需求，打通了从自然语言到专业工业软件操作的闭环。其Agent架构（检索-实例化-执行-反馈）为制造业和CAD领域的AI落地提供了清晰的工程实践指南。

### 社区活跃度 (评分: 8.5/10)
话题时效性强，契合当前AI Agent与MCP工具调用协议的前沿趋势。将大模型能力引入传统工业CAD领域具有极高的行业影响力和应用前景。作者团队具备明显的工业界背景（涉及汽车复杂部件与CATIA深度结合），来源权威性与可信度高。该成果有望在CAD/CAE社区及工业AI领域引发广泛关注。

## 项目链接
https://arxiv.org/abs/2607.05750
