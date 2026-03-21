# AGENTS.md

## Repository Overview

Content repository of agentically generated interactive learning roadmaps in the style of roadmap.sh. Each roadmap is a self-contained HTML file generated from structured JSON data. No build tools, servers, or external dependencies required.

The generation pipeline lives externally in [mr-krabs/workflows/topic-mastery-roadmap](https://github.com/funsaized/mr-krabs/tree/main/workflows/topic-mastery-roadmap). This repo holds only the outputs.

## Build / Run Commands

```bash
# Generate roadmap HTML from JSON data (per-roadmap)
python3 <roadmap-dir>/generate-roadmap.py

# Example
python3 ai-fullstack-healthcare-software/generate-roadmap.py
# Output: ai-fullstack-healthcare-software/roadmap.html

# View a roadmap — just open in browser, no server needed
open <roadmap-dir>/roadmap.html
```

There are no install steps, no dependencies beyond Python 3 stdlib (`json`, `os`), no linter, no test suite, and no CI/CD pipeline.

## Repository Structure

```
roadmaps/
├── README.md                              # Repo overview, pipeline docs, roadmap index
├── .gitignore
└── <roadmap-name>/                        # One directory per roadmap
    ├── roadmap.html                       # Generated interactive HTML (single file, self-contained)
    ├── generate-roadmap.py                # Python script: roadmap-final.json → roadmap.html
    ├── README.md                          # Roadmap-specific docs, stats, table of contents
    ├── review-notes.md                    # Automated review results from pipeline
    ├── architecture/
    │   ├── roadmap-final.json             # Final roadmap data (nodes, edges, resources, layout)
    │   └── layout-spec.md                 # Visual layout specification
    ├── research/
    │   ├── learning-plan.md               # Domain decomposition and dependency graph
    │   └── domains/                       # Per-domain deep research markdown files
    └── synthesis/
        ├── roadmap-data.json              # Pre-architecture synthesized data
        ├── knowledge-map.md               # Unified concept inventory
        ├── dependency-graph.md            # Topic dependency analysis
        ├── cross-references.md            # Inter-domain connections
        ├── learning-paths.md              # Recommended learning sequences
        └── resource-catalog.md            # Deduplicated, ranked resource index
```

## Data Pipeline

```
roadmap-final.json  →  generate-roadmap.py  →  roadmap.html
     (source)              (generator)           (output)
```

- `roadmap-final.json` is the single source of truth for each roadmap
- `generate-roadmap.py` reads it, minifies the JSON, and embeds it into a self-contained HTML file
- `roadmap.html` is the generated output — do NOT hand-edit; regenerate from JSON instead

## JSON Schema (roadmap-final.json)

Top-level keys:
- `metadata` — title, description, nodeCount, resourceCount, totalEstimatedHours, generatedAt
- `layout` — totalWidth, totalHeight, sectionGap, nodeGap, columnCount, nodeWidth/Height
- `colorScheme` — difficulty-keyed color maps (bg, border, text) for beginner/intermediate/advanced/expert, plus milestone and checkpoint
- `progressTracking` — storageKey (localStorage key), feature flags
- `resourcePanel` — maxDisplayed, sortOrder, badge types
- `sections[]` — id, title, description, displayOrder, estimatedHours, color
- `nodes[]` — id, title, description, difficulty, sectionId, displayOrder, keyConcepts[], subTopics[], prerequisites[], resources[], estimatedHours, isMilestone, isCheckpoint, isOptional, color, style
- `edges[]` — from, to (prerequisite relationships)

Node difficulty levels: `beginner`, `intermediate`, `advanced`, `expert`

Resource object shape:
```json
{
  "title": "string",
  "url": "https://...",
  "type": "course|video|book|exercise|documentation|repository",
  "cost": "free|paid",
  "isRecommended": true,
  "estimatedMinutes": 60
}
```

## Code Style

### Python (generate-roadmap.py)

- Python 3, stdlib only (`json`, `os`) — no third-party dependencies
- Compact imports: `import json, os`
- f-string templates for HTML generation with `{{` / `}}` for literal braces
- No type hints used in existing code
- Script-style (no classes, no functions beyond top-level procedural flow)
- Outputs file size after generation

### HTML / CSS / JS (roadmap.html)

- Self-contained single file — all CSS and JS inline, no external dependencies (except Google Fonts)
- Vanilla JavaScript — no frameworks, no build step
- DOM manipulation via `document.createElement`, `document.getElementById`, `innerHTML`
- Event handling via `addEventListener` and inline `onclick` attributes
- localStorage for progress persistence
- CSS custom properties (`:root` variables) for theming
- Responsive grid layout (`grid-template-columns: repeat(3, 1fr)`) with media query breakpoints at 900px and 600px
- BEM-ish class naming: `.section-header`, `.node-badge`, `.panel-section-title`
- Semicolons required in JS
- Template literals for HTML construction inside JS
- Color scheme: difficulty-based (green/blue/orange/red), milestone (gold), checkpoint (purple)

### Markdown

- ATX-style headers (`#`, `##`, `###`)
- Tables use pipe syntax with header separator
- Bold (`**text**`) for emphasis, not italics
- Em dash (`—`) in descriptions, not hyphens
- Code blocks with language tags (````python`, ````json`, ````bash`)
- Research documents follow a consistent structure: overview, key concepts, sub-topics, resources

### Naming Conventions

- Roadmap directories: `kebab-case` matching topic slug (e.g., `ai-fullstack-healthcare-software`)
- JSON node IDs: `kebab-case` (e.g., `fhir-r4-data-model`, `section-foundations`)
- Section IDs: `section-<name>` prefix
- CSS classes: `kebab-case`, component-prefixed (`.node-`, `.section-`, `.panel-`, `.resource-`)
- JS variables: `camelCase`
- localStorage keys: `kebab-case` (e.g., `ai-healthcare-roadmap-progress`)

### Git Conventions

- Short, lowercase commit messages (e.g., `readme`, `initial commit`, `update`)
- No conventional commits prefix used

## Adding a New Roadmap

1. Create a new directory: `<topic-slug>/`
2. Populate `architecture/roadmap-final.json` following the schema above
3. Copy `generate-roadmap.py` from an existing roadmap (or reuse the same script)
4. Run `python3 <topic-slug>/generate-roadmap.py` to generate `roadmap.html`
5. Add research/synthesis markdown docs as needed
6. Add a `README.md` with stats and table of contents
7. Update the root `README.md` roadmap table

## Validation Checklist (from review-notes.md)

When modifying `roadmap-final.json`:
- All nodes must have: id, title, description, difficulty, sectionId, displayOrder, color, resources, prerequisites
- All prerequisite references must point to existing node IDs
- All edge from/to must reference existing nodes
- Graph must be acyclic (topological sort must succeed)
- No node should have prerequisites of higher difficulty than itself
- Every content node (non-checkpoint) should have 2+ resources
- All resource URLs must use `https://` prefix
- Every section must have 2+ nodes

## Key Constraints

- `roadmap.html` is generated — never edit by hand; modify `roadmap-final.json` and regenerate
- HTML files must remain fully self-contained (no external JS/CSS beyond fonts)
- No server-side code — everything runs client-side in the browser
- Progress state is per-browser (localStorage), not synced
- The generation pipeline (7-agent workflow) lives in a separate repo; this repo is outputs only
