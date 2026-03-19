# SMART on FHIR App Development

## Overview

SMART on FHIR (Substitutable Medical Applications, Reusable Technologies on Fast Healthcare Interoperability Resources) is the standard framework for building third-party applications that integrate with EHR systems like Epic. It combines FHIR for data access with OAuth 2.0 for authorization and OpenID Connect for authentication, enabling a "build once, run anywhere" approach for healthcare apps. This domain covers the complete lifecycle of building a SMART app targeting Epic — from understanding launch flows and scopes through embedded rendering, Web Messaging, and multi-tenant deployment.

**Prerequisites from completed domains:** FHIR R4 data model (D-4), OAuth 2.0 and Epic auth flows (D-5), interoperability foundations (D-1).

---

## Key Concepts

### 1. SMART App Launch Framework
The HL7-published SMART App Launch Implementation Guide (currently v2.2.0) defines the standard protocol for apps to obtain authorization, authenticate users, and receive clinical context from an EHR. It builds on OAuth 2.0 Authorization Code flow with PKCE and adds healthcare-specific launch context parameters.

### 2. EHR Launch Flow
- App is launched **from within** an existing EHR session (Epic Hyperspace, Hyperdrive, or MyChart)
- EHR passes an opaque `launch` parameter to the app's launch URL
- App exchanges this parameter during the OAuth authorization request to receive pre-established context (patient ID, encounter ID, user identity)
- Ideal for clinical decision support tools, in-context viewers, and workflow-embedded utilities
- The clinician does not need to re-select the patient — context is inherited from the EHR session

### 3. Standalone Launch Flow
- App is launched **independently**, outside of any EHR session (e.g., a patient mobile app, a provider desktop tool)
- App declares context requirements via scopes like `launch/patient` or `launch/encounter`
- The EHR's authorization server handles user authentication and may prompt for patient selection
- Epic acts as the OAuth 2.0 identity provider
- Suitable for patient-facing apps, research tools, and batch processing interfaces

### 4. SMART Scopes (with Epic Specifics)

**Scope Categories:**
- **`patient/`** — Access limited to the single patient in context (e.g., `patient/Observation.read`)
- **`user/`** — Access tied to the logged-in user's permissions (e.g., `user/MedicationRequest.write`)
- **`system/`** — Server-to-server access without a user session, for backend services (e.g., `system/Patient.read`)

**SMART v1 vs v2 Scopes:**
- **v1**: Uses `.read` and `.write` actions (e.g., `patient/Observation.read`)
- **v2**: Uses granular CRUDS syntax — `.c` (create), `.r` (read), `.u` (update), `.d` (delete), `.s` (search) (e.g., `patient/Observation.rs` for read+search)
- Epic supports both v1 and v2 as of August 2024; apps targeting older Epic versions must use v1

**Launch Context Scopes:**
- `launch` — Request EHR launch context
- `launch/patient` — Request patient context in standalone launch
- `launch/encounter` — Request encounter context
- `openid fhirUser` — Request user identity via OpenID Connect

**Epic-Specific Considerations:**
- Write scopes require additional clinical safety review from Epic
- Unsupported scopes cause authorization failures — request only what's needed
- Scope availability varies by Epic version and customer configuration
- Always use the principle of least privilege

### 5. SMART Discovery (Well-Known Configuration)
- Apps discover OAuth endpoints via `GET [fhir-base]/.well-known/smart-configuration`
- Returns authorization endpoint, token endpoint, supported scopes, capabilities
- Critical for multi-tenant apps that connect to different Epic instances

### 6. Embedded Rendering in Hyperspace and MyChart

**Hyperspace / Hyperdrive (Provider-Facing):**
- SMART apps render inside an iframe within the Hyperspace or Hyperdrive client
- Apps can be activated from various clinical workflow points (patient chart, navigator, activity buttons)
- The iframe receives the EHR launch context automatically
- Hyperdrive (the newer web-based framework replacing Hyperspace) provides better support for modern web standards

**MyChart (Patient-Facing):**
- SMART apps render inside MyChart web and mobile interfaces
- Patient authenticates via MyChart credentials — no separate login required
- Apps receive patient context scoped to the logged-in patient only
- Must handle both MyChart web (iframe) and MyChart mobile (webview) rendering environments
- Design considerations: responsive layout, touch-friendly, limited screen real estate

