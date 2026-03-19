# Dependency Graph: Epic EHR Integration Mastery Roadmap

## Overview
This document defines the complete prerequisite dependency graph for the 65 concepts in the roadmap. The graph is a directed acyclic graph (DAG) — no circular dependencies exist. Each arrow means "must be learned before."

---

## Visual Layer Map

```
LAYER 0 (Entry Points — No Prerequisites)
  └── node-1: EHR Systems and Clinical Data Concepts

LAYER 1 (Depends on Layer 0)
  ├── node-2: Healthcare Data Exchange History ← [node-1]
  ├── node-4: HIPAA Privacy and Security Rules ← [node-1]
  └── node-8: Clinical Terminology Systems ← [node-1]

LAYER 2 (Depends on Layers 0-1)
  ├── node-3: Epic Integration Surfaces ← [node-1, node-2]  ★ MILESTONE
  ├── node-5: BAA Chain of Trust ← [node-4]
  ├── node-6: Cures Act / Information Blocking ← [node-4]
  ├── node-7: FDA SaMD Classification ← [node-4]
  └── node-9: FHIR Terminology Services ← [node-8]  ★ MILESTONE

LAYER 3 (Core Standards)
  ├── node-10: FHIR Resource Model ← [node-2, node-8]
  └── node-27: HL7v2 Message Structure ← [node-2, node-8]

LAYER 4 (API and Protocol Depth)
  ├── node-11: FHIR RESTful API ← [node-10]
  ├── node-13: US Core / USCDI ← [node-10]
  ├── node-28: ADT/ORM/ORU/SIU/MDM Messages ← [node-27]
  └── node-29: MLLP Transport and ACK/NAK ← [node-27]

LAYER 5 (Auth + FHIR Depth)
  ├── node-12: FHIR Search Mastery ← [node-11]
  ├── node-14: Epic FHIR Implementation ← [node-11, node-13]  ★ MILESTONE
  ├── node-15: FHIR Client Libraries ← [node-11]
  ├── node-16: OAuth 2.0 Core ← [node-11, node-4]
  └── node-30: Integration Engines ← [node-29]  ★ MILESTONE

LAYER 6 (OAuth Extensions)
  ├── node-17: PKCE ← [node-16]
  ├── node-18: SMART on FHIR Authorization ← [node-16]
  └── node-19: JWT Backend Service Auth ← [node-16]

LAYER 7 (App Development + Advanced Integration Entry)
  ├── node-20: JWKS and Key Management ← [node-19]  ★ MILESTONE
  ├── node-21: SMART App Launch Framework ← [node-18, node-14]
  ├── node-23: SMART Scopes ← [node-18]
  ├── node-35: Interconnect / Chronicles ← [node-14]
  ├── node-39: FHIR Bulk Data Export ← [node-19, node-14]
  ├── node-44: Orders Integration ← [node-14]
  ├── node-45: Clinical Documentation / AI ← [node-14]
  ├── node-46: Data Writeback (Observation.Create) ← [node-14]
  ├── node-50: ONC Certification ← [node-6, node-13]
  └── node-53: Epic Config Variability ← [node-14]

LAYER 8 (SMART Apps + Epic APIs)
  ├── node-22: EHR/Standalone Launch ← [node-21]
  ├── node-31: CDS Hooks Architecture ← [node-14, node-22]
  ├── node-36: MyChart APIs ← [node-35]
  ├── node-38: In-Basket / SmartForms ← [node-35]
  ├── node-40: Clarity and Caboodle ← [node-35]
  └── node-49: Security Review / SOC 2 ← [node-4, node-5]

LAYER 9 (Advanced Patterns)
  ├── node-24: Embedded Rendering ← [node-22]
  ├── node-26: Multi-Tenant SMART ← [node-22]
  ├── node-32: Card Response Types / Prefetch ← [node-31]
  ├── node-34: CDS Performance / Alert Fatigue ← [node-31]
  ├── node-37: OpenScheduling ← [node-36]
  ├── node-41: ML Data Extraction ← [node-39, node-40]
  ├── node-43: BPA from External Systems ← [node-31, node-46]
  └── node-48: Epic Showroom ← [node-22]

LAYER 10 (Deep Integration)
  ├── node-25: SMART Web Messaging ← [node-24]
  ├── node-33: SMART Launch from CDS Cards ← [node-32]
  ├── node-42: De-identification ← [node-4, node-41]
  ├── node-51: Client ID Lifecycle ← [node-48]  ★ MILESTONE
  └── node-52: Multi-Tenant Healthcare ← [node-26]

LAYER 11 (Operations)
  ├── node-47: Bi-directional Workflows ← [node-43, node-33]  ★ MILESTONE
  ├── node-54: Go-Live Process ← [node-52, node-53]  ★ MILESTONE
  └── node-56: Observability / Tracing ← [node-15, node-54]

LAYER 12 (Production Hardening)
  ├── node-55: Integration Testing ← [node-54]
  ├── node-57: HIPAA-Compliant Logging ← [node-4, node-56]
  ├── node-58: Error Handling / Resilience ← [node-14, node-56]
  └── node-61: Integration Surface Selection ← [node-47]

LAYER 13 (Expert Patterns)
  ├── node-59: Incident Response / Breach ← [node-57, node-5]
  ├── node-60: Scaling and DR ← [node-58]
  └── node-62: Hybrid Architecture Patterns ← [node-30, node-61]

LAYER 14 (Mastery)
  ├── node-63: HL7v2 to FHIR Migration ← [node-27, node-10]
  └── node-64: Reference Architectures ← [node-62, node-60]

LAYER 15 (Capstone)
  └── node-65: Technology Strategy / Maturity Model ← [node-64]  ★ MILESTONE
```

