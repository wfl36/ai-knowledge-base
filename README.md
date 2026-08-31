# AI Knowledge Base Agent

[中文文档](README_CN.md)

> Automatically collect AI content from multiple sources (GitHub Trending, arXiv/blog RSS, Hacker News), intelligently analyze and score it, and generate a structured knowledge base with a static web UI.

## Features

- **Pluggable Multi-Source Collection** — GitHub Trending + RSS (arXiv / vendor blogs) + Hacker News, unified into a generic `Item` model. Adding a source = adding one file; enabled via `AKB_SOURCES`
- **Source-Aware 3D Scoring** — Technical Advancement / Practicality / Community Activity, 1-10 scale; the three axes are reinterpreted per source via per-source prompts (e.g. for articles: insight depth / applicability / timeliness)
- **Dynamic Weight Adjustment** — Auto-adjusts weights based on human review feedback
- **Bonus Scoring** — Breakthrough innovation projects can receive extra points (up to +2)
- **Date-based Storage** — Entries organized under `knowledge/YYYY-MM-DD/` subdirectories
- **Auto Cleanup** — Automatically removes directories older than 15 days on each pipeline run
- **Static Web UI** — Dark-themed SPA with search, tag filtering, and date navigation, deployed on Cloudflare Pages
- **GitHub Actions** — Daily automated collection with auto-commit of results

## Project Structure

```
ai-knowledge-base/
├── .github/workflows/     # GitHub Actions scheduled tasks
├── app/
│   ├── sources/           # Pluggable sources (github / rss / hackernews) + registry
│   ├── crawler/           # GitHub Trending crawler (used by sources/github_trending)
│   ├── agent/             # AI scoring agent (LLM-powered) + per-source prompts
│   ├── storage/           # Knowledge entry storage
│   ├── review/            # Human review management
│   ├── api/               # FastAPI web interface
│   └── main.py            # Main entry point
├── scripts/
│   ├── build_static.py    # Generate data.json from markdown
│   └── build.sh           # Cloudflare Pages build script
├── site/
│   ├── index.html         # Static SPA frontend
│   └── data/              # Generated data.json
├── templates/             # HTML templates (FastAPI)
├── knowledge/             # Generated knowledge entries
│   ├── index.md           # Master index
│   └── 2026-05-17/        # Date-based subdirectory
│       ├── project-a_9.0_2026-05-17.md
│       └── project-b_8.5_2026-05-17.md
└── pyproject.toml
```

## Quick Start

```bash
# Install
python3 -m venv .venv && source .venv/bin/activate
pip install -e .

# Configure
cp .env.example .env
# Edit .env and fill in LLM_API_KEY

# Start web server (with scheduler)
akb serve

# Run a manual crawl + analysis
akb crawl

# Adjust weights based on review feedback
akb adjust-weights

# Build static site data
python3 scripts/build_static.py ./knowledge ./site/data
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| LLM_API_URL | LLM API endpoint | OpenRouter |
| LLM_API_KEY | API Key | Required |
| LLM_MODEL | Model name | minimax/minimax-m3:free |
| LLM_CONCURRENCY | Concurrent LLM analysis requests (higher = faster, too high may hit rate limits) | 5 |
| GITHUB_TOKEN | GitHub Token (optional, increases rate limit) | - |
| GITHUB_MAX_PROJECTS | Max GitHub Trending projects per run | 10 |
| AKB_SOURCES | Enabled sources, comma-separated (github,rss,hackernews) | github,rss,hackernews |
| RSS_FEEDS | RSS/Atom feeds, comma-separated (empty = arXiv cs.AI/cs.CL + HF blog) | (defaults) |
| RSS_MAX_PER_FEED | Max entries per RSS feed | 10 |
| HN_QUERY | Hacker News search query | AI OR LLM OR agent |
| HN_MIN_POINTS | Min HN points to include | 50 |
| HN_MAX_ITEMS | Max HN items per run | 20 |
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
- Each pipeline run automatically cleans up directories older than **15 days**
- The master index (`knowledge/index.md`) is regenerated on every run

## GitHub Actions

The included workflow (`.github/workflows/daily-collect.yml`) runs daily at UTC 00:00 (Beijing 08:00):

1. Crawls GitHub Trending AI projects
2. Analyzes and scores each project via LLM
3. Saves results to date-based subdirectories
4. Builds static site data (`site/data/data.json`)
5. Auto-commits and pushes new entries

Required repository secrets: `LLM_API_URL`, `LLM_API_KEY`, `LLM_MODEL`

## Static Site Deployment

The `site/` directory contains a self-contained SPA that reads `data.json` generated by `build_static.py`. Deploy to Cloudflare Pages with:

- **Build command:** `bash scripts/build.sh`
- **Output directory:** `site`
- **Root directory:** `/`

Live site: [https://ai-knowledge-base-22f.pages.dev](https://ai-knowledge-base-22f.pages.dev)

## License

MIT
