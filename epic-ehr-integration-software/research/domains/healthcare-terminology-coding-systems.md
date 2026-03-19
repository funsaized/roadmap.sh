# Healthcare Terminology and Coding Systems

## Overview

Healthcare terminology and coding systems form the semantic backbone of health IT interoperability. When building software that integrates with Epic, every clinical data element — diagnoses, lab results, medications, procedures, immunizations — is represented using standardized codes. Understanding these coding systems is essential for correctly interpreting FHIR resources, mapping between Epic's internal identifiers and external standards, and building applications that work reliably across different Epic installations.

This domain covers the major coding systems (SNOMED CT, ICD-10, LOINC, RxNorm, CPT, CVX), how Epic maps between internal and standard codes, and how FHIR terminology services enable programmatic code lookup and validation.

**Connection to Epic Integration:** Every FHIR resource returned by Epic's APIs contains coded elements (CodeableConcept fields). An integration developer must understand which coding system applies to which data type, how to handle multiple codings for the same concept, and how to resolve Epic-specific internal codes to standard terminologies.

---

## Key Concepts

### 1. SNOMED CT (Systematized Nomenclature of Medicine Clinical Terms)
- **What:** The most comprehensive multilingual clinical terminology, with 300,000+ concepts maintained by SNOMED International
- **Use Cases:** Clinical findings, disorders, procedures, body structures, organisms, substances
- **Structure:** Hierarchical concept model with concepts, descriptions, and relationships; logic-based definitions
- **In Epic/FHIR:** Used in Condition resources (clinical findings), Procedure resources, and Observation resources. Epic maps internal problem list items to SNOMED CT codes
- **FHIR System URI:** `http://snomed.info/sct`
- **License:** Requires SNOMED International member country affiliation or an Affiliate License for use

### 2. ICD-10 (International Classification of Diseases, 10th Revision)
- **What:** WHO-endorsed classification for diseases, injuries, and causes of death
- **Variants:**
  - **ICD-10-CM** (Clinical Modification) — US diagnoses across all settings
  - **ICD-10-PCS** (Procedure Coding System) — US inpatient procedures
- **Use Cases:** Billing/reimbursement, diagnosis reporting, epidemiological tracking, mortality statistics
- **Structure:** 3-7 character alphanumeric codes; much more specific than ICD-9 (68,000+ diagnosis codes vs ~14,000)
- **In Epic/FHIR:** Primary coding for Condition resources for billing purposes; Epic's diagnosis records typically carry both ICD-10 and SNOMED CT codes
- **FHIR System URI:** `http://hl7.org/fhir/sid/icd-10-cm`
- **Mandated:** HIPAA-covered entities required to use ICD-10 since October 1, 2015

### 3. LOINC (Logical Observation Identifiers Names and Codes)
- **What:** Universal standard for identifying lab tests, clinical observations, surveys, and document types; maintained by the Regenstrief Institute
- **Use Cases:** Laboratory test identification, vital signs, clinical documents, survey instruments, claims attachments
- **Structure:** Six-part naming convention (Component, Property, Time Aspect, System, Scale Type, Method) ensuring unique identification
- **Two Parts:** Laboratory LOINC (lab tests, microbiology) and Clinical LOINC (vital signs, ECGs, documents, surveys)
- **In Epic/FHIR:** Primary coding for Observation resources (labs, vitals), DiagnosticReport resources, and DocumentReference resources
- **FHIR System URI:** `http://loinc.org`
- **License:** Free to use; registration required at loinc.org
- **Size:** 95,000+ codes

### 4. RxNorm
- **What:** Standardized nomenclature for clinical drugs produced by the National Library of Medicine (NLM)
- **Use Cases:** Medication identification, drug interaction checking, prescription interoperability, formulary management
- **Structure:** Normalizes drug names by ingredient, strength, and dose form; assigns RxCUI (Concept Unique Identifiers)
- **Concept Types:** Ingredient (IN), Brand Name (BN), Semantic Clinical Drug (SCD), Semantic Branded Drug (SBD), Generic Pack (GPCK), Branded Pack (BPCK)
- **In Epic/FHIR:** Primary coding for MedicationRequest, MedicationStatement, and Medication resources
- **FHIR System URI:** `http://www.nlm.nih.gov/research/umls/rxnorm`
- **Scope:** Prescription and many OTC drugs approved for US human use; does not include supplements or devices

### 5. CPT (Current Procedural Terminology)
- **What:** Medical procedure and service coding system published by the American Medical Association (AMA)
- **Use Cases:** Professional fee billing, procedure reporting, utilization tracking
- **Structure:** 5-digit numeric codes organized into Category I (procedures/services), Category II (performance measurement), Category III (emerging technology)
- **In Epic/FHIR:** Used in Procedure and Claim resources for billing; maps to Epic's internal procedure records
- **FHIR System URI:** `http://www.ama-assn.org/go/cpt`
- **License:** Copyrighted by AMA; requires license for use in applications

