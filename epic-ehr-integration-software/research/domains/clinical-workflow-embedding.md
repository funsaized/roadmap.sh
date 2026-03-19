# Clinical Workflow Embedding and Advanced Patterns

## Overview

This domain covers the advanced integration patterns that allow external software applications to embed deeply into Epic clinical workflows — beyond simple data reads and standalone apps. It encompasses Best Practice Alerts (BPAs) triggered by external system data, orders integration via FHIR ServiceRequest and MedicationRequest, clinical documentation filing including AI-generated content, data writeback through Observation.Create, and bi-directional workflow patterns combining CDS Hooks with SMART on FHIR apps.

Mastering this domain is critical for building applications that feel native to the clinician's workflow rather than being bolted-on tools that require context switching.

**Prerequisites:** Domains D-4 (FHIR R4), D-5 (OAuth/Auth), D-6 (SMART on FHIR), D-8 (CDS Hooks)

---

## Key Concepts

### 1. Best Practice Alerts (BPAs) from External Systems

- **BPA Architecture:** Epic BPAs consist of criteria records (conditions to evaluate) and base records (alert content/actions). External systems cannot directly trigger a BPA via API — instead, they submit data that satisfies BPA criteria.
- **Indirect BPA Triggering:** External apps push structured data (diagnoses, observations, lab results) into Epic via FHIR APIs. If this data meets pre-configured BPA criteria, the alert fires natively within Epic.
- **CDS Hooks as BPA Pathway:** The `com.epic.cdshooks.request.bpa-trigger-action` extension maps CDS Hooks to Epic's native BPA trigger actions (e.g., "Enter order," "Sign orders," "Open encounter section").
- **BPA Trigger Actions:** Common triggers include `patient-view`, `order-select`, `order-sign`, entering problems/diagnoses, and opening specific encounter sections.
- **Design Pattern:** External system → files Observation/Condition via FHIR → Epic evaluates BPA criteria → BPA fires to clinician → Clinician acts (optionally launching SMART app for details).

### 2. Orders Integration

- **FHIR ServiceRequest:** Used for non-medication orders (procedures, labs, imaging, microbiology, ancillary services). Supports `ServiceRequest.Search` for querying and `ServiceRequest.Create` for specific use cases.
- **FHIR MedicationRequest:** Covers all medication orders — inpatient, outpatient, OTC medications. Each resource instance represents one medication.
- **Order Lifecycle:** States include draft → active → completed/revoked/unknown. The `intent` field distinguishes proposals, plans, orders, filler-orders, and reflex-orders.
- **Incoming Orders from CPOE Systems:** Epic supports incoming order messages from external CPOE applications (e.g., remote device checks creating orders in Epic).
- **Order Categories and Codes:** Orders reference terminology systems (LOINC, SNOMED, CPT) for the specific service/medication. RxNorm is canonical for medications.
- **Order Details and Questions:** The `orderDetail` element carries additional instructions, questionnaire answers, and order-specific metadata.

### 3. Clinical Documentation Integration

- **DocumentReference.Create (Clinical Notes):** Files plain text clinical notes to open or closed encounters. Supports pre-charting (documentation before the visit).
- **DocumentReference.Search (Clinical Notes):** Retrieves existing notes for a patient, enabling AI systems to access prior documentation for context.
- **Binary Resource:** The actual note content is accessed via a Binary resource referenced within the DocumentReference.
- **Note Types:** Progress notes, visit summaries, discharge summaries, nursing notes — each with specific note type identifiers configured per Epic instance.
- **Pre-charting Pattern:** External systems file draft documentation before the encounter begins, reducing clinician documentation burden during the visit.

### 4. AI Content in Clinical Notes

- **Draft-Only Principle:** All AI-generated content filed into Epic must be treated as draft requiring clinician review and attestation. No automatic signatures.
- **Human-in-the-Loop Requirement:** Clinicians must review, edit, and explicitly attest to AI-generated notes before finalization. This is both a safety and medicolegal requirement.
- **Audit Trail:** Epic requires comprehensive auditing — who recorded audio, which model generated the draft, when edits were made, and who attested.
- **AI Scribe Integration Pattern:** Capture conversation → AI generates structured note → file via DocumentReference.Create → clinician reviews in Epic → clinician signs/attests.
- **Safety Concerns:** AI hallucinations, misattributed clinical information, bias from accents/language, and over-reliance on automation.
- **HIPAA/BAA Requirements:** AI vendors processing PHI need Business Associate Agreements. Data use for model training requires explicit patient authorization unless under treatment/payment/operations exceptions.
- **Patient Consent:** Informed consent for AI scribe use is recommended and often legally required. Patients should be able to opt out.

### 5. Data Writeback via Observation.Create

