# Learning Paths: Epic EHR Integration Mastery

## Overview
Four distinct learning paths targeting different goals and time commitments. All paths share the same foundational layer but diverge based on depth and specialization.

---

## Path 1: Quick Start (Fastest Path to Basic Competence)
**Goal:** Build and deploy a basic FHIR-based SMART on FHIR app against Epic
**Time:** ~120 hours (6-8 weeks at 15-20 hrs/week)
**Coverage:** ~30% of total roadmap

### Sequence
1. **EHR Systems and Clinical Data** (node-1, 8h) — Understand what you're working with
2. **Data Exchange History** (node-2, 5h) — Why healthcare IT works this way
3. **Epic Integration Surfaces** (node-3, 5h) — Map all the ways in ★
4. **HIPAA Basics** (node-4, 8h) — Non-negotiable regulatory knowledge
5. **Clinical Terminology** (node-8, 10h) — Enough to read coded data
6. **FHIR Resource Model** (node-10, 15h) — The data model you'll code against
7. **FHIR RESTful API** (node-11, 10h) — CRUD operations
8. **US Core / USCDI** (node-13, 8h) — The interoperability contract
9. **Epic FHIR Implementation** (node-14, 10h) — Epic-specific behavior ★
10. **OAuth 2.0 Core** (node-16, 7h) — Authentication foundation
11. **PKCE** (node-17, 4h) — Mandatory security extension
12. **SMART Authorization** (node-18, 8h) — Healthcare OAuth profile
13. **SMART App Launch** (node-21, 6h) — App launch protocol
14. **EHR/Standalone Launch** (node-22, 8h) — Both launch flows
15. **Epic Showroom Basics** (node-48, 5h) — Distribution awareness
16. **Client ID Lifecycle** (node-51, 4h) — How to go live ★

### Outcome
Can build a SMART on FHIR app that reads patient data from Epic, supports both launch modes, and understands the path to production deployment.

---

## Path 2: Standard (Recommended Full Path)
**Goal:** Production-ready Epic integration developer who can handle FHIR, basic HL7v2, and CDS Hooks
**Time:** ~300 hours (12-16 weeks at 20-25 hrs/week)
**Coverage:** ~65% of total roadmap

### Includes all Quick Start nodes, plus:
17. **BAA Chain** (node-5, 4h) — Contract management
18. **Cures Act / Info Blocking** (node-6, 6h) — Legal obligations
19. **FHIR Search Mastery** (node-12, 10h) — Advanced queries
20. **FHIR Client Libraries** (node-15, 10h) — Hands-on coding
21. **JWT Backend Auth** (node-19, 6h) — System-to-system access
22. **JWKS Management** (node-20, 4h) — Key lifecycle ★
23. **SMART Scopes** (node-23, 4h) — Permission model depth
24. **Embedded Rendering** (node-24, 6h) — Hyperspace/MyChart rendering
25. **Multi-Tenant SMART** (node-26, 10h) — Multi-site architecture
26. **HL7v2 Message Structure** (node-27, 8h) — Legacy format essentials
27. **Message Types** (node-28, 10h) — ADT/ORM/ORU/SIU/MDM
28. **CDS Hooks Architecture** (node-31, 4h) — Clinical decision support
29. **Card Types / Prefetch** (node-32, 6h) — Building CDS services
30. **SMART from CDS Cards** (node-33, 4h) — CDS-to-app flow
31. **Interconnect / Chronicles** (node-35, 4h) — Epic internals
32. **Orders Integration** (node-44, 8h) — FHIR order resources
33. **Data Writeback** (node-46, 6h) — Filing data to Epic
34. **Security Review / SOC 2** (node-49, 12h) — Compliance prep
35. **Config Variability** (node-53, 8h) — Multi-site differences
36. **Go-Live Process** (node-54, 12h) — Deployment management ★

### Outcome
Can build, deploy, and maintain production Epic integrations using FHIR, SMART on FHIR, and CDS Hooks. Understands HL7v2 enough to work alongside legacy interfaces. Can manage the go-live process.

---

