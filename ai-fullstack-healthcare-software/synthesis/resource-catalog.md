# Resource Catalog: AI in Fullstack Healthcare Software

## Overview
This is the deduplicated, ranked master resource catalog across all 13 domains. Resources are tagged by type, difficulty, format, cost, and domain relevance. "Best in Class" resources are marked with ⭐.

Total unique resources after deduplication: 197

---

## Tier 1: Essential Resources (Must-Complete)

### Courses

| # | Title | Platform | Difficulty | Cost | Est. Hours | Domains | Notes |
|---|-------|----------|------------|------|------------|---------|-------|
| ⭐1 | Machine Learning Specialization (Andrew Ng) | Coursera/DeepLearning.AI | Beginner | Free audit | 27 | D-2 | Canonical ML foundations |
| ⭐2 | AI in Healthcare Specialization | Coursera/Stanford | Intermediate | $49/mo | 36 | D-2,3,7,10 | Healthcare-specific ML |
| ⭐3 | ChatGPT Prompt Engineering for Developers | DeepLearning.AI | Beginner | Free | 1 | D-4 | Foundational prompt skills |
| ⭐4 | AI Agents in LangGraph | DeepLearning.AI | Intermediate | Free | 4 | D-12 | Canonical agent course |
| 5 | HL7 FHIR Mastery (Udemy) | Udemy | Beginner | $20-50 | 10 | D-1 | Best FHIR course |
| 6 | MLOps Zoomcamp | DataTalks.Club | Intermediate | Free | 40 | D-11 | MLOps foundations |
| 7 | Generative AI with LLMs | Coursera/DeepLearning.AI | Intermediate | Free audit | 16 | D-8 | Fine-tuning + RLHF |
| 8 | Multi AI Agent Systems with CrewAI | DeepLearning.AI | Intermediate | Free | 2 | D-12 | Multi-agent patterns |
| 9 | Knowledge Graphs for RAG | DeepLearning.AI | Intermediate | Free | 1 | D-5 | KG + RAG integration |
| 10 | AI for Medicine Specialization | Coursera/DeepLearning.AI | Intermediate | $49/mo | 36 | D-3,7 | Medical imaging + prognosis |
| 11 | Reinforcement Learning Specialization | Coursera/U Alberta | Advanced | $49/mo | 40 | D-9 | RL foundations |
| 12 | Machine Learning Engineering for Production (MLOps) | Coursera/DeepLearning.AI | Intermediate | Free audit | 48 | D-11 | Production ML lifecycle |
| 13 | SNOMED CT Foundation Course | SNOMED International | Beginner | Free | 4 | D-5 | Medical ontology |

### Books

| # | Title | Author | Difficulty | Cost | Domains | Notes |
|---|-------|--------|------------|------|---------|-------|
| ⭐14 | Hands-On ML with Scikit-Learn, Keras, TensorFlow (3rd ed) | Aurélien Géron | Beginner-Intermediate | ~$60 | D-2,3 | Best practical ML textbook |
| ⭐15 | Designing Machine Learning Systems | Chip Huyen | Intermediate-Advanced | ~$50 | D-11 | Definitive production ML guide |
| ⭐16 | NLP with Transformers (Revised) | Tunstall, von Werra, Wolf | Intermediate | ~$50 | D-4,8 | Hugging Face ecosystem |
| 17 | Interpretable Machine Learning | Christoph Molnar | Intermediate | Free online | D-2,10 | SHAP, LIME, explainability |
| 18 | Clinical Prediction Models | Ewout Steyerberg | Intermediate-Advanced | ~$80 | D-3 | Clinical model development |
| 19 | Reinforcement Learning: An Introduction | Sutton & Barto | Intermediate-Advanced | Free online | D-9 | Definitive RL textbook |
| 20 | Speech and Language Processing | Jurafsky & Martin | Advanced | Free online | D-6 | ASR and NLG reference |
| 21 | Clinical Decision Support Systems | Eta Berner | Intermediate-Advanced | ~$100 | D-9 | CDS theory and practice |

### Documentation & Specifications

| # | Title | URL | Domains | Notes |
|---|-------|-----|---------|-------|
| ⭐22 | HL7 FHIR R4 Specification | hl7.org/fhir/R4/ | D-1,3,5,9,12 | Authoritative FHIR reference |
| ⭐23 | CDS Hooks Specification | cds-hooks.org | D-1,3,9 | CDS integration standard |
| ⭐24 | FDA AI/ML SaMD Resources | fda.gov/medical-devices/... | D-1,7,8,10 | Regulatory guidance |
| 25 | OpenTelemetry GenAI Semantic Conventions | opentelemetry.io/docs/... | D-11 | AI tracing standards |
| 26 | CQL Specification | cql.hl7.org | D-9 | Clinical quality language |
| 27 | SMART on FHIR Documentation | docs.smarthealthit.org | D-1,12 | EHR app authorization |
| 28 | HHS HIPAA De-identification Guidance | hhs.gov/hipaa/... | D-1,10 | Official de-id guidance |
| 29 | DICOM Standard | dicomstandard.org | D-1,7 | Imaging standard |

