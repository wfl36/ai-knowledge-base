# TutlAit v1: a crowdsourced Moroccan Tamazight speech dataset with Arabic transcriptions and regional accent labels

**评分：** 0.0  
**状态：** 待复核  
**标签：** 无  
**更新日期：** 2026-10-01  
**来源：** rss  

## 项目描述
arXiv:2609.38219v1 Announce Type: new Abstract: Tamazight (Amazigh) is, together with Arabic, one of the two official languages of Morocco, yet it remains severely under-resourced for speech technology: pub licly available labelled audio is scarce, generally lacks information on the regional variety spoken, and is often of uneven transcription quality. This article describes the TutlAit dataset, a corpus of Moroccan Tamazight speech paired with Modern Standard Arabic text and explicit regional accent labels. The data were collected with TutlAit, a purpose-built crowdsourcing web application (React 18 front end, Django 5 / Django REST Framework back-end, PostgreSQL database). Native speakers recruited through targeted LinkedIn and Instagram campaigns created an account, declared their regional variety (Atlas, Souss, Rif or other) and demographic information, and then contributed through two workflows: Text-to Audio, in which an Arabic sentence is displayed and the volunteer records its oral Tamazight rendering in the browser, and Audio-to-Text, in which a Tamazight excerpt is played and the volunteer types its Arabic transcription. A complemen tary set of segments was obtained from freely accessible Tamazight audiovisual media, segmented and annotated with ELAN and imported through a bulk CSV/ZIP pipeline. Every upload is converted server-side to 16kHz mono WAV, hashed with SHA-256 for duplicate rejection, checked for duration bounds and validated by an administrator. The dataset contains 13,384 audio files totalling 75,231 seconds (approximately 20.9 hours, about 3.01GB). The Atlas variety accounts for 9,956 files (14.08h) and the Souss variety for 3,378 files (6.75h); small Rif (22 files) and Kabyle (28 files) subsets are also included. The corpus can be reused for speech recognition, speech translation and accent identification for Moroccan Tamazight.

## 综合总结
LLM 调用失败或响应解析失败

## 技术栈
- 未标注

## 分析摘要
### 技术先进性 (评分: 0.0/10)


### 实用性 (评分: 0.0/10)


### 社区活跃度 (评分: 0.0/10)


## 项目链接
https://arxiv.org/abs/2609.38219
