# Visual Layout Specification — Epic EHR Integration Roadmap

## Canvas Dimensions
- **Total Width:** 960px
- **Total Height:** 3280px
- **Canvas Padding:** 40px all sides

## Layout Strategy
Vertical-flow roadmap inspired by roadmap.sh. Six sections stack top-to-bottom in difficulty progression (beginner → expert). Each section is a visually distinct band with a colored header bar. Within each section, nodes arrange in a 3-column grid (left-to-right, top-to-bottom by displayOrder). The critical learning path flows down the center column where possible, with optional nodes at the margins. Milestone nodes get prominent styling (thicker borders, trophy icon, star badge). Prerequisite edges render as SVG connectors between node centers.

## Section Layout

```
┌──────────────────────────────────────────────────────────────┐
│ 🟢 HEALTHCARE FOUNDATIONS (9 nodes)                     ~40px│
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│ │ EHR Sys  │  │ HDE Hist │  │🏆Epic Int │                    │
│ │ Concepts │  │ Standards│  │ Surfaces │                    │
│ └──────────┘  └──────────┘  └──────────┘                    │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│ │ HIPAA    │  │ BAA &    │  │ Cures Act│                    │
│ │ Privacy  │  │ Trust    │  │ Info Blk │                    │
│ └──────────┘  └──────────┘  └──────────┘                    │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│ │ FDA SaMD │  │ Clinical │  │🏆FHIR    │                    │
│ │          │  │ Terminol │  │ Term Svcs│                    │
│ └──────────┘  └──────────┘  └──────────┘                    │
├──────────────────────────────────────────────────────────────┤
│                        ↕ 80px gap                            │
├──────────────────────────────────────────────────────────────┤
│ 🔵 CORE STANDARDS AND SECURITY (11 nodes)                    │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│ │ FHIR Res │  │ FHIR REST│  │ FHIR     │                    │
│ │ Model    │  │ API      │  │ Search   │                    │
│ └──────────┘  └──────────┘  └──────────┘                    │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│ │ US Core  │  │🏆Epic    │  │ FHIR     │                    │
│ │ Profiles │  │ FHIR Imp │  │ Client   │                    │
│ └──────────┘  └──────────┘  └──────────┘                    │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│ │ OAuth2.0 │  │ PKCE     │  │ SMART    │                    │
│ │ Core     │  │ Modern   │  │ Auth     │                    │
│ └──────────┘  └──────────┘  └──────────┘                    │
│ ┌──────────┐  ┌──────────┐                                   │
│ │ JWT Back │  │🏆JWKS Key│                                   │
│ │ Service  │  │ Mgmt     │                                   │
│ └──────────┘  └──────────┘                                   │
├──────────────────────────────────────────────────────────────┤
│                        ↕ 80px gap                            │
├──────────────────────────────────────────────────────────────┤
│ 🔵🟠 APPLICATION DEVELOPMENT AND INTERFACES (10 nodes)       │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│ │ SMART    │  │ EHR &    │  │ SMART    │                    │
│ │ App Lnch │  │ Standalone│  │ Scopes   │                    │
│ └──────────┘  └──────────┘  └──────────┘                    │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│ │ Embedded │  │ SMART Web│  │ Multi-   │                    │
│ │ Render   │  │ Messaging│  │ Tenant   │                    │
│ └──────────┘  └──────────┘  └──────────┘                    │
│ ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│ │ HL7v2 Msg│  │ ADT,ORM, │  │ MLLP     │                    │
│ │ Structure│  │ ORU,SIU  │  │ Transport│                    │
│ └──────────┘  └──────────┘  └──────────┘                    │
│ ┌──────────┐                                                 │
│ │🏆Integr  │                                                 │
│ │ Engines  │                                                 │
│ └──────────┘                                                 │
├──────────────────────────────────────────────────────────────┤
│                        ↕ 80px gap                            │
├──────────────────────────────────────────────────────────────┤
│ 🟠 ADVANCED INTEGRATION PATTERNS (17 nodes)                  │
│   [6 rows × 3 columns, last row partial]                     │
│   CDS Hooks → Cards → App Launch → Performance               │
│   Interconnect → MyChart → OpenSched                         │
│   In-Basket → Bulk FHIR → Data Warehouses                    │
│   ML Extract → De-identification → BPAs                      │
│   Orders → Clinical Docs → Observation.Create                │
│   🏆Bi-directional Workflow                                   │
├──────────────────────────────────────────────────────────────┤
│                        ↕ 80px gap                            │
├──────────────────────────────────────────────────────────────┤
│ 🟠🔴 DISTRIBUTION AND OPERATIONS (13 nodes)                  │
│   Showroom → Security → ONC Cert                             │
│   Client ID → Multi-Tenant → Config Variability              │
│   🏆Go-Live → Testing → Observability                        │
│   Logging → Error Handling → Incident Response               │
│   Scaling & DR                                               │
├──────────────────────────────────────────────────────────────┤
│                        ↕ 80px gap                            │
├──────────────────────────────────────────────────────────────┤
│ 🔴 ARCHITECTURE AND MASTERY (5 nodes)                        │
│   Decision Matrix → Hybrid Patterns → Migration              │
│   Reference Archs → 🏆Technology Strategy                    │
└──────────────────────────────────────────────────────────────┘
```

