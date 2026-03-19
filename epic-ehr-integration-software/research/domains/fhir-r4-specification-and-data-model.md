# FHIR R4 Specification and Data Model

## Overview

FHIR R4 (Fast Healthcare Interoperability Resources, Release 4) is the first normative release of the FHIR standard, providing a stable, RESTful framework for healthcare data exchange. This domain covers the FHIR resource model, RESTful API interactions, search mechanics, US Core profiles, USCDI alignment, and Epic's specific FHIR implementation — all from the perspective of building software that integrates with Epic EHR systems.

This domain builds on the interoperability foundations (D-1), regulatory landscape (D-2), and terminology systems (D-3) covered previously. Where those domains explained *why* and *what* standards exist, this domain focuses on the *how* — the concrete data model and API surface you'll code against.

---

## Key Concepts

### 1. FHIR Resource Model Fundamentals

- **Resources as the unit of exchange**: FHIR defines ~150 resource types, each representing a clinically or administratively meaningful concept (Patient, Observation, Condition, Encounter, MedicationRequest, etc.)
- **Resource structure**: Every resource has a `resourceType`, an `id`, `meta` (version, lastUpdated, profile), and type-specific elements
- **Data types**: Primitives (string, boolean, date, dateTime, instant, decimal, uri, code) and complex types (HumanName, Address, CodeableConcept, Reference, Identifier, Period, Quantity)
- **References between resources**: Resources link to each other via `Reference` elements containing relative URLs (e.g., `Patient/123`), forming a directed graph
- **Serialization formats**: JSON and XML are both supported; JSON dominates in practice
- **Contained resources**: Resources can embed other resources inline when they lack independent identity
- **Extensions**: FHIR's extensibility mechanism — any element can carry additional data via extension elements with a defining URL

### 2. Resource Categories

- **Clinical resources**: Patient, Observation, Condition, Procedure, AllergyIntolerance, Immunization, DiagnosticReport, MedicationRequest, MedicationStatement, CarePlan, CareTeam, Goal, ServiceRequest, Encounter
- **Administrative resources**: Organization, Practitioner, PractitionerRole, Location, HealthcareService, Schedule, Slot, Appointment, Coverage, Account
- **Infrastructure resources**: Bundle, OperationOutcome, CapabilityStatement, StructureDefinition, ValueSet, CodeSystem, SearchParameter, OperationDefinition
- **Financial resources**: Claim, ExplanationOfBenefit, Coverage

### 3. RESTful API Interactions

- **CRUD operations**: `GET` (read), `POST` (create), `PUT` (update), `PATCH` (partial update), `DELETE` (remove)
- **Instance-level**: `GET /Patient/123` reads a specific patient; `GET /Patient/123/_history/2` reads a specific version
- **Type-level**: `GET /Patient?name=Smith` searches patients; `POST /Patient` creates a new patient
- **System-level**: `GET /metadata` returns CapabilityStatement; `POST /` submits a Bundle transaction
- **Versioning**: Each resource has a version ID (`meta.versionId`) incremented on update; `ETag` / `If-Match` headers enable optimistic concurrency
- **Conditional operations**: Conditional create (`If-None-Exist`), conditional update, conditional delete — match by search parameters instead of IDs
- **Bundle transactions and batches**: Group multiple operations into a single `POST /` request; transactions are all-or-nothing, batches are independent

### 4. FHIR Search

- **Basic search**: `GET /Patient?family=Smith&birthdate=1990-01-01`
- **Search parameter types**: string, token, date, reference, quantity, number, uri, composite, special
- **Prefixes for ordered types**: `eq`, `ne`, `gt`, `lt`, `ge`, `le`, `sa`, `eb`, `ap` — e.g., `date=ge2023-01-01`
- **Modifiers**:
  - `:exact` — case-sensitive exact string match
  - `:contains` — substring match
  - `:missing` — test for presence/absence of a value
  - `:not` — negation
  - `:text` — match on display text of a CodeableConcept
  - `:above` / `:below` — code hierarchy subsumption
  - `:in` / `:not-in` — membership in a ValueSet
  - `:of-type` — match identifier by type
- **Chaining (forward)**: `Observation?patient.name=Smith` — filter by properties of referenced resources
- **Reverse chaining**: `Patient?_has:Observation:patient:code=8867-4` — filter by properties of resources that reference the target
- **`_include`**: `MedicationRequest?_include=MedicationRequest:patient` — return referenced resources in results
- **`_revinclude`**: `Patient?_revinclude=Encounter:subject` — return resources that reference matched resources
- **`_include:iterate`**: Follow references multiple hops deep
- **Result parameters**: `_count`, `_offset`, `_sort`, `_total`, `_elements`, `_summary`
- **Pagination**: Servers return `Bundle.link` entries with `next`/`previous` URLs

