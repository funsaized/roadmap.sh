# CDS Hooks and Clinical Decision Support

## Overview

CDS Hooks is an HL7-published, open-source specification that enables real-time clinical decision support (CDS) directly within a clinician's EHR workflow. Rather than requiring clinicians to navigate to external systems, CDS Hooks uses a trigger-based ("hook") pattern: when a clinician performs a specific action in the EHR (opening a chart, selecting an order, signing orders), the EHR invokes registered external CDS services via RESTful HTTP calls. Those services analyze patient data and return actionable guidance as "cards" displayed inline in the workflow.

For Epic integrators, CDS Hooks represents a critical integration surface — it's how you embed your application's clinical intelligence directly into Epic workflows without requiring the clinician to launch a separate app. Combined with SMART on FHIR app links from cards, CDS Hooks enables a seamless continuum from passive decision support to interactive application experiences.

**Prerequisites:** Solid understanding of FHIR R4 (D-4), OAuth 2.0 / Epic Auth (D-5), and SMART on FHIR (D-6). CDS Hooks builds directly on all three.

---

## Key Concepts

### 1. CDS Hooks Architecture
- **CDS Client**: The EHR system (e.g., Epic) that triggers hooks and displays returned cards
- **CDS Service**: An external service that receives hook requests and returns decision support cards
- **Hook**: A defined point in the clinical workflow where CDS can be invoked
- **Discovery endpoint**: A stable URL (`{baseUrl}/cds-services`) where the CDS Client discovers available services
- **RESTful interaction model**: Services communicate via JSON over HTTPS

### 2. Hook Types
Standard hooks defined in the specification:
- **`patient-view`**: Triggered when a clinician opens a patient's record. Most common starting hook for integrators.
- **`order-select`**: Fires when a clinician selects one or more orders (medications, procedures, labs)
- **`order-sign`**: Fires immediately before orders are signed — all order details available but still in draft
- **`encounter-start`**: Triggered at patient check-in or admission
- **`encounter-discharge`**: Fired during discharge process
- **`appointment-book`**: Invoked when scheduling future appointments

Epic currently supports **`patient-view`**, **`order-select`**, and **`order-sign`** as the primary hooks.

### 3. CDS Service Discovery
- Services expose a discovery endpoint at `{baseUrl}/cds-services`
- Returns a JSON object listing all available services with their metadata
- Each service entry includes: `hook` (which hook it responds to), `title`, `description`, `id`, and `prefetch` templates
- The EHR registers and calls discovered services when the corresponding hook fires

### 4. Hook Request Structure
When a hook fires, the CDS Client sends a POST request containing:
- **`hookInstance`**: Unique ID for this specific invocation
- **`hook`**: The hook that was triggered (e.g., `patient-view`)
- **`fhirServer`**: Base URL of the EHR's FHIR server
- **`fhirAuthorization`**: OAuth2 bearer token for FHIR API access
- **`context`**: Hook-specific contextual data (patient ID, user ID, encounter, selected orders, etc.)
- **`prefetch`**: Pre-fetched FHIR resources requested by the service

### 5. Card Response Types
CDS Services return cards — the primary mechanism for delivering guidance:

**Information Cards**
- Display textual information for the clinician to read
- Used for guidelines, alerts, patient education references
- Include `summary` (short text), `detail` (longer markdown), `indicator` (info/warning/critical), and `source`

**Suggestion Cards**
- Provide actionable suggestions the clinician can accept with a single click
- Accepting a suggestion automatically populates changes into the EHR UI
- Each suggestion contains `actions` — FHIR-based create, update, or delete operations
- Critical for reducing clinician burden: one-click acceptance vs. manual data entry

**App Link Cards**
- Provide links to external applications, typically SMART on FHIR apps
- Enable launching a full interactive application from a CDS card
- Support deep linking to specific pages within the app
- The `appContext` parameter passes CDS-specific context to the launched app

**Card Indicators**
- `info`: Informational, no urgency
- `warning`: Needs attention, potential issue
- `critical`: Urgent, requires immediate action

### 6. Prefetch Mechanism
- CDS Services declare prefetch templates at discovery time
- Templates are FHIR search queries with **prefetch tokens** (e.g., `{{context.patientId}}`)
- The EHR resolves tokens and fetches the requested FHIR resources before calling the service
- Prefetch data is included directly in the hook request, eliminating additional FHIR API calls
- **Critical for performance**: reduces round-trips and keeps response times under 500ms

