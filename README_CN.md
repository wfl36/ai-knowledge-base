# AI 知识库 Agent

[English](README.md)

> 自动抓取 GitHub Trending AI 项目，智能分析评分，生成结构化知识库，并提供静态 Web 界面

## 功能

- **GitHub Trending 爬虫** — 每日自动抓取 AI 相关项目（关键词过滤，最多20条）
- **三维评分 Agent** — 技术先进性 / 实用性 / 社区活跃度，1-10 分制
- **动态权重调整** — 根据人工复核反馈自动调整权重
- **特别加分机制** — 突破性创新项目可获得额外加分（最高+2）
- **按日期归档** — 知识条目按日期存放在 `knowledge/YYYY-MM-DD/` 子目录
- **自动清理** — 每次运行自动删除超过15天的日期目录
- **静态 Web 界面** — 暗色主题 SPA，支持搜索、标签筛选、日期导航，部署在 Cloudflare Pages
- **GitHub Actions** — 每日自动采集，结果自动提交

## 项目结构

```
ai-knowledge-base/
├── .github/workflows/     # GitHub Actions 定时任务
├── app/
│   ├── crawler/           # GitHub Trending 爬虫
│   ├── agent/             # AI 评分 Agent (LLM 驱动)
│   ├── storage/           # 知识条目存储
│   ├── review/            # 人工复核管理
│   ├── api/               # FastAPI Web 界面
│   └── main.py            # 主入口
├── scripts/
│   ├── build_static.py    # 从 markdown 生成 data.json
│   └── build.sh           # Cloudflare Pages 构建脚本
├── site/
│   ├── index.html         # 静态 SPA 前端
│   └── data/              # 生成的 data.json
├── templates/             # HTML 模板 (FastAPI)
├── knowledge/             # 生成的知识条目
│   ├── index.md           # 总纲
│   └── 2026-05-17/        # 按日期建子目录
│       ├── project-a_9.0_2026-05-17.md
│       └── project-b_8.5_2026-05-17.md
└── pyproject.toml
```

## 快速开始

```bash
# 安装
python3 -m venv .venv && source .venv/bin/activate
pip install -e .

# 配置
cp .env.example .env
# 编辑 .env 填入 LLM_API_KEY

# 启动 Web 服务（含定时任务）
akb serve

# 手动执行一次抓取+分析
akb crawl

# 根据复核反馈调整权重
akb adjust-weights

# 构建静态站点数据
python3 scripts/build_static.py ./knowledge ./site/data
```

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| LLM_API_URL | LLM API 地址 | OpenRouter |
| LLM_API_KEY | API Key | 必填 |
| LLM_MODEL | 模型名 | z-ai/glm-5.1 |
| LLM_CONCURRENCY | LLM 分析并发数（越大越快，过大可能触发 API 限流） | 5 |
| GITHUB_TOKEN | GitHub Token（可选，提升请求频率限制） | - |
| CRAWL_SCHEDULE | 定时抓取 cron | 0 0 * * * |
| API_HOST | FastAPI 监听地址 | 127.0.0.1 |
| API_PORT | FastAPI 端口 | 8900 |
| KNOWLEDGE_DIR | 知识库目录 | ./knowledge |

## 评分体系

三个维度各 1-10 分，初始权重各 33.3%：

| 维度 | 评估内容 |
|------|---------|
| 技术先进性 | 技术栈先进性、创新程度、技术深度、前沿性 |
| 实用性 | 问题解决能力、应用场景、可扩展性、商业价值 |
| 社区活跃度 | Star增长、Issue响应、PR处理、文档质量 |

总评分低于6分自动标记为"待复核"状态。

## 数据保留策略

- 知识条目按日期归档存放在 `knowledge/YYYY-MM-DD/` 子目录中
- 每次 pipeline 运行自动清理超过 **15天** 的日期目录
- 总纲 `knowledge/index.md` 每次运行时重新生成

## GitHub Actions

内置工作流（`.github/workflows/daily-collect.yml`）每天 UTC 00:00（北京时间 08:00）自动运行：

1. 抓取 GitHub Trending AI 项目
2. 通过 LLM 分析评分
3. 保存到按日期归档的子目录
4. 构建静态站点数据（`site/data/data.json`）
5. 自动提交并推送新条目

需要配置的仓库 Secrets：`LLM_API_URL`、`LLM_API_KEY`、`LLM_MODEL`

## 静态站点部署

`site/` 目录包含一个自包含 SPA，读取 `build_static.py` 生成的 `data.json`。部署到 Cloudflare Pages：

- **构建命令：** `bash scripts/build.sh`
- **输出目录：** `site`
- **根目录：** `/`

在线地址：[https://ai-knowledge-base-22f.pages.dev](https://ai-knowledge-base-22f.pages.dev)

## License

MIT
