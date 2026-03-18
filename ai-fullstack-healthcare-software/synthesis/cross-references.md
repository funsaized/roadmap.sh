# Cross-References: How Domains Relate and Reinforce Each Other

## Overview
This document maps the interconnections between all 13 domains, identifying where concepts from one domain reinforce, extend, or depend on concepts from another.

---

## Cross-Cutting Themes

### 1. HIPAA and PHI Handling
Appears in virtually every domain:
- **D-1:** Foundational definitions (18 identifiers, Safe Harbor, Expert Determination, BAAs)
- **D-4:** PHI in LLM prompts, de-identification pipelines, no-train clauses
- **D-6:** PHI in clinical notes for summarization, audio recordings
- **D-7:** PHI burnt into DICOM images, metadata de-identification
- **D-8:** PHI in training data, federated learning alternatives
- **D-10:** PHI detection tools (Presidio, NLM Scrubber), automated redaction
- **D-11:** Audit logging as PHI, encryption, retention requirements
- **D-12:** PHI masking in agent traces, FHIR API access scoping

### 2. FDA Regulatory Classification
Threaded throughout clinical AI domains:
- **D-1:** SaMD/SiMD definitions, 510(k)/De Novo/PMA pathways, CDS exemption criteria
- **D-3:** Predictive models as potential SaMD, GMLP principles
- **D-7:** Imaging AI — majority of FDA-cleared AI devices are radiology
- **D-8:** PCCPs for model updates, continuous learning regulatory framework
- **D-10:** Deep dive into regulatory pathways, clinical validation study design, CONSORT-AI
- **D-11:** Post-market surveillance, TPLC approach, real-world performance monitoring

### 3. Clinical Safety and Patient Harm Prevention
The ethical core running through all domains:
- **D-2:** Bias/fairness, clinical evaluation metrics (sensitivity vs specificity tradeoffs)
- **D-3:** Alert fatigue, false positive/negative clinical impact
- **D-4:** Hallucination in clinical context, safety constraints in prompts
- **D-6:** Faithfulness in summarization, clinical accuracy in generated content
- **D-8:** RLHF for clinical safety alignment, DPO
- **D-9:** CDS Five Rights, alert management
- **D-10:** Guardrails, hallucination detection, content moderation, HITL patterns
- **D-12:** Agent safety boundaries, confidence-based routing, prohibited actions

### 4. Healthcare Interoperability Standards
The integration backbone:
- **D-1:** FHIR R4, HL7v2, DICOM, X12/EDI, CDS Hooks, SMART on FHIR (foundational)
- **D-3:** CDS Hooks for predictive model delivery, FHIR RiskAssessment
- **D-5:** FHIR Terminology Services, SNOMED/LOINC/RxNorm APIs
- **D-7:** DICOM pipeline integration, DICOMweb, PACS
- **D-9:** CDS Hooks services, CQL + FHIR, Da Vinci PAS IG
- **D-12:** FHIR API agents, SMART on FHIR auth for agents

### 5. Bias, Fairness, and Health Equity
Woven through ML and clinical domains:
- **D-2:** Bias sources, fairness metrics, mitigation strategies (foundational)
- **D-3:** Demographic stratification of predictive models, Optum algorithm case
- **D-7:** Skin tone bias in dermatology AI, imaging dataset representation
- **D-8:** 91.7% of medical LLMs show measurable bias per systematic review
- **D-10:** Bias auditing, subgroup performance analysis, FUTURE-AI fairness principle
- **D-11:** Stratified monitoring dashboards, equity-aware drift detection

### 6. Clinical Workflow Integration
How AI actually fits into clinical practice:
- **D-1:** CDS Hooks (workflow triggers), SMART on FHIR (app embedding)
- **D-3:** Alert fatigue, model serving at point of care
- **D-6:** Ambient documentation in exam room, EHR write-back
- **D-9:** Prior auth automation, care gap closure, scheduling optimization
- **D-11:** Latency optimization for real-time workflows, autoscaling for clinical patterns
- **D-12:** Multi-step clinical workflow orchestration, HITL review queues