---

## Edge List (86 prerequisite relationships)

| # | From | To | Meaning |
|---|------|----|---------|
| 1 | node-1 | node-2 | EHR concepts → data exchange history |
| 2 | node-1 | node-3 | EHR concepts → Epic surfaces overview |
| 3 | node-2 | node-3 | Exchange history → Epic surfaces overview |
| 4 | node-1 | node-4 | EHR concepts → HIPAA |
| 5 | node-4 | node-5 | HIPAA → BAA chain |
| 6 | node-4 | node-6 | HIPAA → Cures Act |
| 7 | node-4 | node-7 | HIPAA → FDA SaMD |
| 8 | node-1 | node-8 | EHR concepts → terminology systems |
| 9 | node-8 | node-9 | Terminology → FHIR terminology services |
| 10 | node-2 | node-10 | Exchange history → FHIR resource model |
| 11 | node-8 | node-10 | Terminology → FHIR resource model |
| 12 | node-10 | node-11 | FHIR resources → RESTful API |
| 13 | node-11 | node-12 | RESTful API → FHIR search |
| 14 | node-10 | node-13 | FHIR resources → US Core profiles |
| 15 | node-11 | node-14 | RESTful API → Epic FHIR implementation |
| 16 | node-13 | node-14 | US Core → Epic FHIR implementation |
| 17 | node-11 | node-15 | RESTful API → client libraries |
| 18 | node-11 | node-16 | RESTful API → OAuth 2.0 core |
| 19 | node-4 | node-16 | HIPAA → OAuth 2.0 core |
| 20 | node-16 | node-17 | OAuth → PKCE |
| 21 | node-16 | node-18 | OAuth → SMART authorization |
| 22 | node-16 | node-19 | OAuth → JWT backend auth |
| 23 | node-19 | node-20 | JWT auth → JWKS management |
| 24 | node-18 | node-21 | SMART auth → SMART app launch |
| 25 | node-14 | node-21 | Epic FHIR → SMART app launch |
| 26 | node-21 | node-22 | SMART launch → EHR/standalone flows |
| 27 | node-18 | node-23 | SMART auth → SMART scopes |
| 28 | node-22 | node-24 | Launch flows → embedded rendering |
| 29 | node-24 | node-25 | Embedded rendering → web messaging |
| 30 | node-22 | node-26 | Launch flows → multi-tenant SMART |
| 31 | node-2 | node-27 | Exchange history → HL7v2 structure |
| 32 | node-8 | node-27 | Terminology → HL7v2 structure |
| 33 | node-27 | node-28 | HL7v2 structure → message types |
| 34 | node-27 | node-29 | HL7v2 structure → MLLP/ACK |
| 35 | node-29 | node-30 | MLLP/ACK → integration engines |
| 36 | node-14 | node-31 | Epic FHIR → CDS Hooks |
| 37 | node-22 | node-31 | Launch flows → CDS Hooks |
| 38 | node-31 | node-32 | CDS architecture → card types/prefetch |
| 39 | node-32 | node-33 | Cards → SMART launch from cards |
| 40 | node-31 | node-34 | CDS architecture → performance/fatigue |
| 41 | node-14 | node-35 | Epic FHIR → Interconnect/Chronicles |
| 42 | node-35 | node-36 | Interconnect → MyChart APIs |
| 43 | node-36 | node-37 | MyChart → OpenScheduling |
| 44 | node-35 | node-38 | Interconnect → In-Basket/SmartForms |
| 45 | node-19 | node-39 | JWT auth → Bulk Data Export |
| 46 | node-14 | node-39 | Epic FHIR → Bulk Data Export |
| 47 | node-35 | node-40 | Interconnect → Clarity/Caboodle |
| 48 | node-39 | node-41 | Bulk export → ML extraction |
| 49 | node-40 | node-41 | Clarity/Caboodle → ML extraction |
| 50 | node-4 | node-42 | HIPAA → de-identification |
| 51 | node-41 | node-42 | ML extraction → de-identification |
| 52 | node-31 | node-43 | CDS Hooks → BPA triggering |
| 53 | node-46 | node-43 | Data writeback → BPA triggering |
| 54 | node-14 | node-44 | Epic FHIR → orders integration |
| 55 | node-14 | node-45 | Epic FHIR → clinical documentation |
| 56 | node-14 | node-46 | Epic FHIR → data writeback |
| 57 | node-43 | node-47 | BPA → bi-directional workflows |
| 58 | node-33 | node-47 | SMART from cards → bi-directional |
| 59 | node-22 | node-48 | Launch flows → Showroom |
| 60 | node-4 | node-49 | HIPAA → security review/SOC 2 |
| 61 | node-5 | node-49 | BAA → security review/SOC 2 |
| 62 | node-6 | node-50 | Cures Act → ONC certification |
| 63 | node-13 | node-50 | US Core → ONC certification |
| 64 | node-48 | node-51 | Showroom → client ID lifecycle |
| 65 | node-26 | node-52 | Multi-tenant SMART → multi-tenant healthcare |
| 66 | node-14 | node-53 | Epic FHIR → config variability |
| 67 | node-52 | node-54 | Multi-tenant → go-live |
| 68 | node-53 | node-54 | Config variability → go-live |
| 69 | node-54 | node-55 | Go-live → integration testing |
| 70 | node-15 | node-56 | Client libraries → observability |
| 71 | node-54 | node-56 | Go-live → observability |
| 72 | node-4 | node-57 | HIPAA → compliant logging |
| 73 | node-56 | node-57 | Observability → compliant logging |
| 74 | node-14 | node-58 | Epic FHIR → resilience patterns |
| 75 | node-56 | node-58 | Observability → resilience patterns |
| 76 | node-57 | node-59 | Compliant logging → incident response |
| 77 | node-5 | node-59 | BAA → incident response |
| 78 | node-58 | node-60 | Resilience → scaling/DR |
| 79 | node-47 | node-61 | Bi-directional → surface selection |
| 80 | node-30 | node-62 | Integration engines → hybrid architectures |
| 81 | node-61 | node-62 | Surface selection → hybrid architectures |
| 82 | node-27 | node-63 | HL7v2 → v2-to-FHIR migration |
| 83 | node-10 | node-63 | FHIR resources → v2-to-FHIR migration |
| 84 | node-62 | node-64 | Hybrid architectures → reference architectures |
| 85 | node-60 | node-64 | Scaling/DR → reference architectures |
| 86 | node-64 | node-65 | Reference architectures → technology strategy |

