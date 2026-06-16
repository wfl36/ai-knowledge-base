# PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions

**评分：** 9.0  
**状态：** 正常  
**标签：** Agent, 手机自动化, GUI, 基准测试, 论文  
**更新日期：** 2026-06-16  
**来源：** rss  

## 项目描述
arXiv:2606.14832v1 Announce Type: new Abstract: Phone agents are increasingly expected to complete real mobile workflows rather than merely predict the next screen action. However, much of the current mobile-agent literature still evaluates agents primarily as GUI controllers that observe a screen, emit taps and swipes, and are scored by target app state. Real phone-use tasks are broader: they require deciding when to use app GUIs, device-side commands, or structured tools, while leaving evidence that the intended side effect actually occurred. We introduce PhoneHarness, a mixed-action benchmark and execution harness for studying phone-use agents on verifiable mobile workflows. PhoneHarness runs a device-side agent loop over GUI, CLI, and host-side tool actions, combining deterministic action routing with bounded GUI delegation and auditable execution traces. Its benchmark, PhoneHarness Bench, evaluates whether agents complete tasks with observable side effects, not only whether they produce plausible final answers. On the annotated evaluation split, PhoneHarness reaches a 75.0% pass rate, outperforming the strongest non-PhoneHarness settings by 12.9 percentage points. PhoneHarness and PhoneHarness Bench therefore play distinct but mutually dependent roles: the harness makes mixed phone workflows executable, while the benchmark measures whether agents can use that harness reliably and safely. Our findings suggest that reliable phone automation depends on action-surface routing and verifiable execution, not only visual GUI control.

## 综合总结
PhoneHarness提出了一种全新的手机Agent范式，突破了传统纯GUI控制的局限，引入了混合动作（GUI、CLI、工具）路由与可验证执行机制。该研究不仅提供了一个支持确定性动作路由和可审计轨迹的执行线束，还发布了基于可观察副作用评估的PhoneHarness Bench基准。实验表明，该方法相比最强基线提升了12.9%的通过率，证明了可靠的手机自动化必须依赖动作表面路由和可验证执行，而非单一的视觉GUI控制。该成果对端侧Agent的工程实践与未来研究具有重要突破性价值。

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 9.0/10)
突破了传统手机Agent仅依赖GUI视觉控制的局限，创新性地提出混合动作表面路由（GUI/CLI/Tool）与可验证执行框架。技术架构结合了确定性路由与有界GUI委托，论证严谨，实验结果显著优于现有基线（提升12.9%），展现了极高的研究深度与前瞻性。

### 实用性 (评分: 8.5/10)
对手机自动化和Agent开发者具有极高的实践指导意义。提出的执行线束和基准测试直接针对真实工作流中的“副作用验证”痛点，为构建可靠、可审计的端侧自动化系统提供了清晰的工程实践路径和评估标准。

### 社区活跃度 (评分: 9.5/10)
发布于2026年，处于手机Agent研究的最前沿，时效性极强。作者团队阵容强大，包含多位业界与学界知名研究者，来源权威性极高。该研究直击当前手机Agent纯GUI控制的可靠性痛点，有望在社区内引发对“可验证执行”范式的广泛关注与跟进。

## 项目链接
https://arxiv.org/abs/2606.14832
