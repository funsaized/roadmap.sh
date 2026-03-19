# Cross-References: How Domains Relate and Reinforce Each Other

## Overview
The 15 domains in this roadmap are not isolated silos — they form a deeply interconnected web. This document maps the major cross-domain relationships, identifying where concepts from one domain enable, constrain, or enhance understanding of another.

---

## Cross-Reference Matrix

| Domain | Strongly Connected To | Nature of Connection |
|--------|----------------------|---------------------|
| D-1: Interoperability Foundations | D-2, D-3, D-4, D-7, D-15 | Provides the "why" context for all technical standards |
| D-2: Regulatory Compliance | D-4, D-5, D-8, D-10, D-12, D-13, D-14 | Constrains every technical design decision |
| D-3: Terminology Systems | D-4, D-7, D-8, D-15 | Semantic layer enabling meaningful data exchange |
| D-4: FHIR R4 | D-5, D-6, D-8, D-9, D-10, D-11, D-15 | The data model backbone for modern Epic integration |
| D-5: OAuth/Epic Auth | D-6, D-8, D-9, D-10, D-12, D-13, D-14 | Security layer gating all API access |
| D-6: SMART on FHIR | D-8, D-11, D-12, D-13, D-15 | Primary app development framework |
| D-7: HL7v2 | D-9, D-11, D-15 | Legacy integration surface; migration source |
| D-8: CDS Hooks | D-6, D-9, D-11, D-12, D-14 | Clinical workflow trigger mechanism |
| D-9: Epic APIs | D-6, D-7, D-8, D-10, D-11 | Proprietary surfaces filling FHIR gaps |
| D-10: Bulk Data | D-5, D-9, D-14, D-15 | Population-level data access |
| D-11: Workflow Embedding | D-4, D-5, D-6, D-7, D-8, D-9 | Where all surfaces converge in clinical use |
| D-12: App Orchard/Showroom | D-2, D-5, D-6, D-13 | Distribution gateway requiring compliance |
| D-13: Multi-Tenant/Go-Live | D-5, D-6, D-9, D-12, D-14 | Operational reality of multi-site deployment |
| D-14: Production Ops | D-2, D-5, D-9, D-10, D-13 | Operational discipline for reliability |
| D-15: Architecture Synthesis | D-1 through D-14 | Capstone connecting all domains |

---

## Key Cross-Domain Themes

### Theme 1: HIPAA Permeates Everything
D-2 (Regulatory) is not a standalone domain — its requirements cascade through:
- **D-5 (Auth):** Technical safeguards → OAuth implementation, audit logging
- **D-10 (Bulk Data):** De-identification requirements → data extraction patterns
- **D-12 (Showroom):** BAA chain → vendor security review
- **D-13 (Multi-Tenant):** PHI segregation → tenant isolation architecture
- **D-14 (Ops):** Breach notification → incident response, compliant logging

### Theme 2: FHIR as Universal Data Language
D-4 (FHIR R4) provides the shared vocabulary for:
- **D-6 (SMART):** Apps consume FHIR resources via authorized access
- **D-8 (CDS Hooks):** Prefetch data and suggestion actions are FHIR resources
- **D-10 (Bulk Data):** Export format is NDJSON (FHIR resources, one per line)
- **D-11 (Writeback):** DocumentReference.Create, Observation.Create, ServiceRequest — all FHIR
- **D-15 (Architecture):** FHIR-first strategy as the recommended posture

### Theme 3: OAuth as Universal Security Gate
D-5 (OAuth/Auth) underpins:
- **D-6 (SMART):** SMART is a profile of OAuth 2.0
- **D-8 (CDS Hooks):** Services receive FHIR access tokens
- **D-9 (Epic APIs):** All Interconnect API calls require OAuth tokens
- **D-10 (Bulk Data):** Backend Services auth (JWT assertion) for unattended access
- **D-13 (Multi-Tenant):** Separate OAuth configuration per Epic instance

