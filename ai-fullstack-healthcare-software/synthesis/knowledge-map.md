# Knowledge Map: AI in Fullstack Healthcare Software

## Overview
This knowledge map inventories 156 unique concepts across 13 domains, organized from beginner foundations through expert-level agentic systems. Each concept includes prerequisite links showing what must be learned first.

---

## Section 1: Foundations (Beginner) — Estimated 80 hours

### Domain 1: Healthcare Data Foundations and Regulatory Landscape (35-45 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| FHIR R4 Fundamentals (Resources, REST API, Bundles, Profiles) | None | Beginner |
| HL7v2 Message Structure (ADT, ORM, ORU, MLLP) | None | Beginner |
| DICOM Standard (Files, PACS, DICOMweb, Modalities) | None | Beginner |
| X12/EDI Healthcare Transactions (837, 835, 270/271, 278) | None | Beginner |
| CDS Hooks Specification (Hooks, Services, Cards, Prefetch) | FHIR R4 | Beginner |
| SMART on FHIR (OAuth2, App Launch, Scopes) | FHIR R4 | Beginner |
| Medical Terminologies (ICD-10, CPT, SNOMED CT, LOINC, RxNorm) | None | Beginner |
| HIPAA Privacy and Security Rules (PHI, BAAs, Minimum Necessary) | None | Beginner |
| HIPAA De-identification (Safe Harbor, Expert Determination) | HIPAA Privacy | Beginner |
| FDA SaMD/SiMD Classification (Class I/II/III, 510(k), De Novo, PMA) | None | Beginner |
| FDA CDS Exemption Criteria (Four criteria, design implications) | FDA SaMD | Beginner |
| ONC Cures Act and Information Blocking (HTI-1, USCDI, Disincentives) | None | Beginner |
| State AI Healthcare Laws (CA AB 3030, TX TRAIGA, CO AI Act) | None | Beginner |
| Healthcare Data Pipeline Architecture (ETL, conversion patterns) | FHIR R4, HL7v2, DICOM | Beginner |
| Synthetic Data Generation (Synthea, privacy-safe development) | FHIR R4 | Beginner |

### Domain 2: ML Fundamentals for Healthcare Engineers (80-97 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| Supervised Learning: Classification (Logistic Regression, Random Forest, XGBoost) | None | Beginner |
| Supervised Learning: Regression (Linear, Ridge, Lasso, GBR) | None | Beginner |
| Unsupervised Learning: Clustering (K-Means, DBSCAN, Hierarchical) | None | Beginner |
| Unsupervised Learning: Anomaly Detection (Isolation Forest, Autoencoders) | None | Beginner |
| Feature Engineering from EHR/FHIR Data | FHIR R4, Medical Terminologies | Intermediate |
| Clinical Evaluation Metrics (Sensitivity, Specificity, PPV, NPV, AUC-ROC, Calibration) | Classification | Beginner |
| Bias and Fairness in Clinical ML (Sources, Metrics, Mitigation) | Clinical Eval Metrics | Intermediate |
| Model Interpretability (SHAP, LIME, Intrinsic Methods) | Classification | Intermediate |
| Cross-Validation for Clinical Data (Temporal, Patient-level, Site-level splits) | Classification | Intermediate |
| ML Pipeline and Lifecycle Management | All D-2 concepts | Intermediate |

---

## Section 2: Core AI Modalities (Intermediate) — Estimated 200 hours

### Domain 3: Predictive AI in Clinical Applications (72 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| Clinical Risk Stratification (LACE, HOSPITAL Score, Readmission) | Classification, Feature Engineering | Intermediate |
| Mortality and No-Show Prediction | Classification, Clinical Eval Metrics | Intermediate |
| Healthcare Regression (LOS, Cost, Staffing, Wait Time) | Regression, Feature Engineering | Intermediate |
| Ranking and Recommendation (Specialist Matching, Treatment, Formulary) | Classification, Regression | Intermediate |
| Patient Cohort Segmentation and Disease Phenotyping | Clustering, Feature Engineering | Intermediate |
| Healthcare Fraud and Anomaly Detection | Anomaly Detection, X12/EDI | Intermediate |
| CDS Hooks Integration for Predictive Models | CDS Hooks, FHIR R4 | Intermediate |
| FHIR RiskAssessment Resource | FHIR R4, Clinical Risk Stratification | Intermediate |
| Predictive Model Serving Patterns (Real-time, Batch, Streaming) | ML Pipeline | Intermediate |
| Alert Fatigue Management | CDS Hooks Integration | Intermediate |

