# D-9: Epic Interconnect, MyChart, and Proprietary APIs

## Overview

This domain covers Epic's proprietary integration surfaces beyond the open FHIR standard — the Interconnect gateway, MyChart patient portal APIs, OpenScheduling, Chronicles database concepts, SmartForms, and In-Basket messaging. These are the Epic-specific layers that external application developers must understand to build deeply integrated solutions that go beyond what standard FHIR endpoints offer.

**Why this matters for integrators:** While FHIR covers a growing share of Epic integration use cases, many production workflows — scheduling, billing, messaging, clinical documentation — still require or benefit from Epic's proprietary APIs exposed through Interconnect. Understanding Chronicles is essential for debugging data issues and knowing what data is available where.

---

## Key Concepts

### 1. Epic Interconnect Architecture

**Interconnect** is Epic's proprietary web services gateway — a middleware layer that exposes both REST and SOAP endpoints for workflows not fully covered by FHIR.

- **Role:** Sits between external applications and the Epic backend (Chronicles). Handles authentication, routing, and protocol translation.
- **REST vs SOAP:** Modern Interconnect services use REST with JSON; legacy services use SOAP with WSDL/XSD contracts. New development should target REST where available.
- **Federated model:** There is no central Epic API endpoint. Each Epic customer organization runs its own Interconnect instance. Developers must connect to each organization individually.
- **Relationship to FHIR:** Epic's FHIR APIs are served through Interconnect. The FHIR surface is a standardized subset of what Interconnect can do. Proprietary Interconnect web services cover workflows where FHIR specifications don't yet exist (billing, advanced scheduling, In-Basket).
- **Client IDs:** Every application connecting through Interconnect must have a registered client ID obtained via open.epic.com. The client ID defines allowed scopes and is synced to individual customer instances.
- **Performance:** Interconnect must handle high-throughput clinical workflows. External integrations are subject to rate limiting and must not degrade clinical system performance.

### 2. Chronicles Database

**Chronicles** is Epic's core transactional database — a proprietary hierarchical (non-relational) database built on InterSystems Caché/IRIS, descended from MUMPS.

- **Master Files (INIs):** The fundamental organizational unit. Each master file stores records of a specific entity type:
  - **EPT** — Patient records
  - **ORD** — Orders
  - **EMP** — Users/employees
  - **SER** — Providers
  - **DEP** — Departments
  - **EAF** — Appointment records
- **Records:** Individual instances within a master file (e.g., one patient = one EPT record).
- **Items:** Data fields within a record (e.g., "Date of Birth", "Specialty"). Items can be single-valued or multi-valued.
- **Contacts:** Time-stamped snapshots within records, often corresponding to encounters/visits.
- **Dynamic vs Static master files:** Dynamic files store transactional/patient data; static files store configuration and reference data.
- **Why integrators care:** You never query Chronicles directly. But understanding its structure explains why certain FHIR resources map oddly to Epic data, why some data isn't available via API, and why different Epic instances return different data for the same API call.

**Companion databases:**
- **Clarity:** SQL-based relational database extracted from Chronicles for reporting. Refresh cycles vary (often nightly).
- **Caboodle:** Enterprise data warehouse for long-term analytics built on top of Clarity extracts.

### 3. MyChart APIs

**MyChart** is Epic's patient-facing portal. MyChart APIs enable patient-initiated workflows:

- **Patient authentication:** MyChart credentials (username/password) or SMART on FHIR standalone launch with patient authorization.
- **Capabilities:** Appointment viewing/scheduling, secure messaging with providers, lab results access, medication lists, billing/payments, proxy access for dependents.
- **MyChart Central:** Epic's initiative to allow a single Epic-issued ID to connect MyChart records across multiple provider organizations — important for apps that aggregate patient data.
- **Embedded apps:** Third-party apps can be surfaced inside the MyChart portal. When launched from MyChart, the patient is already authenticated, simplifying the OAuth flow.

### 4. MyChart APIs vs FHIR Patient Access API

