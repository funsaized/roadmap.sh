# Dependency Graph: AI in Fullstack Healthcare Software

## Domain-Level Dependencies

```
D-1 (Healthcare Data) ──→ D-3 (Predictive AI)
D-1 ──→ D-4 (Foundation Models)
D-1 ──→ D-5 (Embeddings/RAG)
D-1 ──→ D-7 (Computer Vision)

D-2 (ML Fundamentals) ──→ D-3
D-2 ──→ D-4
D-2 ──→ D-5
D-2 ──→ D-7
D-2 ──→ D-8 (Fine-Tuning)

D-4 ──→ D-5
D-4 ──→ D-8
D-4 ──→ D-10 (AI Safety)
D-4 ──→ D-11 (Observability)

D-5 ──→ D-6 (Generative AI)
D-5 ──→ D-8
D-5 ──→ D-9 (Decisioning)
D-5 ──→ D-12 (Agentic Systems)

D-6 ──→ D-9
D-6 ──→ D-10
D-6 ──→ D-12

D-3 ──→ D-9
D-3 ──→ D-10
D-3 ──→ D-11

D-10 ──→ D-11
D-10 ──→ D-12
D-10 ──→ D-13 (Capstone)

D-11 ──→ D-12
D-11 ──→ D-13

D-9 ──→ D-12
D-9 ──→ D-13

D-12 ──→ D-13
```

## Concept-Level Prerequisite Graph

### Foundation Layer (No Prerequisites)
```
FHIR R4 Fundamentals
HL7v2 Message Structure
DICOM Standard
X12/EDI Transactions
Medical Terminologies
HIPAA Privacy and Security
FDA SaMD/SiMD Classification
ONC Cures Act
State AI Healthcare Laws
Supervised Learning: Classification
Supervised Learning: Regression
Unsupervised Learning: Clustering
Unsupervised Learning: Anomaly Detection
```

### Layer 1 (Depends on Foundation)
```
CDS Hooks ← FHIR R4
SMART on FHIR ← FHIR R4
HIPAA De-identification ← HIPAA Privacy
FDA CDS Exemption ← FDA SaMD
Healthcare Data Pipeline ← FHIR R4 + HL7v2 + DICOM
Synthetic Data Generation ← FHIR R4
Clinical Evaluation Metrics ← Classification
Feature Engineering from EHR ← FHIR R4 + Medical Terminologies
```

### Layer 2 (Depends on Layer 1)
```
Bias and Fairness ← Clinical Eval Metrics
Model Interpretability (SHAP/LIME) ← Classification
Cross-Validation for Clinical Data ← Classification
ML Pipeline and Lifecycle ← All D-2 basics
Transformer Architecture ← Classification
```

### Layer 3 (Intermediate — Core AI Modalities)
```
Clinical Risk Stratification ← Classification + Feature Engineering
Healthcare Regression (LOS/Cost) ← Regression + Feature Engineering
Healthcare LLM Landscape ← Transformer Architecture
CNN Architectures for Medical Imaging ← Classification
Medical Embeddings (BioBERT etc.) ← Transformer Architecture
SNOMED CT / UMLS Navigation ← Medical Terminologies
Medical Speech-to-Text ← Transformer Architecture
```

### Layer 4 (Applied Intermediate)
```
Prompt Engineering ← Healthcare LLM Landscape
Patient Cohort Segmentation ← Clustering + Feature Engineering
FHIR RiskAssessment ← FHIR R4 + Risk Stratification
Vector Databases ← Medical Embeddings
Medical Image Segmentation ← CNN Architectures
Vision Transformers ← Transformer Architecture
Audio Perception ← Classification
```

### Layer 5 (Advanced Intermediate)
```
Clinical Note Summarization ← Prompt Engineering
Structured Output Extraction ← Prompt Engineering + FHIR R4
PHI-Safe LLM Integration ← HIPAA De-identification + Prompt Engineering
RAG Pipeline ← Vector Databases + Prompt Engineering
Knowledge Graphs ← SNOMED/UMLS + RAG Pipeline
CDS Hooks for Predictive Models ← CDS Hooks + Risk Stratification
DICOM AI Integration ← DICOM Pipeline
```

### Layer 6 (Advanced)
```
Parameter-Efficient Fine-Tuning (LoRA/QLoRA) ← Transformer Architecture + ML Pipeline
RLHF/DPO ← Fine-Tuning + Bias/Fairness
Hybrid Rules+ML+LLM ← RAG + Knowledge Graphs
CDS Rules Engines ← CDS Fundamentals
CQL ← CDS Rules Engines + FHIR
Reinforcement Learning for Treatment ← Regression + Clustering
PHI Detection and Redaction ← HIPAA De-id + NER
Guardrail Frameworks ← Prompt Engineering + PHI Detection
Hallucination Detection ← LLM Evaluation + RAG
Distributed Tracing ← Production LLM Architecture
Model Versioning ← ML Pipeline
Drift Detection ← Model Versioning + Clinical Eval Metrics
```

### Layer 7 (Expert)
```
Agent Architectures (ReAct) ← Prompt Engineering + RAG
FHIR API Agents ← FHIR R4 + SMART + Agent Architectures
LangGraph/LangChain ← Agent Architectures
Workflow Orchestration ← FHIR API Agents + LangGraph
HITL Patterns ← Workflow Orchestration + Guardrails
Agent Safety ← HITL + Safety Checks
Multi-Agent Systems ← LangGraph + Orchestration
```

### Layer 8 (Capstone)
```
Multi-Modal Architecture ← ALL prior domains
Production System Integration ← ALL prior domains
```

## Critical Path (Shortest Path to Competence)

For a fullstack engineer who wants to ship their first AI-powered healthcare feature:

```
FHIR R4 → HIPAA Privacy → Classification → Clinical Eval Metrics
→ Transformer Architecture → Prompt Engineering → PHI-Safe LLM Integration
→ RAG Pipeline → Guardrail Frameworks → Production LLM Architecture
→ Distributed Tracing
```

**Estimated time: ~120 hours (Quick Start path)**

This path enables building a RAG-based clinical Q&A system with proper safety guardrails, PHI handling, and basic observability.

## Comprehensive Path (Full Mastery)

All 13 domains in dependency order, with parallel tracks where possible:

**Track A (Data + Regulatory):** D-1 → D-10 (safety) → D-11 (ops)
**Track B (ML Core):** D-2 → D-3 → D-9 (decisioning)
**Track C (LLM + Knowledge):** D-4 → D-5 → D-6 → D-8 (fine-tuning)
**Track D (Perception):** D-7
**Convergence:** D-12 (agentic) → D-13 (capstone)

**Estimated time: 400-500 hours (full mastery)**