- **Flowsheet Filing:** `Observation.Create (Vitals)` files data to flowsheet rows. Supports vital signs, device readings, and other structured measurements.
- **Patient-Entered Flowsheets (PEFs):** Patient-facing apps write to PEFs, but an Epic user must first place an order to create the flowsheet episode.
- **Encounter Linkage:** Provider/backend apps require strict encounter matching via Encounter FHIR ID. Cannot write to closed encounters or future appointments.
- **Flowsheet Row Mapping:** Requires Epic Flowsheet IDs, Encoded Flowsheet IDs, or LOINC codes — obtained from Epic customer IT administrators during installation.
- **No Overwrite:** Unlike HL7v2, FHIR Observation.Create does not overwrite existing readings at the same timestamp.
- **Single Reading Limitation:** Patient-facing apps can file only one reading per request. For bulk filing, HL7v2 interfaces are recommended.
- **Value Types:** `valueQuantity` (numeric with UCUM units), `valueString`, `valueBoolean` — matching the flowsheet row's data type.

### 6. Bi-directional Workflow Patterns

- **CDS Hooks → SMART App Launch:** The canonical bi-directional pattern: Epic fires a CDS Hook at a workflow point → external CDS service returns a card → card includes a SMART app link → clinician launches the app → app reads/writes FHIR data back to Epic.
- **Data In + Guidance Out:** External system files data (Observation, Condition) → Epic evaluates → CDS Hook fires → external service provides contextual guidance → clinician acts.
- **Closed-Loop Pattern:** Order placed in Epic → CDS Hook fires → external system evaluates → returns recommendation → clinician accepts → order modified or new order created → result filed back.
- **Event-Driven via HL7v2:** ADT messages (admit/discharge/transfer) trigger external system actions → external system processes → files results back via FHIR APIs.
- **Subscription-Based:** FHIR Subscriptions (where supported) notify external systems of resource changes, enabling reactive workflows.

### 7. Epic Hyperdrive and Embedded App Experience

- **Hyperdrive Architecture:** Epic's modern Chromium-based Windows client replacing Hyperspace. Contains embedded browser for web-based SMART apps.
- **SMART App Compatibility:** SMART on FHIR apps generally work without code changes when transitioning from Hyperspace to Hyperdrive.
- **Speech Recognition API:** Hyperdrive provides APIs for speech recognition systems to interact with controls in embedded (iframed) non-Epic web applications.
- **Client Test Harness:** Available for validating E-Signature, Login, Voice Recognition, and SMART on FHIR integrations within the Hyperdrive environment.
- **Plugin Infrastructure:** Windows-native plugin system for deeper integrations (encoders, signature pads, etc.).

### 8. Alert Fatigue and Clinical Safety

- **Performance Target:** CDS service responses should complete within ~500ms to avoid disrupting clinical workflow.
- **Minimally Intrusive Design:** Cards should be actionable and contextually relevant. Avoid information-only cards that train clinicians to dismiss alerts.
- **Suppression Logic:** Implement logic to avoid re-alerting for conditions already acknowledged or acted upon.
- **Contextual Relevance:** Use prefetch data and patient context to ensure alerts are appropriate for the specific clinical scenario.

---

## Learning Resources

### Official Documentation

1. **Epic on FHIR — DocumentReference.Create (Clinical Notes)**
   - URL: https://fhir.epic.com/Specifications?api=1046
   - Type: API specification
   - Coverage: Filing clinical notes to patient charts via FHIR R4
   - Essential for: Understanding note filing mechanics and constraints

2. **Epic on FHIR — Observation.Create (Vitals)**
   - URL: https://fhir.epic.com/Specifications?api=963
   - Type: API specification
   - Coverage: Filing flowsheet data and vital signs from external apps
   - Essential for: Data writeback implementation

3. **Epic on FHIR — ServiceRequest API**
   - URL: https://fhir.epic.com/Specifications?api=1054
   - Type: API specification
   - Coverage: Non-medication order search and lifecycle
   - Essential for: Orders integration

4. **Epic Hyperdrive Developer Resources**
   - URL: https://open.epic.com/Hyperdrive
   - Type: Developer guide
   - Coverage: Hyperdrive client integration, test harness, migration from Hyperspace
   - Essential for: Understanding the embedded app runtime environment

5. **CDS Hooks Official Specification and Best Practices**
   - URL: https://cds-hooks.org/best-practices/
   - Type: Standard specification
   - Coverage: Hook definitions, card design, performance guidelines, alert fatigue mitigation
   - Essential for: Designing effective clinical decision support

### Tutorials and Guides

6. **Techno-Soft: Integrating SMART App with Epic — Step by Step**
   - URL: https://techno-soft.com/integrating-smart-app-with-epic.html
   - Type: Tutorial
   - Coverage: End-to-end SMART on FHIR app integration with Epic, including embedded workflow
   - Difficulty: Intermediate

