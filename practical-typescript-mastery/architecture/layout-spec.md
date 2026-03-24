# Visual Layout Specification — Practical TypeScript Mastery Roadmap

## Overview
A vertically-scrolling interactive roadmap (roadmap.sh style) with 6 horizontal section bands stacked top-to-bottom in difficulty progression order. Each section contains a 3-column grid of clickable rounded-rectangle nodes connected by prerequisite edges. Total canvas: 1400px wide × ~3640px tall.

## Layout Strategy
- **Direction:** Top-to-bottom vertical flow (easiest → hardest)
- **Sections:** Horizontal bands with colored backgrounds and sticky headers
- **Nodes:** 280px × 60px (regular), 280px × 80px (expandable), centered in column cells
- **Columns:** 3 per section, evenly spaced
- **Section gap:** 80px between bands
- **Node gap:** 20px between rows

## Section Layout (Top to Bottom)

```
┌──────────────────────────────────────────────────────────────────┐
│  SECTION 1: Foundations (35h, beginner)                   🟢     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │Structural│  │Type      │  │Union &   │                      │
│  │Typing    │  │Erasure   │  │Intersect │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │Type      │  │Discrim.  │  │Literal   │                      │
│  │Narrowing │  │Unions  ★ │  │Types     │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │type vs   │  │any/unkn/ │  │strict &  │                      │
│  │interface │  │never   ★ │  │Safety  ★ │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │Module    │  │Project   │  │TSConfig  │                      │
│  │Resolut.  │  │Refs      │  │Layering  │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌──────────────────────────────────┐                           │
│  │ ✓ Foundations Complete (chkpt)   │                           │
│  └──────────────────────────────────┘                           │
├──────────────────────────────────────────────────────────────────┤
│  SECTION 2: Type System Depth (55h, intermediate)        🔵     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │State     │  │Branded   │  │Utility & │                      │
│  │Modeling  │  │Types     │  │Mapped  ★ │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ... (16 nodes in 3-column grid) ...                            │
│  ┌──────────────────────────────────┐                           │
│  │ ✓ Type Depth Complete (chkpt)    │                           │
│  └──────────────────────────────────┘                           │
├──────────────────────────────────────────────────────────────────┤
│  SECTION 3: Frontend Workflows (20h, intermediate-adv)   🟠     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │React     │  │Hooks &   │  │Context & │                      │
│  │Props     │  │State     │  │State Mgmt│                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │Advanced  │  │Event &   │  │E2E API   │                      │
│  │Comps     │  │Ref Typing│  │Safety  ★ │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
├──────────────────────────────────────────────────────────────────┤
│  SECTION 4: Backend Workflows (20h, intermediate-adv)    🔵     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │Typed     │  │Middleware│  │Error     │                      │
│  │Routes    │  │Augment.  │  │Envelopes │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │Database  │  │Typed     │  │E2E Type  │                      │
│  │Types     │  │Events    │  │Sharing ★ │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌──────────────────────────────────┐                           │
│  │ ✓ Workflows Complete (chkpt)     │                           │
│  └──────────────────────────────────┘                           │
├──────────────────────────────────────────────────────────────────┤
│  SECTION 5: Tooling & Operations (18h, intermediate)     🟣     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │tsc CI    │  │ts-eslint │  │VS Code   │                      │
│  │Gate      │  │Typed Lint│  │Mastery   │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │Type-Level│  │Coverage &│  │CI Design │                      │
│  │Testing   │  │Hygiene   │  │        ★ │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ┌──────────┐  ┌──────────────────────────────────┐             │
│  │Testing   │  │ ✓ Tooling Complete (chkpt)        │             │
│  │Stack     │  └──────────────────────────────────┘             │
│  └──────────┘                                                    │
├──────────────────────────────────────────────────────────────────┤
│  SECTION 6: Scale, Migration & Governance (42h, adv)     🔴     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │JS→TS     │  │Codemod   │  │Type Debt │                      │
│  │Migration │  │Tools     │  │Tracking  │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│  ... (13 nodes in 3-column grid) ...                            │
│  ┌──────────────────────────────────┐                           │
│  │ 🏆 TypeScript Mastery (final)    │                           │
│  └──────────────────────────────────┘                           │
└──────────────────────────────────────────────────────────────────┘
```

