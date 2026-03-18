# Healthcare Data Foundations and Regulatory Landscape

## Overview

This domain covers the foundational healthcare data standards and regulatory frameworks that every AI-in-healthcare developer must understand before building AI-powered features. It answers two critical questions: **What data does healthcare AI consume?** and **What rules constrain how AI can operate in clinical settings?**

This is the first domain in the learning plan because every subsequent domain — from predictive AI to agentic systems — depends on understanding FHIR resources, DICOM imaging pipelines, X12 claims data, HIPAA de-identification requirements, and FDA software classification. Without this foundation, developers will build AI features that cannot integrate with real EHR systems or that violate regulatory requirements.

**Estimated total time: 35-45 hours**

---

## Key Concepts

### A. Healthcare Data Standards

#### 1. FHIR R4 (Fast Healthcare Interoperability Resources, Release 4)
- **What it is:** The modern HL7 standard for exchanging healthcare data using RESTful APIs, JSON/XML resources, and web-native patterns
- **Key concepts:** Resources (Patient, Observation, Condition, MedicationRequest, Encounter, etc.), Bundles, Search parameters, Profiles, Extensions, Implementation Guides
- **AI relevance:** FHIR is the primary input/output format for AI features in modern healthcare apps. AI models consume FHIR resources as input (patient data for predictions) and produce FHIR-compatible output (risk scores as Observations, recommendations as CarePlans)
- **Prerequisite for:** Domains D-3 (Predictive AI needs FHIR patient data), D-4 (LLMs process FHIR clinical notes), D-5 (RAG systems search FHIR data stores), D-7 (imaging results stored as FHIR DiagnosticReport)

#### 2. HL7v2 (Health Level Seven Version 2)
- **What it is:** Legacy pipe-delimited messaging standard still powering ~95% of US hospital internal communications
- **Key concepts:** Segments (MSH, PID, OBR, OBX), Message types (ADT, ORM, ORU), MLLP protocol, Z-segments (custom extensions)
- **AI relevance:** Many AI systems must ingest HL7v2 data from legacy systems. NLP and data transformation AI can automate HL7v2-to-FHIR conversion
- **Relationship to FHIR:** HL7v2 is the predecessor; most organizations run both simultaneously. Understanding HL7v2 is essential for building AI that works with legacy hospital infrastructure

#### 3. DICOM (Digital Imaging and Communications in Medicine)
- **What it is:** The international standard for medical imaging data — format, storage, and transmission
- **Key concepts:** DICOM files (image data + metadata), PACS (Picture Archiving and Communication Systems), DICOMweb (RESTful access), SOP Classes, Transfer Syntax, Modalities (CT, MRI, X-ray, Ultrasound)
- **AI relevance:** All medical imaging AI pipelines start with DICOM data. Understanding DICOM metadata, de-identification of burnt-in PHI, and conversion to ML-ready formats (NIfTI, PNG) is essential
- **Prerequisite for:** D-7 (Computer Vision and Medical Imaging AI)

#### 4. X12/EDI (Electronic Data Interchange)
- **What it is:** HIPAA-mandated electronic formats for administrative and financial healthcare transactions
- **Key transaction sets:**
  - **837** (Healthcare Claim — Professional, Institutional, Dental): Provider submits claims to payer
  - **835** (Electronic Remittance Advice): Payer returns payment details to provider
  - **270/271** (Eligibility Inquiry/Response): Verify patient insurance coverage
  - **278** (Prior Authorization Request/Response): Request service authorization
  - **276/277** (Claim Status Inquiry/Response): Check claim adjudication status
- **AI relevance:** Claims and eligibility data feeds predictive models for prior auth likelihood, denial prediction, cost estimation, and revenue cycle optimization
- **Prerequisite for:** D-3 (Predictive AI for revenue cycle), D-9 (Decisioning AI for prior auth automation)