7. **First Line Software: Options for Building and Integrating User-Facing Applications into Epic**
   - URL: https://firstlinesoftware.com/blog/options-for-building-and-integrating-user-facing-applications-into-epic-and-other-ehrs/
   - Type: Blog/guide
   - Coverage: Comparison of integration approaches (SMART, embedded, standalone)
   - Difficulty: Intermediate

8. **6b.health: Working with Epic FHIR Sandboxes and Production Endpoints**
   - URL: https://6b.health/insight/working-with-epic-fhir-sandboxes-production-endpoints-best-practices/
   - Type: Practical guide
   - Coverage: Testing strategies for FHIR integrations, sandbox vs production differences
   - Difficulty: Intermediate

### Video Content

9. **YouTube: Epic FHIR Integration Tutorial**
   - URL: https://www.youtube.com/watch?v=_LYP4G74NWw
   - Type: Video tutorial
   - Coverage: SMART on FHIR app registration, OAuth flow, and FHIR API calls with Epic
   - Difficulty: Beginner-Intermediate

10. **YouTube: Epic CDS Hooks Integration**
    - URL: https://www.youtube.com/watch?v=1HGcI4o0EyA
    - Type: Video
    - Coverage: CDS Hooks workflow, card design, real-time clinical decision support
    - Difficulty: Intermediate

### Industry Analysis and Safety

11. **Foley & Lardner: HIPAA Compliance Risks with AI Scribes in Healthcare**
    - URL: https://www.foley.com/p/102kdn0/hipaa-compliance-risks-with-ai-scribes-in-health-care-what-digital-health-leader/
    - Type: Legal analysis
    - Coverage: BAA requirements, PHI handling, model training restrictions, consent
    - Essential for: AI integration compliance

12. **Epic AI for Clinicians**
    - URL: https://www.epic.com/software/ai-clinicians/
    - Type: Product page
    - Coverage: Epic's native AI capabilities — charting, summarization, order suggestions
    - Essential for: Understanding Epic's AI strategy and integration expectations

13. **PubMed Central: AI Scribe Clinical Validation Study**
    - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12460601/
    - Type: Research paper
    - Coverage: Accuracy validation, safety considerations, clinical workflow impact
    - Difficulty: Advanced

### FHIR Standard References

14. **HL7 FHIR Build — ServiceRequest Resource**
    - URL: https://build.fhir.org/servicerequest-definitions.html
    - Type: Specification
    - Coverage: Full ServiceRequest resource definition, elements, and constraints
    - Essential for: Orders integration design

15. **HL7 FHIR Build — MedicationRequest Resource**
    - URL: https://build.fhir.org/medicationrequest.html
    - Type: Specification
    - Coverage: Full MedicationRequest resource definition for medication orders
    - Essential for: Medication ordering workflows

### Community and Ecosystem

16. **HIXNY: How SMART on FHIR Embeds Data in Clinical Workflows**
    - URL: https://hixny.org/how-smart-on-fhir-embeds-data-in-clinical-workflows/
    - Type: Industry article
    - Coverage: Real-world embedded app deployment patterns and lessons learned
    - Difficulty: Intermediate

17. **SiteRocket: CDS Hooks — Embedding Decision Support Directly in the EHR**
    - URL: https://www.siterocket.com/blog/cds-hooks-embedding-decision-support-directly-in-the-ehr
    - Type: Blog/guide
    - Coverage: Practical CDS Hooks implementation patterns, card design
    - Difficulty: Intermediate

---

## Learning Path

### Phase 1: Writeback Foundations (Week 1, ~8 hours)
1. Study the Observation.Create API spec — understand flowsheet filing, value types, encounter linkage
2. Study the DocumentReference.Create API — understand note filing, Binary resources, note types
3. Practice filing vitals and notes in the Epic sandbox environment
4. **Milestone:** Successfully file a vital sign reading and a clinical note via the sandbox API

### Phase 2: Orders Integration (Week 2, ~8 hours)
1. Study ServiceRequest and MedicationRequest FHIR resources (HL7 specs + Epic API docs)
2. Understand order lifecycle (draft → active → completed) and intent types
3. Implement order search queries filtered by patient, encounter, category, and status
4. Study incoming CPOE order patterns and Epic's order processing
5. **Milestone:** Query and interpret order data; understand the order creation flow

### Phase 3: BPA and CDS Integration Patterns (Week 2-3, ~10 hours)
1. Review Epic's BPA architecture — criteria records, base records, trigger actions
2. Map CDS Hooks to BPA trigger actions via `com.epic.cdshooks.request.bpa-trigger-action`
3. Design a complete BPA trigger pattern: external data filing → criteria evaluation → alert display
4. Implement a CDS Hook service that returns actionable cards with SMART app links
5. **Milestone:** Design a complete BPA trigger flow from external data through to clinician alert

