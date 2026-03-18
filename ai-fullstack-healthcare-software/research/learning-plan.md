# Learning Plan: Building & Integrating Applications of AI in Fullstack Healthcare Software

## Topic Overview

A practitioner roadmap to mastering AI integration in provider-facing healthcare software — from foundational ML concepts through production-grade agentic systems, covering every AI modality relevant to clinical workflows, administrative operations, and patient engagement.

**Target Audience:** Fullstack software engineers and technical leads (2-8 years experience) in healthcare technology.
**Assumed Baseline:** Backend/frontend development, REST APIs, databases, cloud infrastructure, surface-level healthcare familiarity, basic HIPAA awareness.
**Total Estimated Time:** 350-480 hours

---

## Domain List

### D-1: Healthcare Data Foundations and Regulatory Landscape
**Difficulty:** Beginner | **Prerequisites:** None | **Est. Time:** 25-35 hours
Healthcare-specific data formats (FHIR R4, HL7v2, DICOM, X12/EDI, CDS Hooks, SMART on FHIR) and regulatory framework (HIPAA, FDA SaMD/SiMD, ONC Cures Act, state AI laws, CMS).

### D-2: ML Fundamentals for Healthcare Engineers
**Difficulty:** Beginner | **Prerequisites:** None | **Est. Time:** 30-40 hours
Core ML concepts for healthcare: supervised/unsupervised learning, feature engineering from EHR data, bias/fairness, ML pipeline, interpretability, clinical evaluation metrics.

### D-3: Predictive AI in Clinical Applications
**Difficulty:** Intermediate | **Prerequisites:** D-1, D-2 | **Est. Time:** 35-45 hours
Classification, regression, ranking/recommendation, clustering/anomaly detection for healthcare use cases.

### D-4: Foundation Models and Prompt Engineering for Healthcare
**Difficulty:** Intermediate | **Prerequisites:** D-1, D-2 | **Est. Time:** 30-40 hours
LLM fundamentals, prompt engineering for clinical tasks, structured output extraction, safety constraints, healthcare LLM landscape.

### D-5: Embeddings, Knowledge Systems and RAG for Healthcare
**Difficulty:** Intermediate | **Prerequisites:** D-1, D-2, D-4 | **Est. Time:** 30-40 hours
Medical embeddings, vector search, RAG, medical ontologies, knowledge graphs, rule-based systems, hybrid systems.

### D-6: Generative AI Applications in Healthcare
**Difficulty:** Intermediate | **Prerequisites:** D-4, D-5 | **Est. Time:** 30-40 hours
Clinical note summarization, ambient documentation, speech-to-text, synthetic data, video models for telehealth.

### D-7: Computer Vision and Medical Imaging AI
**Difficulty:** Intermediate | **Prerequisites:** D-1, D-2 | **Est. Time:** 25-35 hours
Medical image analysis, DICOM pipelines, document OCR, audio perception, FDA SaMD for diagnostic imaging.

### D-8: Fine-Tuning and Model Adaptation for Healthcare
**Difficulty:** Advanced | **Prerequisites:** D-2, D-4, D-5 | **Est. Time:** 30-40 hours
Domain-specific models, LoRA/QLoRA, RLHF, training data curation, medical benchmarks, FDA change control.

### D-9: Decisioning AI and Clinical Decision Support
**Difficulty:** Advanced | **Prerequisites:** D-3, D-5, D-6 | **Est. Time:** 25-35 hours
RL for treatment optimization, CDS rules engines, CDS Hooks, prior auth automation, alert fatigue management.

### D-10: AI Safety, Guardrails and Clinical Evaluation
**Difficulty:** Advanced | **Prerequisites:** D-3, D-4, D-6 | **Est. Time:** 30-40 hours
PHI detection/redaction, clinical safety checks, hallucination detection, FDA SaMD compliance, clinical validation.

### D-11: AI Observability and Production Operations
**Difficulty:** Advanced | **Prerequisites:** D-3, D-4, D-10 | **Est. Time:** 25-30 hours
Distributed tracing, audit logging, drift detection, model routing, caching, cost/latency optimization.

### D-12: Agentic Systems for Healthcare
**Difficulty:** Expert | **Prerequisites:** D-5, D-6, D-9, D-10, D-11 | **Est. Time:** 35-45 hours
Tool-using agents, multi-step workflow orchestration, human-in-the-loop patterns, multi-model architectures.

### D-13: Capstone - Multi-Modal Healthcare AI Architecture
**Difficulty:** Expert | **Prerequisites:** D-9, D-10, D-11, D-12 | **Est. Time:** 30-40 hours
End-to-end system design, reference architectures, build-vs-buy, AI governance, scaling patterns.

---

## Dependency Graph

D-1, D-2: No prerequisites (concurrent)
D-3: requires D-1, D-2
D-4: requires D-1, D-2
D-7: requires D-1, D-2
D-5: requires D-1, D-2, D-4
D-6: requires D-4, D-5
D-8: requires D-2, D-4, D-5
D-9: requires D-3, D-5, D-6
D-10: requires D-3, D-4, D-6
D-11: requires D-3, D-4, D-10
D-12: requires D-5, D-6, D-9, D-10, D-11
D-13: requires D-9, D-10, D-11, D-12

Critical Path: D-1/D-2 -> D-4 -> D-5 -> D-6 -> D-10 -> D-11 -> D-12 -> D-13

## Cross-Cutting Themes

1. HIPAA and PHI Handling
2. FDA Regulatory Classification
3. Clinical Safety and Patient Harm Prevention
4. Healthcare Interoperability Standards
5. Bias, Fairness and Health Equity
6. Clinical Workflow Integration

## Research Priorities

1. Foundation domains (D-1, D-2)
2. Core AI modality domains (D-3, D-4, D-5, D-6, D-7)
3. Adaptation and operations (D-8, D-9, D-10, D-11)
4. Agentic and capstone (D-12, D-13)
