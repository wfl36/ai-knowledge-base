# AI 知识库 Agent

[English](README.md)

> 自动从多个信息源（GitHub Trending、arXiv/博客 RSS、Hacker News）采集 AI 内容，智能分析评分，生成结构化知识库，并提供静态 Web 界面

## 功能

- **可插拔多源采集** — GitHub Trending + RSS（arXiv / 厂商博客）+ Hacker News，统一抽象为通用 `Item`。加一个源 = 加一个文件；由 `AKB_SOURCES` 控制启用
- **按源自适应三维评分** — 技术先进性 / 实用性 / 社区活跃度，1-10 分制；三维含义按来源用各自提示词重新解释（如文章：洞见深度 / 可落地性 / 时效性）
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
│   ├── sources/           # 可插拔信息源 (github / rss / hackernews) + 注册表
│   ├── crawler/           # GitHub Trending 爬虫 (被 sources/github_trending 复用)
│   ├── agent/             # AI 评分 Agent (LLM 驱动) + 按源提示词
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
| AKB_SOURCES | 启用的信息源，逗号分隔（github,rss,hackernews） | github,rss,hackernews |
| RSS_FEEDS | RSS/Atom 订阅源，逗号分隔（留空用默认：arXiv cs.AI/cs.CL + HF 博客） | （默认） |
| RSS_MAX_PER_FEED | 每个 RSS 源最多抓取条数 | 10 |
| HN_QUERY | Hacker News 搜索词 | AI OR LLM OR agent |
| HN_MIN_POINTS | HN 纳入的最低 points | 50 |
| HN_MAX_ITEMS | 每次运行 HN 最多条数 | 20 |
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
