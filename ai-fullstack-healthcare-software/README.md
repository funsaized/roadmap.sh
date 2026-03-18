# Building & Integrating Applications of AI in Fullstack Healthcare Software

A practitioner's roadmap to mastering AI integration in provider-facing healthcare software — from foundational ML concepts through production-grade agentic systems, covering every AI modality relevant to clinical workflows, administrative operations, and patient engagement.

## Usage

Open `roadmap.html` in any modern browser (Chrome, Firefox, Safari, Edge). No server or build step required — it's a single self-contained file.

### Features

- **Progress tracking** — Check off topics as you complete them. Progress is saved in your browser's localStorage.
- **Detail panel** — Click any topic node to see its description, key concepts, sub-topics, prerequisites, and curated learning resources.
- **Search & filter** — Use the search bar to find topics by name or concept. Filter by difficulty level (beginner/intermediate/advanced/expert).
- **Section collapse** — Click section headers to collapse/expand sections.
- **Prerequisite navigation** — Click prerequisite links in the detail panel to jump to the referenced topic.
- **Prerequisite locking** — Topics with unfinished prerequisites show a lock icon. Complete prerequisites first to unlock them.

## Statistics

| Metric | Value |
|---|---|
| Total topics | 77 |
| Learning resources | 165 |
| Estimated hours | 450 |
| Sections | 5 |
| Milestones | 17 |
| Checkpoints | 4 |
| Difficulty levels | 4 (beginner, intermediate, advanced, expert) |

## Table of Contents

### 1. Foundations (17 topics, ~80h)
Healthcare data standards, regulatory landscape, and ML fundamentals.
- FHIR R4, HL7v2, DICOM, X12/EDI, CDS Hooks, Medical Terminologies
- HIPAA, FDA SaMD, ONC Cures Act
- Supervised/Unsupervised Learning, Clinical Metrics, Bias & Fairness, Feature Engineering

### 2. Core AI Modalities (28 topics, ~200h)
Major AI paradigms applied to healthcare.
- **Predictive AI** — Risk stratification, regression, ranking, clustering, integration
- **Generative AI** — Transformers, healthcare LLMs, prompt engineering, structured output, PHI-safe LLMs
- **Knowledge AI** — Medical embeddings, vector DBs, ontologies, RAG, knowledge graphs
- **Clinical NLP** — Note summarization, ambient documentation, speech-to-text, prior auth generation
- **Perception AI** — CNN medical imaging, segmentation, clinical imaging pipelines, DICOM integration

### 3. Model Adaptation (7 topics, ~50h)
Fine-tuning foundation models for healthcare domains.
- Fine-tuning strategies, domain models, training data curation
- RLHF/DPO, medical benchmarks, FDA PCCPs

### 4. Production & Safety (17 topics, ~120h)
Decisioning systems, safety guardrails, and production observability.
- CDS systems, CQL, treatment optimization, prior auth automation
- PHI detection, guardrails, hallucination mitigation, FDA compliance
- Tracing, observability, model versioning, drift detection, audit logging

### 5. Autonomous Systems (8 topics, ~50h)
Agentic AI systems with human oversight.
- Agent architecture, FHIR agents, LangGraph
- Workflow orchestration, human-in-the-loop, agent safety, multi-agent systems

## File Structure

```
roadmap.html                          # Interactive roadmap (open in browser)
README.md                             # This file
architecture/roadmap-final.json       # Source data (77 nodes, 103 edges, 165 resources)
architecture/layout-spec.md           # Layout design specification
```

## Generated

2026-03-18