### Phase 4: AI Documentation and Safety (Week 3-4, ~8 hours)
1. Study Epic's AI charting strategy and draft-only principles
2. Review HIPAA/BAA requirements for AI scribes (Foley & Lardner analysis)
3. Design an AI note integration: capture → generate → file → review → attest
4. Implement audit trail requirements: model provenance, edit history, attestation
5. Study patient consent requirements and opt-out mechanisms
6. **Milestone:** Design a compliant AI note filing workflow with all safety controls documented

### Phase 5: Bi-directional Workflows and Advanced Patterns (Week 4-5, ~10 hours)
1. Implement the full CDS Hooks → SMART app → FHIR writeback loop
2. Design closed-loop workflows (order → evaluate → recommend → modify → file result)
3. Study HL7v2 ADT-triggered workflows as complement to FHIR-based patterns
4. Understand Hyperdrive's embedded app environment and speech recognition APIs
5. Address alert fatigue: suppression logic, contextual relevance, performance optimization
6. **Milestone:** Working bi-directional prototype that reads context, provides guidance, and writes results back

### Phase 6: Production Readiness (Week 5-6, ~6 hours)
1. Test in sandbox then pilot in production-like environments
2. Validate flowsheet row mapping with customer IT administrators
3. Performance tune CDS service responses to <500ms target
4. Document deployment configuration requirements per Epic instance
5. **Milestone:** Production-ready integration checklist with all configuration points documented

**Total estimated time: 50 hours over 6 weeks**

---

## Practical Exercises

### Exercise 1: Flowsheet Data Filing
**Objective:** File vital signs from a simulated external device into Epic via Observation.Create
- Create an OAuth-authenticated client that connects to the Epic sandbox
- File heart rate, blood pressure (multi-component), and SpO2 readings
- Handle error cases: duplicate timestamps, missing encounter, invalid flowsheet IDs
- Verify filed data appears correctly in the patient's flowsheet
- **Deliverable:** Working code + error handling matrix

### Exercise 2: Clinical Note Filing with AI Content
**Objective:** Simulate an AI scribe workflow filing notes into Epic
- Generate a simulated clinical note (use a template with placeholder AI content)
- File it via DocumentReference.Create to an encounter
- Implement the review/attestation tracking layer
- Add audit fields: model name, generation timestamp, edit history
- Document the consent and BAA checklist
- **Deliverable:** Note filing service + compliance documentation

### Exercise 3: BPA Trigger Design
**Objective:** Design a complete BPA trigger pattern from an external risk scoring system
- Define a clinical scenario (e.g., sepsis risk score > threshold)
- Map the data flow: external system calculates risk → files Observation → Epic evaluates BPA criteria → alert fires
- Design the BPA criteria record and base record (document-level, not code)
- Create a CDS Hook service that provides the risk details when the BPA triggers
- **Deliverable:** Architecture diagram + CDS Hook implementation + BPA configuration specification

### Exercise 4: Bi-directional Order Workflow
**Objective:** Implement a closed-loop medication interaction checker
- Build a CDS Hook service listening on `order-sign`
- When triggered, evaluate the ordered medication against an external drug interaction database
- Return a card with interaction severity, affected medications, and a SMART app link for details
- In the SMART app, display interaction details and allow the clinician to modify or proceed
- **Deliverable:** CDS service + SMART app + integration test suite

### Exercise 5: Hyperdrive Embedded App Testing
**Objective:** Validate an existing SMART on FHIR app in the Hyperdrive environment
- Set up the Hyperdrive Client Test Harness
- Launch a SMART app from an EHR context and verify launch context parameters
- Test speech recognition API integration (if available)
- Document any behavioral differences from Hyperspace
- **Deliverable:** Test report with Hyperspace vs Hyperdrive comparison

---

## Connections to Other Domains

- **D-4 (FHIR R4):** All writeback and read patterns use FHIR resources — Observation, DocumentReference, ServiceRequest, MedicationRequest
- **D-5 (OAuth/Auth):** Every API call requires OAuth 2.0 authentication; scopes must match the intended writeback operations
- **D-6 (SMART on FHIR):** Embedded apps, EHR launch context, and the SMART app link from CDS cards all build on SMART foundations
- **D-7 (HL7v2):** HL7v2 interfaces remain important for bulk data filing, ADT-triggered workflows, and scenarios where FHIR has limitations
- **D-8 (CDS Hooks):** BPA trigger patterns and bi-directional workflows are direct extensions of CDS Hooks concepts
- **D-9 (Epic APIs):** Proprietary Epic APIs (encoders, speech recognition) complement standard FHIR patterns in the Hyperdrive environment
- **D-2 (Regulatory):** AI documentation integration requires deep understanding of HIPAA, BAA requirements, and emerging FDA guidance on clinical AI