## Color Coding

| Difficulty | Background | Border | Usage |
|---|---|---|---|
| beginner | #E8F5E9 | #4CAF50 | Foundation concepts |
| beginner-intermediate | #E0F2F1 | #26A69A | Transition topics |
| intermediate | #E3F2FD | #2196F3 | Core modeling & tooling |
| intermediate-advanced | #E8EAF6 | #5C6BC0 | Applied patterns |
| advanced | #FFF3E0 | #FF9800 | Scale & performance |
| expert | #FFEBEE | #F44336 | Cutting-edge features |

## Special Node Styles
- **Milestone nodes (★):** 3px border, gold accent, trophy badge
- **Checkpoint nodes (✓):** Purple border (#9C27B0), centered, full-width appearance
- **Optional nodes:** Dashed border, 0.8 opacity
- **Expandable nodes:** 80px tall (vs 60px), expand icon in corner

## Edge Routing
- Edges connect prerequisite → dependent nodes
- Within same section: straight vertical/diagonal lines
- Cross-section: L-shaped paths routed through section gaps
- Edge color matches source node's difficulty border color
- Arrowheads on target end

## Interactive Behavior

### Node Click → Detail Panel (Right Sidebar)
```
┌─────────────────────────────────┐
│ [Node Title]           [×close] │
│ ─────────────────────────────── │
│ [difficulty badge] [Xh est.]    │
│                                 │
│ Description text...             │
│                                 │
│ KEY CONCEPTS                    │
│ • concept-1  • concept-2       │
│                                 │
│ SUB-TOPICS (if expandable)      │
│ □ sub-topic-1                   │
│ □ sub-topic-2                   │
│                                 │
│ RESOURCES                       │
│ ★ [Title] [doc] [free] [1h]    │
│ ★ [Title] [course] [paid] [5h] │
│   [Title] [book] [paid] [20h]  │
│   [Show 3 more...]             │
│                                 │
│ PREREQUISITES                   │
│ ✓ Node A (completed)           │
│ ○ Node B (not started)         │
│                                 │
│ [Mark Complete ✓]               │
└─────────────────────────────────┘
```

### Resource Badges
- **Type:** doc | course | book | exercise | repo | video
- **Difficulty:** beginner | intermediate | advanced
- **Cost:** free (green) | paid (amber)
- **Time:** estimated completion time

### Resource Sort Order
1. Recommended (★) first
2. Then by type: course → exercise → documentation → book → repository → video

## Progress Tracking

### Per-Node State
- Stored in localStorage under key `ts-roadmap-progress`
- Each node: `{ completed: boolean, completedAt: timestamp }`

### Visual Indicators
- **Completed node:** Green checkmark overlay, slightly muted colors
- **Available node:** Full color, clickable
- **Locked node:** Grayed out, lock icon, tooltip shows missing prerequisites
- **Section progress bar:** Horizontal bar under section header showing X/Y complete
- **Overall progress:** Floating badge in top-right: "42% Complete (27/64 nodes)"

### Prerequisite Lock Logic
A node is unlocked when ALL its prerequisite nodes are marked complete.
Locked nodes are still visible but have reduced opacity and show a lock icon.

## Responsive Behavior
- **Desktop (>1200px):** Full 3-column layout, detail panel as right sidebar
- **Tablet (768-1200px):** 2-column layout, detail panel as modal overlay
- **Mobile (<768px):** 1-column layout, detail panel as full-screen modal

## Data File
All layout data is in `roadmap-final.json`. The HTML builder reads this single file to render the complete interactive roadmap. No additional data files needed.

## Node Statistics
- Total nodes: 64 (59 content + 5 checkpoints)
- Total edges: 88
- Sections: 6
- Resources: 90 (85 content + 5 checkpoint exercises)
- Expandable nodes: 37
- Milestone nodes: 12
- Optional nodes: 2