---

## Tier 2: Recommended Resources (High Value)

### Courses & Tutorials

| # | Title | Platform | Difficulty | Cost | Domains |
|---|-------|----------|------------|------|---------|
| 30 | MIT 6.S897 Machine Learning for Healthcare | MIT OCW | Advanced | Free | D-2,3 |
| 31 | Stanford CS224N: NLP with Deep Learning | YouTube | Advanced | Free | D-4 |
| 32 | Full Stack LLM Bootcamp | fullstackdeeplearning.com | Intermediate | Free | D-11 |
| 33 | Prompt Engineering Specialization | Coursera/Vanderbilt | Beginner-Intermediate | $49/mo | D-4 |
| 34 | David Silver RL Course | YouTube/DeepMind | Intermediate-Advanced | Free | D-9 |
| 35 | Evaluations of AI in Healthcare | Coursera/Stanford | Intermediate | Free audit | D-10 |
| 36 | Clinical Decision Support Systems | Coursera/Glasgow | Intermediate | Free audit | D-9 |
| 37 | Retrieval Augmented Generation | DeepLearning.AI | Intermediate | Free | D-5 |
| 38 | Agentic AI with LangChain/LangGraph | Coursera | Intermediate | $49/mo | D-12 |

### Video Content

| # | Title | Source | Difficulty | Domains |
|---|-------|--------|------------|---------|
| 39 | The Illustrated Transformer (blog + course) | Jay Alammar / DeepLearning.AI | Beginner-Intermediate | D-4 |
| 40 | StatQuest ML Videos | YouTube | Beginner | D-2 |
| 41 | MONAI Tutorial Videos | YouTube/Project MONAI | Intermediate | D-7 |
| 42 | Attention Is All You Need Explained | Yannic Kilcher/YouTube | Intermediate | D-4 |

### Open-Source Tools & Frameworks

| # | Tool | URL | Domains | Purpose |
|---|------|-----|---------|---------|
| ⭐43 | MONAI | github.com/Project-MONAI/MONAI | D-7 | Medical imaging AI framework |
| ⭐44 | LangChain/LangGraph | langchain-ai.github.io/langgraph | D-5,12 | Agent orchestration |
| ⭐45 | MLflow | github.com/mlflow/mlflow | D-11 | Model lifecycle management |
| ⭐46 | Evidently AI | github.com/evidentlyai/evidently | D-11 | Drift detection & monitoring |
| 47 | Microsoft Presidio | github.com/microsoft/presidio | D-10 | PHI/PII detection |
| 48 | NVIDIA NeMo Guardrails | github.com/NVIDIA/NeMo-Guardrails | D-10 | LLM guardrails |
| 49 | LiteLLM | github.com/BerriAI/litellm | D-11 | Model routing/proxy |
| 50 | Arize Phoenix | github.com/Arize-ai/phoenix | D-11 | LLM observability |
| 51 | Langfuse | github.com/langfuse/langfuse | D-11 | LLM engineering platform |
| 52 | Synthea | github.com/synthetichealth/synthea | D-1,6 | Synthetic patient data |
| 53 | HAPI FHIR | github.com/hapifhir/hapi-fhir | D-1,3,9 | FHIR server |
| 54 | pydicom | github.com/pydicom/pydicom | D-1,7 | DICOM processing |
| 55 | highdicom | github.com/ImagingDataCommons/highdicom | D-7 | AI → DICOM encoding |
| 56 | OHIF Viewer | github.com/OHIF/Viewers | D-7 | Medical image viewer |
| 57 | nnU-Net | github.com/MIC-DKFZ/nnUNet | D-7 | Self-configuring segmentation |
| 58 | Orthanc | orthanc-server.com | D-7 | DICOM server |
| 59 | Hugging Face PEFT | huggingface.co/docs/peft | D-8 | Parameter-efficient fine-tuning |
| 60 | OpenAI Whisper | github.com/openai/whisper | D-6 | Speech recognition |
| 61 | scikit-learn | scikit-learn.org | D-2,3 | ML library |
| 62 | SHAP | github.com/shap/shap | D-2,11 | Model explainability |
| 63 | Guardrails AI | github.com/guardrails-ai/guardrails | D-10 | Output validation |
| 64 | CrewAI | docs.crewai.com | D-12 | Multi-agent framework |
| 65 | cqf-ruler | github.com/DBCG/cqf-ruler | D-9 | CQL execution engine |

### Datasets