**Rendering Best Practices:**
- Design for iframe constraints (no popup windows, limited navigation)
- Handle cross-origin restrictions properly
- Support both desktop and mobile viewport sizes
- Test in all target rendering environments (Hyperspace, Hyperdrive, MyChart web, MyChart mobile)

### 7. SMART Web Messaging
- Defined by the HL7 SMART Web Messaging specification
- Uses HTML5 `window.postMessage` for bidirectional communication between embedded SMART apps and the host EHR
- Enables tight workflow integration beyond simple data retrieval

**Message Types:**
- `status.handshake` — Establish communication channel
- `ui.done` — Signal the EHR that the app has completed its task
- `scratchpad.create` / `scratchpad.update` / `scratchpad.read` / `scratchpad.delete` — Interact with the EHR's draft resource area (e.g., propose unsigned orders, add note snippets)
- `fhir.http` — Perform FHIR interactions routed through the EHR context

**Key Security:**
- `targetOrigin` parameter must be set to the specific EHR origin (provided during SMART launch)
- Never use wildcard `*` for targetOrigin
- Message origin validation on both sides

**Use Cases:**
- Pushing clinical decision support recommendations as draft orders
- Sharing risk scores or note text with the EHR session
- Signaling workflow completion to close the app panel
- Accessing draft/ephemeral resources not yet in the FHIR server

### 8. Multi-Tenant Architecture
Building a SMART app that works across multiple Epic instances (different health systems):

**Challenges:**
- Each Epic customer has its own FHIR base URL and OAuth endpoints
- Scope support and FHIR resource extensions vary by Epic version and customer configuration
- Different health systems may have different Epic modules enabled

**Architecture Patterns:**
- **Configuration-driven tenant management** — Store per-tenant: FHIR base URL, client ID, supported scopes, custom mappings
- **Dynamic endpoint discovery** — Use `.well-known/smart-configuration` to resolve OAuth endpoints per tenant
- **Token management** — Separate token storage per tenant; never mix tokens across organizations
- **Data isolation** — Strict tenant boundaries for HIPAA compliance
- **FHIR normalization layer** — Handle minor resource variations and extensions across instances
- **Caching strategy** — Cache relatively static resources (Practitioner, Location) per tenant

### 9. SMART App Registration and Distribution
- Register apps on Epic's developer portal at fhir.epic.com
- Specify launch type, required scopes, redirect URIs
- Receive a client_id for sandbox and production
- Production distribution via Epic Showroom (formerly App Orchard)
- Each health system must individually approve and enable your app

### 10. Client Libraries and Tooling
- **fhirclient (client-js)** — Official SMART on FHIR JavaScript client library (`npm i fhirclient`)
- Works in browser and Node.js environments
- Handles SMART launch negotiation, token management, FHIR API calls
- Python: `fhirclient` package for Python-based SMART apps
- .NET: `Hl7.Fhir.R4` + custom SMART launch handling

---

## Learning Resources

### Official Documentation and Specifications

1. **SMART App Launch IG (HL7)**
   - URL: https://build.fhir.org/ig/HL7/smart-app-launch/
   - Type: Specification
   - Description: The authoritative implementation guide for SMART App Launch v2.x. Covers both launch flows, scope definitions, discovery, and conformance requirements.
   - Difficulty: Intermediate-Advanced
   - Cost: Free

2. **Epic on FHIR — OAuth 2.0 Documentation**
   - URL: https://fhir.epic.com/Documentation?docId=oauth2
   - Type: Documentation
   - Description: Epic's official documentation for implementing OAuth 2.0 and SMART on FHIR launch flows. Includes Epic-specific scope details, launch parameters, and token handling.
   - Difficulty: Intermediate
   - Cost: Free

3. **SMART Web Messaging IG (HL7)**
   - URL: https://build.fhir.org/ig/HL7/smart-web-messaging/
   - Type: Specification
   - Description: The HL7 implementation guide defining the Web Messaging protocol for SMART apps to communicate with the host EHR via postMessage.
   - Difficulty: Intermediate-Advanced
   - Cost: Free