**Prefetch optimization strategies:**
- Request only the data your service actually needs
- Use date parameters to limit result sets
- Leverage `_include` and `_revinclude` to reduce query count
- Use `$lastn` for observation queries
- Avoid broad queries (e.g., all vitals for all time)

### 7. SMART on FHIR Launch from Cards
- App Link cards include a `url` pointing to the SMART app's launch endpoint
- Epic initiates the SMART EHR launch sequence when the clinician clicks the link
- The `launch` token and `iss` parameter are appended to the URL
- Standard OAuth 2.0 authorization flow follows
- `appContext` parameter enables the CDS service to pass context to the SMART app
- This creates a seamless flow: CDS card → one-click → full interactive app

### 8. Security Model
- CDS Services MUST be hosted over HTTPS
- The CDS Client issues a JSON Web Token (JWT) with each request for service authentication
- FHIR access tokens are short-lived, scoped to minimum necessary access
- CDS Clients maintain an allowlist of trusted CDS Service endpoints
- CORS must be enabled on CDS Service endpoints for browser-based CDS Clients
- Mutual TLS recommended for additional security

### 9. Epic-Specific CDS Implementation
- Epic supports CDS Hooks through its "Epic on FHIR" platform
- Supported hooks: `patient-view`, `order-select`, `order-sign`
- Cards can appear in different Epic UI locations: pop-up alerts, Storyboard prompts, BPA (Best Practice Alert) integration
- Epic can invoke CDS services selectively using native rule engine capabilities (e.g., only trigger for specific patient populations)
- Testing available through Epic's FHIR sandbox environment
- CDS services registered through App Orchard / Showroom undergo review
- Epic supports deep linking from App Link cards to specific pages within SMART apps
- Display behavior varies by card placement: pop-ups allow single-click app launch; Storyboard prompts may require an additional click

### 10. Performance Requirements
- **500ms response time target**: CDS Services should return within 500 milliseconds
- EHR will not wait indefinitely — services that exceed timeout are dropped
- Prefetch is the primary performance lever
- Parallelization and caching recommended for complex logic
- Performance characteristics may differ significantly between sandbox/test and production environments
- Monitor response times continuously in production
- The CDS Client's own FHIR API performance can be a bottleneck

### 11. Feedback and Analytics
- CDS Hooks supports a **feedback** mechanism where the CDS Client reports back whether a card was accepted, dismissed, or overridden
- Enables CDS Service developers to track effectiveness and refine recommendations
- Critical for reducing alert fatigue — if cards are consistently dismissed, the logic needs adjustment

### 12. System Actions
- CDS Services can return `systemActions` — automated actions performed without user interaction
- Used for background updates, automatic data population
- Requires careful consideration of patient safety and clinical workflow impact

### 13. CDS 5 Rights Framework
- Right **Information** — clinically relevant, evidence-based
- Right **Person** — targeted to the appropriate clinician role
- Right **Channel** — delivered through the right format (card type)
- Right **Format** — clear, actionable, not overwhelming
- Right **Time** — triggered at the appropriate workflow point (hook selection)

---

## Learning Resources

### Official Specifications and Documentation

1. **CDS Hooks Specification (Current)**
   - URL: https://cds-hooks.org/specification/current/
   - Type: Specification
   - Description: The authoritative specification document. Covers the complete API including discovery, hook request/response, prefetch, cards, suggestions, and security. Essential reading.
   - Difficulty: Intermediate-Advanced

2. **CDS Hooks Best Practices**
   - URL: https://cds-hooks.org/best-practices/
   - Type: Guide
   - Description: Official best practices for both CDS Service developers and CDS Client implementers. Covers performance optimization, prefetch strategies, security, and deployment considerations.
   - Difficulty: Intermediate-Advanced

3. **Epic on FHIR — CDS Hooks Documentation**
   - URL: https://fhir.epic.com/Specifications?api=1058
   - Type: Documentation
   - Description: Epic's specific CDS Hooks implementation details, including supported hooks, request/response examples, and Epic-specific behaviors. Required reading for Epic integrators.
   - Difficulty: Advanced

4. **HL7 CDS Hooks Implementation Guide (Build)**
   - URL: https://build.fhir.org/ig/HL7/cds-hooks/
   - Type: Implementation Guide
   - Description: The HL7 FHIR Implementation Guide for CDS Hooks. Provides formal definitions, conformance requirements, and detailed technical specifications.
   - Difficulty: Advanced