| Aspect | MyChart APIs | FHIR Patient Access API |
|--------|-------------|------------------------|
| **Standard** | Mix of FHIR + Epic proprietary | Strictly HL7 FHIR R4 + US Core IG |
| **Regulatory driver** | Epic product strategy | CMS Interoperability Rule mandate |
| **Data scope** | Full clinical + scheduling + messaging + billing | Claims, encounters, formulary, USCDI clinical subset |
| **Authentication** | MyChart credentials, SAML, SMART on FHIR | OAuth 2.0 + OpenID Connect |
| **Write operations** | Yes (scheduling, messaging, vitals filing) | Primarily read-only |
| **Portability** | Epic-specific | Works across any compliant EHR/payer |
| **Best for** | Deep Epic-embedded patient apps | Cross-vendor patient data aggregation |

**Key insight for developers:** If your app only targets Epic health systems and needs write capabilities (scheduling, messaging), MyChart APIs offer richer functionality. If you need to work across multiple EHR vendors, build on the standard FHIR Patient Access API and accept the reduced scope.

### 5. OpenScheduling

**OpenScheduling** enables patient self-scheduling through APIs, powering the scheduling flows in MyChart and third-party applications.

- **Core FHIR operations:**
  - `Appointment.$find` (STU3/R4) — Search available appointment slots by specialty, visit type, provider, location, date range
  - `Appointment.$book` (STU3/R4) — Book an appointment using a patient ID and slot from `$find` results
- **Workflow:** End user enters criteria → app calls `$find` → presents available slots → user selects → app calls `$book` → appointment confirmed
- **Integration with MyChart:** OpenScheduling slots surface in MyChart's self-scheduling flow. Third-party apps can offer the same scheduling experience.
- **Configuration dependency:** Available visit types, providers, and time slots are configured per Epic instance. Your app must handle variability across organizations.
- **Real-time availability:** Slots reflect live scheduling data from Chronicles, not cached/stale data.

### 6. SmartForms

**SmartForms** are Epic's structured data capture templates used within clinical workflows:

- **Purpose:** Point-and-click clinical documentation that captures discrete, structured data rather than free-text narrative.
- **Types:** NoteWriter SmartForms (clinical documentation), Flowsheet SmartForms (regulatory/measurement data capture), Operative Log SmartForms, Delivery Summary SmartForms.
- **Clinical decision support:** SmartForms can embed dynamic, context-aware CDS logic — presenting tailored recommendations based on patient data.
- **Scripting:** Flowsheet SmartForms support complex scripting behaviors for conditional logic and calculated fields.
- **Integration relevance:** External apps typically don't create SmartForms but may need to read data captured via SmartForms through FHIR Observation or DocumentReference resources. Understanding SmartForms helps debug why clinical data appears in certain FHIR resource types.

### 7. In-Basket Messaging

**In-Basket** is Epic's internal messaging and task management system for clinical staff:

- **Message types:** Patient messages (from MyChart), staff-to-staff messages, system-generated alerts (results, orders needing signatures, referral notifications).
- **API integration approaches:**
  - FHIR Communication resources (limited)
  - HL7v2 MDM T02 messages for filing documents/messages
  - Epic In-Basket Accelerator (Salesforce integration example using FHIR + HL7v2)
- **MyChart In-Basket ART:** Epic's AI-powered auto-response drafting for patient messages — indicates a growing API surface for In-Basket interaction.
- **Integration patterns:** Third-party apps most commonly send messages *into* In-Basket (e.g., external triage results, referral notifications) rather than reading from it.

### 8. Hyperspace and Hyperdrive

- **Hyperspace:** Epic's Windows desktop client for clinicians. SMART on FHIR apps can launch embedded within Hyperspace.
- **Hyperdrive:** Epic's modern web-based client, replacing Hyperspace. Uses web technologies and supports embedded web apps more naturally.
- **Integration relevance:** Understanding the launch context (EHR launch vs standalone launch) affects how your app receives patient/encounter context and authentication tokens.

### 9. Care Everywhere

Epic's health information exchange (HIE) network for sharing patient data between Epic organizations and with non-Epic systems:

- Uses standard protocols (IHE XCA, XCPD, C-CDA documents)
- Enables query-based exchange between participating organizations
- External integrators don't directly use Care Everywhere APIs but should understand it as the mechanism that populates "outside records" in Epic

### 10. Epic Client Application Environment

- **Client IDs and Scopes:** Every integration requires a registered client ID with defined scopes
- **Non-production vs Production IDs:** Separate client IDs for sandbox testing and production
- **App Orchard (now Showroom):** Epic's marketplace for distributing third-party apps to Epic customers
- **Connection workflow:** Developer registers app → customer requests client ID sync → developer approves → customer configures on their instance

---

## Learning Resources

### Official Documentation and Portals

1. **Open.Epic Developer Portal**
   - URL: https://open.epic.com/
   - Type: Documentation portal
   - Description: Central hub for all Epic integration documentation, step-by-step developer guides, data sharing playbooks, and API/interface specifications. Start here for any Epic integration work.
   - Cost: Free

2. **Epic FHIR API Documentation (fhir.epic.com)**
   - URL: https://fhir.epic.com/
   - Type: API documentation + sandbox
   - Description: Complete FHIR API specifications, sandbox environment with test patients, client ID registration, and "Try It" interactive testing. Includes Appointment.$find and Appointment.$book specs for OpenScheduling.
   - Cost: Free

3. **Epic FHIR Appointment.$find Specification**
   - URL: https://fhir.epic.com/Specifications?api=839
   - Type: API reference
   - Description: Detailed specification for the OpenScheduling slot search operation, including parameters, examples, and version-specific behavior.
   - Cost: Free

4. **Epic FHIR Appointment.$book Specification**
   - URL: https://fhir.epic.com/Specifications?api=840
   - Type: API reference
   - Description: Specification for booking appointments via the OpenScheduling API.
   - Cost: Free

5. **Open.Epic Developer Resources Page**
   - URL: https://open.epic.com/DeveloperResources
   - Type: Documentation hub
   - Description: Step-by-step developer guide, playbooks for common integration patterns, and links to all API specifications.
   - Cost: Free

### Technical Guides and Articles

6. **DreamFactory: How to Securely Access and Unlock Epic EpicCare Data (2025 Guide)**
   - URL: https://blog.dreamfactory.com/how-to-securely-access-and-unlock-epic-epiccare-data-2025-guide-to-integration-options-for-apps-ai-and-analytics
   - Type: Technical article
   - Description: Comprehensive overview of Epic integration options covering Chronicles, Clarity, Caboodle, FHIR APIs, and Interconnect. Good for understanding the full landscape of data access methods.
   - Cost: Free

7. **Joshua Mandel: Epic Data Architecture (EHI Living Manual)**
   - URL: https://joshuamandel.com/ehi-living-manual/00-04-epic-data-architecture/
   - Type: Technical reference
   - Description: Detailed explanation of Epic's Chronicles data architecture from a health IT expert. Covers master files, items, contacts, and how data flows between Chronicles, Clarity, and Caboodle.
   - Cost: Free

8. **Surety Systems: The Backbone of Epic — Understanding Chronicles**
   - URL: https://www.suretysystems.com/insights/the-backbone-of-epic-understanding-the-role-of-epic-chronicles/
   - Type: Technical article
   - Description: Accessible explanation of Chronicles architecture, its role in Epic's EHR platform, and how it relates to other Epic databases.
   - Cost: Free

9. **Dash Technologies: Epic EHR API Integration Guide (eBook)**
   - URL: https://dashtechinc.com/ebook/epic-ehr-api-integration-a-step-by-step-guide/
   - Type: eBook / guide
   - Description: Step-by-step integration guide covering Epic's FHIR-based API ecosystem, SMART on FHIR setup, and authentication methods.
   - Cost: Free (download)

### Video Tutorials

10. **YouTube: How to Implement EPIC EHR/EMR Integration with Your Health App System**
    - URL: https://www.youtube.com/watch?v=VTkV_7PYyJA
    - Type: Video tutorial
    - Description: Overview of Epic EHR integration approaches, API integration patterns, and step-by-step design walkthrough.
    - Cost: Free

