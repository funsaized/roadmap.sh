# Knowledge Map: Integrating Software Applications with the Epic EHR System

## Overview
This knowledge map contains 65 unique concepts organized across 6 sections and 15 research domains, covering the complete practitioner journey from healthcare foundations to expert-level integration architecture.

---

## Section 1: Healthcare Foundations (Beginner)

### D-1: Healthcare Interoperability Foundations
- **EHR Systems and Clinical Data Concepts**: EHR vs EMR distinction, ADT events, CPOE, clinical documents, orders/results lifecycle, patient demographics, vital signs/observations
- **Healthcare Data Exchange History**: HL7v2 emergence (1987), HIPAA (1996), HITECH/Meaningful Use (2009), FHIR (2014), 21st Century Cures Act (2016), ONC Final Rule (2020)
- **Epic Integration Surfaces Overview**: FHIR R4 APIs, SMART on FHIR, CDS Hooks, HL7v2 Bridges, Care Everywhere, MyChart, Bulk FHIR, Interconnect, App Orchard/Showroom; Epic's federated model (each customer runs independent instance)
- **Interoperability Levels**: Foundational → Structural → Semantic → Organizational
- **Key Organizations**: HL7 International, IHE, ONC, SMART Health IT, Argonaut Project

### D-2: Healthcare Regulatory and Compliance Landscape
- **HIPAA Privacy and Security Rules**: PHI protection, minimum necessary standard, administrative/physical/technical safeguards, AES-256 at rest, TLS 1.2+ in transit, 6-year audit log retention
- **Business Associate Agreements**: Chain of trust (Covered Entity → BA → Subcontractors), flow-down requirements, BAA registry management
- **21st Century Cures Act and Information Blocking**: Eight exceptions, $1M/violation penalties, active enforcement since September 2023
- **FDA SaMD Classification**: Class I/II/III risk levels, four-criteria CDS exclusion test, AI/ML-based SaMD regulation, PCCP for algorithm evolution
- **State Privacy Laws**: CCPA/CPRA, 42 CFR Part 2, varying breach notification timelines

### D-3: Healthcare Terminology and Coding Systems
- **SNOMED CT**: 300K+ clinical concepts, hierarchical, used in Condition/Procedure FHIR resources
- **ICD-10-CM/PCS**: 68K+ diagnosis codes, mandatory for billing since 2015
- **LOINC**: 95K+ codes for labs/observations, six-part naming convention (Component/Property/Time/System/Scale/Method)
- **RxNorm**: Standardized drug nomenclature (IN, BN, SCD, SBD concept types)
- **CPT**: AMA-published procedure codes (requires license)
- **CVX**: CDC vaccine codes for Immunization resources
- **FHIR Terminology Services**: CodeSystem, ValueSet, ConceptMap resources; $lookup, $validate-code, $expand, $translate operations
- **CodeableConcept**: Multi-coding data type carrying codes from multiple systems simultaneously
- **Epic Internal Code Mapping**: Masterfile records, crosswalks, Identity ID Types (IIT)

---

## Section 2: Core Standards and Security (Intermediate)

### D-4: FHIR R4 Specification and Data Model
- **FHIR Resource Model**: ~150 resource types, JSON/XML serialization, References, extensions, contained resources
- **RESTful API Interactions**: CRUD (GET/POST/PUT/PATCH/DELETE), Bundle transactions/batches, conditional operations, versioning with ETag/If-Match
- **FHIR Search**: Parameter types (string/token/date/reference/quantity), modifiers (:exact/:contains/:missing), chaining, _include/_revinclude, pagination
- **US Core Profiles and USCDI**: Must Support obligations, USCDI v1-v5, profile validation
- **Epic FHIR Implementation**: fhir.epic.com, CapabilityStatement per site, write-back for select resources, rate limits, Epic-specific extensions
- **FHIR Client Libraries**: client-js (JS), fhirclient (Python), HAPI FHIR (Java), Firely SDK (.NET), FHIRPath

