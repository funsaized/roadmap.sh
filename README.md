# roadmaps

Agentically generated interactive learning roadmaps in the style of [roadmap.sh](https://roadmap.sh) — structured, visual developer learning paths with progress tracking, curated resources, and prerequisite-based topic ordering.

Each roadmap is a self-contained HTML file generated from a structured JSON data source. No build tools or servers required — just open in a browser.

## How It Works

Each roadmap is produced through a multi-stage agentic pipeline:

1. **Research** — Domain research across the roadmap's topic areas, producing detailed markdown documents per domain
2. **Synthesis** — Cross-referencing, dependency graphing, and knowledge mapping across all researched domains
3. **Architecture** — Structuring topics into a DAG (directed acyclic graph) of nodes with prerequisites, difficulty levels, milestones, and curated learning resources
4. **Review** — Automated validation of JSON structure, referential integrity, graph acyclicity, resource coverage, and domain completeness
5. **Generation** — A Python script compiles the final JSON into a single self-contained interactive HTML file

## Features

- **Progress tracking** — Check off topics as you learn. Progress persists in localStorage.
- **Detail panel** — Click any topic to see descriptions, key concepts, sub-topics, prerequisites, and curated resources
- **Search and filter** — Find topics by name or concept. Filter by difficulty level.
- **Prerequisite locking** — Topics with unfinished prerequisites are locked until you complete them
- **Section collapse** — Expand/collapse sections to focus on what matters
- **Prerequisite navigation** — Click prerequisite links to jump directly to the referenced topic
- **Fully offline** — Each roadmap is a single HTML file with zero external dependencies (except fonts)

## Roadmaps

| Roadmap | Topics | Resources | Est. Hours |
|---------|--------|-----------|------------|
| [AI in Fullstack Healthcare Software](ai-fullstack-healthcare-software/) | 77 | 165 | 450 |

## Repository Structure

```
roadmaps/
├── README.md
└── <roadmap-name>/
    ├── roadmap.html                   # Interactive roadmap (open in browser)
    ├── generate-roadmap.py            # HTML generator script
    ├── README.md                      # Roadmap-specific documentation
    ├── review-notes.md                # Automated review results
    ├── architecture/
    │   ├── roadmap-final.json         # Structured roadmap data (nodes, edges, resources)
    │   └── layout-spec.md             # Visual layout specification
    ├── research/
    │   ├── learning-plan.md           # Domain decomposition and dependency graph
    │   └── domains/                   # Per-domain research documents
    └── synthesis/
        ├── knowledge-map.md           # Unified concept map
        ├── dependency-graph.md        # Topic dependency analysis
        ├── cross-references.md        # Inter-domain connections
        ├── learning-paths.md          # Recommended learning sequences
        └── resource-catalog.md        # Curated resource index
```

## Inspired By

[roadmap.sh](https://roadmap.sh) — the community-driven developer roadmap platform (350k+ GitHub stars). This project takes the same philosophy of structured, visual learning paths and applies it to niche/specialized domains using agentic generation.
