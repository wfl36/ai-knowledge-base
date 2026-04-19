# AI Knowledge Base Agent

[中文文档](README_CN.md)

> Automatically crawl GitHub Trending AI projects, intelligently analyze and score them, and generate structured knowledge entries.

## Features

- **GitHub Trending Crawler** — Daily auto-crawl of AI-related projects (keyword filtering, up to 20 entries)
- **3D Scoring Agent** — Technical Advancement / Practicality / Community Activity, 1-10 scale
- **Dynamic Weight Adjustment** — Inspired by e-commerce rating algorithms, auto-adjusts weights based on human review feedback
- **Bonus Scoring Mechanism** — Breakthrough innovation projects can receive extra points (up to +2)
- **Date-based Storage** — Entries organized under `knowledge/YYYY-MM-DD/` subdirectories
- **Auto Cleanup** — Automatically removes directories older than 30 days on each pipeline run
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
│   ├── index.md           # Master index
│   ├── 2026-04-19/        # Date-based subdirectory
│   │   ├── project-a_9.0_2026-04-19.md
│   │   └── project-b_8.5_2026-04-19.md
│   └── 2026-04-20/        # Next day entries
│       └── ...
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

## Data Retention

- Knowledge entries are stored in date-based subdirectories (`knowledge/YYYY-MM-DD/`)
- Each pipeline run automatically cleans up directories older than **30 days**
- The master index (`knowledge/index.md`) is regenerated on every run
- Version snapshots keep the last 5 versions

## GitHub Actions

The included workflow (`.github/workflows/daily-collect.yml`) runs daily at UTC 00:00 (Beijing 08:00):

1. Crawls GitHub Trending AI projects
2. Analyzes and scores each project via LLM
3. Saves results to date-based subdirectories
4. Auto-commits and pushes new entries

Required repository secrets: `LLM_API_URL`, `LLM_API_KEY`, `LLM_MODEL`

## License

MIT
