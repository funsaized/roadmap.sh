# Visual Layout Specification — AI in Fullstack Healthcare Software Roadmap

## Overview

A vertically-stacked, section-banded roadmap inspired by roadmap.sh. Five sections flow top-to-bottom in difficulty progression (Foundations → Core AI Modalities → Model Adaptation → Production & Safety → Autonomous Systems). Each section contains nodes arranged in a 3-column grid. Checkpoint nodes mark section transitions for progress validation.

## Layout Dimensions

| Property | Value |
|---|---|
| Total Width | 980px |
| Total Height | 3640px |
| Column Count | 3 |
| Node Width | 280px |
| Node Height (standard) | 60px |
| Node Height (expandable) | 80px |
| Node Gap (horizontal) | 20px |
| Node Gap (vertical) | 20px |
| Section Gap | 80px |
| Section Header Height | 80px |
| Left Margin | 40px |
| Top Margin | 40px |

## Color Scheme

### Difficulty Colors
- **Beginner** — bg: #E8F5E9, border: #4CAF50 (green)
- **Intermediate** — bg: #E3F2FD, border: #2196F3 (blue)
- **Advanced** — bg: #FFF3E0, border: #FF9800 (orange)
- **Expert** — bg: #FFEBEE, border: #F44336 (red)

### Special Node Types
- **Milestone** — bg: #FFF8E1, border: #FFC107, badge: ★, icon: 🏆, borderWidth: 3
- **Checkpoint** — bg: #F3E5F5, border: #9C27B0, badge: ✓, icon: ✓
- **Optional** — borderStyle: dashed, opacity: 0.8
- **Recommended** — borderWidth: 3

## ASCII Mockup

```
┌─────────────────────────── 980px ───────────────────────────┐
│                                                              │
│  ╔══════════════════════════════════════════════════════════╗ │
│  ║  FOUNDATIONS (80hrs, beginner)                           ║ │
│  ╠══════════════════════════════════════════════════════════╣ │
│  ║  [🏆 FHIR R4    ] [HL7v2 Legacy ] [DICOM Imaging ]     ║ │
│  ║  [X12/EDI Trans ] [CDS Hooks    ] [Med Terminol. ]     ║ │
│  ║  [🏆 HIPAA      ] [FDA SaMD     ] [ONC Cures Act ]     ║ │
│  ║  [Synthetic Data] [🏆 Supervised] [Unsupervised  ]     ║ │
│  ║  [🏆 Clin Metric] [Bias/Fairness] [Interpretabil.]     ║ │
│  ║  [Feature Eng.  ] [ML Pipeline  ]                      ║ │
│  ╚══════════════════════════════════════════════════════════╝ │
│                         ↓                                    │
│  ╔══════════════════════════════════════════════════════════╗ │
│  ║  ✓ Foundations Complete (checkpoint)                     ║ │
│  ╠══════════════════════════════════════════════════════════╣ │
│  ║  CORE AI MODALITIES (200hrs, intermediate)              ║ │
│  ║  ┌─ Predictive AI ──────────────────────────────┐       ║ │
│  ║  │ [🏆 Risk Strat] [HC Regression] [Ranking/Rec] │      ║ │
│  ║  │ [Cluster/Anom ] [🏆 Pred Integ]              │      ║ │
│  ║  └──────────────────────────────────────────────┘       ║ │
│  ║  ┌─ Generative AI ──────────────────────────────┐       ║ │
│  ║  │ [🏆 Transformer] [HC LLMs     ] [🏆 Prompts ] │      ║ │
│  ║  │ [Struct Output ] [🏆 PHI-Safe ] [LLM Eval   ] │      ║ │
│  ║  └──────────────────────────────────────────────┘       ║ │
│  ║  ┌─ Knowledge AI ───────────────────────────────┐       ║ │
│  ║  │ [Med Embeddings] [Vector DBs  ] [Ontologies ] │      ║ │
│  ║  │ [🏆 RAG       ] [Knowledge Gr]              │       ║ │
│  ║  └──────────────────────────────────────────────┘       ║ │
│  ║  ┌─ Clinical NLP ───────────────────────────────┐       ║ │
│  ║  │ [Note Summary ] [Ambient Doc ] [Speech-Text ] │      ║ │
│  ║  │ [Prior Auth   ] [-- Patient --] [-- Synth -- ] │     ║ │
│  ║  └──────────────────────────────────────────────┘       ║ │
│  ║  ┌─ Perception AI ──────────────────────────────┐       ║ │
│  ║  │ [CNN Medical  ] [🏆 Segment. ] [Clin Imaging] │      ║ │
│  ║  │ [DICOM Integ  ] [-- Audio -- ]               │      ║ │
│  ║  └──────────────────────────────────────────────┘       ║ │
│  ╚══════════════════════════════════════════════════════════╝ │
│                         ↓                                    │
│  ╔══════════════════════════════════════════════════════════╗ │
│  ║  ✓ Core Modalities Complete (checkpoint)                ║ │
│  ╠══════════════════════════════════════════════════════════╣ │
│  ║  MODEL ADAPTATION (50hrs, advanced)                     ║ │
│  ║  [🏆 Fine-Tuning] [Domain Models] [Training Data]      ║ │
│  ║  [RLHF/DPO     ] [Med Benchmrk ] [FDA PCCPs    ]      ║ │
│  ╚══════════════════════════════════════════════════════════╝ │
│                         ↓                                    │
│  ╔══════════════════════════════════════════════════════════╗ │
│  ║  ✓ Model Adaptation Complete (checkpoint)               ║ │
│  ╠══════════════════════════════════════════════════════════╣ │
│  ║  PRODUCTION & SAFETY (120hrs, advanced)                 ║ │
│  ║  [CDS Systems  ] [CQL          ] [RL Treatment  ]      ║ │
│  ║  [Prior Auth   ] [Care Gaps    ] [PHI Detection ]      ║ │
│  ║  [🏆 Guardrails] [Hallucination] [🏆 FDA Compl.]      ║ │
│  ║  [Eval Framewk ] [Tracing      ] [Observability ]      ║ │
│  ║  [Model Version] [Drift Detect ] [Routing/Cost  ]      ║ │
│  ║  [Audit Logging]                                        ║ │
│  ╚══════════════════════════════════════════════════════════╝ │
│                         ↓                                    │
│  ╔══════════════════════════════════════════════════════════╗ │
│  ║  ✓ Production & Safety Complete (checkpoint)            ║ │
│  ╠══════════════════════════════════════════════════════════╣ │
│  ║  AUTONOMOUS SYSTEMS (50hrs, expert)                     ║ │
│  ║  [Agent Arch   ] [🏆 FHIR Agent] [LangGraph    ]      ║ │
│  ║  [🏆 Workflow  ] [HITL Patterns] [Agent Safety  ]      ║ │
│  ║  [🏆 Multi-Agnt]                                       ║ │
│  ╚══════════════════════════════════════════════════════════╝ │
│                                                              │
└──────────────────────────────────────────────────────────────┘

Legend:
  [🏆 Name] = Milestone node (gold border, star badge)
  [-- Name --] = Optional node (dashed border, reduced opacity)
  ✓ = Checkpoint node (purple, progress gate)
```

