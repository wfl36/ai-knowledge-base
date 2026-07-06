# Zackriya-Solutions/meetily

**评分：** 8.5  
**状态：** 正常  
**标签：** 语音识别, NLP, Rust, 会议助手, 语音转文字, 文本摘要, 隐私保护, 本地部署, 高质量, 开源  
**更新日期：** 2026-07-06  
**来源：** github  

## 项目描述
Privacy first, AI meeting assistant with 4x faster Parakeet/Whisper live transcription, speaker diarization, and Ollama summarization built on Rust. 100% local processing. no cloud required. Meetily (Meetly Ai -https://meetily.ai) is the #1 Self-hosted, Open-source Ai meeting note taker for macOS & Windows.

## 综合总结
Meetily 是一款主打隐私优先的开源 AI 会议助手，基于 Rust 构建了 100% 本地化的处理流水线。它整合了 Whisper/Parakeet 实现高速实时转录与说话人分离，并利用 Ollama 生成会议摘要，完美规避了云端数据泄露风险。项目直击会议记录与隐私保护的刚需痛点，工程整合度极高，在开源社区获得了极高的关注度与认可，是替代商业 SaaS 会议助手的优秀开源方案。

## 技术栈
- Rust

## 分析摘要
### 技术先进性 (评分: 8.0/10)
项目基于 Rust 构建，具备天然的内存安全与高性能优势。技术栈整合了 Parakeet/Whisper 实现了 4 倍速的实时语音转录，并结合了说话人分离技术，在会议场景下技术针对性极强。同时，通过集成 Ollama 实现端侧 LLM 摘要，打造了完全本地化的端到端 AI 处理流水线。虽然底层模型非自研，但在工程优化、推理加速与本地化部署整合方面展现了较高的技术先进性。

### 实用性 (评分: 9.0/10)
实用性极高。会议记录是高频刚需场景，而数据隐私是企业及个人用户的核心痛点。Meetily 主打 100% 本地处理、无需云端，彻底解决了会议数据外泄的担忧。支持 macOS 和 Windows 双平台，自托管且开源，相比高昂的商业 SaaS 会议助手（如 Otter、Fireflies），不仅零成本且数据自主可控，应用价值和解决问题能力突出。

### 社区活跃度 (评分: 8.5/10)
项目在 GitHub 上已获得近 2 万 Star 和接近 2 千 Fork，显示出极高的社区关注度和用户认可度。庞大的 Fork 基数也表明有大量开发者参与二次开发或私有部署。尽管今日 Star 增长为 0（可能处于稳定期或统计节点特征），但整体社区体量已证明其拥有活跃的生态基础和良好的传播度。

## 项目链接
https://github.com/Zackriya-Solutions/meetily