## Node Dimensions
- **Regular nodes:** 280px × 60px
- **Expandable nodes:** 280px × 80px (has subTopics)
- **Column gap:** 20px horizontal
- **Row gap:** 20px vertical

## Color Coding

| Difficulty     | Background | Border  | Text    |
|---------------|-----------|---------|---------|
| Beginner      | #E8F5E9   | #4CAF50 | #2E7D32 |
| Intermediate  | #E3F2FD   | #2196F3 | #1565C0 |
| Advanced      | #FFF3E0   | #FF9800 | #E65100 |
| Expert        | #FFEBEE   | #F44336 | #C62828 |

## Special Node Styles
- **Milestone nodes** (9 total): 3px border, 🏆 icon, ★ badge
- **Optional nodes** (3 total: nodes 40, 41, 42): dashed border, 80% opacity
- **Standard nodes**: 2px solid border, full opacity

## Edge Rendering
- Edges connect prerequisite → dependent via SVG paths
- Same-section edges: straight or L-shaped connectors
- Cross-section edges: S-curved paths bridging section gaps
- Edge color matches source node's border color
- Arrow heads on target end (6px triangles)
- 86 total edges

## Resource Panel
- Slides in from right on node click (400px wide)
- Resources grouped by type: Course → Video → Book → Exercise → Docs → Repo → Community
- Each resource shows: title (linked), type badge (colored), difficulty badge, cost badge (green=free, red=paid), time estimate
- Recommended resources marked with ★ and sorted first
- Max 10 visible, "Show more" button for overflow

## Progress Tracking
- Stored in localStorage under key `epic-ehr-roadmap-progress`
- Four states per node: not-started (default), in-progress (⏳), completed (✅), skipped (⏭️)
- Click node toggles state cycle
- Progress bar at top shows % completed
- Section-level progress indicators
- State colors overlay the node background with semi-transparent tint

## Interactive Behaviors
1. **Node click**: Opens resource panel for that node
2. **Node right-click/long-press**: Cycles progress state
3. **Section collapse**: Click section header to collapse/expand
4. **Zoom**: Mouse wheel or pinch to zoom (min 50%, max 200%)
5. **Pan**: Click-drag on canvas background
6. **Path highlight**: Hover a node to highlight its prerequisite chain
7. **Filter**: Toggle buttons for difficulty levels, progress states, learning paths

## Milestone Nodes (9)
1. node-3: Epic Integration Surfaces Overview
2. node-9: FHIR Terminology Services
3. node-14: Epic FHIR Implementation
4. node-20: JWKS and Key Management
5. node-30: Integration Engines
6. node-47: Bi-directional Workflow Patterns
7. node-51: Client ID Lifecycle
8. node-54: Go-Live Process
9. node-65: Technology Strategy and Maturity Model