4. **SMART Health IT Documentation**
   - URL: https://docs.smarthealthit.org/
   - Type: Documentation
   - Description: Official documentation from the SMART Health IT project, including client library docs, tutorials, and architecture overviews.
   - Difficulty: Beginner-Intermediate
   - Cost: Free

5. **Epic Developer Resources Portal**
   - URL: https://open.epic.com/DeveloperResources
   - Type: Documentation / Portal
   - Description: Epic's central hub for developer tools including step-by-step guides, data sharing playbooks, and API specifications.
   - Difficulty: Beginner-Intermediate
   - Cost: Free

### Video Tutorials

6. **Epic SMART on FHIR Integration Masterclass (Mindbowser)**
   - URL: https://www.youtube.com/watch?v=_LYP4G74NWw
   - Type: Video Tutorial
   - Description: Comprehensive walkthrough of SMART on FHIR with Epic — covers launch types, authentication patterns, sandbox development, and the production review process with live demo.
   - Duration: ~60 min
   - Difficulty: Intermediate
   - Cost: Free

7. **Masterclass to Epic Integration with SMART on FHIR (Mindbowser)**
   - URL: https://www.youtube.com/watch?v=J8r0byyKVJs
   - Type: Video Tutorial
   - Description: Expert-led session covering application types, launch modes, app registration on Epic platform with demonstrations.
   - Duration: ~45 min
   - Difficulty: Intermediate
   - Cost: Free

8. **Building SMART on FHIR Apps with MeldRx (Epic & Cerner)**
   - URL: https://www.youtube.com/watch?v=DE2RHlxF-AE
   - Type: Video Tutorial
   - Description: Demonstrates building a SMART app connecting to Epic sandbox without EHR-specific coding changes. Shows cloud-based FHIR sandbox creation and app registration.
   - Duration: ~30 min
   - Difficulty: Beginner-Intermediate
   - Cost: Free

### Open-Source Projects and Repositories

9. **SMART on FHIR client-js**
   - URL: https://github.com/smart-on-fhir/client-js
   - Type: Open-Source Library
   - Description: Official JavaScript client library for SMART on FHIR. Handles launch negotiation, OAuth flows, token management, and FHIR API access. Works in browser and Node.js.
   - Install: `npm i fhirclient`
   - Cost: Free

10. **SMART on FHIR client-js Examples**
    - URL: https://github.com/smart-on-fhir/client-js-examples
    - Type: Code Examples
    - Description: Working example applications demonstrating how to use the client-js library for both EHR launch and standalone launch scenarios.
    - Cost: Free

### Written Guides and Tutorials

11. **Integrating SMART on FHIR Apps with Epic (Technosoft)**
    - URL: https://techno-soft.com/integrating-smart-app-with-epic.html
    - Type: Tutorial / Blog
    - Description: Detailed walkthrough of integrating a SMART app with Epic, from App Orchard registration through OAuth handshake and FHIR data access.
    - Difficulty: Intermediate
    - Cost: Free

12. **How to Build a SMART on FHIR App That Integrates with Epic (Itirra)**
    - URL: https://itirra.com/blog/how-to-build-a-smart-on-fhir-app-that-integrates-with-epic/
    - Type: Blog / Guide
    - Description: Strategic guide covering framework understanding, key challenges, security/compliance, and technical steps for building and testing.
    - Difficulty: Intermediate
    - Cost: Free

13. **How to Integrate with Epic EHR Using Python and SMART on FHIR APIs (Spritle)**
    - URL: https://www.spritle.com/blog/how-to-integrate-with-epic-ehr-using-python-and-smart-on-fhir-apis/
    - Type: Tutorial
    - Description: Python-focused guide covering Backend Services App setup, JWT authentication, and pulling patient data from Epic FHIR API.
    - Difficulty: Intermediate
    - Cost: Free

### Sandbox and Testing

14. **Epic on FHIR Developer Portal / Sandbox**
    - URL: https://fhir.epic.com/Developer/Index
    - Type: Interactive Sandbox
    - Description: Epic's FHIR sandbox for testing SMART app launches, OAuth flows, and API calls with test patient data. Includes "Try It" features for no-code testing.
    - Cost: Free (requires account)