### Tutorials and Practical Guides

5. **CDS Hooks Quick Start Guide**
   - URL: https://cds-hooks.org/quickstart/
   - Type: Tutorial
   - Description: Official quick start tutorial walking through implementing a `patient-view` hook service. Covers discovery endpoint creation, service development, and sandbox testing. Best first hands-on exercise.
   - Difficulty: Intermediate

6. **Medblocks: HL7 CDS Hooks — A Practical Guide**
   - URL: https://medblocks.com/blog/hl7-cds-hooks-a-practical-guide
   - Type: Blog/Tutorial
   - Description: Practical walkthrough of creating a CDS Hook service in 10 minutes using Node.js. Includes Ngrok setup for external access and testing with the CDS Hooks sandbox.
   - Difficulty: Intermediate

7. **UW-FHIR CDS Hooks Tutorial (GitHub)**
   - URL: https://github.com/uw-fhir/CDS-Hooks-Tutorial
   - Type: Tutorial/Repository
   - Description: University of Washington tutorial guiding users through building a custom CDS Service with Node.js and testing it with the official CDS Hooks sandbox. Step-by-step with code.
   - Difficulty: Intermediate

### Video Content

8. **HL7 FHIR CDS Hooks — A Practical Guide (Sidharth Ramesh, 2024)**
   - URL: https://www.youtube.com/watch?v=QR09gCbytJk
   - Type: Video Tutorial
   - Description: Comprehensive video covering CDS Hooks introduction, components, how they work in EHRs, and a live demo of a Patient View CDS Hook implementation.
   - Difficulty: Intermediate

9. **Leveraging CQL and CDS Hooks to Enhance CDS (FHIR DevDays 2023)**
   - URL: https://www.youtube.com/watch?v=4gEBZK9mAw0
   - Type: Conference Talk
   - Description: FHIR DevDays talk on using Clinical Quality Language (CQL) with CDS Hooks, including a hands-on tutorial for building a type 2 diabetes decision support system.
   - Difficulty: Advanced

10. **Respecting Patient Privacy with FHIR Consent and CDS Hooks (FHIR DevDays 2024)**
    - URL: https://www.youtube.com/watch?v=0DbADsFMTUg
    - Type: Conference Talk
    - Description: Advanced talk on using CDS Hooks for consent management and patient privacy — relevant for understanding CDS Hooks in complex, real-world regulatory scenarios.
    - Difficulty: Advanced

### Example Code and Tools

11. **CDS Hooks Sandbox**
    - URL: https://sandbox.cds-hooks.org
    - Type: Interactive Tool
    - Description: Official mock EHR for testing CDS services. Simulates hook triggers, displays returned cards, and allows testing against open or secured FHIR endpoints. Essential development tool.
    - Difficulty: Intermediate

12. **cds-hooks/cds-service-example-nodejs (GitHub)**
    - URL: https://github.com/cds-hooks/cds-service-example-nodejs
    - Type: Example Code
    - Description: Reference Node.js implementation of a CDS service. Docker-deployable. Good starting template for building your own service.
    - Difficulty: Intermediate

13. **cds-hooks/cds-service-example-python (GitHub)**
    - URL: https://github.com/cds-hooks/cds-service-example-python
    - Type: Example Code
    - Description: Reference Python/Flask implementation of a CDS service. Docker-deployable.
    - Difficulty: Intermediate

14. **microsoft/cds-services (GitHub)**
    - URL: https://github.com/microsoft/cds-services
    - Type: Example Code
    - Description: Microsoft's CDS Hook services starter kit with examples including patient-view and order-sign (CDC opioid guidelines MME dosage). Production-quality patterns.
    - Difficulty: Advanced

### Research and Deep-Dive

15. **CDS Hooks in Clinical Practice (PubMed Central)**
    - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9382378/
    - Type: Research Paper
    - Description: Academic paper examining CDS Hooks implementation in clinical practice, including real-world outcomes, challenges, and lessons learned.
    - Difficulty: Advanced

---

## Learning Path

### Phase 1: Foundations (3-4 hours)
1. **Read the CDS Hooks specification** — Focus on architecture, discovery, hooks, and cards sections
2. **Explore the CDS Hooks sandbox** — Navigate the mock EHR, trigger hooks, observe card behavior
3. **Watch the Sidharth Ramesh practical guide video** — See a live demo end-to-end