| # | Dataset | URL | Domains | Purpose |
|---|---------|-----|---------|---------|
| ⭐66 | MIMIC-IV | physionet.org/content/mimiciv/3.1/ | D-2,3,8,9 | Clinical data (257K+ patients) |
| 67 | MIMIC-III | physionet.org/content/mimiciii/1.4/ | D-2,3,6,8 | ICU patient data |
| 68 | MIMIC-CXR | physionet.org/content/mimic-cxr/2.0.0/ | D-7 | Chest X-rays + reports |
| 69 | NIH ChestX-ray14 | kaggle.com/datasets/nih-chest-xrays/data | D-7 | 112K chest X-rays |
| 70 | CheXpert | stanfordmlgroup.github.io/competitions/chexpert/ | D-7 | 224K chest radiographs |
| 71 | Medical Segmentation Decathlon | medicaldecathlon.com | D-7 | 10 segmentation tasks |
| 72 | ISIC Archive | isic-archive.com | D-7 | Skin lesion images |
| 73 | PhysioNet Heart Sound 2016 | physionet.org/content/challenge-2016/ | D-7 | Heart sound classification |
| 74 | Kaggle Diabetes Readmission | kaggle.com/datasets/brandao/diabetes | D-3 | Readmission prediction |
| 75 | i2b2/n2c2 NLP Datasets | portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/ | D-10 | PHI de-identification |

### Research Papers

| # | Title | Year | Domains | Key Contribution |
|---|-------|------|---------|-----------------|
| 76 | Large Language Models in Medicine (Med-PaLM 2) | 2023 | D-4,8 | Healthcare LLM capabilities |
| 77 | GPT-4 on Medical Challenge Problems | 2023 | D-4 | USMLE benchmarking |
| 78 | Medprompt Technical Report | 2023 | D-4 | Advanced medical prompting |
| 79 | CONSORT-AI Extension | 2020 | D-10 | AI clinical trial reporting |
| 80 | Adapted LLMs for Clinical Summarization | 2024 | D-6 | Fine-tuned LLMs > experts |

### GitHub Projects for Practice

| # | Project | URL | Domains | Purpose |
|---|---------|-----|---------|---------|
| 81 | Azure Healthcare Agent Orchestrator | github.com/Azure-Samples/healthcare-agent-orchestrator | D-12 | Production multi-agent reference |
| 82 | FHIR AI Hackathon Kit | github.com/intersystems-community/FHIR-AI-Hackathon-Kit | D-12 | FHIR + agents tutorial |
| 83 | AI Clinician (RL for Sepsis) | github.com/matthieukomorowski/AI_Clinician | D-9 | RL treatment optimization |
| 84 | MONAI Tutorials | github.com/Project-MONAI/tutorials | D-7 | Medical imaging exercises |
| 85 | MIMIC-III Benchmarks | github.com/YerevaNN/mimic3-benchmarks | D-3 | Clinical prediction benchmarks |
| 86 | Medical Graph RAG | github.com/ImprintLab/Medical-Graph-RAG | D-5 | KG + RAG for healthcare |
| 87 | ClinicalBERT | github.com/EmilyAlsentzer/clinicalBERT | D-5,8 | Clinical embedding model |
| 88 | LLM Medical Finetuning | github.com/Shekswess/LLM-Medical-Finetuning | D-8 | QLoRA medical fine-tuning |
| 89 | StanfordMIMI/clin-summ | github.com/StanfordMIMI/clin-summ | D-6 | Clinical summarization |
| 90 | Healthcare Prompt Engineering Workshop | github.com/KarinBrisker/Healthcare-Prompt-Engineering-Workshop | D-4 | Prompt engineering practice |

### Community Resources

| # | Resource | URL | Domains |
|---|----------|-----|---------|
| 91 | HL7 FHIR Chat (Zulip) | chat.fhir.org | D-1,3,9 |
| 92 | MONAI Community | github.com/Project-MONAI/MONAI/discussions | D-7 |
| 93 | PhysioNet Forums | physionet.org | D-2,3,8 |
| 94 | Hugging Face Hub (Medical Models) | huggingface.co/models | D-4,5,8 |
| 95 | Open Medical-LLM Leaderboard | huggingface.co/spaces/openlifescienceai/... | D-8 |
| 96 | AMIA | amia.org | D-6,9 |
| 97 | MLOps Community | mlops.community | D-11 |

---

## Resource Count by Domain

| Domain | Resources |
|--------|-----------|
| D-1: Healthcare Data Foundations | 37 |
| D-2: ML Fundamentals | 23 |
| D-3: Predictive AI | 33 |
| D-4: Foundation Models | 30 |
| D-5: Embeddings/RAG | 33 |
| D-6: Generative AI | 35 |
| D-7: Computer Vision | 35 |
| D-8: Fine-Tuning | 24 |
| D-9: Decisioning AI | 34 |
| D-10: AI Safety | 31 |
| D-11: Observability | 31 |
| D-12: Agentic Systems | 23 |
| **Unique after deduplication** | **197** |

Note: Many resources serve multiple domains (e.g., Stanford AI in Healthcare covers D-2, D-3, D-7, D-10).