### 6. CVX (Vaccines Administered)
- **What:** CDC-maintained numeric code set identifying vaccine products
- **Use Cases:** Immunization data exchange, immunization registries (IIS), vaccine forecasting, clinical decision support
- **Related:** MVX codes (Manufacturer of Vaccines) paired with CVX for trade-name specificity
- **In Epic/FHIR:** Used in Immunization resources; Epic maps internal vaccine records to CVX codes
- **FHIR System URI:** `http://hl7.org/fhir/sid/cvx`
- **CDC Mapping:** CDC provides CVX-to-CPT mapping tables for translating between systems

### 7. Epic Internal Code Mapping
- **What:** Epic uses internal identifiers (Epic IDs, DAT records, masterfile entries) that must be mapped to standard terminologies
- **Key Concepts:**
  - **Identity ID Types (IIT):** Metadata records managing specific identifier sets within Epic
  - **Masterfile records:** Epic's internal database records for diagnoses, procedures, medications, etc.
  - **Crosswalks:** Mapping tables between Epic's internal IDs and standard codes (SNOMED, ICD-10, LOINC, etc.)
  - **Canonical data models:** Intermediate schema normalizing FHIR fields from different EHR vendors
- **Challenge:** The same lab test may be coded differently across Epic installations; organizations must maintain their own terminology mappings
- **In Practice:** When Epic returns a FHIR resource, the `coding` array in a CodeableConcept may contain both an Epic internal code and one or more standard codes

### 8. FHIR Terminology Services
- **What:** FHIR defines a set of resources and operations for working with coded data
- **Core Resources:**
  - **CodeSystem:** Declares and describes a code system (defines which codes exist and what they mean)
  - **ValueSet:** Specifies a set of codes from one or more CodeSystems intended for a specific use context
  - **ConceptMap:** Defines mappings between codes in different systems (source → target with equivalence)
- **Key Operations:**
  - **`$lookup`** (on CodeSystem): Retrieve details about a specific code — display name, definition, status, designations, properties
  - **`$validate-code`** (on CodeSystem or ValueSet): Check if a coded value is valid within a CodeSystem or permitted by a ValueSet
  - **`$expand`** (on ValueSet): Enumerate all codes that are members of a ValueSet
  - **`$translate`** (on ConceptMap): Translate a code from one system to another using defined mappings
  - **`$subsumes`** (on CodeSystem): Test whether one code subsumes another in a hierarchical code system

### 9. CodeableConcept in FHIR
- **What:** The FHIR data type used for coded data elements throughout all FHIR resources
- **Structure:** Contains a `coding` array (each entry has `system`, `code`, `display`) and an optional `text` field
- **Multiple Codings:** A single CodeableConcept can carry codes from multiple systems simultaneously (e.g., both SNOMED CT and ICD-10 for the same diagnosis)
- **Relevance:** Every integration developer must understand how to parse and produce CodeableConcept values correctly

### 10. UMLS (Unified Medical Language System)
- **What:** NLM's compendium that links 200+ biomedical vocabularies including SNOMED CT, ICD-10, LOINC, RxNorm, CPT
- **Components:** Metathesaurus (concepts and relationships), Semantic Network (categories), SPECIALIST Lexicon (language processing)
- **Use Cases:** Cross-terminology mapping, concept normalization, NLP in healthcare
- **Access:** Free UTS account required; provides browser, API, and bulk downloads
- **Relevance:** The foundational resource for understanding how different coding systems relate to each other

### 11. Value Set Authority Center (VSAC)
- **What:** NLM repository of official value sets used in US clinical quality measures and public health reporting
- **Use Cases:** Clinical quality measures (CQMs), electronic clinical quality measures (eCQMs), public health reporting
- **Relevance:** Many Epic-based quality reporting workflows reference VSAC value sets

### 12. NDC (National Drug Code)
- **What:** FDA-maintained unique product identifier for human drugs in the US
- **Structure:** 3-segment code (labeler, product, package)
- **Relevance:** Often appears alongside RxNorm in medication-related FHIR resources; Epic maps between NDC and RxNorm

---

## Learning Resources

### Official Documentation and References

1. **FHIR R4 Terminology Services Specification**
   - URL: https://build.fhir.org/terminology-service.html
   - Type: Official specification
   - Description: Complete specification of FHIR terminology resources and operations ($lookup, $validate-code, $expand, $translate, $subsumes)
   - Difficulty: Intermediate
   - Cost: Free

2. **NLM Health Data Standards and Terminologies Tutorial**
   - URL: https://www.nlm.nih.gov/oet/ed/healthdatastandards/02-530.html
   - Type: Online tutorial/course
   - Description: Official NLM tutorial covering LOINC, SNOMED CT, RxNorm, and their role in health data standards
   - Difficulty: Beginner
   - Cost: Free

