# Healthcare Interoperability Foundations

## Domain Overview

This foundational domain covers the purpose of Electronic Health Record (EHR) systems, the history of healthcare data exchange, core clinical data concepts, and a comprehensive overview of every integration surface Epic exposes. Mastery of these foundations is essential before diving into specific standards (FHIR, HL7v2), authentication (OAuth/SMART), or Epic-specific tooling in later domains.

**Relevance to Epic Integration:** Every integration you build with Epic sits on top of these foundational concepts. Understanding *why* healthcare data exchange works the way it does — the regulatory drivers, the historical baggage, and the clinical workflows that generate data — prevents costly architectural mistakes and helps you navigate Epic's federated model.

---

## Key Concepts

### 1. Electronic Health Records (EHRs)

- **Purpose:** Digital longitudinal record of a patient's health information, replacing paper charts. Supports clinical decision-making, care coordination, quality reporting, and billing.
- **EHR vs EMR:** EMR (Electronic Medical Record) is a single-practice digital chart; EHR implies interoperability — sharing data across organizational boundaries.
- **Major EHR vendors:** Epic Systems, Oracle Health (Cerner), MEDITECH, Allscripts/Veradigm, athenahealth. Epic holds ~38% of the US acute care market.
- **Key EHR modules:** Registration/scheduling, clinical documentation, CPOE (Computerized Provider Order Entry), pharmacy, lab, radiology, billing/revenue cycle.

### 2. History of Healthcare Data Exchange

- **1960s–1970s:** Early mainframe clinical systems at academic centers. VA develops VistA (Decentralized Hospital Computer Program).
- **1980s–1990s:** HL7 v2 standard emerges (1987). Institute of Medicine publishes landmark reports advocating electronic records (1991, 1997). HIPAA (1996) establishes electronic transaction standards and privacy rules.
- **2000s:** Growth of Health Information Exchanges (HIEs). IHE (Integrating the Healthcare Enterprise) profiles provide implementation guidance.
- **2009:** HITECH Act provides $27B in incentive payments ("Meaningful Use") to drive EHR adoption. US hospital EHR adoption jumps from ~10% to >95%.
- **2014–2016:** HL7 FHIR standard published. 21st Century Cures Act (2016) mandates open APIs and prohibits information blocking.
- **2020–present:** ONC Cures Act Final Rule. TEFCA launches. USCDI becomes the baseline dataset. Information blocking enforcement begins (Sep 2023). HTI-1 rule (Jan 2024) further advances requirements.

### 3. Healthcare Interoperability Levels

- **Foundational:** System A can send data to System B (transport-level connectivity).
- **Structural:** Data arrives in a standardized format (e.g., HL7v2 message segments, C-CDA XML structure).
- **Semantic:** Both systems interpret the data identically (shared terminologies like SNOMED CT, LOINC, ICD-10, RxNorm).
- **Organizational:** Governance, policy, and legal frameworks enable trust (e.g., TEFCA, BAAs, data use agreements).

### 4. Clinical Data Concepts

- **Patient demographics:** Name, DOB, sex, address, identifiers (MRN, SSN). Carried in HL7 PID segments and FHIR Patient resources.
- **ADT events:** Admission, Discharge, Transfer — the fundamental "patient movement" messages that trigger downstream workflows.
- **Orders and results:** ORM (Order Entry) and ORU (Observation Result) messages. The order-result cycle is the backbone of lab, radiology, and pharmacy integrations.
- **Clinical documents:** Discharge summaries, progress notes, operative reports. Exchanged as C-CDA (Consolidated Clinical Document Architecture) documents or FHIR DocumentReference resources.
- **Medications:** Prescriptions, medication administration records, allergy lists. Critical for clinical decision support.
- **Problems/Diagnoses:** Coded conditions (ICD-10, SNOMED CT) that drive billing, quality measures, and care plans.
- **Vital signs and observations:** Height, weight, blood pressure, temperature, pulse oximetry — mapped to LOINC codes in FHIR Observation resources.

### 5. Key Standards Organizations