### D-5: OAuth 2.0 Security Standards and Epic Auth
- **OAuth 2.0 Core**: Authorization code flow, client credentials, access/refresh tokens, scopes, redirect URIs
- **PKCE (RFC 7636)**: code_verifier/code_challenge, S256 method, mandatory for SMART apps
- **SMART on FHIR Authorization**: FHIR-aware scopes (patient/user/system), .well-known/smart-configuration, launch context, OpenID Connect fhirUser claim
- **JWT Backend Service Auth (RFC 7523)**: client_credentials with JWT assertions, RS384 signing, 5-minute expiry, system-level scopes
- **JWKS and Key Management**: JWKS URL vs static upload, key rotation, kid matching, HSM storage
- **Token Lifecycle**: Caching, refresh strategies, secure storage (memory only), no PHI in logs

---

## Section 3: Application Development and Interfaces (Intermediate)

### D-6: SMART on FHIR App Development
- **SMART App Launch Framework**: HL7 SMART App Launch IG v2.2.0, app registration, launch negotiation
- **EHR Launch and Standalone Launch**: Opaque launch parameter vs launch/patient scope, context inheritance
- **Embedded Rendering**: Hyperspace/Hyperdrive iframes, MyChart web/mobile, cross-origin restrictions, responsive design
- **SMART Web Messaging**: postMessage protocol, scratchpad.create/read/update/delete, ui.done, targetOrigin security
- **Multi-Tenant SMART Architecture**: Configuration-driven tenant management, dynamic endpoint discovery, token isolation, FHIR normalization

### D-7: HL7v2 Interfaces and Integration Engines
- **HL7v2 Message Structure**: Segments (MSH/PID/PV1/ORC/OBR/OBX), pipe-delimited format, components/sub-components, Z-segments
- **Message Types**: ADT (A01-A40), ORM (O01), ORU (R01), SIU (S12-S26), MDM (T01-T11)
- **MLLP Transport**: TCP framing (SB/EB/CR), synchronous acknowledgment
- **ACK/NAK Patterns**: AA/AE/AR codes, exponential backoff retry, dead letter queues
- **Integration Engines**: Mirth Connect/NextGen Connect, Rhapsody, InterSystems Health Connect, Epic Bridges/Space Bridge

---

## Section 4: Advanced Integration Patterns (Advanced)

### D-8: CDS Hooks and Clinical Decision Support
- **CDS Hooks Architecture**: CDS Client/Service roles, discovery endpoint, RESTful interaction
- **Hook Types**: patient-view, order-select, order-sign (Epic-supported)
- **Card Response Types**: Information, suggestion (one-click FHIR actions), app link (SMART launch)
- **Prefetch Mechanism**: Token resolution, performance optimization, 500ms response target
- **CDS 5 Rights Framework**: Right Information/Person/Channel/Format/Time
- **Alert Fatigue**: Suppression logic, feedback analytics, contextual relevance

### D-9: Epic Interconnect, MyChart, and Proprietary APIs
- **Interconnect Architecture**: Web services gateway, REST/SOAP endpoints, per-customer instances
- **Chronicles Database**: Hierarchical (MUMPS-derived), master files (EPT/ORD/SER/DEP/EAF), records/items/contacts
- **Clarity and Caboodle**: SQL relational copy (18K+ tables, nightly refresh) vs dimensional EDW (star schema)
- **MyChart APIs**: Patient authentication, scheduling, messaging, MyChart Central cross-org identity
- **OpenScheduling**: Appointment.$find and Appointment.$book FHIR operations
- **In-Basket and SmartForms**: Clinical messaging, structured data capture, Hyperdrive integration