3. **SNOMED CT Starter Guide**
   - URL: https://www.snomed.org/what-is-snomed-ct
   - Type: Official documentation
   - Description: SNOMED International's overview and practical guides for understanding SNOMED CT concepts, relationships, and reference sets
   - Difficulty: Beginner–Intermediate
   - Cost: Free

4. **LOINC Official Website and Search Tool**
   - URL: https://loinc.org
   - Type: Interactive tool / database
   - Description: Official LOINC database with online search, code lookup, and the RELMA mapping assistant for download
   - Difficulty: Beginner–Intermediate
   - Cost: Free (registration required)

5. **RxNorm Overview and API (NLM)**
   - URL: https://www.nlm.nih.gov/research/umls/rxnorm/overview.html
   - Type: Documentation / API reference
   - Description: NLM's comprehensive guide to RxNorm concepts, relationships, and the RxNorm API for programmatic drug lookups
   - Difficulty: Intermediate
   - Cost: Free

6. **Epic on FHIR Developer Portal**
   - URL: https://fhir.epic.com
   - Type: Developer documentation / sandbox
   - Description: Epic's FHIR API documentation showing which standard terminologies are used for each resource type, with a testing sandbox
   - Difficulty: Intermediate
   - Cost: Free (registration required)

7. **UMLS Terminology Services (UTS) Browser**
   - URL: https://uts.nlm.nih.gov/uts/umls/home
   - Type: Interactive browser / API
   - Description: NLM's portal for browsing and searching across 200+ biomedical vocabularies; includes API access and the Metathesaurus browser
   - Difficulty: Intermediate
   - Cost: Free (UTS account required)

8. **CDC CVX Code Set**
   - URL: https://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=cvx
   - Type: Reference database
   - Description: Complete, searchable list of CVX vaccine codes maintained by the CDC, with status and mapping information
   - Difficulty: Beginner
   - Cost: Free

### Video Content

9. **LOINC Beginner's Guide (YouTube)**
   - URL: https://www.youtube.com/watch?v=cfSSopb4Bo0
   - Type: Video tutorial
   - Description: Simple introduction to LOINC names and codes, how they work in practice
   - Duration: ~15 minutes
   - Difficulty: Beginner
   - Cost: Free

10. **Introduction to LOINC (YouTube)**
    - URL: https://www.youtube.com/watch?v=Ydcb2Df8gHY
    - Type: Video tutorial
    - Description: Overview of LOINC global use, concept model, data structures, and implementation resources
    - Difficulty: Beginner
    - Cost: Free

### Interactive Tools and Exercises

11. **FHIR Drills — ConceptMap Tutorial**
    - URL: https://fhir-drills.github.io/conceptmap.html
    - Type: Interactive tutorial / exercises
    - Description: Hands-on exercises for working with FHIR ConceptMap resources and terminology operations
    - Difficulty: Intermediate
    - Cost: Free

12. **NLM Clinical Tables Search Service (FHIR)**
    - URL: https://clinicaltables.nlm.nih.gov/fhirLookup.html
    - Type: Interactive API tool
    - Description: NLM's FHIR-based lookup service for clinical terminologies including LOINC, SNOMED CT, and ICD-10
    - Difficulty: Intermediate
    - Cost: Free

### Books and Written Guides

13. **Health Informatics: Practical Guide (7th Edition) — William Hersh**
    - Type: Textbook
    - Description: Comprehensive health informatics textbook with chapters on clinical terminologies and coding systems; widely used in graduate programs
    - Difficulty: Beginner–Intermediate
    - Cost: Paid

14. **Terminologies in FHIR — Medblocks Blog**
    - URL: https://medblocks.com/blog/terminologies-in-fhir
    - Type: Blog/written guide
    - Description: Practical developer-oriented guide to understanding CodeSystem, ValueSet, ConceptMap, and terminology operations in FHIR
    - Difficulty: Intermediate
    - Cost: Free

---

## Learning Path

### Phase 1: Foundations (3–4 hours)
**Goal:** Understand what coding systems are and why they exist