### 5. US Core Profiles and USCDI

- **What US Core is**: An HL7 Implementation Guide (IG) that constrains FHIR R4 resources for US healthcare — defines minimum required elements, terminology bindings, and search parameters
- **Must Support**: Elements marked "Must Support" must be populated by servers if data exists and must be handled by clients; this is the practical contract for interoperability
- **USCDI (United States Core Data for Interoperability)**: ONC-defined standardized data set that EHRs must support; US Core profiles are the FHIR implementation of USCDI
- **USCDI versions**: v1 (baseline, supported through May 2024 Epic), v3 (August 2024 Epic+), v5 (in development at Epic)
- **Key US Core profiles**:
  - US Core Patient Profile → USCDI Patient Demographics
  - US Core AllergyIntolerance Profile → Allergies and Intolerances
  - US Core Condition Profile → Problems, Health Concerns, Encounter Diagnoses
  - US Core Observation Profiles (Lab, Vitals, Clinical Test, SDOH) → Clinical data
  - US Core DocumentReference Profile → Clinical Notes (progress notes, discharge summaries, consultation notes)
  - US Core CarePlan Profile → Assessment and Plan of Treatment
  - US Core CareTeam Profile → Care Team Members
  - US Core DiagnosticReport Profiles → Lab Reports, Diagnostic Imaging
  - US Core Medication/MedicationRequest Profiles → Medications
  - US Core Immunization Profile → Immunizations
  - US Core Procedure Profile → Procedures
  - US Core Encounter Profile → Encounters
- **Additional USCDI Requirements**: Treated as Must Support for ONC certification; appear in US Core 6.1.0+

### 6. Epic FHIR Implementation

- **Epic on FHIR portal**: `fhir.epic.com` — documentation, sandbox, client registration
- **Supported FHIR versions**: DSTU2, STU3, R4 (R4 is current standard)
- **Supported resources (R4)**: Patient, Encounter, Observation, Condition, AllergyIntolerance, MedicationRequest, Medication, Procedure, Immunization, DiagnosticReport, DocumentReference, CarePlan, CareTeam, Coverage, Appointment, Practitioner, PractitionerRole, Organization, Location, Binary, ServiceRequest, Goal, and many more
- **Operations supported**: Read, Search, Create (for select resources), $match (Patient), $book/$find (Appointment), $expand (ValueSet)
- **Write-back resources**: Patient (create), Condition (create), AllergyIntolerance (create), Observation (create for vitals, SmartData), DocumentReference (create for clinical notes), MedicationRequest (create via CDS Hooks)
- **CapabilityStatement**: Each Epic instance publishes its own at `/metadata` — always check this first as capabilities vary by site

### 7. Epic FHIR Coverage Gaps and Limitations

- **Variable implementations across sites**: Each health system customizes Epic extensively; FHIR coverage, endpoints, and terminology mappings differ between organizations
- **Limited write-back**: Most resources are read-only; write access is restricted to specific clinical workflows
- **Rate limits**: 80 DocumentReference (Generated CCDA) searches per patient per day; general API rate limiting applies
- **Data mapping complexity**: Epic's proprietary data model doesn't always map cleanly to FHIR; expect gaps and extensions
- **No real-time subscriptions** (limited): Batch-oriented in many scenarios; Subscriptions framework support is still evolving
- **Custom extensions**: Epic uses proprietary extensions for data not covered by base FHIR (check `StructureDefinition` resources)
- **Sandbox vs. production differences**: The open.epic.com sandbox is a reference implementation; production environments have different configurations, data, and access controls
- **Security evolution**: Static keys being deprecated (August 2025 for sandbox, May 2026 for production); JWK Set URL (JKU) required

### 8. FHIR Client Libraries

- **JavaScript/TypeScript**: `@smart-on-fhir/client-js` (SMART launch + FHIR client), `fhir.js` (lightweight CRUD client)
- **Python**: `fhirclient` (SMART on FHIR support, typed models), `fhirpy` (async/sync, dict-based, version-agnostic)
- **Java**: HAPI FHIR (comprehensive framework — client, server, parser, validator; supports DSTU2–R5)
- **.NET**: Firely SDK (`Hl7.Fhir.*` NuGet packages)
- **FHIRPath**: Expression language for traversing FHIR resources (`fhirpath.js`, `fhirpath-py`)