11. **YouTube: Epic Chronicles Database Architecture Explained**
    - URL: https://www.youtube.com/watch?v=UtDRlaKiwd0
    - Type: Video tutorial
    - Description: Visual explanation of Chronicles database concepts including master files, records, items, and contacts.
    - Cost: Free

12. **YouTube: Epic EHR Integration Using FHIR APIs and OAuth 2.0 (Webinar)**
    - URL: https://www.youtube.com/watch?v=mbjXXvsa5I8
    - Type: Webinar recording
    - Description: Live demonstration of Epic integration using FHIR APIs with OAuth 2.0 authentication, including hands-on examples.
    - Cost: Free

### Code Examples and Repositories

13. **GitHub: Epic In-Basket Accelerator (Salesforce)**
    - URL: https://github.com/healthcare-and-life-sciences/epic-in-basket
    - Type: Code repository
    - Description: Reference implementation showing how to send In-Basket messages to Epic from Salesforce using FHIR APIs and HL7v2 interfaces. Demonstrates practical In-Basket integration patterns.
    - Cost: Free / open source

14. **Stack Overflow: Connect to Epic Medical System via Interconnect**
    - URL: https://stackoverflow.com/questions/18495878/connect-to-epic-medical-system-via-interconnect
    - Type: Community Q&A
    - Description: Developer discussion about connecting to Epic via Interconnect web services, including practical insights about WSDL access and authentication. Older but still relevant for understanding Interconnect fundamentals.
    - Cost: Free

### Community and Reference

15. **Connect Care Builders: Epic Master Files Reference**
    - URL: https://builders.connect-care.ca/Resources/master-files
    - Type: Reference documentation
    - Description: Practical reference for Epic master file concepts, useful for understanding how Chronicles structures map to the data you access through APIs.
    - Cost: Free

16. **Spritle Software: How to Integrate with EPIC EHR Using Python and SMART on FHIR APIs**
    - URL: https://www.spritle.com/blog/how-to-integrate-with-epic-ehr-using-python-and-smart-on-fhir-apis/
    - Type: Technical tutorial
    - Description: Hands-on guide for Python developers covering app registration, JWT authentication, and FHIR API calls against Epic. Includes code examples.
    - Cost: Free

---

## Learning Path

### Phase 1: Chronicles and Data Architecture Foundations (3–4 hours)

**Goal:** Understand how Epic stores data internally so you can reason about what's available via APIs.

1. Read the Joshua Mandel EHI data architecture guide
2. Watch the Chronicles database architecture video
3. Study master file concepts (EPT, ORD, SER, DEP, EAF)
4. Understand the Chronicles → Clarity → Caboodle data flow
5. Learn the difference between dynamic and static master files

**Milestone:** Can explain why the same patient data might appear differently in a FHIR API response vs a Clarity SQL query.

### Phase 2: Interconnect Architecture (2–3 hours)

**Goal:** Understand how Interconnect sits between your app and Chronicles.

1. Review the Open.Epic developer resources and architecture overview
2. Read the DreamFactory integration guide for the full landscape
3. Study the federated model — understand that each customer = separate endpoint
4. Review client ID registration process on open.epic.com
5. Understand REST vs SOAP service availability

**Milestone:** Can diagram the request flow from external app → Interconnect → Chronicles and back.

### Phase 3: MyChart APIs and Patient Access (3–4 hours)

**Goal:** Know when to use MyChart APIs vs standard FHIR Patient Access.

1. Review MyChart API documentation on fhir.epic.com
2. Study the MyChart vs FHIR Patient Access comparison table (above)
3. Understand MyChart authentication flows (embedded vs standalone)
4. Learn about MyChart Central and cross-organization identity
5. Review the Patient-Facing Consumer Health Apps Playbook on open.epic.com

**Milestone:** Can make an informed architectural decision about MyChart APIs vs FHIR Patient Access for a given use case.

### Phase 4: OpenScheduling (3–4 hours)