## Edge Routing Strategy

- **Same-section edges**: Straight vertical or short diagonal lines within the section band
- **Cross-section edges**: L-shaped connectors dropping vertically from source section into target section, then horizontal to target node
- **Edge color**: Matches source node's difficulty border color
- **Arrow heads**: Triangular, pointing from prerequisite to dependent
- **Edge avoidance**: Edges route around intermediate nodes; crossing minimization via column alignment of heavily-connected nodes

## Resource Panel Design

When a node is clicked, a slide-out panel (400px wide) appears on the right showing:

1. **Node header**: Title, difficulty badge, estimated hours, section
2. **Description**: Full text
3. **Key concepts**: Pill-shaped tags
4. **Sub-topics** (if expandable): Collapsible list
5. **Resources**: Sorted list with badges
   - ★ Recommended resources appear first
   - Type badge (course/video/book/exercise/doc/repo)
   - Difficulty badge (colored dot)
   - Cost badge (FREE green / PAID orange)
   - Time estimate
   - Max 10 shown, "Show more" button for overflow

## Progress Tracking

- **Per-node checkbox**: Click to mark complete, stored in localStorage
- **Section progress bar**: Horizontal bar showing X/Y nodes complete
- **Overall percentage**: Top-right corner, circular progress indicator
- **Prerequisite locking**: Nodes with incomplete prerequisites show a lock icon overlay and reduced opacity; clicking shows "Complete prerequisites first: [list]"
- **Storage**: `localStorage` key `ai-healthcare-roadmap-progress`

## Node Counts

| Section | Nodes | Checkpoints |
|---|---|---|
| Foundations | 17 | 0 |
| Core AI Modalities | 28 (incl 1 checkpoint) | 1 |
| Model Adaptation | 7 (incl 1 checkpoint) | 1 |
| Production & Safety | 17 (incl 1 checkpoint) | 1 |
| Autonomous Systems | 8 (incl 1 checkpoint) | 1 |
| **Total** | **77** | **4** |

## Interactivity Model

1. **Hover**: Node border thickens, slight shadow lift
2. **Click**: Opens resource panel, highlights prerequisite chain
3. **Right-click / long-press**: Toggle complete/incomplete
4. **Section collapse**: Click section header to collapse/expand
5. **Zoom**: Ctrl+scroll or pinch to zoom; min 50%, max 200%
6. **Pan**: Click-drag on background to pan
7. **Search**: Top search bar filters nodes by title/concept
8. **Learning path filter**: Dropdown to highlight Quick Start / Standard / Comprehensive / Expert paths