### 9. Profiling and Conformance

- **StructureDefinition**: Defines constraints on resources (profiles, extensions)
- **CapabilityStatement**: Server's declaration of supported resources, operations, and search parameters
- **ImplementationGuide**: Packages of profiles, examples, and documentation (US Core is an IG)
- **Validation**: Resources can be validated against profiles using HAPI FHIR validator, Inferno, or the official HL7 validator
- **FHIR Shorthand (FSH)**: Domain-specific language for authoring FHIR profiles and IGs; compiled by SUSHI

### 10. Important FHIR Operations

- **$everything**: Retrieve all data for a Patient or Encounter
- **$validate**: Check a resource against a profile
- **$expand**: Expand a ValueSet to its member codes
- **$match**: Patient matching (Epic supports this)
- **$convert**: Convert between FHIR versions
- **$summary**: Generate summary documents (e.g., International Patient Summary)

---

## Learning Resources

### Online Courses

1. **Health Informatics on FHIR — Georgia Tech (edX Professional Certificate)**
   - Platform: edX
   - URL: https://www.edx.org/certificates/professional-certificate/gtx-health-informatics-on-fhir
   - Duration: ~12 weeks (self-paced)
   - Cost: Paid (audit free)
   - Covers: FHIR fundamentals, health informatics context, practical application
   - Why: Best structured academic introduction to FHIR with hands-on components

2. **Ingesting FHIR Data with the Healthcare API — Google Cloud (Coursera)**
   - Platform: Coursera
   - URL: https://www.coursera.org/projects/googlecloud-ingesting-fhir-data-with-the-healthcare-api-yhvbk
   - Duration: ~1.5 hours
   - Cost: Free with Coursera account
   - Covers: FHIR data model basics, CRUD operations via Google Healthcare API
   - Why: Quick hands-on lab with real FHIR API calls

### Official Documentation and Specifications

3. **HL7 FHIR R4 Specification**
   - URL: https://hl7.org/fhir/R4/
   - Type: Reference specification
   - Covers: Complete FHIR R4 standard — resources, data types, API, search, operations
   - Why: The authoritative source; every FHIR developer should bookmark this

4. **US Core Implementation Guide (latest)**
   - URL: https://hl7.org/fhir/us/core/
   - Type: Implementation guide
   - Covers: US-specific FHIR profiles, Must Support definitions, USCDI mappings
   - Why: Defines the minimum data contract for US EHR interoperability

5. **Epic on FHIR Documentation**
   - URL: https://fhir.epic.com/
   - Type: Vendor documentation + sandbox
   - Covers: Epic-specific FHIR API specs, supported resources, OAuth2 flows, sandbox access
   - Why: Essential reference for anyone building Epic integrations

6. **ONC USCDI Reference**
   - URL: https://www.healthit.gov/isa/united-states-core-data-interoperability-uscdi
   - Type: Government specification
   - Covers: USCDI data classes and elements, version history, expansion process
   - Why: Understanding what data EHRs are required to share

### Video Content

7. **HL7 FHIR DevDays Presentations**
   - URL: https://www.devdays.com/
   - Type: Conference talks and tutorials
   - Covers: FHIR search, profiling, implementation patterns, tool demos
   - Why: Practitioner-focused content from FHIR implementers; new content annually
   - Notable: Gino Canessa's "Intro to FHIR Search" presentation (https://www.devdays.com/wp-content/uploads/2024/07/6.10.24-Gino-Canessa-Intro-to-FHIR-Search.pdf)

8. **FHIR Drills — Interactive Tutorial**
   - URL: https://fhir-drills.github.io/
   - Type: Interactive web-based exercises
   - Covers: FHIR API basics, CRUD operations, search, references
   - Why: Learn by doing — guided exercises against a live FHIR server

### Books and Written Guides

9. **"Principles of Health Interoperability: FHIR, HL7 and SNOMED CT" by Tim Benson (Springer)**
   - Type: Book (4th edition, 2021)
   - Covers: FHIR architecture, data model, health terminology integration
   - Why: Comprehensive reference that bridges theory and practice

### Libraries and Tools

10. **HAPI FHIR (Java)**
    - URL: https://hapifhir.io/
    - Type: Open-source framework
    - Covers: FHIR client, server, parser, validator for Java
    - Why: Industry-standard Java FHIR library; powers many production systems

11. **SMART on FHIR JavaScript Client**
    - URL: https://docs.smarthealthit.org/client-js/
    - GitHub: https://github.com/smart-on-fhir/client-js
    - Type: Client library
    - Covers: OAuth2 + FHIR client for browser and Node.js apps
    - Why: The standard library for SMART app development