### D-10: Bulk Data Analytics and Population Health
- **FHIR Bulk Data Export**: Async workflow (kick-off → poll → download NDJSON), _type/_typeFilter/_since parameters, 2-week retention
- **SMART Backend Services**: JWT-based system auth for unattended bulk operations
- **Cogito Analytics Suite**: Reporting Workbench, SlicerDicer, Radar dashboards
- **Healthy Planet**: Population health management, risk stratification, care gap identification
- **ML Data Extraction**: ETL pipelines (Chronicles → Clarity → Cloud Data Lake → Feature Store → ML), NLP on clinical notes, federated learning
- **De-identification**: Safe Harbor (18 identifiers) vs Expert Determination, Limited Data Sets, NLP-based text scrubbing

### D-11: Clinical Workflow Embedding and Advanced Patterns
- **BPA Triggering from External Systems**: Indirect triggering via FHIR data filing, CDS Hooks to BPA action mapping
- **Orders Integration**: ServiceRequest (labs/imaging/procedures), MedicationRequest (medications), order lifecycle
- **Clinical Documentation**: DocumentReference.Create for note filing, AI scribe integration (draft-only, human-in-the-loop)
- **Data Writeback**: Observation.Create for flowsheet filing, encounter linkage, UCUM units, patient-entered flowsheets
- **Bi-directional Workflow Patterns**: CDS→SMART→writeback loops, closed-loop orders, ADT-triggered workflows, FHIR Subscriptions

---

## Section 5: Distribution and Operations (Advanced/Expert)

### D-12: App Orchard Showroom and Epic Distribution
- **Showroom Tiers**: Cornerstone Partners → Workshop → Toolbox → Connection Hub ($500/yr)
- **Blueprint and Vendor Services**: Blueprint recommended practices, $1,900/yr Vendor Services program
- **Security Review**: TLS 1.2+, OAuth PKCE, encryption at rest, vulnerability management
- **SOC 2 Compliance**: Type 2 operational effectiveness, Trust Services Criteria, de facto industry requirement
- **ONC Certification**: 170.315(g)(10), USCDI v3 mandate by January 2026
- **Client ID Lifecycle**: Registration → development → customer activation → production go-live

### D-13: Multi-Tenant Operations and Go-Live
- **Multi-Tenant Architecture**: Data isolation models, tenant routing, configuration per Epic instance
- **Epic Deployment Models**: Community Connect (shared instance), Garden Plot (SaaS)
- **Configuration Variability**: Module activation differences, FHIR resource availability, terminology mappings
- **Version Management**: Quarterly upgrades, version fragmentation, backward compatibility (2-3 versions)
- **Go-Live Process**: Pre-go-live (4-8 weeks testing), event (command center, ATE support), post-go-live (2-6 weeks stabilization)
- **Integration Testing**: Unit → Integration → SIT → UAT → Performance → Security → Regression

### D-14: Production Operations, Monitoring, and Reliability
- **Observability**: Three pillars (metrics/logs/traces), OpenTelemetry, SLIs/SLOs/SLAs, error budgets
- **HIPAA-Compliant Logging**: PHI-free logs, 6-year retention, WORM storage, data masking/redaction
- **Resilience Patterns**: Retry with exponential backoff, circuit breaker, bulkhead isolation, idempotent operations
- **Incident Response**: NIST framework, HIPAA breach notification (60-day timeline), blameless post-mortems
- **Scaling and DR**: Horizontal scaling, connection pooling, RPO/RTO targets, graceful degradation

---

## Section 6: Architecture and Mastery (Expert)

### D-15: Integration Architecture and Mastery Synthesis
- **Integration Surface Selection**: Decision matrix across data direction, latency, granularity, write-back, regulatory fit
- **Hybrid Architecture Patterns**: HL7v2+FHIR enrichment, SMART+CDS Hooks combo, FHIR facade, Bulk+real-time
- **HL7v2 to FHIR Migration**: Four-phase approach (assess → shadow → cutover → decommission)
- **Reference Architectures**: CDS app, RPM platform, population health pipeline, patient mobile app, lab modernization
- **Technology Strategy**: FHIR-first posture, cloud platform selection (GCP/Azure/AWS), maturity model (Level 1-5)
- **Integration Maturity Model**: Ad Hoc → Managed → Standardized → Optimized → Innovating
