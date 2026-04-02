# Layout Specification — Prediction Market Trading Strategies Roadmap

## Overview

A vertical-flow, multi-column interactive roadmap inspired by roadmap.sh. Four horizontal
section bands stack top-to-bottom (Foundations → Core Methods → Advanced Strategies → Expert
Integration). Within each section, domains run left-to-right as columns. Nodes stack
top-to-bottom within each domain column.

**Canvas:** 1580 × 4936 px  
**Nodes:** 154 (150 content + 4 checkpoints)  
**Edges:** 246 (231 prerequisite + 15 checkpoint)  

## Visual Structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│  FOUNDATIONS  (103h, beginner)                          #4CAF50 green  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                 │
│  │ Probability  │  │  Pred Market │  │  Financial   │                 │
│  │ & Bayesian   │  │  Mechanics   │  │  Markets     │                 │
│  │              │  │              │  │              │                 │
│  │ [1.1] ─────> │  │ [2.1]        │  │ [3.1]        │                 │
│  │ [1.2]        │  │ [2.2]        │  │ [3.2]        │                 │
│  │ [1.3] ──┐    │  │ [2.3]        │  │ [3.3]        │                 │
│  │ [1.4] <─┘    │  │ [2.4]        │  │ ...          │                 │
│  │ ...          │  │ ...          │  │ [3.13]       │                 │
│  │ [1.10]       │  │ [2.14]       │  │              │                 │
│  └──────────────┘  └──────────────┘  └──────────────┘                 │
│                    ┌─────────────────────────┐                        │
│                    │  ✓ Foundations Complete  │  (gold checkpoint)     │
│                    └─────────────────────────┘                        │
├─────────────────────────────────────────────────────────────────────────┤
│  CORE METHODS  (173h, intermediate)                     #2196F3 blue  │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐         │
│  │Forecasting │ │  Pricing   │ │ Info/Rsrch │ │    Risk    │         │
│  │& Calibratn │ │  Theory    │ │  Sources   │ │ Management │         │
│  │ [4.1]-[4.8]│ │[5.1]-[5.14]│ │[6.1]-[6.7] │ │[7.1]-[7.10]│         │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘         │
│                    ┌─────────────────────────┐                        │
│                    │ ✓ Core Methods Complete  │                        │
│                    └─────────────────────────┘                        │
├─────────────────────────────────────────────────────────────────────────┤
│  ADVANCED STRATEGIES  (435h, advanced)                  #FF9800 org   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│  │  Quant   │ │ Arbitrage│ │Portfolio │ │  Market  │ │  Event   │   │
│  │ Modeling │ │Cross-Plat│ │Construct │ │  Making  │ │ Driven   │   │
│  │[8.1-8.8] │ │[9.1-9.8] │ │[10.1-11] │ │[11.1-10] │ │[12.1-10] │   │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘   │
│                    ┌─────────────────────────┐                        │
│                    │  ✓ Advanced Complete     │                        │
│                    └─────────────────────────┘                        │
├─────────────────────────────────────────────────────────────────────────┤
│  EXPERT INTEGRATION  (292h, expert)                     #F44336 red   │
│  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐             │
│  │  Algorithmic   │ │  Behavioral   │ │  Strategy      │             │
│  │  Systems       │ │  Psychology   │ │  Integration   │             │
│  │ [13.1]-[13.8]  │ │ [14.1]-[14.10]│ │ [15.1]-[15.8]  │             │
│  └────────────────┘ └────────────────┘ └────────────────┘             │
│                    ┌─────────────────────────┐                        │
│                    │  ✓ Expert Complete       │                        │
│                    └─────────────────────────┘                        │
└─────────────────────────────────────────────────────────────────────────┘
```

## Node Design

Each node is a rounded rectangle (240×56 px) with:

| Property        | Value                                                  |
|-----------------|--------------------------------------------------------|
| Background      | `#21262d` (dark card)                                  |
| Text            | `#f0f6fc` (light)                                      |
| Corner radius   | 8px                                                    |
| Left accent bar | 4px wide, colored by difficulty level                  |
| Recommended     | Purple border (`#9C27B0`, 3px solid)                   |
| Optional        | Dashed border                                          |
| Milestone       | Gold border (`#FFD700`, 3px solid) + star icon         |
| Checkpoint      | Full gold background, centered across section columns  |

### Color Coding

- **Beginner:** `#4CAF50` (green)
- **Intermediate:** `#2196F3` (blue)
- **Advanced:** `#FF9800` (orange)
- **Expert:** `#F44336` (red)
- **Checkpoint:** `#FFD700` (gold)

## Edge / Connector Design

- Prerequisite edges: solid `#484f58` lines, 1.5px, with arrow heads
- Checkpoint edges: dashed `#FFD700` lines, animated pulse
- Cross-section edges drawn with curved bezier paths to avoid clutter
- Same-domain edges use straight vertical connectors

## Resource Panel

Right sidebar (400px) slides in on node click:

```
┌──────────────────────────────────┐
│  [Node Title]                    │
│  difficulty badge  |  domain     │
├──────────────────────────────────┤
│  Description                     │
│  Full text description...        │
├──────────────────────────────────┤
│  Key Concepts                    │
│  • concept 1                     │
│  • concept 2                     │
├──────────────────────────────────┤
│  Resources                       │
│  ★ [Recommended] Title    FREE   │
│    📹 Video Title         FREE   │
│    📖 Book Title          PAID   │
│    🔧 Tool Title          FREE   │
├──────────────────────────────────┤
│  Prerequisites                   │
│  ← Node A  ← Node B             │
│  Next Steps                      │
│  → Node C  → Node D             │
└──────────────────────────────────┘
```

## Progress Tracking

- **Node level:** Three-state checkbox (not started / in progress / complete)
- **Section level:** Progress bar with "X of Y complete (Z%)"
- **Overall:** Top header bar showing total completion percentage
- **Prerequisite locking:** Incomplete prereqs show node at 50% opacity with lock icon
- **Storage:** `localStorage` for persistence without server

## Learning Paths

| Path           | Hours | Coverage                                    |
|----------------|-------|---------------------------------------------|
| Quick Start    | 150h  | 25 core nodes across foundations + sizing   |
| Standard       | 400h  | All foundations + core methods + intro adv  |
| Comprehensive  | 750h  | Through advanced, selective expert          |
| Expert         | 1003h | All 150 nodes, full mastery                 |

## Theme

Dark mode (GitHub-style): background `#0d1117`, cards `#21262d`, borders `#30363d`.
Font: Inter for UI, JetBrains Mono for code/data. Highlight glow: `rgba(56,139,253,0.4)`.

## Files

- `roadmap-final.json` — Complete layout data with coordinates, colors, resources, edges
- `layout-spec.md` — This document