12. **fhirclient (Python)**
    - URL: https://pypi.org/project/fhirclient/
    - GitHub: https://github.com/smart-on-fhir/client-py
    - Type: Client library
    - Covers: FHIR R4 models, SMART on FHIR auth, Pythonic API
    - Why: Best Python library for SMART-enabled FHIR apps

### Community and Reference

13. **Awesome FHIR (GitHub)**
    - URL: https://github.com/fhir-fuel/awesome-FHIR
    - Type: Curated list
    - Covers: FHIR tools, libraries, servers, learning resources
    - Why: Community-maintained directory of the FHIR ecosystem

14. **HAPI FHIR Search Tutorial (GitHub)**
    - URL: https://github.com/hapifhir/fhir-tutorial
    - Type: Tutorial repository
    - Covers: Search parameters, chaining, _include, _revinclude with exercises
    - Why: Step-by-step search tutorial with code examples

---

## Learning Path

### Phase 1: FHIR Fundamentals (Week 1–2, ~15 hours)

**Goal**: Understand the FHIR data model and be able to read/write FHIR resources

1. Start with the edX "Health Informatics on FHIR" first course module for context
2. Read the FHIR R4 specification overview: https://hl7.org/fhir/R4/overview.html
3. Study core data types: https://hl7.org/fhir/R4/datatypes.html
4. Walk through the Patient resource in detail: https://hl7.org/fhir/R4/patient.html
5. Study 5 more clinical resources: Observation, Condition, Encounter, MedicationRequest, AllergyIntolerance
6. Complete FHIR Drills exercises (https://fhir-drills.github.io/) for CRUD operations

**Milestone**: Can read a FHIR Patient JSON and identify every element's purpose; can hand-author a valid Observation resource

### Phase 2: FHIR Search Mastery (Week 3, ~10 hours)

**Goal**: Use FHIR search effectively including modifiers, chaining, and includes

1. Read the FHIR search specification: https://hl7.org/fhir/R4/search.html
2. Study Gino Canessa's DevDays search tutorial
3. Practice search queries against a public FHIR server (e.g., HAPI test server at https://hapi.fhir.org/)
4. Work through the HAPI FHIR search tutorial on GitHub
5. Practice with modifiers (`:exact`, `:contains`, `:missing`, `:not`)
6. Practice chaining, `_include`, `_revinclude`

**Milestone**: Can construct complex search queries with chaining and includes; understands pagination

### Phase 3: US Core and USCDI (Week 4, ~8 hours)

**Goal**: Understand US Core profiles and how they constrain FHIR for US interoperability

1. Read the US Core IG overview and "Must Support" documentation
2. Walk through US Core Patient, Observation, Condition profiles — compare to base FHIR resources
3. Study the USCDI data classes at healthit.gov
4. Map US Core profiles to USCDI data classes using the IG's mapping page
5. Understand "Additional USCDI Requirements" in US Core 6.1.0+

**Milestone**: Can identify which US Core profile applies to a given clinical concept; understands Must Support obligations

### Phase 4: Epic FHIR Implementation (Week 5, ~10 hours)

**Goal**: Navigate Epic's FHIR implementation and build against the sandbox

1. Register at open.epic.com and obtain a client ID
2. Review Epic's CapabilityStatement from the sandbox
3. Explore supported resources and operations at fhir.epic.com/Specifications
4. Compare Epic's resource support to US Core requirements — identify gaps
5. Test read and search operations against Epic sandbox endpoints
6. Use the SMART on FHIR Launchpad at open.epic.com/launchpad

**Milestone**: Can query Epic's sandbox for Patient, Observation, and Condition data; understands Epic-specific limitations

### Phase 5: Client Library Development (Week 6, ~10 hours)

**Goal**: Build working FHIR client code using established libraries

1. Choose your primary language (JS, Python, or Java)
2. Set up a development environment with the appropriate FHIR client library
3. Implement basic CRUD operations against the HAPI public test server
4. Add SMART on FHIR authentication for Epic sandbox
5. Build a simple data retrieval script that pulls patient demographics, conditions, and medications
6. Handle pagination, error responses, and OperationOutcome parsing

**Milestone**: Working code that authenticates with Epic sandbox and retrieves clinical data

---

## Practical Exercises

### Exercise 1: FHIR Resource Exploration (Beginner, ~2 hours)

Using the public HAPI FHIR test server (https://hapi.fhir.org/baseR4):
- `GET /Patient?_count=5` — retrieve patients
- Read one patient by ID
- Explore the patient's references (encounters, observations)
- Create a new Patient resource via POST
- Update the patient via PUT

### Exercise 2: Search Deep Dive (Intermediate, ~3 hours)

Against the HAPI test server:
- Search for patients by name with `:exact` and `:contains` modifiers
- Search observations by date range using `ge` and `le` prefixes
- Chain: Find all observations for patients named "Smith"
- Use `_include` to get Patient resources alongside Observations
- Use `_revinclude` to get Conditions when searching Patients
- Test `_summary=count` to get result counts without data

### Exercise 3: US Core Profile Validation (Intermediate, ~2 hours)

- Download a US Core Patient profile from the IG
- Create a Patient resource that conforms to US Core (include race, ethnicity extensions)
- Validate against the profile using the FHIR validator (https://validator.fhir.org/)
- Fix validation errors and understand why they occur

### Exercise 4: Epic Sandbox — First Contact (Intermediate, ~3 hours)

1. Register an app at open.epic.com
2. Use the Epic sandbox base URL to query the CapabilityStatement (`GET /metadata`)
3. Search for test patients: `GET /Patient?family=Argonaut`
4. Retrieve a patient's conditions: `GET /Condition?patient=[id]`
5. Retrieve medications: `GET /MedicationRequest?patient=[id]`
6. Try a DocumentReference search and observe the CCDA content

### Exercise 5: Epic SMART on FHIR Launch (Advanced, ~4 hours)

1. Go to open.epic.com/launchpad
2. Configure a SMART app launch (standalone or EHR launch)
3. Complete the OAuth2 authorization flow
4. Use the access token to call secured FHIR endpoints
5. Retrieve the launch context (patient, encounter)
6. Build a simple web page that displays the patient's problem list

### Exercise 6: Build a FHIR Client Application (Advanced, ~6 hours)

Using your chosen language and library:

**Python example with fhirclient:**
```python
from fhirclient import client
from fhirclient.models.patient import Patient
from fhirclient.models.condition import Condition

# Configure for Epic sandbox
settings = {
    'app_id': 'your_client_id',
    'api_base': 'https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4'
}
smart = client.FHIRClient(settings=settings)

# Search for patients
search = Patient.where(struct={'family': 'Argonaut'})
patients = search.perform_resources(smart.server)
for p in patients:
    print(f"{p.name[0].given[0]} {p.name[0].family}")

# Get conditions for first patient
patient_id = patients[0].id
cond_search = Condition.where(struct={'patient': patient_id})
conditions = cond_search.perform_resources(smart.server)
for c in conditions:
    print(f"  Condition: {c.code.text}")
```

**JavaScript example with @smart-on-fhir/client-js:**
```javascript
import FHIR from 'fhirclient';

// Standalone launch
FHIR.oauth2.authorize({
  clientId: 'your_client_id',
  scope: 'patient/*.read launch/patient',
  redirectUri: './callback.html',
  iss: 'https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4'
});

// After redirect, in callback:
FHIR.oauth2.ready().then(client => {
  // Read current patient
  client.patient.read().then(patient => {
    console.log(`Patient: ${patient.name[0].given[0]} ${patient.name[0].family}`);
  });

  // Search conditions
  client.request(`Condition?patient=${client.patient.id}`)
    .then(bundle => {
      bundle.entry?.forEach(e => {
        console.log(`Condition: ${e.resource.code?.text}`);
      });
    });
});
```

### Exercise 7: Coverage Gap Analysis (Advanced, ~3 hours)

1. Query Epic sandbox CapabilityStatement (`GET /metadata`)
2. Parse the supported resources and interactions
3. Compare against US Core required profiles (list from US Core IG)
4. Document which US Core profiles Epic supports, partially supports, or doesn't support
5. For partial support, identify which search parameters or operations are missing
6. Write up findings as a compatibility matrix

---

## Connections to Other Domains

- **D-1 (Interoperability Foundations)**: FHIR R4 is the modern implementation of the interoperability concepts introduced there
- **D-3 (Terminology and Coding)**: FHIR resources use the code systems (SNOMED CT, LOINC, ICD-10, RxNorm, CPT) studied in D-3; CodeableConcept and ValueSet bindings tie them together
- **Upcoming — SMART on FHIR / OAuth2**: Deep dive into the authorization framework that secures FHIR API access
- **Upcoming — Epic App Orchard**: Where FHIR-based apps get distributed to Epic customers
- **Upcoming — CDS Hooks**: Clinical decision support that uses FHIR resources as context