### Phase 2: Build Your First Service (4-6 hours)
4. **Complete the CDS Hooks Quick Start tutorial** — Build a `patient-view` service
5. **Follow the UW-FHIR tutorial** — Build and test with the sandbox
6. **Study the Node.js and Python example repos** — Understand project structure, discovery endpoints, card responses

### Phase 3: Advanced Concepts (4-5 hours)
7. **Deep-dive into prefetch optimization** — Study the best practices guide, implement efficient prefetch templates
8. **Implement suggestion cards with FHIR actions** — Build cards that create/update resources on acceptance
9. **Add App Link cards with SMART launch** — Wire up a SMART on FHIR app launch from a CDS card
10. **Study CDS Hooks security model** — JWT validation, FHIR token scoping, mutual TLS

### Phase 4: Epic-Specific Implementation (3-4 hours)
11. **Study Epic's CDS Hooks documentation** — Understand Epic-supported hooks, UI placement options, and behavioral differences
12. **Test against Epic's FHIR sandbox** — Register your service and validate behavior in Epic's environment
13. **Study performance requirements** — Optimize for the 500ms response target
14. **Review Microsoft's cds-services examples** — Production-quality patterns for order-sign with clinical guidelines

### Phase 5: Production Readiness (3-4 hours)
15. **Implement feedback handling** — Track card acceptance/dismissal rates
16. **Performance testing and optimization** — Load testing, caching strategies, monitoring
17. **Watch DevDays talks** — Learn from real-world implementation challenges and advanced patterns
18. **Read the PubMed Central research paper** — Understand clinical outcomes and alert fatigue mitigation

**Total estimated time: 17-23 hours**

---

## Practical Exercises

### Exercise 1: Patient Greeting Service (Beginner)
Build a CDS service that responds to `patient-view` hooks and returns an information card with the patient's name, age, and any active conditions. Use prefetch to request Patient and Condition resources.

### Exercise 2: Drug Interaction Checker (Intermediate)
Build a service responding to `order-select` that checks a new medication order against the patient's active medications list. Return warning cards for known interactions. Use prefetch for MedicationRequest resources.

### Exercise 3: Suggestion Cards with Actions (Intermediate)
Extend Exercise 2 to include suggestion cards that offer alternative medications when an interaction is detected. The suggestion should include a FHIR `create` action for the alternative MedicationRequest.

### Exercise 4: SMART App Launch from Card (Advanced)
Build a CDS service that returns an App Link card pointing to a SMART on FHIR app. Pass relevant context via `appContext`. Build a minimal SMART app that receives this context and displays detailed clinical information. Test the full flow in the CDS Hooks sandbox.

### Exercise 5: Performance Optimization Lab (Advanced)
Take your Exercise 2 service and optimize it for production-level performance:
- Implement efficient prefetch templates with date filters
- Add response caching for reference data (drug interaction databases)
- Measure and log response times
- Target consistent sub-500ms responses under load
- Implement graceful degradation when the FHIR server is slow

### Exercise 6: Epic Sandbox Integration (Advanced)
Register your CDS service with Epic's FHIR sandbox. Test all three supported hooks (`patient-view`, `order-select`, `order-sign`). Document behavioral differences between the CDS Hooks sandbox and Epic's implementation. Validate JWT handling with Epic's authentication.

---

## Connections to Other Domains

- **FHIR R4 (D-4)**: CDS Hooks uses FHIR resources throughout — prefetch queries, card actions, and FHIR server interactions all require solid FHIR knowledge
- **OAuth 2.0 / Epic Auth (D-5)**: Security model relies on OAuth tokens for FHIR server access and JWT for service authentication
- **SMART on FHIR (D-6)**: App Link cards launch SMART apps — the CDS-to-SMART launch flow is a primary integration pattern
- **Epic APIs (D-9)**: CDS Hooks is one of several Epic integration surfaces; understanding how it fits alongside Interconnect and MyChart APIs is important
- **Clinical Workflow Embedding (D-11)**: CDS Hooks is a key mechanism for embedding intelligence into clinical workflows — complements other embedding patterns
- **App Orchard / Showroom (D-12)**: CDS services distributed through Epic require App Orchard registration and review
- **Production Operations (D-14)**: Performance monitoring, alert fatigue management, and reliability patterns are critical for production CDS services
