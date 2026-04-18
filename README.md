# AI Knowledge Base Agent

[中文文档](README_CN.md)

> Automatically crawl GitHub Trending AI projects, intelligently analyze and score them, and generate structured knowledge entries.

## Features

- **GitHub Trending Crawler** — Daily auto-crawl of AI-related projects (keyword filtering, up to 20 entries)
- **3D Scoring Agent** — Technical Advancement / Practicality / Community Activity, 1-10 scale
- **Dynamic Weight Adjustment** — Inspired by e-commerce rating algorithms, auto-adjusts weights based on human review feedback
- **Bonus Scoring Mechanism** — Breakthrough innovation projects can receive extra points (up to +2)
- **Knowledge Entry Output** — Markdown format with index and individual project files
- **Version Management** — Auto snapshots, keeps last 5 versions, supports diff
- **Human Review** — FastAPI review dashboard, auto-flags entries below 6 for review
- **GitHub Actions** — Daily automated collection with auto-commit of results

## Project Structure

```
ai-knowledge-base/
├── .github/workflows/     # GitHub Actions scheduled tasks
├── app/
│   ├── crawler/           # GitHub Trending crawler
│   ├── agent/             # AI scoring agent (LLM-powered)
│   ├── storage/           # Knowledge entry storage + version management
│   ├── review/            # Human review management
│   ├── api/               # FastAPI web interface
│   └── main.py            # Main entry point
├── templates/             # HTML templates
├── knowledge/             # Generated knowledge entries
└── tests/                 # Tests
```

## Quick Start

```bash
# Install
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Configure
cp .env.example .env
# Edit .env and fill in LLM_API_KEY

# Start web server
akb serve

# Run a manual crawl + analysis
akb crawl

# Adjust weights
akb adjust-weights
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| LLM_API_URL | LLM API endpoint | OpenRouter |
| LLM_API_KEY | API Key | Required |
| LLM_MODEL | Model name | z-ai/glm-5.1 |
| GITHUB_TOKEN | GitHub Token (optional) | - |
| CRAWL_SCHEDULE | Cron schedule for crawling | 0 0 * * * |
| API_HOST | FastAPI listen address | 127.0.0.1 |
| API_PORT | FastAPI port | 8900 |
| KNOWLEDGE_DIR | Knowledge base directory | ./knowledge |

## Scoring System

Three dimensions, each scored 1-10, with initial equal weights of 33.3%:

| Dimension | Evaluation Criteria |
|-----------|-------------------|
| Technical Advancement | Tech stack sophistication, innovation level, technical depth, cutting-edge relevance |
| Practicality | Problem-solving capability, use cases, scalability, commercial value |
| Community Activity | Star growth, Issue response, PR processing, documentation quality |

Entries with a total score below 6 are automatically flagged as "pending review".

## License

MIT