### Domain 4: Foundation Models and Prompt Engineering for Healthcare (60 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| Transformer Architecture (Self-Attention, Multi-Head, Positional Encoding) | Classification | Intermediate |
| Healthcare LLM Landscape (Med-PaLM, BioGPT, GPT-4, ClinicalBERT) | Transformer Architecture | Intermediate |
| Prompt Engineering Techniques (Zero-shot, Few-shot, CoT, Self-Consistency) | Healthcare LLM Landscape | Intermediate |
| Clinical Note Summarization with LLMs | Prompt Engineering | Intermediate |
| Structured Output Extraction (JSON Schema, FHIR Resource Generation, NER) | Prompt Engineering, FHIR R4 | Intermediate |
| PHI-Safe LLM Integration (BAAs, De-identification Pipelines, Zero-Trust) | HIPAA De-identification, Prompt Engineering | Intermediate |
| LLM Evaluation for Healthcare (Benchmarks, Hallucination, Red-Teaming) | Prompt Engineering | Intermediate |
| Production LLM Architecture (Caching, Cost Optimization, Prompt Management) | PHI-Safe LLM Integration | Intermediate |

### Domain 5: Embeddings, Knowledge Systems and RAG for Healthcare (80 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| Medical Embedding Models (BioBERT, PubMedBERT, ClinicalBERT, SapBERT) | Transformer Architecture | Intermediate |
| Vector Databases for Clinical Search (Pinecone, Weaviate, FAISS, pgvector) | Medical Embeddings | Intermediate |
| SNOMED CT, UMLS, and Medical Ontology Navigation | Medical Terminologies | Intermediate |
| FHIR Terminology Services (CodeSystem, ValueSet, ConceptMap) | FHIR R4, SNOMED/UMLS | Intermediate |
| RAG Pipeline for Healthcare (Chunking, Retrieval, Re-ranking, Citation) | Vector Databases, Prompt Engineering | Intermediate |
| Medical Knowledge Graphs (Neo4j, Graph Construction, GraphRAG) | SNOMED/UMLS, RAG Pipeline | Intermediate |
| Hybrid Rules + ML + LLM Architectures | RAG Pipeline, Knowledge Graphs | Advanced |
| RAG Evaluation Metrics (Faithfulness, Relevance, Hallucination) | RAG Pipeline | Intermediate |

### Domain 6: Generative AI Applications in Healthcare (85 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| Clinical Note Summarization Pipelines (Extractive, Abstractive, Section-Aware) | Clinical Note Summarization with LLMs, RAG | Intermediate |
| Ambient Clinical Documentation (DAX, Abridge, Architecture) | Medical Speech-to-Text, Note Summarization | Intermediate |
| Medical Speech-to-Text (Whisper, Dragon Medical, Cloud ASR) | Transformer Architecture | Intermediate |
| Prior Authorization Letter Generation | RAG Pipeline, Structured Output | Intermediate |
| Patient Content Generation (Health Literacy, Multilingual, AVS) | Prompt Engineering | Intermediate |
| Synthetic Clinical Data Generation (Synthea, GANs, VAEs, Privacy) | Synthetic Data Generation (D-1) | Intermediate |
| Generative AI for Medical Imaging (Diffusion, Data Augmentation) | Transformer Architecture | Intermediate |
| Video Models for Telehealth | Medical Speech-to-Text | Intermediate |

### Domain 7: Computer Vision and Medical Imaging AI (80 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| DICOM Pipeline and Medical Imaging Modalities | DICOM Standard | Intermediate |
| CNN Architectures for Medical Imaging (ResNet, DenseNet, EfficientNet) | Classification | Intermediate |
| Vision Transformers for Medical Imaging | Transformer Architecture | Intermediate |
| Medical Image Segmentation (U-Net, nnU-Net, MONAI) | CNN Architectures | Intermediate |
| Clinical Imaging Applications (Radiology, Pathology, Dermatology, Ophthalmology) | Medical Image Segmentation | Intermediate |
| DICOM AI Integration (Orthanc, OHIF, highdicom, DICOMweb) | DICOM Pipeline | Intermediate |
| Audio Perception for Clinical Sounds (Heart, Respiratory, Fall Detection) | Classification | Intermediate |
| Wound Assessment and Document OCR | CNN Architectures | Intermediate |