### Theme 4: Clinical Context Flows Through Integration Surfaces
The clinical workflow spans multiple domains:
- **Entry:** D-7 (HL7v2) ADT events signal patient movement
- **Trigger:** D-8 (CDS Hooks) fire at workflow points
- **Display:** D-6 (SMART) apps render in clinical context
- **Action:** D-11 (Writeback) files data back to Epic
- **Analytics:** D-10 (Bulk Data) exports population-level data

### Theme 5: Terminology Bridges Syntax and Semantics
D-3 (Terminology) connects to every data-carrying domain:
- **D-4 (FHIR):** CodeableConcept bindings use SNOMED, ICD-10, LOINC, RxNorm
- **D-7 (HL7v2):** OBX segments carry LOINC codes, DG1 segments carry ICD-10
- **D-8 (CDS Hooks):** Clinical logic depends on correctly coded patient data
- **D-15 (Migration):** v2-to-FHIR requires terminology mapping

### Theme 6: Distribution Requires Operational Excellence
D-12 (Showroom) listing depends on:
- **D-2:** HIPAA compliance, BAA chain integrity
- **D-5:** Proper OAuth/PKCE implementation
- **D-6:** Working SMART on FHIR launch flows
- **D-13:** Multi-tenant readiness
- **D-14:** Production monitoring and incident response
- **D-49 (SOC 2):** De facto requirement from customer procurement

---

## Reinforcement Patterns

### Concepts That Deepen With Repeated Exposure

| Concept | First Encountered | Deepened In | Mastered In |
|---------|------------------|-------------|-------------|
| FHIR resources | D-4 (data model) | D-6 (in app context) | D-11 (writeback) |
| OAuth scopes | D-5 (theory) | D-6 (SMART scopes) | D-10 (system scopes) |
| Coding systems | D-3 (standalone) | D-4 (in FHIR resources) | D-8 (in CDS logic) |
| HL7v2 messages | D-7 (structure) | D-9 (In-Basket MDM) | D-15 (migration) |
| Epic architecture | D-1 (surfaces map) | D-9 (Chronicles deep) | D-15 (hybrid design) |
| Multi-tenancy | D-6 (app config) | D-13 (go-live) | D-14 (per-site monitoring) |
| Regulatory compliance | D-2 (rules) | D-12 (Showroom review) | D-14 (breach response) |

### Skills That Compound Across Domains

1. **FHIR API fluency** — Used in D-4, D-6, D-8, D-10, D-11 (increasingly complex queries and operations)
2. **OAuth token management** — Used in D-5, D-6, D-8, D-10, D-14 (increasingly complex lifecycle management)
3. **Clinical data interpretation** — Used in D-1, D-3, D-4, D-8, D-11 (increasingly actionable insights)
4. **Multi-site awareness** — Used in D-9, D-12, D-13, D-14 (increasingly operational discipline)

---

## Domain Dependency Clusters

### Cluster 1: "Read Data from Epic" (Minimum Viable Integration)
D-1 → D-3 → D-4 → D-5 → D-6
Enables: Reading patient data via FHIR with proper auth

### Cluster 2: "Write Data to Epic" (Clinical Workflow Integration)
Cluster 1 + D-8 → D-11
Enables: Filing observations, notes, and orders; triggering BPAs; bi-directional workflows

### Cluster 3: "Legacy Interface Management"
D-1 → D-7 → D-9
Enables: Working with HL7v2 interfaces alongside FHIR

### Cluster 4: "Production Operations"
D-2 → D-5 → D-12 → D-13 → D-14
Enables: Deploying, monitoring, and maintaining integrations at scale

### Cluster 5: "Population Health and Analytics"
D-5 → D-10 → D-9 (Clarity/Caboodle)
Enables: Bulk data extraction for analytics and ML

### Cluster 6: "Architecture and Strategy" (Capstone)
All clusters → D-15
Enables: Designing multi-surface architectures and migration strategies