1. Read the NLM Health Data Standards tutorial (resource #2) for a broad overview
2. Watch both LOINC beginner videos (#9, #10) for a concrete example of how one coding system works
3. Browse the CDC CVX code list (#8) to see a simple, real-world code set

**Milestone:** Can explain what SNOMED CT, ICD-10, LOINC, RxNorm, CPT, and CVX are and when each is used

### Phase 2: Deep Dive into Major Systems (5–6 hours)
**Goal:** Understand each coding system's structure and how to look up codes

4. Explore SNOMED CT via the starter guide (#3) and UMLS browser (#7)
5. Search for common lab tests on loinc.org (#4) — e.g., glucose, hemoglobin A1c, COVID PCR
6. Use the RxNorm API (#5) to look up common medications — e.g., metformin, lisinopril
7. Review ICD-10-CM structure via the NLM tutorial; search for common diagnoses
8. Understand CPT's role in billing vs clinical coding; note AMA licensing requirements

**Milestone:** Can look up codes in each system and explain the six-part LOINC naming convention, SNOMED CT hierarchy, and RxNorm concept types

### Phase 3: FHIR Terminology Services (4–5 hours)
**Goal:** Use FHIR terminology operations programmatically

9. Read the FHIR Terminology Services specification (#1)
10. Work through FHIR Drills ConceptMap exercises (#11)
11. Practice $lookup and $validate-code using NLM Clinical Tables FHIR service (#12)
12. Read the Medblocks "Terminologies in FHIR" guide (#14)
13. Understand CodeableConcept structure and how multiple codings coexist

**Milestone:** Can execute $lookup, $validate-code, $expand, and $translate operations against a FHIR terminology server

### Phase 4: Epic-Specific Terminology (3–4 hours)
**Goal:** Understand how Epic handles terminology mapping in practice

14. Explore Epic on FHIR documentation (#6) — review how Condition, Observation, MedicationRequest, and Immunization resources use standard codes
15. Study how CodeableConcept arrays in Epic FHIR responses contain both Epic internal codes and standard terminology codes
16. Understand Epic's masterfile system and how internal records map to external standards
17. Practice with Epic's FHIR sandbox — query patient data and examine the coding arrays returned

**Milestone:** Can interpret coded data in Epic FHIR responses, identify which standard system each code belongs to, and handle cases where standard codes are missing

**Total estimated time: 15–19 hours**

---

## Practical Exercises

### Exercise 1: Code System Scavenger Hunt
Search each coding system's browser/tool for these clinical concepts and record the codes:
- **Diabetes Mellitus Type 2:** Find in ICD-10-CM, SNOMED CT
- **Hemoglobin A1c:** Find in LOINC
- **Metformin 500mg tablet:** Find in RxNorm
- **Influenza vaccine:** Find in CVX
- **Office visit, established patient:** Find in CPT

### Exercise 2: LOINC Six-Part Name Analysis
Using loinc.org, look up 5 common lab tests and break each LOINC code into its six parts (Component, Property, Time, System, Scale, Method). Compare similar tests to understand how the parts differentiate them (e.g., serum glucose vs urine glucose).

### Exercise 3: FHIR CodeableConcept Parsing
Given sample FHIR JSON from Epic's sandbox (Condition, Observation, MedicationRequest resources), write code or pseudocode that:
- Extracts all coding systems present in each CodeableConcept
- Identifies the "preferred" code for a given system
- Handles cases where a standard code is missing (fallback to text)

### Exercise 4: FHIR Terminology Operations
Using a public FHIR terminology server (e.g., https://tx.fhir.org or NLM's service):
- Perform a `$lookup` on SNOMED CT code 73211009 (Diabetes mellitus)
- `$validate-code` to check if "E11.9" is valid in ICD-10-CM
- `$expand` a ValueSet to see all codes for a condition category
- `$translate` between SNOMED CT and ICD-10 using a ConceptMap

### Exercise 5: Cross-System Mapping Challenge
For 5 common clinical conditions, find the corresponding codes in SNOMED CT, ICD-10-CM, and (where applicable) LOINC. Document where mappings are 1:1 vs 1:many, and identify cases where precision is lost in translation. Use the UMLS Metathesaurus browser to explore concept relationships.

### Exercise 6: Epic FHIR Sandbox Terminology Exploration
Using Epic's open FHIR sandbox:
- Query Condition resources and catalog all coding systems present
- Query Observation resources for lab results and verify LOINC codes
- Query MedicationRequest resources and verify RxNorm codes
- Document any Epic-specific code systems found in the responses

---

## Connections to Other Domains

- **D-1 (Interoperability Foundations):** Coding systems are the semantic layer that makes syntactic interoperability meaningful
- **D-2 (Regulatory Compliance):** HIPAA mandates ICD-10; Meaningful Use/Promoting Interoperability requires SNOMED CT, LOINC, and RxNorm
- **D-4 (FHIR R4):** Every FHIR resource uses CodeableConcept with these coding systems; deep FHIR work requires terminology fluency
- **D-5 (OAuth/Auth):** Scopes may limit which coded data an app can access
- **D-6 (SMART on FHIR):** Apps must correctly interpret coded data from multiple Epic instances with potentially different local code mappings
- **D-7 (HL7v2):** HL7v2 messages use the same coding systems in OBX segments (LOINC), DG1 segments (ICD-10), etc.
- **D-8 (CDS Hooks):** Clinical decision support relies on correctly coded clinical data to trigger appropriate recommendations