#### 5. CDS Hooks (Clinical Decision Support Hooks)
- **What it is:** HL7 standard for triggering real-time clinical decision support within EHR workflows
- **Key concepts:** Hooks (patient-view, order-select, order-sign, encounter-start, encounter-discharge, appointment-book), CDS Services, Cards (information, suggestion, app link), Prefetch templates
- **AI relevance:** CDS Hooks is THE integration point for embedding AI into clinical workflows. AI-powered CDS services receive patient context at decision points and return recommendations as cards
- **Prerequisite for:** D-9 (Decisioning AI and CDS), D-12 (Agentic Systems that respond to clinical events)

#### 6. SMART on FHIR (Substitutable Medical Applications, Reusable Technologies)
- **What it is:** Framework combining OAuth 2.0 + OpenID Connect with FHIR APIs to enable third-party app integration with EHRs
- **Key concepts:** EHR Launch vs. Standalone Launch, Scopes (patient/*.read, launch/encounter), SMART App Launch Framework, App registration with EHR vendors (Epic App Orchard, Cerner/Oracle Ignite)
- **AI relevance:** SMART on FHIR is how AI-powered applications get deployed inside EHRs. "Write once, deploy to Epic, Cerner, and any SMART-enabled EHR"
- **Prerequisite for:** All domains that involve deploying AI features within EHR contexts

#### 7. USCDI (United States Core Data for Interoperability)
- **What it is:** ONC-defined minimum dataset that must be available for exchange across healthcare systems
- **Key concepts:** USCDI versions (v3 required by HTI-1, v5 released July 2024), Data classes and elements, Relationship to FHIR US Core profiles
- **AI relevance:** Defines the minimum data AI systems can expect to be available from certified EHRs

### B. Regulatory Framework

#### 8. HIPAA (Health Insurance Portability and Accountability Act)
- **What it is:** Federal law governing the privacy and security of protected health information (PHI)
- **Key components for developers:**
  - **Privacy Rule:** Who can access PHI, minimum necessary principle, patient rights
  - **Security Rule:** Administrative, physical, and technical safeguards for ePHI
  - **Breach Notification Rule:** Requirements when PHI is compromised
  - **Business Associate Agreements (BAAs):** Required contracts when third parties handle PHI (including AI/cloud vendors)
- **AI-specific concerns:** PHI in training data, PHI in prompts to LLMs, PHI in logs/metrics, PHI in model weights

#### 9. HIPAA De-identification: Safe Harbor Method
- **What it is:** Prescriptive method requiring removal of 18 specific identifiers from data
- **The 18 identifiers:** Names, geographic data below state level (with ZIP code exception for populations >20,000), dates (except year, with age >89 aggregation), phone numbers, fax numbers, email addresses, SSNs, medical record numbers, health plan beneficiary numbers, account numbers, certificate/license numbers, vehicle identifiers, device identifiers, URLs, IP addresses, biometric identifiers, full-face photos, any other unique identifier
- **Practical guidance:** Can be automated with regex patterns and NLP-based NER. Good for large datasets where some data granularity loss is acceptable
- **Limitation:** Removes data that may be valuable for AI training (exact dates, geographic precision)

#### 10. HIPAA De-identification: Expert Determination Method
- **What it is:** Flexible method where a qualified statistical expert certifies that re-identification risk is "very small"
- **Process:** Expert applies statistical/scientific methods, considers data context and recipient capabilities, documents methods and justification
- **Practical guidance:** More expensive but preserves greater data utility. Preferred for AI training datasets where date precision or geographic detail matters
- **Techniques used:** k-anonymity, l-diversity, t-closeness, differential privacy, data suppression, generalization, noise addition

#### 11. FDA Software as a Medical Device (SaMD)
- **What it is:** Software intended for medical purposes that performs those functions without being part of hardware
- **Classification framework:**
  - **Class I:** Lowest risk, general controls, often exempt from premarket review
  - **Class II:** Moderate risk, requires 510(k) clearance or De Novo classification. As of 2024, ALL FDA-authorized AI/ML SaMDs are Class II
  - **Class III:** Highest risk, requires Premarket Approval (PMA)
- **Key regulatory pathways:** 510(k) (substantial equivalence), De Novo (novel low-moderate risk), PMA (high risk)
- **AI/ML specifics:** Predetermined Change Control Plans (PCCPs) allow manufacturers to plan for algorithmic updates post-market. FDA finalized PCCP guidance in December 2024

#### 12. FDA Software in a Medical Device (SiMD)
- **What it is:** Software that is integral to a hardware medical device (device wouldn't function without it)
- **Distinction from SaMD:** SiMD is embedded in hardware; SaMD is standalone software
- **Example:** Software controlling an insulin pump based on glucose readings (SiMD) vs. a mobile app that recommends insulin dosing (SaMD)

#### 13. FDA CDS Exemption Criteria (Section 520(o)(1)(E))
- **What it is:** Four criteria that, if ALL met, exempt CDS software from FDA device regulation
- **The four criteria:**
  1. **Not intended to acquire, process, or analyze medical images or signals** from IVD or signal acquisition systems
  2. **Intended to display, analyze, or print medical information** (patient data, clinical guidelines, drug labels)
  3. **Intended to support or provide recommendations** to healthcare professionals (not replace judgment)
  4. **Intended to enable independent review** by the HCP of the basis for recommendations (transparency requirement)
- **Critical implication:** If your AI CDS tool processes medical images, replaces clinical judgment, or doesn't allow independent review, it's likely a regulated medical device
- **Time-critical decisions:** Software for time-critical decisions generally fails criterion 4 (no time for independent review)

#### 14. ONC Cures Act and Information Blocking
- **What it is:** 21st Century Cures Act provisions enforced by ONC promoting interoperability and prohibiting information blocking
- **Key rules:**
  - **Information Blocking:** Practices that interfere with access, exchange, or use of EHI are prohibited (with eight exceptions)
  - **HTI-1 Final Rule (Jan 2024):** AI/algorithm transparency requirements for certified health IT, USCDI v3 baseline
  - **HTI-2 (2024):** Expanded certification, TEFCA requirements
  - **Disincentives (effective July 2024):** Financial penalties for providers who information block (Medicare payment reductions, MIPS zero scores, ACO exclusion)
- **AI relevance:** AI systems must not create information blocking. AI-generated data must be accessible. Certified health IT using AI must meet transparency requirements

#### 15. State AI Healthcare Laws
- **What it is:** Rapidly evolving state-level regulations specific to AI in healthcare
- **Key examples:**
  - **California AB 3030 (Jan 2025):** Must disclose when generative AI produces patient communications with clinical info
  - **California SB 1120 "Physicians Make Decisions Act" (Jan 2025):** Restricts health plan AI from overriding provider judgment
  - **Texas TRAIGA (Jan 2026):** Must disclose AI use in diagnosis/treatment to patients
  - **Illinois HB 1806 (Aug 2025):** AI cannot make independent therapeutic decisions; requires licensed professional review
  - **Colorado AI Act (2024):** Duty-of-care for high-risk AI systems, risk assessments, deployer/developer obligations
- **Pattern:** Transparency disclosure, anti-discrimination, human oversight requirements, use-case restrictions

#### 16. CMS Reimbursement and Quality Reporting
- **What it is:** Centers for Medicare & Medicaid Services rules affecting how AI-assisted services are reimbursed
- **Key concepts:** CPT codes for AI-assisted procedures, quality measure reporting (eCQMs), MIPS, value-based care programs
- **AI relevance:** Understanding reimbursement determines which AI features have a business case

### C. Cross-Cutting Concepts

#### 17. Healthcare Data Pipeline Architecture
- **What it is:** How data flows from source systems (EHR, PACS, claims) through transformation to AI-ready formats
- **Key patterns:** HL7v2 → FHIR conversion, DICOM → NIfTI for imaging ML, X12 → structured data for predictive models, real-time streaming vs. batch ETL

#### 18. Medical Terminologies and Code Systems
- **What it is:** Standardized vocabularies used across healthcare data
- **Key systems:** ICD-10 (diagnoses), CPT/HCPCS (procedures), SNOMED CT (clinical terms), LOINC (lab observations), RxNorm (medications), NDC (drug products)
- **AI relevance:** AI models must understand and correctly use these code systems. NLP systems map free text to coded concepts. Prerequisite for D-5 (Knowledge Systems)

#### 19. Synthetic Data Generation for Healthcare
- **What it is:** Creating realistic but non-real patient data for development and testing
- **Key tool:** Synthea — open-source generator producing complete patient histories in FHIR R4 format
- **AI relevance:** Essential for developing and testing AI features without touching real PHI

---

## Learning Resources

### Online Courses

1. **HL7 FHIR Mastery: A Course for Newbies and Pros** (Udemy)
   - URL: https://www.udemy.com/course/hl7-fhir-mastery-a-course-for-newbies-and-pros/
   - Duration: ~10 hours
   - Cost: ~$20-50 (Udemy sales)
   - Level: Beginner to Intermediate
   - Covers: FHIR R4 standard, resources, search, profiles, implementation. Frequently updated (July 2025 update). Rated 4.4/5

2. **Health Informatics: Data and Interoperability Standards** (Georgia Tech Professional Education)
   - URL: https://pe.gatech.edu/courses/health-informatics-data-and-interoperability-standards
   - Duration: Self-paced
   - Cost: Varies
   - Level: Intermediate
   - Covers: FHIR, SMART on FHIR, healthcare data standards, hands-on with web tools

3. **FHIR Fundamentals Course** (Medblocks)
   - URL: https://medblocks.com/training/courses/fhir-fundamentals
   - Duration: Self-paced
   - Cost: Check site
   - Level: Beginner
   - Covers: Hands-on projects with FHIR, Epic and Cerner integration, data types, resources, financial workflows

4. **Ingesting FHIR Data with the Healthcare API** (Google Cloud / Coursera)
   - URL: https://www.coursera.org/projects/googlecloud-ingesting-fhir-data-with-the-healthcare-api-yhvbk
   - Duration: ~1.5 hours
   - Cost: Free with Coursera trial
   - Level: Beginner
   - Covers: Google Cloud Healthcare API, importing/exporting FHIR data

5. **Firely FHIR Training Courses**
   - URL: https://fire.ly/training-3/
   - Duration: 3-day overview course; data modeling course available
   - Cost: Paid (professional training)
   - Level: Beginner to Intermediate
   - Covers: 50% hands-on exercises, FHIR profiling, implementation patterns

6. **HL7 + FHIR Training** (HL7 Training Institute)
   - URL: https://hl7trainingtutorials.com/hl7-fhir-training/
   - Duration: Multi-day
   - Cost: Paid
   - Level: Beginner to Intermediate
   - Covers: Both HL7v2 and FHIR, Mirth Connect, Postman, HAPI FHIR Server, real-time examples

### Video Tutorials and Talks

7. **FHIR for Developers — DevDays Presentations**
   - URL: https://www.youtube.com/results?search_query=HL7+FHIR+DevDays
   - Various talks from annual FHIR DevDays conferences covering hands-on FHIR development, AI microservice invocation with FHIR, CDS Hooks implementation
   - Free

8. **How to Set Up Your Own FHIR Server with HAPI FHIR** (YouTube)
   - URL: https://www.youtube.com/watch?v=bZraNRnRGVc
   - Duration: ~15 min
   - Covers: Docker-based HAPI FHIR server setup, REST interactions

9. **SMART on FHIR Tutorial** (Cerner Engineering)
   - URL: https://engineering.cerner.com/smart-on-fhir-tutorial/
   - Covers: Step-by-step browser-based SMART app development
   - Free

### Books

10. **"FHIR for Developers" by Dave Hay**
    - Level: Beginner to Intermediate
    - Covers: Practical FHIR development, resources, search, profiles
    - Relevant chapters: All — focused on developer implementation

11. **"Health Information Technology Standards" (various academic texts)**
    - Level: Intermediate
    - Covers: HL7v2, FHIR, DICOM, X12, CDA standards comprehensively

12. **"HIPAA for Developers" (online guides and compliance resources)**
    - URL: https://www.vanta.com/resources/develop-hipaa-compliant-software
    - Level: Beginner
    - Covers: Practical HIPAA compliance for software development teams

### Official Documentation and Specifications

13. **HL7 FHIR R4 Specification**
    - URL: https://hl7.org/fhir/R4/
    - The definitive reference. Covers every resource, data type, search parameter, and operation
    - Free

14. **CDS Hooks Specification**
    - URL: https://cds-hooks.org/ and https://cds-hooks.hl7.org/1.0/
    - Official specification for CDS Hooks standard
    - Free

15. **SMART on FHIR Documentation**
    - URL: https://docs.smarthealthit.org/
    - Official docs for SMART App Launch, client libraries, tutorials
    - Free

16. **DICOM Standard**
    - URL: https://www.dicomstandard.org/
    - AI-specific page: https://www.dicomstandard.org/ai
    - The complete DICOM specification and AI integration guidance
    - Free

17. **HHS HIPAA De-identification Guidance**
    - URL: https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html
    - Official HHS guidance on Safe Harbor and Expert Determination methods
    - Free

18. **FDA SaMD Guidance Page**
    - URL: https://www.fda.gov/medical-devices/digital-health-center-excellence/software-medical-device-samd
    - Official FDA resources on SaMD classification, AI/ML action plan, guidances
    - Free

19. **FDA AI/ML SaMD Page**
    - URL: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-software-medical-device
    - List of FDA-authorized AI/ML devices, action plan, transparency principles
    - Free

20. **ONC Cures Act Final Rule**
    - URL: https://healthit.gov/regulations/cures-act-final-rule/
    - Official ONC page on information blocking rules, HTI-1, USCDI
    - Free

21. **ONC Information Blocking Portal**
    - URL: https://unblock.federalregister.gov/
    - Federal Register portal for information blocking rules and disincentives
    - Free

22. **X12 Healthcare Transactions**
    - URL: https://x12.org/flow/health-care
    - Overview of X12 healthcare transaction sets
    - Free overview; full TR3 specs require purchase

### Interactive Exercises and Practice

23. **Synthea — Synthetic Patient Generator**
    - URL: https://github.com/synthetichealth/synthea
    - Docs: https://synthetichealth.github.io/synthea/
    - Generate FHIR R4 patient bundles for hands-on practice. Customizable by disease, location, population
    - Free, open source

24. **HAPI FHIR JPA Server Starter**
    - URL: https://github.com/hapifhir/hapi-fhir-jpaserver-starter
    - Set up your own FHIR server with Docker in minutes. Practice CRUD operations, search, profiles
    - Free, open source

25. **SMART App Launcher (Testing Tool)**
    - URL: https://launch.smarthealthit.org/
    - Test SMART on FHIR apps without EHR vendor registration
    - Free

26. **Google Cloud Healthcare API FHIR Lab**
    - URL: https://developers.google.com/open-health-stack/resources/getting-started-with-fhir
    - Hands-on getting started with FHIR on Google Cloud
    - Free tier available

27. **MITRE FHIR for Research — Synthea Module**
    - URL: https://mitre.github.io/fhir-for-research/modules/synthea-overview
    - Educational module on using Synthea for FHIR data generation
    - Free

### GitHub Repositories

28. **HAPI FHIR** (Core Library)
    - URL: https://github.com/hapifhir/hapi-fhir
    - The most widely used open-source Java FHIR implementation
    - Stars: 2k+

29. **Synthea**
    - URL: https://github.com/synthetichealth/synthea
    - Open-source synthetic patient generator
    - Stars: 2k+

30. **SMART on FHIR Client Libraries**
    - JavaScript: https://github.com/smart-on-fhir/client-js
    - Python: https://github.com/smart-on-fhir/client-py
    - Multiple language support for SMART app development

31. **HL7 FHIR Open Source Implementations List**
    - URL: https://confluence.hl7.org/display/FHIR/Open+Source+Implementations
    - Comprehensive list of open-source FHIR servers and clients

32. **Pydicom**
    - URL: https://github.com/pydicom/pydicom
    - Python library for reading/writing DICOM files — essential for imaging AI pipelines

### Community Resources

33. **HL7 FHIR Chat (Zulip)**
    - URL: https://chat.fhir.org/
    - Official HL7 FHIR community chat. Very active, includes implementers and spec authors

34. **r/healthIT** (Reddit)
    - URL: https://www.reddit.com/r/healthIT/
    - Discussions on healthcare IT, interoperability, EHR integration

35. **FHIR DevDays** (Annual Conference)
    - URL: https://www.devdays.com/
    - Premier FHIR developer conference. Recordings often available on YouTube

### Podcasts

36. **Health IT on the Record** (CHIME/AEHIS)
    - Covers healthcare IT leadership, interoperability trends

37. **Digital Health Today**
    - URL: https://digitalhealthtoday.com/
    - Covers digital health innovation including data standards and regulation

---

## Learning Path

### Phase 1: Healthcare Data Standards Fundamentals (12-15 hours)

**Cluster 1.1: FHIR R4 Core (6-8 hours)**
- Start with FHIR R4 specification overview (resources, data types, REST API)
- Complete the Udemy FHIR Mastery course or Medblocks FHIR Fundamentals
- Set up HAPI FHIR server locally with Docker
- Practice CRUD operations on Patient, Observation, Condition resources
- **Milestone:** Can create, read, search, and update FHIR resources on a local server

**Cluster 1.2: Legacy and Specialty Standards (3-4 hours)**
- HL7v2 message structure (MSH, PID, OBR, OBX segments), ADT/ORM/ORU messages
- DICOM overview: file format, metadata, PACS, DICOMweb
- X12/EDI: 837, 835, 270/271, 278 transaction sets
- Understand when each standard is used and how they relate
- **Milestone:** Can identify which standard is used for a given healthcare data exchange scenario

**Cluster 1.3: CDS Hooks and SMART on FHIR (3-4 hours)**
- CDS Hooks specification: hooks, services, cards, prefetch
- SMART on FHIR: launch framework, OAuth 2.0 flow, scopes
- Walk through Cerner SMART on FHIR tutorial
- Test with SMART App Launcher
- **Milestone:** Can describe how an AI-powered CDS service integrates with an EHR via CDS Hooks and SMART on FHIR

### Phase 2: Medical Terminologies and Data Pipelines (5-7 hours)

**Cluster 2.1: Code Systems and Terminologies (2-3 hours)**
- ICD-10, CPT/HCPCS for diagnoses and procedures
- SNOMED CT for clinical concepts
- LOINC for lab observations
- RxNorm and NDC for medications
- How terminologies appear in FHIR resources (Coding, CodeableConcept)
- **Milestone:** Can map a clinical scenario to appropriate code systems

**Cluster 2.2: Data Pipeline Patterns (3-4 hours)**
- HL7v2 to FHIR conversion patterns (using Mirth Connect or similar)
- DICOM to ML-ready format conversion (pydicom, dcm2niix)
- X12 parsing for predictive models
- Synthea for generating test data
- **Milestone:** Can generate synthetic FHIR data with Synthea and load it into a HAPI FHIR server

### Phase 3: HIPAA and De-identification (6-8 hours)

**Cluster 3.1: HIPAA Fundamentals (3-4 hours)**
- Privacy Rule: PHI definition, minimum necessary, permitted uses
- Security Rule: administrative, physical, technical safeguards
- BAA requirements for AI/cloud vendors
- PHI in AI contexts: training data, prompts, logs, model weights
- **Milestone:** Can identify PHI in a dataset and explain BAA requirements for an AI vendor

**Cluster 3.2: De-identification Methods (3-4 hours)**
- Safe Harbor: the 18 identifiers, automation strategies, limitations
- Expert Determination: process, statistical methods, documentation
- Practical implementation: NER-based PHI detection, regex patterns, k-anonymity
- Trade-offs: data utility vs. privacy for AI training
- **Milestone:** Can apply Safe Harbor de-identification to a synthetic dataset and explain when Expert Determination is preferred

### Phase 4: FDA and Regulatory Compliance (8-10 hours)

**Cluster 4.1: FDA SaMD/SiMD Framework (3-4 hours)**
- SaMD vs. SiMD definitions and examples
- Risk classification (Class I/II/III) and regulatory pathways (510(k), De Novo, PMA)
- AI/ML-specific guidance: PCCP, total product lifecycle approach, transparency principles
- **Milestone:** Can classify a hypothetical AI healthcare feature as SaMD or non-device and identify the regulatory pathway

**Cluster 4.2: CDS Exemption Criteria (2-3 hours)**
- The four criteria for CDS exemption from device regulation
- Examples of exempt vs. regulated CDS
- Design implications: how to build AI CDS features that qualify for exemption
- **Milestone:** Can evaluate an AI CDS feature against the four exemption criteria

**Cluster 4.3: ONC, State Laws, and CMS (3-4 hours)**
- ONC Cures Act: information blocking rules, eight exceptions, disincentives
- HTI-1: AI transparency requirements for certified health IT
- State AI healthcare laws: California AB 3030, Texas TRAIGA, Illinois HB 1806, Colorado AI Act
- CMS reimbursement context for AI-assisted services
- **Milestone:** Can identify the regulatory requirements for deploying an AI feature in a given state

### Phase 5: Integration Exercise (4-5 hours)

**Capstone practical exercise combining all concepts:**
- Design the data flow and regulatory compliance plan for a hypothetical AI feature (e.g., readmission risk prediction embedded in an EHR via CDS Hooks)
- **Milestone:** Can produce a written design document covering data standards, integration patterns, HIPAA compliance, and FDA classification for an AI healthcare feature

---

## Practical Exercises

### Exercise 1: FHIR Server Setup and Exploration (2 hours)
- Deploy HAPI FHIR server with Docker
- Load Synthea-generated patient data
- Query patients, observations, conditions using FHIR search
- Create a new Observation resource representing an AI-generated risk score
- **Tools:** Docker, HAPI FHIR, Synthea, Postman or curl

### Exercise 2: CDS Hooks Mock Service (2-3 hours)
- Build a simple CDS Hooks service that responds to `patient-view` hook
- Service queries FHIR server for patient conditions
- Returns an information card with a mock risk assessment
- **Tools:** Node.js or Python, FHIR client library, CDS Hooks spec

### Exercise 3: HIPAA De-identification Pipeline (2 hours)
- Take a Synthea-generated FHIR bundle
- Implement Safe Harbor de-identification: remove all 18 identifier types
- Verify completeness of de-identification
- Document which data elements were removed and impact on AI utility
- **Tools:** Python, FHIR JSON processing

### Exercise 4: FDA Classification Analysis (1-2 hours)
- Given 5 hypothetical AI healthcare features, classify each as:
  - Non-device (CDS exemption met)
  - SaMD Class I/II/III
  - SiMD
- Justify each classification against the four CDS exemption criteria and IMDRF risk framework
- **Format:** Written analysis document

### Exercise 5: Regulatory Compliance Checklist (1-2 hours)
- For a hypothetical AI-powered clinical note summarization feature:
  - Map HIPAA requirements (PHI handling, BAA, de-identification strategy)
  - Assess FDA classification
  - Identify applicable state laws (pick 2-3 states)
  - Identify ONC/Cures Act implications
  - Draft compliance checklist
- **Format:** Compliance matrix document

---

## Connections to Other Domains

This domain is a **prerequisite for 4 other domains:**

- **D-3 (Predictive AI):** Requires understanding FHIR patient data as model input, X12 claims data for revenue cycle predictions, regulatory constraints on predictive tools
- **D-4 (Foundation Models/Prompt Engineering):** Requires understanding FHIR data structures for prompt construction, HIPAA constraints on PHI in prompts, FDA CDS exemption criteria for LLM-based features
- **D-5 (Embeddings/Knowledge Systems/RAG):** Requires understanding FHIR search and data access patterns, medical terminologies (SNOMED, LOINC, ICD-10) for knowledge graphs
- **D-7 (Computer Vision/Medical Imaging):** Requires understanding DICOM standard, imaging data pipelines, FDA SaMD classification for imaging AI

**Cross-cutting relevance:** The regulatory knowledge (HIPAA, FDA, ONC, state laws) from this domain applies to EVERY subsequent domain in the learning plan. This is why it's positioned first — regulatory compliance must be threaded throughout all AI development work.