---

## Section 3: Model Adaptation (Advanced) — Estimated 50 hours

### Domain 8: Fine-Tuning and Model Adaptation for Healthcare (87 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| Domain-Specific Biomedical Models (BioBERT, ClinicalBERT, Meditron, PMC-LLaMA) | Healthcare LLM Landscape, Medical Embeddings | Advanced |
| Parameter-Efficient Fine-Tuning (LoRA, QLoRA, Adapters, PEFT) | Transformer Architecture, ML Pipeline | Advanced |
| Training Data Curation from Clinical Corpora (MIMIC, PHI Handling) | HIPAA De-identification, Domain Models | Advanced |
| RLHF and DPO for Clinical Safety Alignment | Fine-Tuning, Bias and Fairness | Advanced |
| Medical Benchmarks and Evaluation (MedQA, PubMedQA, MMLU, HealthBench) | LLM Evaluation | Advanced |
| FDA Predetermined Change Control Plans (PCCPs) | FDA SaMD, ML Pipeline | Advanced |

---

## Section 4: Production & Safety (Advanced) — Estimated 120 hours

### Domain 9: Decisioning AI and Clinical Decision Support (70 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| CDS Fundamentals (Five Rights, Intervention Types, Knowledge-based vs Non-knowledge) | CDS Hooks, Clinical Risk Stratification | Advanced |
| CDS Rules Engines (Drools, OpenCDS, Architecture) | CDS Fundamentals | Advanced |
| Clinical Quality Language (CQL) | CDS Rules Engines, FHIR R4 | Advanced |
| CDS Hooks Integration (Services, Cards, SMART App Launch) | CQL, CDS Hooks | Advanced |
| Reinforcement Learning for Treatment Optimization (DTRs, Insulin, Warfarin, Sepsis) | Regression, Clustering | Advanced |
| Scheduling and Resource Optimization (Staff, OR, Bed Management) | RL Fundamentals | Advanced |
| Prior Authorization Automation (Da Vinci PAS, X12 278, CRD) | X12/EDI, Prior Auth Letter Gen, CDS Hooks | Advanced |
| Care Gap Closure (HEDIS, CMS Star Ratings, CQL Measures) | CQL, CDS Hooks | Advanced |
| Alert Fatigue Management with AI (Prioritization, Contextual Suppression) | Alert Fatigue Management (D-3), Classification | Advanced |
| Clinical Trial Matching (NLP Criteria Extraction, EHR Matching) | RAG Pipeline, NER | Advanced |

### Domain 10: AI Safety, Guardrails and Clinical Evaluation (80 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| PHI Detection and Redaction (NER, Presidio, NLM Scrubber) | HIPAA De-identification, NER | Advanced |
| Clinical Safety Checks (Drug Interactions, Contraindications, Dosage Validation) | Medical Terminologies, Structured Output | Advanced |
| LLM Guardrail Frameworks (NeMo Guardrails, Guardrails AI, HITL) | Prompt Engineering, PHI Detection | Advanced |
| Hallucination Detection and Mitigation (MedHallu, Cross-reference, Entailment) | LLM Evaluation, RAG Pipeline | Advanced |
| Content Moderation for Healthcare AI | Guardrail Frameworks | Advanced |
| FDA SaMD Compliance Deep Dive (510(k), De Novo, PCCP, TPLC, GMLP) | FDA SaMD (D-1), PCCPs (D-8) | Advanced |
| Clinical Evaluation Study Design (RCTs, MRMC, Adaptive Trials) | Clinical Eval Metrics | Advanced |
| Reporting Guidelines (CONSORT-AI, SPIRIT-AI, DECIDE-AI) | Clinical Eval Study Design | Advanced |
| Evaluation Frameworks (TEHAI, FUTURE-AI, MEDIC, QUEST) | Clinical Eval Study Design | Advanced |
| Bias and Fairness Assessment for Production AI | Bias and Fairness (D-2) | Advanced |