### Community Resources

15. **SMART on FHIR Google Group**
    - URL: https://groups.google.com/g/smart-on-fhir
    - Type: Community Forum
    - Description: Active community for SMART on FHIR developers. Good for troubleshooting launch flow issues, scope questions, and implementation advice.
    - Cost: Free

16. **Azure Health Data Services — SMART on FHIR (Microsoft)**
    - URL: https://learn.microsoft.com/en-us/azure/healthcare-apis/fhir/smart-on-fhir
    - Type: Documentation
    - Description: Microsoft's guide to SMART on FHIR with Azure FHIR server. Useful for understanding SMART compliance testing and cloud-hosted FHIR backends.
    - Difficulty: Intermediate
    - Cost: Free

---

## Learning Path

### Phase 1: SMART Foundations (Days 1–3)
**Goal:** Understand the SMART App Launch protocol and both launch flows.

1. Read the SMART App Launch IG overview sections (Resource #1)
2. Study Epic's OAuth 2.0 documentation specific to SMART launch (Resource #2)
3. Watch the Mindbowser Masterclass for practical overview (Resource #6)
4. Understand the difference between EHR launch and standalone launch
5. Study SMART discovery (`.well-known/smart-configuration`)

**Milestone:** Can diagram both launch flows and explain when to use each.

### Phase 2: Scopes and Authorization Deep Dive (Days 4–5)
**Goal:** Master SMART scopes including Epic-specific behavior.

1. Study scope categories: patient/, user/, system/ contexts
2. Learn SMART v1 vs v2 scope syntax differences
3. Review Epic's scope support documentation
4. Understand launch context scopes (launch, launch/patient, openid fhirUser)
5. Practice scope selection for different app types

**Milestone:** Can specify the correct scope set for a given app use case and explain Epic-specific scope constraints.

### Phase 3: First SMART App with Epic Sandbox (Days 6–10)
**Goal:** Build and test a working SMART app against Epic's sandbox.

1. Create an account on fhir.epic.com
2. Register a test application with both EHR and standalone launch support
3. Use client-js library to implement OAuth flow (Resource #9, #10)
4. Build a simple patient viewer that works in both launch modes
5. Test with Epic sandbox test patients

**Milestone:** Working app that successfully completes both EHR and standalone launch flows against Epic sandbox.

### Phase 4: Embedded Rendering (Days 11–14)
**Goal:** Understand and implement embedded rendering for Hyperspace and MyChart.

1. Study iframe rendering constraints and cross-origin requirements
2. Learn Hyperspace vs Hyperdrive rendering differences
3. Understand MyChart web and mobile rendering environments
4. Adapt your sandbox app for embedded display
5. Implement responsive design for different rendering contexts

**Milestone:** App renders correctly in simulated Hyperspace iframe and MyChart webview contexts.

### Phase 5: Web Messaging (Days 15–18)
**Goal:** Implement SMART Web Messaging for workflow integration.

1. Read the SMART Web Messaging IG (Resource #3)
2. Implement status.handshake message exchange
3. Implement scratchpad operations (create, read, update)
4. Implement ui.done for workflow completion signaling
5. Understand security requirements (targetOrigin, origin validation)

**Milestone:** App can exchange Web Messages with a simulated EHR host, including scratchpad operations.

### Phase 6: Multi-Tenant Architecture (Days 19–22)
**Goal:** Design architecture for apps serving multiple Epic instances.

1. Study configuration-driven tenant management patterns
2. Implement dynamic endpoint discovery per tenant
3. Design tenant-isolated token storage
4. Build a FHIR resource normalization layer for cross-instance variations
5. Plan caching strategy for static resources

**Milestone:** Architecture document and proof-of-concept supporting 2+ simulated Epic tenants.

### Phase 7: Integration and Production Readiness (Days 23–25)
**Goal:** Prepare for production deployment.

1. Review Epic's app review and certification process
2. Understand Epic Showroom listing requirements
3. Plan per-site enablement workflow
4. Implement production-grade error handling and logging
5. Document scope justification for each requested scope

**Milestone:** Production readiness checklist completed; app architecture reviewed against Epic requirements.

**Total estimated time: 25 days (assuming part-time, ~2-3 hours/day)**

---

## Practical Exercises

### Exercise 1: SMART Launch Flow Comparison
**Difficulty:** Beginner | **Time:** 2 hours
- Register a test app on fhir.epic.com with both EHR and standalone launch configured
- Use Epic's sandbox Launchpad to trigger an EHR launch; capture and examine the launch parameter and token response
- Trigger a standalone launch; compare the authorization request and token response
- Document the differences in context received between the two flows

### Exercise 2: Build a Patient Summary SMART App
**Difficulty:** Intermediate | **Time:** 8 hours
- Using `fhirclient` (client-js), build a web app that:
  - Supports both EHR and standalone launch
  - Reads Patient, Condition, MedicationRequest, and Observation resources
  - Displays a simple patient summary dashboard
- Test against Epic sandbox with multiple test patients
- Implement proper error handling for scope rejections

### Exercise 3: Scope Audit Exercise
**Difficulty:** Intermediate | **Time:** 3 hours
- Given a hypothetical app use case (e.g., "medication adherence tracker for patients"), determine:
  - Required scopes in both v1 and v2 syntax
  - Appropriate launch type (EHR vs standalone)
  - Context scopes needed
- Repeat for 3 different app types: provider CDS tool, patient wellness app, backend analytics service
- Validate scope choices against Epic's supported scope list

### Exercise 4: Embedded Rendering Prototype
**Difficulty:** Intermediate | **Time:** 6 hours
- Build a SMART app that detects its rendering context (iframe vs full page)
- Implement responsive layout that works in:
  - Full browser window (standalone)
  - Narrow iframe (simulating Hyperspace sidebar)
  - Mobile viewport (simulating MyChart mobile)
- Test with simulated iframe embedding at various dimensions
- Handle cross-origin communication constraints

### Exercise 5: Web Messaging Implementation
**Difficulty:** Advanced | **Time:** 8 hours
- Build a prototype that simulates Web Messaging:
  - Create a mock "EHR host" page that embeds your SMART app in an iframe
  - Implement the status.handshake flow
  - Implement scratchpad.create to propose a draft order
  - Implement ui.done to signal completion
- Ensure proper targetOrigin usage and origin validation
- Log all messages for debugging

### Exercise 6: Multi-Tenant Configuration Manager
**Difficulty:** Advanced | **Time:** 10 hours
- Build a tenant management module that:
  - Stores per-tenant configuration (FHIR base URL, client ID, supported scopes)
  - Dynamically discovers OAuth endpoints via .well-known/smart-configuration
  - Manages separate token stores per tenant
  - Routes API calls to the correct tenant's FHIR server
- Test with Epic sandbox as one tenant and a public HAPI FHIR server as another
- Implement tenant data isolation checks

---

## Connections to Other Domains

- **D-4 (FHIR R4):** SMART apps interact with FHIR resources — understanding the data model is essential for building queries and displaying data
- **D-5 (OAuth 2.0 / Epic Auth):** SMART App Launch builds directly on OAuth 2.0; the auth domain provides the security foundation
- **D-1 (Interoperability Foundations):** SMART on FHIR is the practical realization of interoperability standards in app development
- **Upcoming — App Orchard / Epic Showroom:** SMART apps must go through Epic's distribution process for production deployment
- **Upcoming — CDS Hooks:** Often deployed alongside SMART apps for clinical decision support; CDS Hooks can launch SMART apps
- **Upcoming — Production Operations:** Multi-tenant architecture patterns inform operational monitoring and scaling

---

## Sandbox Project

**Recommended Sandbox Project: Patient Medication Dashboard**

Build a SMART on FHIR app that:
1. Supports both EHR launch (from Hyperspace) and standalone launch
2. Reads Patient, MedicationRequest, and AllergyIntolerance resources
3. Displays an interactive medication list with allergy cross-references
4. Uses Web Messaging to propose a medication review note via scratchpad
5. Is designed for embedded rendering in both Hyperspace and MyChart
6. Supports configuration for multiple Epic tenants

**Platform:** fhir.epic.com sandbox
**Library:** fhirclient (client-js)
**Test with:** Epic sandbox test patients (e.g., Camila Lopez, Jason Argonaut)
