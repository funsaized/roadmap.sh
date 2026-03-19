# Learning Plan: Epic EHR Integration

## Topic Overview

A practitioner roadmap to mastering Epic EHR integration — covering all integration surfaces, standards, certification, and production operations.

### Target Audience
Fullstack software engineers and technical leads (2-8 years experience).

### Estimated Total Time: 250-380 hours

---

## Learning Domains

### D-1: Healthcare Interoperability Foundations
Beginner | Prerequisites: None | Time: 15-25 hours
EHR systems, healthcare data exchange history, clinical data concepts, Epic integration surfaces overview.
Acceptance: Explain EHR purpose, name all Epic integration surfaces, describe HL7v2 to FHIR evolution.

### D-2: Healthcare Regulatory and Compliance Landscape
Beginner | Prerequisites: D-1 | Time: 15-25 hours
HIPAA for app developers, Cures Act, ONC certification, FDA SaMD, BAA chain, information blocking.
Acceptance: Explain HIPAA obligations, BAA chain, FDA regulation triggers, information blocking rules.

### D-3: Healthcare Terminology and Coding Systems
Beginner | Prerequisites: D-1 | Time: 12-18 hours
SNOMED CT, ICD-10, LOINC, RxNorm, CPT, CVX. Epic internal code mapping. FHIR terminology services.
Acceptance: Identify correct coding system per data type, explain Epic terminology mapping.

### D-4: FHIR R4 Specification and Data Model
Intermediate | Prerequisites: D-1, D-3 | Time: 30-40 hours
FHIR resource model, RESTful interactions, search, US Core profiles, USCDI, Epic FHIR implementation.
Acceptance: Read FHIR resources, construct search queries, use client library, identify Epic coverage gaps.

### D-5: OAuth 2.0 Security Standards and Epic Auth
Intermediate | Prerequisites: D-1, D-2 | Time: 15-25 hours
OAuth 2.0 flows with Epic, OIDC, PKCE, JWT backend auth, JWKS, TLS, certificate management.
Acceptance: Implement OAuth flow, generate JWT assertions, manage asymmetric keys, publish JWKS.

### D-6: SMART on FHIR App Development
Intermediate | Prerequisites: D-4, D-5 | Time: 30-40 hours
SMART App Launch, EHR vs standalone launch, scopes, embedded rendering, Web Messaging, multi-tenant.
Acceptance: Build working SMART app on Epic sandbox, implement both launch flows, handle context.

### D-7: HL7v2 Interfaces and Integration Engines
Intermediate | Prerequisites: D-1, D-3 | Time: 25-35 hours
HL7v2 message structure, ADT/ORM/ORU/SIU/MDM, MLLP, ACK/NAK, integration engines (Mirth, Rhapsody).
Acceptance: Parse HL7v2 messages, explain message flows, describe MLLP, set up basic interface.

### D-8: CDS Hooks and Clinical Decision Support
Advanced | Prerequisites: D-4, D-6 | Time: 20-30 hours
CDS Hooks spec, hook types, prefetch, card responses, SMART app launch from cards, Epic CDS implementation.
Acceptance: Implement CDS Hooks service, construct card responses, optimize with prefetch.

### D-9: Epic Interconnect MyChart and Proprietary APIs
Advanced | Prerequisites: D-4, D-5, D-6 | Time: 20-30 hours
Interconnect architecture, MyChart APIs, OpenScheduling, Chronicles awareness, SmartForms, In-Basket.
Acceptance: Explain Interconnect, describe OpenScheduling, compare MyChart vs FHIR Patient Access.

### D-10: Bulk Data Analytics and Population Health
Advanced | Prerequisites: D-4, D-5 | Time: 15-25 hours
Bulk FHIR Export, Backend Services auth, Caboodle, Clarity, Cogito, ML data extraction patterns.
Acceptance: Implement Bulk FHIR workflow, explain Caboodle vs Clarity, describe ML data patterns.

### D-11: Clinical Workflow Embedding and Advanced Patterns
Advanced | Prerequisites: D-6, D-8, D-9 | Time: 25-35 hours
BPAs from external systems, orders integration, note writing, AI in clinical docs, bi-directional workflows.
Acceptance: Design BPA trigger pattern, describe orders integration, design bi-directional workflow.

### D-12: App Orchard Showroom and Epic Distribution
Advanced | Prerequisites: D-6, D-2 | Time: 15-25 hours
Showroom listing, Connection Hub, security review, legal agreements, SOC 2, ONC certification.
Acceptance: Describe full listing process, explain security review requirements, SOC 2 expectations.

### D-13: Multi-Tenant Operations and Go-Live
Advanced | Prerequisites: D-6, D-7, D-12 | Time: 20-30 hours
Multi-tenant architecture, version differences, config variability, go-live processes, IT governance.
Acceptance: Design multi-tenant architecture, describe go-live process, identify stakeholders.

### D-14: Production Operations Monitoring and Reliability
Expert | Prerequisites: D-6, D-7, D-10, D-13 | Time: 20-30 hours
Monitoring, error handling, rate limiting, HIPAA logging, incident response, scaling, DR.
Acceptance: Design monitoring strategy, implement HIPAA-compliant logging, describe incident response.

### D-15: Integration Architecture and Mastery Synthesis
Expert | Prerequisites: D-6, D-7, D-8, D-9, D-10, D-11, D-13, D-14 | Time: 20-30 hours
Integration surface selection, hybrid architectures, migration strategies, reference architectures, tech strategy.
Acceptance: Design multi-surface architecture, recommend integration surfaces, design migration plan.

---

## Dependency Graph
D-1->D-2, D-1->D-3, D-1+D-3->D-4, D-1+D-2->D-5, D-4+D-5->D-6, D-1+D-3->D-7, D-4+D-6->D-8, D-4+D-5+D-6->D-9, D-4+D-5->D-10, D-6+D-8+D-9->D-11, D-6+D-2->D-12, D-6+D-7+D-12->D-13, D-6+D-7+D-10+D-13->D-14, D-6+D-7+D-8+D-9+D-10+D-11+D-13+D-14->D-15

Critical Path: D-1->D-3->D-4->D-6->D-8->D-11->D-13->D-14->D-15

## Cross-Cutting Themes
1. Security and Privacy
2. Epic-Specific Implementation Details
3. Regulatory Compliance
4. Testing and Sandbox Development
5. Multi-Tenant and Configuration Variability
6. Clinical Workflow Awareness
7. Standards Evolution