---

## Critical Path (Minimum Path to Competence)

The shortest path through the graph for a developer who needs to build and ship a FHIR-based Epic integration:

```
node-1 → node-2 → node-3 → node-4 → node-8 → node-10 → node-11 → node-13 → node-14 → node-16 → node-17 → node-18 → node-21 → node-22 → node-48 → node-51
```

This covers: clinical data context → FHIR fundamentals → US Core → Epic FHIR → OAuth/PKCE/SMART → app development → distribution.

**Estimated time: ~120 hours (critical path only)**

---

## Milestone Nodes

These nodes represent key checkpoints where a learner has achieved a meaningful level of capability:

1. **node-3** (Epic Integration Surfaces) — Can describe all Epic integration surfaces and when to use each
2. **node-9** (FHIR Terminology Services) — Can work with coded clinical data programmatically
3. **node-14** (Epic FHIR Implementation) — Can query Epic's sandbox and understand Epic-specific behavior
4. **node-20** (JWKS Key Management) — Can implement production-grade authentication for all Epic auth flows
5. **node-30** (Integration Engines) — Can route and transform HL7v2 messages through middleware
6. **node-47** (Bi-directional Workflows) — Can build closed-loop integrations combining CDS, SMART, and FHIR writeback
7. **node-51** (Client ID Lifecycle) — Can navigate Epic's distribution process for production deployment
8. **node-54** (Go-Live Process) — Can manage the full go-live process with stakeholders
9. **node-65** (Technology Strategy) — Can design multi-year integration architecture strategy