---

## Domain Interaction Matrix

| From \ To | D-1 | D-2 | D-3 | D-4 | D-5 | D-6 | D-7 | D-8 | D-9 | D-10 | D-11 | D-12 | D-13 |
|-----------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|------|
| **D-1** | — | | ✓ | ✓ | ✓ | | ✓ | | | | | | |
| **D-2** | | — | ✓ | ✓ | ✓ | | ✓ | ✓ | | | | | |
| **D-3** | | | — | | | | | | ✓ | ✓ | ✓ | | |
| **D-4** | | | | — | ✓ | | | ✓ | | ✓ | ✓ | | |
| **D-5** | | | | | — | ✓ | | ✓ | ✓ | | | ✓ | |
| **D-6** | | | | | | — | | | ✓ | ✓ | | ✓ | |
| **D-7** | | | | | | | — | | | | | | |
| **D-8** | | | | | | | | — | | | | | |
| **D-9** | | | | | | | | | — | | | ✓ | ✓ |
| **D-10** | | | | | | | | | | — | ✓ | ✓ | ✓ |
| **D-11** | | | | | | | | | | | — | ✓ | ✓ |
| **D-12** | | | | | | | | | | | | — | ✓ |

## Key Reinforcement Patterns

### 1. FHIR as Universal Language
FHIR R4 (introduced in D-1) appears as input/output format in every subsequent domain. Mastering FHIR early creates compound returns across all later learning.

### 2. Evaluation Metrics Cascade
Clinical evaluation metrics (D-2) → Applied to predictive models (D-3) → Extended for LLMs (D-4: benchmarks) → Adapted for RAG (D-5: faithfulness) → Formalized for regulation (D-10: CONSORT-AI) → Operationalized in monitoring (D-11: drift detection).

### 3. Safety Layer Stack
Each domain adds a safety layer: PHI handling (D-1) → Bias detection (D-2) → Alert fatigue (D-3) → Hallucination awareness (D-4) → RAG grounding (D-5) → Faithfulness checking (D-6) → FDA compliance (D-7) → RLHF alignment (D-8) → CDS guardrails (D-9) → Comprehensive guardrail frameworks (D-10) → Production monitoring (D-11) → Agent safety boundaries (D-12).

### 4. The RAG Thread
Embeddings (D-5) + Prompt engineering (D-4) + Knowledge graphs (D-5) = RAG, which is then applied in: clinical Q&A (D-5), generative content (D-6), evidence retrieval for CDS (D-9), hallucination mitigation (D-10), and agent tool use (D-12).

### 5. The Production Thread
ML pipeline concepts (D-2) → Model serving patterns (D-3) → LLM architecture (D-4) → Model versioning and PCCP (D-8) → Safety monitoring (D-10) → Full observability stack (D-11) → Agent orchestration infrastructure (D-12).

---

## Contradictions Resolved

1. **Difficulty of "Fine-Tuning" concept:** D-4 presents it as intermediate (when to fine-tune vs prompt), D-8 covers implementation at advanced level. Resolution: Understanding *when* to fine-tune is intermediate; *doing* it is advanced.

2. **FDA CDS Exemption scope:** D-1 introduces the four criteria; D-3 and D-9 apply them differently. Resolution: Same criteria, but application context matters (predictive tools vs. rules-based CDS have different exemption likelihoods).

3. **RAG vs Fine-Tuning:** D-5 advocates RAG as the primary pattern; D-8 covers fine-tuning. These are complementary, not competing — RAG for dynamic knowledge, fine-tuning for behavioral adaptation. The hybrid approach (fine-tuned model + RAG) is the production standard.

4. **Estimated hours:** Domain research files give varying time estimates. This synthesis normalizes to 400-500 total hours for comprehensive coverage, consistent with the original scope specification.
