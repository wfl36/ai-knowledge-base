# AI 知识库 Agent

> 自动抓取 GitHub Trending AI 项目，智能分析评分，生成结构化知识条目

## 功能

- **GitHub Trending 爬虫** — 每日自动抓取 AI 相关项目（关键词过滤，最多20条）
- **三维评分 Agent** — 技术先进性 / 实用性 / 社区活跃度，1-10 分制
- **动态权重调整** — 参考淘宝店铺评分算法，根据人工复核反馈自动调整权重
- **特别加分机制** — 突破性创新项目可获得额外加分（最高+2）
- **知识条目输出** — Markdown 格式，含总纲和独立项目文件
- **版本管理** — 自动快照，保留最近5个版本，支持对比
- **人工复核** — FastAPI 审核页面，低于6分自动标记待复核
- **GitHub Actions** — 每日自动采集，结果自动提交

## 项目结构

```
ai-knowledge-base/
├── .github/workflows/     # GitHub Actions 定时任务
├── app/
│   ├── crawler/           # GitHub Trending 爬虫
│   ├── agent/             # AI 评分 Agent (LLM 驱动)
│   ├── storage/           # 知识条目存储 + 版本管理
│   ├── review/            # 人工复核管理
│   ├── api/               # FastAPI Web 界面
│   └── main.py            # 主入口
├── templates/             # HTML 模板
├── knowledge/             # 生成的知识条目
└── tests/                 # 测试
```

## 快速开始

```bash
# 安装
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# 配置
cp .env.example .env
# 编辑 .env 填入 LLM_API_KEY

# 启动 Web 服务
akb serve

# 手动执行一次抓取+分析
akb crawl

# 调整权重
akb adjust-weights
```

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| LLM_API_URL | LLM API 地址 | OpenRouter |
| LLM_API_KEY | API Key | 必填 |
| LLM_MODEL | 模型名 | z-ai/glm-5.1 |
| GITHUB_TOKEN | GitHub Token (可选) | - |
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

## License

MIT