- **HL7 International:** Publishes HL7v2, v3, CDA, and FHIR standards.
- **IHE (Integrating the Healthcare Enterprise):** Creates implementation profiles (XDS, XCA, PIX/PDQ) that specify how standards are used together.
- **ONC (Office of the National Coordinator):** US federal agency that sets interoperability policy, manages USCDI, and certifies health IT.
- **SMART Health IT:** Developed the SMART on FHIR app launch framework (originated at Harvard/Boston Children's).
- **Argonaut Project:** Industry collaborative (including Epic) that accelerated FHIR adoption by defining implementation guides.

### 6. Regulatory Drivers

- **HIPAA (1996):** Privacy Rule, Security Rule, and electronic transaction standards.
- **HITECH Act (2009):** Meaningful Use incentives, breach notification requirements.
- **21st Century Cures Act (2016):** Anti-information-blocking, patient access API mandates, USCDI.
- **ONC Cures Act Final Rule (2020):** Conditions of certification, standardized API requirements (FHIR R4-based).
- **CMS Interoperability Rules:** Patient access API, provider directory API, payer-to-payer data exchange.
- **HTI-1 Rule (2024):** Algorithm transparency, updated certification criteria, USCDI v3.

### 7. Epic Integration Surfaces — Complete Overview

| Integration Surface | Protocol/Standard | Direction | Description |
|---|---|---|---|
| **FHIR R4 APIs** | REST/JSON (FHIR R4) | Read/Write | Primary modern API. 750+ endpoints on open.epic.com. Supports USCDI data classes. Used for patient access, clinical data queries, and write-back. |
| **SMART on FHIR Apps** | OAuth 2.0 + FHIR | Embedded | Third-party apps launched inside Epic Hyperspace (EHR client) or MyChart. Receive auth token + FHIR server URL. |
| **CDS Hooks** | REST/JSON | Event-driven | Clinical decision support triggered by EHR workflow events (patient-open, order-select, etc.). Returns "cards" with recommendations or app launch links. |
| **HL7v2 Interfaces** | TCP/MLLP (HL7v2) | Bidirectional | Traditional message-based integration. ADT (A01-A08), ORM, ORU, SIU, MDM, DFT messages. Configured via Epic Bridges. |
| **Epic Bridges** | HL7v2/DICOM | Bidirectional | Epic's native interface engine for configuring HL7v2 and DICOM connections to/from Epic. Paired with Space Bridge for message transformations. |
| **Care Everywhere** | IHE XCA/XDS.b, C-CDA, FHIR | Query-based | Cross-organization patient data exchange. 20M+ records/day. Works with both Epic and non-Epic systems. |
| **MyChart APIs** | FHIR R4 + OAuth 2.0 | Patient-directed | Patient-facing API access. Patients authorize third-party apps via MyChart credentials. Supports read and limited write (e.g., vitals filing). |
| **Epic Web Services** | SOAP/REST | Various | Purpose-built proprietary web services for specific functions (personnel management, document retrieval, fax services, etc.). Listed at open.epic.com. |
| **Bulk FHIR** | FHIR Bulk Data ($export) | Read (batch) | Population-level data export in NDJSON format. Used for analytics, quality measures, and research. |
| **App Orchard / Showroom** | Marketplace | Distribution | Epic's marketplace for third-party app discovery and deployment. Organizations browse, evaluate, and connect apps to their Epic instance. |
| **Interconnect** | Middleware | Internal | Epic's web application server that hosts FHIR endpoints and web services. External requests route through Interconnect to the Epic backend. |

### 8. Epic's Federated Model

- Each Epic customer (health system) runs its own independent Epic instance.
- There is no central Epic "cloud" that all customers share (unlike some SaaS EHRs).
- Each health system controls which apps connect, which FHIR resources are exposed, and what data is available.
- This means your integration must handle per-site configuration differences, varying FHIR capability statements, and different approval processes.
- Client IDs from open.epic.com work across all Epic organizations, but each org must independently approve your app's connection.

### 9. USCDI (United States Core Data for Interoperability)

- The standardized minimum dataset that certified health IT must support for interoperability.
- USCDI v1 (2020): Patient demographics, allergies, medications, problems, procedures, lab results, vital signs, clinical notes, care team, immunizations, assessment/plan, goals, health concerns, procedures, provenance.
- Updated annually (v3 as of 2024, v5 in development) with expanding data classes.

### 10. Health Information Exchange Models

- **Query-based exchange:** Pull data on demand (e.g., Care Everywhere querying another system).
- **Directed exchange:** Push data to a known recipient (e.g., Direct messaging for referrals).
- **Consumer-mediated exchange:** Patient controls sharing (e.g., MyChart API, patient-authorized FHIR access).
- **TEFCA (Trusted Exchange Framework):** National framework for cross-network exchange via Qualified Health Information Networks (QHINs).

---

## Learning Resources

### Official Documentation and References

1. **ONC HealthIT.gov — Interoperability Portal**
   - URL: https://healthit.gov/interoperability/
   - Type: Reference / Policy documentation
   - Cost: Free
   - Description: Authoritative source for US interoperability policy, USCDI specifications, Cures Act Final Rule details, and TEFCA information. Essential for understanding the regulatory landscape that drives Epic integration requirements.

2. **Epic Open Developer Portal (open.epic.com)**
   - URL: https://open.epic.com/
   - Type: Developer documentation / Sandbox
   - Cost: Free
   - Description: Central hub for all Epic integration documentation. Browse FHIR APIs, HL7v2 interface specs, web services catalog, and register sandbox applications. This is where your hands-on Epic integration work begins.

3. **HL7 FHIR R4 Specification**
   - URL: https://hl7.org/fhir/R4/
   - Type: Technical specification
   - Cost: Free
   - Description: The complete FHIR R4 specification. Dense but essential reference for understanding resources, data types, search parameters, and RESTful patterns. Bookmark the resource index and capability statement pages.

### Online Courses and Tutorials

4. **InteropTrainer — Free HL7 FHIR Course**
   - URL: https://freecourse.interoptrainer.com/
   - Type: Interactive online course
   - Cost: Free
   - Description: Beginner-friendly comprehensive introduction to FHIR. No registration required. Covers resources, data types, RESTful operations, and search. Work-in-progress but regularly updated.

5. **ONC FHIR Education and Resource Page**
   - URL: https://ecqi.healthit.gov/fhir/education
   - Type: Educational portal with video series
   - Cost: Free
   - Description: ONC's curated FHIR educational materials including the eCQM FHIR Sparks video series and introductory resources. Good starting point for understanding FHIR in the regulatory context.

6. **Google for Developers — Getting Started with FHIR**
   - URL: https://developers.google.com/open-health-stack/resources/getting-started-with-fhir
   - Type: Tutorial / Resource compilation
   - Cost: Free
   - Description: Curated collection of materials to quickly understand FHIR from a developer perspective. Links to specification, implementation guides, and tools.

### Video Content

7. **Introduction to HL7 FHIR: A Tutorial for Beginners — Dr. Chris Paton (YouTube)**
   - URL: https://www.youtube.com/watch?v=wxXe1g2YjHo
   - Type: Video tutorial
   - Cost: Free
   - Duration: ~30 minutes
   - Description: Developed from ONC Curriculum Development Project content. Uses diagrams and screenshots to explain FHIR concepts for newcomers.

8. **FHIR Drills — Simple Patient Tutorial**
   - URL: https://fhir-drills.github.io/simple-patient.html
   - Type: Interactive hands-on exercise
   - Cost: Free
   - Description: Guided walkthrough of basic FHIR CRUD operations using a Patient resource. Excellent first hands-on exercise for developers new to FHIR.

### Books and Written Guides

9. **Smile Digital Health — Free FHIR Essentials Overview Guide**
   - URL: https://www.smiledigitalhealth.com/training/free-fhir-essentials-overview-guide
   - Type: Written guide (downloadable)
   - Cost: Free (registration may be required)
   - Description: In-depth introduction to FHIR concepts for both technical and non-technical audiences. Good companion to the specification itself.

10. **AMA Journal of Ethics — Development of Electronic Health Record (2011)**
    - URL: https://journalofethics.ama-assn.org/article/development-electronic-health-record/2011-03
    - Type: Journal article
    - Cost: Free
    - Description: Historical perspective on EHR development from the American Medical Association. Provides essential context for understanding why healthcare IT works the way it does.

### Community and Reference Resources

11. **HL7 Confluence — FHIR Implementation Guides**
    - URL: https://confluence.hl7.org/display/FHIR
    - Type: Community wiki / Reference
    - Cost: Free
    - Description: Central location for FHIR implementation guides, project pages, and community discussions. Essential for understanding how FHIR is profiled for specific US use cases (US Core, Da Vinci, etc.).

12. **SMART Health IT Documentation**
    - URL: https://docs.smarthealthit.org/
    - Type: Developer documentation
    - Cost: Free
    - Description: Official SMART on FHIR technical documentation. Covers the app launch framework, scopes, authorization, and tutorials. Foundation for Domain 6 (SMART on FHIR App Development).

---

## Learning Path

### Phase 1: Why Healthcare IT Is Different (Days 1–2, ~4 hours)

**Goal:** Understand the historical, regulatory, and organizational context that makes healthcare data exchange uniquely complex.

1. Read the AMA Journal of Ethics article on EHR development history
2. Browse ONC HealthIT.gov interoperability portal — understand USCDI, Cures Act, TEFCA
3. Learn the four levels of interoperability (foundational, structural, semantic, organizational)
4. Understand HIPAA basics as they relate to data exchange (Privacy Rule, Security Rule, minimum necessary)

**Milestone:** Can explain why healthcare interoperability is harder than typical API integration, name the major regulatory drivers, and describe what USCDI is.

### Phase 2: Clinical Data Concepts (Days 3–4, ~4 hours)

**Goal:** Understand the types of clinical data you'll be working with and how they flow through healthcare systems.

1. Learn core clinical data types: demographics, problems, medications, allergies, labs, vitals, notes, orders/results
2. Understand the ADT (Admit/Discharge/Transfer) event model — why it matters for integration
3. Learn about clinical coding systems at a high level: ICD-10, SNOMED CT, LOINC, RxNorm, CPT (detailed coverage in Domain 3)
4. Understand the concept of a patient encounter and the clinical workflow that generates data

**Milestone:** Can describe the major categories of clinical data, explain what an ADT event is, and name the primary coding systems used in US healthcare.

### Phase 3: Healthcare Data Exchange Standards Overview (Days 5–6, ~5 hours)

**Goal:** Get a bird's-eye view of the standards landscape before deep-diving into specific standards in later domains.

1. Watch Dr. Chris Paton's FHIR introductory video
2. Complete InteropTrainer's free FHIR course (first 3–4 modules)
3. Read Google's "Getting Started with FHIR" overview
4. Understand the relationship between HL7v2, HL7v3/CDA, and FHIR — why all three still exist
5. Learn what IHE profiles are and how they relate to HL7 standards

**Milestone:** Can explain the difference between HL7v2, CDA, and FHIR. Can describe what a FHIR resource is. Understands that standards exist at multiple layers (transport, content, terminology, workflow).

### Phase 4: Epic Integration Surfaces Map (Days 7–8, ~5 hours)

**Goal:** Know every way software can connect to Epic and when to use each approach.

1. Explore open.epic.com — browse the API catalog, read developer resources
2. Map all Epic integration surfaces (FHIR, HL7v2, SMART on FHIR, CDS Hooks, Care Everywhere, MyChart API, Web Services, Bridges, Bulk FHIR)
3. Understand Epic's federated model — each health system runs independently
4. Learn about App Orchard / Showroom and how third-party apps get distributed
5. Complete FHIR Drills "Simple Patient" tutorial using Epic's sandbox

**Milestone:** Can name all Epic integration surfaces, explain when you'd use each one, and describe how Epic's federated model affects integration architecture. Have successfully made at least one FHIR API call against Epic's sandbox.

---

## Practical Exercises

### Exercise 1: EHR Ecosystem Map (30 min)
Draw a diagram showing a typical hospital's data flow: patient registration → ADT messages → orders → results → clinical documentation → billing. Label which systems are involved (EHR, LIS, RIS, PAS, billing) and what data flows between them. This builds intuition for where integration points exist.

### Exercise 2: Explore open.epic.com (45 min)
1. Create a free account at open.epic.com
2. Browse the FHIR API catalog — note the available resource types
3. Read the HL7v2 interface specifications page
4. Explore the Web Services page
5. Document: How many FHIR resources does Epic support? What HL7v2 message types are listed? What proprietary web services are available?

### Exercise 3: First FHIR API Call (1 hour)
1. Go to FHIR Drills (https://fhir-drills.github.io/simple-patient.html)
2. Complete the Simple Patient tutorial
3. Then use Epic's open sandbox (fhir.epic.com) to query a Patient resource
4. Compare: What fields are available? What does Epic's capability statement say?

### Exercise 4: Standards Timeline (30 min)
Create a timeline of healthcare IT milestones: HL7v2 (1987), HIPAA (1996), HITECH/Meaningful Use (2009), FHIR DSTU1 (2014), 21st Century Cures Act (2016), ONC Final Rule (2020), Information Blocking Enforcement (2023). For each, write one sentence about its impact on integration developers.

### Exercise 5: Integration Surface Decision Matrix (45 min)
For each of these scenarios, identify which Epic integration surface(s) you would use and why:
- A patient-facing mobile app that shows lab results
- A clinical decision support tool that recommends medications
- A population health analytics platform that needs bulk data
- A lab system that sends results into Epic
- A specialist app launched from within the EHR during a patient encounter

---

## Connections to Other Domains

- **Domain 2 (Regulatory Landscape):** Builds directly on the regulatory drivers introduced here (HIPAA, Cures Act, ONC rules).
- **Domain 3 (Terminology Systems):** The coding systems mentioned here (ICD-10, SNOMED, LOINC) are covered in depth.
- **Domain 4 (FHIR R4):** Deep dive into the FHIR standard introduced in Phase 3.
- **Domain 5 (OAuth 2.0 / Epic Auth):** Authentication details for the FHIR APIs described here.
- **Domain 6 (SMART on FHIR):** The app launch framework for the embedded app surface described here.
- **Domain 7 (HL7v2):** Deep dive into the HL7v2 message-based integration surface.
- **Domain 12 (App Orchard / Showroom):** Distribution mechanism for apps built on these integration surfaces.