## Path 3: Comprehensive (Full Coverage)
**Goal:** Complete mastery of all Epic integration surfaces and operational discipline
**Time:** ~430 hours (20-24 weeks at 20-25 hrs/week)
**Coverage:** ~90% of total roadmap

### Includes all Standard nodes, plus:
37. **FDA SaMD** (node-7, 6h) — Medical device regulation
38. **FHIR Terminology Services** (node-9, 5h) — Terminology operations ★
39. **MLLP / ACK-NAK** (node-29, 5h) — HL7v2 transport
40. **Integration Engines** (node-30, 15h) — Mirth Connect etc. ★
41. **CDS Performance / Fatigue** (node-34, 3h) — Production CDS
42. **MyChart APIs** (node-36, 4h) — Patient portal integration
43. **OpenScheduling** (node-37, 4h) — Patient self-scheduling
44. **In-Basket / SmartForms** (node-38, 4h) — Messaging integration
45. **Bulk Data Export** (node-39, 10h) — Population data access
46. **Clarity / Caboodle** (node-40, 8h) — Epic data warehouses
47. **Clinical Documentation / AI** (node-45, 8h) — Note filing + AI scribe
48. **BPA from External Systems** (node-43, 8h) — Alert triggering
49. **Bi-directional Workflows** (node-47, 10h) — Closed-loop integration ★
50. **SMART Web Messaging** (node-25, 8h) — EHR communication
51. **ONC Certification** (node-50, 4h) — Certification requirements
52. **Multi-Tenant Healthcare** (node-52, 10h) — Architecture patterns
53. **Integration Testing** (node-55, 8h) — Testing strategy
54. **Observability / Tracing** (node-56, 15h) — Monitoring infrastructure
55. **HIPAA Logging** (node-57, 10h) — Compliant log management
56. **Resilience Patterns** (node-58, 12h) — Circuit breaker, retry, bulkhead
57. **Incident Response** (node-59, 10h) — Breach notification, runbooks
58. **Scaling / DR** (node-60, 10h) — Production hardening

### Outcome
Full operational mastery of all Epic integration surfaces with production-grade monitoring, resilience, and incident response capabilities.

---

## Path 4: Expert (Full Mastery + Architecture)
**Goal:** Integration architect who can design multi-year strategy and lead complex multi-surface implementations
**Time:** ~480 hours (24-30 weeks at 20 hrs/week)
**Coverage:** 100% of roadmap

### Includes all Comprehensive nodes, plus:
59. **ML Data Extraction** (node-41, 10h) — ML pipeline patterns
60. **De-identification** (node-42, 6h) — Privacy engineering
61. **Integration Surface Selection** (node-61, 5h) — Decision framework
62. **Hybrid Architecture Patterns** (node-62, 10h) — Multi-surface design
63. **HL7v2 to FHIR Migration** (node-63, 8h) — Migration planning
64. **Reference Architectures** (node-64, 10h) — Production-ready patterns
65. **Technology Strategy / Maturity Model** (node-65, 7h) — Long-term roadmapping ★

### Outcome
Can evaluate any Epic integration requirement, design hybrid architectures, plan migrations, produce reference architectures, and develop multi-year technology strategy. The highest-value skill level for an Epic integration practitioner.

---

## Path Comparison

| Metric | Quick Start | Standard | Comprehensive | Expert |
|--------|------------|----------|---------------|--------|
| Hours | ~120 | ~300 | ~430 | ~480 |
| Weeks (20h/wk) | 6 | 15 | 22 | 24 |
| Nodes covered | 16 | 36 | 58 | 65 |
| Milestones hit | 3 | 5 | 7 | 9 |
| Sections touched | 3 | 5 | 5 | 6 |
| Can build SMART app | ✓ | ✓ | ✓ | ✓ |
| Can deploy to prod | Basic | Yes | Yes | Yes |
| Can handle HL7v2 | No | Basic | Yes | Yes |
| Can build CDS Hooks | No | Yes | Yes | Yes |
| Can do bulk export | No | No | Yes | Yes |
| Can architect multi-surface | No | No | Basic | Yes |
| Can plan migrations | No | No | No | Yes |