### Domain 11: AI Observability and Production Operations (60 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| Distributed Tracing with OpenTelemetry for AI | Production LLM Architecture | Advanced |
| LLM Observability Platforms (Arize Phoenix, Langfuse, LangSmith) | Distributed Tracing | Advanced |
| HIPAA Audit Logging and Compliance Trails | HIPAA Privacy, Distributed Tracing | Advanced |
| Model Versioning and Rollback (MLflow Model Registry) | ML Pipeline | Advanced |
| Drift Detection (Data, Concept, Label Drift; Evidently AI) | Model Versioning, Clinical Eval Metrics | Advanced |
| Explainability Interfaces for Clinicians | Model Interpretability (D-2) | Advanced |
| Model Routing and Fallback Chains (LiteLLM) | Production LLM Architecture | Advanced |
| Response Caching (Exact, Semantic, Prompt Caching) | Model Routing | Advanced |
| Cost and Latency Optimization (Token Budgeting, Model Tiering) | Model Routing, Caching | Advanced |
| Feedback Loops and Continuous Improvement | Observability Platforms | Advanced |
| CI/CD/CT for ML (Continuous Training) | Model Versioning, Drift Detection | Advanced |

---

## Section 5: Autonomous Systems (Expert) — Estimated 50 hours

### Domain 12: Agentic Systems for Healthcare (57 hrs)

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| Agent Architectures (ReAct, Plan-Execute, Tool-Using) | Prompt Engineering, RAG Pipeline | Expert |
| FHIR API Agents (Tool Schemas, SMART on FHIR Auth) | FHIR R4, SMART on FHIR, Agent Architectures | Expert |
| LangGraph / LangChain / CrewAI for Healthcare | Agent Architectures | Expert |
| Multi-Step Clinical Workflow Orchestration (Prior Auth, Care Coord, Documentation) | FHIR API Agents, LangGraph | Expert |
| Human-in-the-Loop Patterns (Confidence Routing, Review Queues, Escalation) | Workflow Orchestration, Guardrail Frameworks | Expert |
| Agent Safety Boundaries (Scope Constraints, Audit, Hallucination Mitigation) | HITL Patterns, Agent Safety | Expert |
| Multi-Agent Systems (Orchestrator, Specialist Agents, Delegation) | LangGraph, Workflow Orchestration | Expert |
| Agent Testing Frameworks (MedSentry, Promptfoo, QUEST, Red Teaming) | Agent Safety, Clinical Evaluation | Expert |

### Domain 13: Capstone — Multi-Modal Healthcare AI Architecture

| Concept | Prerequisites | Difficulty |
|---------|--------------|------------|
| Multi-Modal Architecture Design (Combining Predictive, Generative, Perception, Decisioning, Agentic) | All prior domains | Expert |
| Production System Integration (FHIR, CDS Hooks, Observability, Safety, Routing) | All prior domains | Expert |

---

## Concept Count Summary

| Section | Domains | Concepts |
|---------|---------|----------|
| Foundations | D-1, D-2 | 25 |
| Core AI Modalities | D-3, D-4, D-5, D-6, D-7 | 44 |
| Model Adaptation | D-8 | 6 |
| Production & Safety | D-9, D-10, D-11 | 31 |
| Autonomous Systems | D-12, D-13 | 10 |
| **Total** | **13** | **116** |

## Cross-Domain Concept Deduplication Notes

The following concepts appear across multiple domains and have been consolidated:
- **HIPAA De-identification** → Covered in D-1 (foundational) with depth in D-10 (PHI detection tools)
- **FDA SaMD/SiMD** → Introduced in D-1, detailed in D-7 (imaging specific) and D-10 (comprehensive compliance)
- **Clinical Evaluation Metrics** → Introduced in D-2, applied in D-3 (predictive), D-10 (safety evaluation)
- **CDS Hooks** → Introduced in D-1, applied in D-3 (predictive integration), D-9 (decisioning)
- **Medical Terminologies** → Introduced in D-1, deep-dived in D-5 (ontologies, UMLS)
- **FHIR R4** → Introduced in D-1, used across D-3, D-4, D-5, D-9, D-12
- **Bias and Fairness** → Introduced in D-2, applied in D-3, D-8, D-10
- **Model Interpretability** → Introduced in D-2, applied in D-11 (explainability interfaces)
- **Prompt Engineering** → Core in D-4, applied in D-5 (RAG), D-6, D-9, D-12
- **Synthetic Data** → Introduced in D-1 (Synthea), expanded in D-6 (GANs, VAEs)
- **Alert Fatigue** → Introduced in D-3, expanded in D-9 (AI-driven management)
- **PCCPs** → Introduced in D-8, detailed in D-10 (FDA compliance)
- **Production LLM Architecture** → Introduced in D-4, expanded in D-11 (routing, caching)