**Goal:** Be able to implement patient self-scheduling against Epic.

1. Read the Appointment.$find specification on fhir.epic.com
2. Read the Appointment.$book specification
3. Test both operations in the Epic FHIR sandbox
4. Understand configuration dependencies (visit types, providers vary by organization)
5. Study error handling for scheduling conflicts and unavailable slots

**Milestone:** Can execute a complete $find → select slot → $book flow in the sandbox.

### Phase 5: SmartForms, In-Basket, and Advanced Integration (3–4 hours)

**Goal:** Understand Epic's clinical workflow integration surfaces.

1. Study SmartForms concepts and how they capture structured data
2. Review the Epic In-Basket Accelerator on GitHub
3. Understand In-Basket message types and integration patterns (FHIR + HL7v2)
4. Learn about Hyperspace vs Hyperdrive launch contexts
5. Review Care Everywhere as it affects "outside records" data

**Milestone:** Can describe how to send a notification into a provider's In-Basket from an external system.

### Total estimated time: 14–19 hours

---

## Practical Exercises

### Exercise 1: Chronicles Data Model Mapping
**Difficulty:** Beginner | **Time:** 1 hour

Map 5 common FHIR resources (Patient, Encounter, Observation, MedicationRequest, Appointment) to their likely Chronicles master file origins (EPT, contacts, ORD, EAF). Document which data fields might not map cleanly and why.

### Exercise 2: OpenScheduling Sandbox Walkthrough
**Difficulty:** Intermediate | **Time:** 2 hours

Using the Epic FHIR sandbox at fhir.epic.com:
1. Call `Appointment.$find` with different specialty and date range parameters
2. Parse the response to extract available slots
3. Call `Appointment.$book` to schedule an appointment
4. Handle error cases (no slots available, invalid patient ID, conflict)
5. Document the full request/response flow

### Exercise 3: MyChart vs FHIR Decision Matrix
**Difficulty:** Intermediate | **Time:** 1.5 hours

Given three scenarios, determine the optimal API surface:
- A patient-facing wellness app that works with Epic and Cerner
- A custom scheduling widget embedded in an Epic hospital's website
- A clinical trial recruitment tool that reads patient data from 50 Epic sites

For each, document: which APIs to use, authentication approach, data available, and trade-offs.

### Exercise 4: In-Basket Integration Design
**Difficulty:** Advanced | **Time:** 2 hours

Design an integration that sends external lab results into a provider's In-Basket:
1. Review the Epic In-Basket Accelerator code on GitHub
2. Design the message flow (your system → HL7v2 MDM T02 or FHIR → Epic In-Basket)
3. Define the data mapping (external lab format → Epic In-Basket message)
4. Document authentication, error handling, and retry logic
5. Consider multi-site deployment (how does this work across different Epic instances?)

### Exercise 5: End-to-End Integration Architecture
**Difficulty:** Advanced | **Time:** 3 hours

Design a complete integration architecture for a telehealth app that:
- Allows patients to self-schedule via OpenScheduling
- Launches embedded in MyChart for authenticated patients
- Sends visit summaries to the provider's In-Basket after the visit
- Reads patient medications and allergies via FHIR
- Works across 3 different Epic health systems with different configurations

Document: API surface choices, authentication flows, data model, configuration management, and deployment strategy per site.

---

## Connections to Other Domains

- **D-4 (FHIR R4):** Interconnect serves FHIR APIs; understanding FHIR resources is prerequisite to using any Epic API
- **D-5 (OAuth 2.0 / Epic Auth):** All Interconnect and MyChart API calls require proper OAuth 2.0 authentication
- **D-6 (SMART on FHIR):** EHR launch context in Hyperspace/Hyperdrive uses SMART on FHIR; MyChart embedded apps use SMART standalone launch
- **D-7 (HL7v2):** In-Basket integration often requires HL7v2 messages alongside FHIR; legacy Interconnect services may use HL7v2 patterns
- **D-8 (CDS Hooks):** SmartForms and In-Basket alerts relate to clinical decision support embedded in Epic workflows
