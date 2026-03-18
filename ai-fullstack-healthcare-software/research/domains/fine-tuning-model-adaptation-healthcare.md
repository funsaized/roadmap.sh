# Fine-Tuning and Model Adaptation for Healthcare

## Overview

This domain covers the techniques, tools, and regulatory considerations for adapting foundation models to healthcare-specific tasks. It bridges the gap between general-purpose LLMs (covered in D-4) and production-grade clinical AI systems. The focus is on practical fine-tuning workflows — choosing the right technique (full fine-tuning, LoRA, QLoRA, RLHF), curating training data from clinical corpora while handling PHI, evaluating models against medical benchmarks, and managing FDA change control for model updates.

**Difficulty Level:** Advanced

**Prerequisites from prior domains:**
- D-2: ML fundamentals (gradient descent, loss functions, overfitting)
- D-4: Foundation models, transformer architecture, prompt engineering
- D-5: Embeddings and knowledge systems (understanding representation learning)
- D-1: HIPAA, FDA SaMD/SiMD regulatory foundations

---

## Key Concepts

### 1. Domain-Specific Biomedical Models

**BioBERT** — A BERT model pre-trained on large-scale biomedical literature (PubMed abstracts + PMC full-text articles). Excels at biomedical text mining tasks: named entity recognition, relation extraction, question answering on biomedical literature. Best choice when working with research/literature-derived text rather than clinical notes.

**ClinicalBERT** — BERT model further pre-trained on clinical notes from the MIMIC-III dataset. Optimized for understanding clinical language including abbreviations, shorthand, and the unique syntax of discharge summaries, nursing notes, and radiology reports. Preferred for tasks involving EHR-derived text.

**Med-PaLM / Med-PaLM 2** — Google's medical LLM, first AI to pass USMLE-style questions. Med-PaLM 2 achieved 86.5% on MedQA. Powers MedLM on Google Cloud. Not open-source but represents the commercial state of the art. Med-PaLM M extends to multimodal (images + text).

**Med-Gemini** — Google's multimodal successor to Med-PaLM, built on Gemini architecture. Achieved 91.1% on MedQA. Handles 2D/3D medical images and genomic data alongside text.

**Meditron** — Open-source medical LLM built on Llama 2, developed by EPFL with Yale and Meta. Trained on curated medical literature and clinical guidelines. Designed for low-resource healthcare settings. Over 30,000 downloads within months of release.

**PMC-LLaMA** — Open-source biomedical LLM adapted from LLaMA. Two-stage training: knowledge injection from 4.8M biomedical papers + 30K medical textbooks, then medical instruction tuning. The 13B version surpasses ChatGPT on some medical QA benchmarks.

**Me-LLaMA** — Published 2024, integrates both biomedical literature AND clinical notes (unlike models trained on only one corpus). Represents the trend toward comprehensive medical language understanding.

**Relationship:** BioBERT and ClinicalBERT are encoder-only models (good for classification/extraction tasks). Med-PaLM, Meditron, PMC-LLaMA are decoder/generative models (good for QA, summarization, dialogue). Choosing the right base model depends on your task type and data domain.

### 2. Fine-Tuning Techniques

**Full Fine-Tuning** — Updates all parameters of the pre-trained model on your task-specific dataset. Produces the best theoretical performance but requires significant compute (multiple GPUs, days of training), risks catastrophic forgetting of pre-trained knowledge, and is prone to overfitting on small medical datasets. Rarely practical for LLMs with billions of parameters.

**Transfer Learning / Feature Extraction** — Freezes most model layers, only training the final task-specific head. Fast and cheap but limited expressiveness. Works well for simple classification tasks on top of BioBERT/ClinicalBERT.

**LoRA (Low-Rank Adaptation)** — Freezes original weights and injects small trainable low-rank matrices into attention layers. Trains <1% of original parameters. Dramatically reduces memory and compute requirements while achieving near-full-fine-tuning performance. Key hyperparameters: rank `r` (8-64), `lora_alpha` (scaling factor, typically 2x rank), `lora_dropout`, target modules (query/value projections).

**QLoRA (Quantized LoRA)** — Combines LoRA with 4-bit NormalFloat (NF4) quantization of the frozen base model. Reduces memory footprint ~75% versus standard fine-tuning. Enables fine-tuning 7B-70B parameter models on a single consumer GPU (8-16GB VRAM). Uses double quantization and paged optimizers for further efficiency.

**Adapter Layers** — Inserts small bottleneck layers between transformer blocks. Similar philosophy to LoRA but different architecture. Less commonly used in 2024 than LoRA/QLoRA.

**Relationship:** LoRA → QLoRA is an evolution toward efficiency. Full fine-tuning → LoRA → QLoRA represents a spectrum from maximum expressiveness to maximum efficiency. For healthcare, QLoRA is the practical default for most teams.

### 3. RLHF for Clinical Safety

**Reinforcement Learning from Human Feedback (RLHF)** — A post-training alignment technique that uses human preference data to fine-tune model behavior. Critical for healthcare because it can teach models to be cautious, evidence-based, and safety-conscious beyond what supervised fine-tuning alone achieves.

**RLHF Pipeline for Clinical LLMs:**
1. Start with a supervised fine-tuned (SFT) medical model
2. Collect clinician preference data (ranking model outputs for correctness, safety, appropriateness)
3. Train a reward model on preference pairs
4. Fine-tune the LLM using PPO (Proximal Policy Optimization) to maximize the learned reward

**DPO (Direct Preference Optimization)** — A simpler alternative to full RLHF that skips the reward model training step. Directly optimizes the policy from preference pairs. Lower computational overhead, increasingly popular in 2024.

**Clinical Safety Alignment Goals:**
- Diagnostic caution (recommend seeking professional help for serious symptoms)
- Evidence-based responses (cite guidelines, avoid speculation)
- Harm avoidance (refuse to provide dangerous medical advice)
- Bias mitigation (consistent quality across demographics)
- Appropriate uncertainty expression

**Safe RLHF** — Method accepted at ICLR 2024 Spotlight, with open-source dataset PKU-SafeRLHF for safety alignment research.

### 4. Training Data Curation from Clinical Corpora

**Clinical Data Sources:**
- MIMIC-III: 40,000+ adult ICU patients (2001-2012), extensive clinical notes, freely available via PhysioNet
- MIMIC-IV: 364,627+ unique patients (2008-2022), modular architecture, MIMIC-IV-Note for clinical text
- PubMed/PMC: Biomedical literature (abstracts and full-text articles)
- Clinical practice guidelines (AMA, specialty societies)
- De-identified EHR data from institutional data warehouses

**Data Access Requirements (PhysioNet/MIMIC):**
1. Create PhysioNet account
2. Complete CITI "Data or Specimens Only Research" training
3. Sign Data Use Agreement (DUA)
4. Obtain credentialed user status

**Data Quality Considerations:**
- Label quality: Clinical annotations require domain expertise (physicians, nurses)
- Class imbalance: Rare conditions underrepresented
- Temporal shifts: Clinical practice changes over time
- Institutional bias: Single-site data may not generalize
- Annotation inter-rater reliability measurement

**Instruction Tuning Datasets for Medical LLMs:**
- Medical Meadow WikiDoc
- MedQuAD (Medical Question Answering Dataset)
- ChatDoctor-HealthCareMagic-500k
- Doctor-HealthCare-100k
- MedReason (medical reasoning chains)

### 5. PHI Handling in Training

**HIPAA De-identification Methods:**

**Safe Harbor Method** — Remove 18 specific identifiers (names, dates except year, phone numbers, SSN, medical record numbers, etc.). Prescriptive and straightforward but removes significant data utility. Ages >89 aggregated to 90+.

**Expert Determination Method** — A qualified statistician certifies re-identification risk is "very small." More flexible, preserves richer data (e.g., month-level dates, regional geography). Better for ML training data but requires statistical expertise.

**De-identification Tools and Techniques:**
- Rule-based NER systems for PHI detection
- ML-based de-identification (trained on I2B2 DEID dataset)
- Philips/AWS automated PHI de-identification pipeline
- Synthetic data generation as alternative to de-identification
- Microsoft Presidio (open-source PII/PHI detection)

**Key Principles for ML Training with Clinical Data:**
- Minimum Necessary Principle: only use data elements actually needed
- De-identify before training whenever possible
- If training on PHI required (rare), must be under BAA with compute provider
- Audit trails for all data access during training
- Data retention and deletion policies for training artifacts
- Federated learning as alternative to centralizing PHI

### 6. Medical Benchmarks and Evaluation

**Standard Medical QA Benchmarks:**

**MedQA** — Based on USMLE-style questions. The primary benchmark for medical LLM evaluation. Multiple-choice format covering clinical knowledge, diagnosis, treatment. Current SOTA >90% (Med-Gemini 91.1%).

**PubMedQA** — Biomedical research question answering. Tests ability to understand and reason about biomedical literature. PMC-LLaMA 13B achieved ~77.9%.

**MedMCQA** — From Indian medical entrance exams (AIIMS/NEET). Broader coverage of medical topics than MedQA alone.

**MMLU Medical Subsets** — Clinical knowledge, medical genetics, anatomy, professional medicine, college biology/medicine subsets from the broader MMLU benchmark.

**Beyond Multiple Choice:**

**HealthBench** — OpenAI benchmark using multi-turn synthetic clinical conversations. Evaluates accuracy, completeness, context awareness, communication quality.

**MedQA-CS** — OSCE-style benchmark simulating clinical skill examination. Instruction-following tasks that test clinical reasoning beyond factual recall.

**MedHELM** — Stanford's holistic medical LLM evaluation framework.

**Open Medical-LLM Leaderboard** — Hugging Face platform for standardized medical LLM evaluation across MedQA, PubMedQA, MedMCQA, and MMLU medical subsets. Allows model submission and comparison.

**Clinical Safety Evaluation:**

**CSEDB (Clinical Safety-Effectiveness Dual-Track Benchmark)** — Evaluates critical illness recognition, guideline adherence, medication safety. Models show performance drops in high-risk scenarios.

**Key Evaluation Concerns:**
- Knowledge-Practice Gap: High benchmark scores ≠ clinical competence
- Drug name fragility (brand vs. generic name sensitivity)
- Demographic bias (91.7% of medical LLMs show measurable bias per systematic review)
- Hallucination rates in clinical contexts

### 7. FDA Predetermined Change Control Plans (PCCPs)

**Background:** Traditional FDA regulatory pathways (510(k), De Novo, PMA) require new submissions for each device modification. This conflicts with ML models that improve through continuous learning.

**PCCP Framework (Final guidance December 2024):**

A PCCP allows manufacturers to pre-specify planned modifications to AI/ML-enabled medical devices and receive FDA authorization upfront, avoiding per-update submissions.

**Three Required Elements:**
1. **Description of Modifications** — What specific changes are anticipated (retraining frequency, data sources, performance thresholds, scope of algorithm changes)
2. **Modification Protocol** — How changes will be developed, tested, validated, and implemented. Includes data collection protocols, retraining procedures, performance verification methods
3. **Impact Assessment** — Risk/benefit analysis of planned modifications and risk mitigation strategies

**Regulatory Timeline:**
- 2019: FDA discussion paper on AI/ML SaMD framework
- 2021: AI/ML SaMD Action Plan
- October 2023: Joint FDA/Health Canada/MHRA guiding principles for PCCPs
- April 2023: Draft guidance for AI/ML-enabled device software
- August 2024: Broader draft guidance for PCCPs across all medical devices
- December 2024: Final guidance published

**Practical Implications for Engineers:**
- Must define upfront what model changes are permissible without new submissions
- Need robust monitoring and validation infrastructure
- Performance boundaries (e.g., "AUC must remain above 0.85") must be predefined
- Data drift detection triggers for retraining must be documented
- Version control and model lineage tracking are regulatory requirements

### 8. Fine-Tuning Infrastructure and Tooling

**Core Libraries:**
- Hugging Face Transformers: Model loading, training, inference
- PEFT (Parameter-Efficient Fine-Tuning): LoRA, QLoRA, adapter implementations
- bitsandbytes: 4-bit/8-bit quantization
- TRL (Transformer Reinforcement Learning): SFT, RLHF, DPO training
- Accelerate: Distributed training, mixed precision
- DeepSpeed: Memory-efficient training at scale

**Higher-Level Platforms:**
- Unsloth: 2-5x faster fine-tuning with memory optimization
- LLaMA Factory: UI-driven fine-tuning pipeline
- Axolotl: Configuration-driven fine-tuning framework

**Hardware Considerations:**
- QLoRA 7B model: 1x consumer GPU (16GB VRAM minimum)
- QLoRA 70B model: 1x A100 80GB or 2x A100 40GB
- Full fine-tuning 7B: 4-8x A100 80GB
- RLHF adds ~2-3x compute overhead over SFT

---

## Learning Resources

### Online Courses

1. **Hugging Face PEFT Documentation & Tutorials**
   - Platform: Hugging Face
   - URL: https://huggingface.co/docs/peft
   - Duration: ~10 hours self-paced
   - Cost: Free
   - Covers: LoRA, QLoRA, adapter methods with code examples

2. **Generative AI with LLMs (Coursera/DeepLearning.AI)**
   - Platform: Coursera
   - URL: https://www.coursera.org/learn/generative-ai-with-llms
   - Duration: ~16 hours
   - Cost: Free to audit, ~$49 for certificate
   - Covers: Fine-tuning, RLHF, PEFT techniques — general but foundational

3. **Harvard AIM2 Focused Tutorials — Medical AI**
   - Platform: Harvard Medical School
   - URL: https://zitniklab.hms.harvard.edu/AIM2/focused_tutorials/
   - Duration: Variable
   - Cost: Free
   - Covers: AI in medicine tutorials including model adaptation

4. **AWS Prescriptive Guidance: Fine-Tuning for Healthcare NLP**
   - Platform: AWS
   - URL: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/fine-tuning.html
   - Duration: ~3 hours reading
   - Cost: Free
   - Covers: Production-oriented fine-tuning guidance for healthcare

### Video Tutorials and Talks

5. **Fine-Tune MedGemma with Hugging Face (Google Colab)**
   - URL: https://colab.research.google.com/github/google-health/medgemma/blob/main/notebooks/fine_tune_with_hugging_face.ipynb
   - Format: Interactive Colab notebook
   - Covers: SFT + QLoRA on Google's MedGemma model

6. **Databricks: Efficient Fine-Tuning with LoRA Guide**
   - URL: https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms
   - Format: Blog + code examples
   - Covers: Practical LoRA implementation with production considerations

7. **Lightning AI: LoRA Insights**
   - URL: https://lightning.ai/pages/community/lora-insights/
   - Format: Technical deep-dive article
   - Covers: LoRA theory, hyperparameter selection, practical tips

### Books

8. **"Natural Language Processing with Transformers" by Lewis Tunstall, Leandro von Werra, Thomas Wolf**
   - Publisher: O'Reilly, 2022
   - Relevant Chapters: Ch. 7 (Question Answering), Ch. 9 (Fine-Tuning), Ch. 11 (Future Directions)
   - Difficulty: Intermediate
   - Note: By Hugging Face team members, covers fine-tuning fundamentals applicable to healthcare

9. **"Biomedical Natural Language Processing" by Kevin Bretonnel Cohen and Dina Demner-Fushman**
   - Publisher: John Benjamins, 2014 (updated concepts still relevant)
   - Relevant: Foundational biomedical NLP concepts, evaluation methodology
   - Difficulty: Intermediate-Advanced

10. **"Deep Learning for the Life Sciences" by Bharath Ramsundar et al.**
    - Publisher: O'Reilly, 2019
    - Relevant Chapters: Model training, molecular/medical applications
    - Difficulty: Intermediate
    - Note: Good bridge between general DL and life sciences applications

### Documentation and References

11. **FDA Final Guidance: PCCP for AI-Enabled Device Software Functions (Dec 2024)**
    - URL: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-software-medical-device
    - Essential reading for anyone building FDA-regulated AI that will be updated

12. **FDA/Health Canada/MHRA: Guiding Principles for PCCPs in ML-Enabled Medical Devices**
    - URL: https://www.fda.gov/medical-devices/software-medical-device-samd/predetermined-change-control-plans-machine-learning-enabled-medical-devices-guiding-principles
    - International harmonization of ML device update frameworks

13. **PhysioNet MIMIC-IV Documentation**
    - URL: https://physionet.org/content/mimiciv/3.1/
    - Essential for accessing clinical training data

14. **Hugging Face Open Medical-LLM Leaderboard**
    - URL: https://huggingface.co/spaces/openlifescienceai/open_medical_llm_leaderboard
    - Standardized evaluation platform for medical LLMs

15. **Hugging Face Blog: Medical LLM Evaluation**
    - URL: https://huggingface.co/blog/leaderboard-medicalllm
    - Context on benchmark design and interpretation

### GitHub Repositories

16. **Shekswess/LLM-Medical-Finetuning**
    - URL: https://github.com/Shekswess/LLM-Medical-Finetuning
    - Fine-tuning Mistral/Llama2/Llama3/Gemma 7-8B on medical data with LoRA/QLoRA
    - Includes notebooks in `src/finetuning_notebooks`

17. **google-health/medgemma**
    - URL: https://github.com/google-health/medgemma
    - Google's medical model fine-tuning notebooks

18. **PKU-Alignment/safe-rlhf**
    - URL: https://github.com/PKU-Alignment/safe-rlhf
    - Safe RLHF implementation with open-source safety dataset (ICLR 2024 Spotlight)

19. **TheDecodeLab/LLM-Healthcare**
    - URL: https://github.com/TheDecodeLab/LLM-Healthcare
    - LLM for Healthcare course materials with Hugging Face integration

20. **OValery16/Tutorial-about-LLM-Finetuning-using-QLORA**
    - URL: https://github.com/OValery16/Tutorial-about-LLM-Finetuning-using-QLORA
    - Step-by-step QLoRA fine-tuning tutorial

### Community Resources

21. **r/MachineLearning and r/HealthIT** — Reddit communities discussing medical AI
22. **Hugging Face Discord** — Active community for fine-tuning questions and PEFT support
23. **PhysioNet Forums** — Community for MIMIC dataset questions and clinical data research
24. **EleutherAI Discord** — Open-source LLM training discussions

---

## Learning Path

### Phase 1: Foundations of Model Adaptation (Week 1-2, ~15 hours)

**Concepts:** Transfer learning principles, full fine-tuning mechanics, catastrophic forgetting, domain-specific pre-training

**Activities:**
1. Review transformer fine-tuning fundamentals from D-4 foundation
2. Study BioBERT and ClinicalBERT architectures and their pre-training approaches
3. Read the BioBERT paper and ClinicalBERT paper
4. Explore the Hugging Face model hub for biomedical models

**Milestone:** Can explain when to use BioBERT vs. ClinicalBERT vs. a general LLM and articulate the trade-offs of full fine-tuning

### Phase 2: Parameter-Efficient Fine-Tuning (Week 2-3, ~20 hours)

**Concepts:** LoRA theory and implementation, QLoRA quantization, PEFT library usage, hyperparameter selection (rank, alpha, target modules)

**Activities:**
1. Work through Hugging Face PEFT documentation and tutorials
2. Complete the QLoRA tutorial notebook (OValery16 repo)
3. Fine-tune a small model (e.g., Phi-2 or Llama-3.1 8B) on a medical dataset using QLoRA
4. Experiment with different LoRA ranks and observe the accuracy/efficiency trade-off

**Milestone:** Successfully fine-tune a 7B+ model on medical QA data using QLoRA on a single GPU

### Phase 3: Clinical Data Curation and PHI Handling (Week 3-4, ~15 hours)

**Concepts:** HIPAA de-identification (Safe Harbor vs. Expert Determination), MIMIC data access, training data quality, annotation pipelines, synthetic data generation

**Activities:**
1. Apply for MIMIC-IV access on PhysioNet (complete CITI training)
2. Study the 18 Safe Harbor identifiers and practice identifying PHI in sample clinical notes
3. Build a simple de-identification pipeline using rule-based + ML approaches
4. Curate an instruction-tuning dataset from public medical QA resources

**Milestone:** Have MIMIC access approved, can de-identify a clinical note, and have a curated medical fine-tuning dataset ready

### Phase 4: RLHF and Clinical Safety Alignment (Week 4-5, ~15 hours)

**Concepts:** Reward modeling, PPO for LLMs, DPO as alternative, clinical safety alignment goals, preference data collection from clinicians

**Activities:**
1. Study the RLHF pipeline through Coursera Generative AI with LLMs course
2. Explore PKU-SafeRLHF dataset and implementation
3. Implement DPO training on your fine-tuned medical model
4. Define safety criteria specific to your clinical use case

**Milestone:** Understand the full RLHF pipeline, have run DPO alignment on a medical model

### Phase 5: Medical Benchmark Evaluation (Week 5-6, ~12 hours)

**Concepts:** MedQA, PubMedQA, MedMCQA evaluation, MMLU medical subsets, clinical safety benchmarks, knowledge-practice gap awareness

**Activities:**
1. Evaluate your fine-tuned model on MedQA and PubMedQA
2. Compare performance against the Open Medical-LLM Leaderboard baselines
3. Test for demographic bias using varied patient scenarios
4. Evaluate drug name robustness (brand vs. generic)

**Milestone:** Have quantitative benchmark scores for your model with bias analysis documented

### Phase 6: FDA Change Control and Production Readiness (Week 6-7, ~10 hours)

**Concepts:** PCCP framework, SaMD classification, model versioning, performance monitoring, retraining triggers, regulatory documentation

**Activities:**
1. Read FDA PCCP final guidance (December 2024)
2. Draft a sample PCCP for a hypothetical clinical AI model update
3. Design a model versioning and lineage tracking system
4. Define performance boundaries and drift detection triggers

**Milestone:** Can write a PCCP document and articulate the regulatory pathway for model updates

---

## Practical Exercises

### Exercise 1: BioBERT NER Fine-Tuning (Beginner)
Fine-tune BioBERT for biomedical named entity recognition on the BC5CDR dataset (chemical-disease relations). Use Hugging Face Transformers with standard fine-tuning. Evaluate with entity-level F1 score. ~4 hours.

### Exercise 2: QLoRA Medical QA Model (Intermediate)
Fine-tune Llama-3.1 8B Instruct on the MedQuAD dataset using QLoRA. Compare performance at LoRA ranks 8, 16, 32. Evaluate on held-out MedQA questions. Document GPU memory usage and training time at each rank. ~8 hours.

### Exercise 3: Clinical Note De-identification Pipeline (Intermediate)
Build an end-to-end de-identification pipeline: ingest synthetic clinical notes → detect PHI entities → replace with synthetic substitutes → validate de-identification quality. Use the I2B2 DEID dataset format. Measure precision/recall of PHI detection. ~6 hours.

### Exercise 4: DPO Safety Alignment (Advanced)
Take your QLoRA fine-tuned medical model and apply DPO alignment using clinician preference pairs. Create 100+ preference pairs where the "preferred" response is safer/more evidence-based. Measure safety improvements using a custom rubric. ~10 hours.

### Exercise 5: PCCP Document Drafting (Advanced)
For a hypothetical clinical decision support tool that uses an ML model for sepsis risk prediction: draft a complete PCCP covering (a) planned modifications (monthly retraining with new patient data), (b) modification protocol (data validation, retraining, testing), and (c) impact assessment. ~6 hours.

### Exercise 6: End-to-End Medical Model Adaptation (Capstone)
Complete pipeline: select base model → curate training data from public sources → de-identify any clinical data → fine-tune with QLoRA → align with DPO → evaluate on medical benchmarks → document model card with performance boundaries suitable for PCCP inclusion. ~20 hours.

---

## Connections to Other Domains

**Builds on:**
- D-1 (Healthcare Data & Regulatory): HIPAA de-identification, FDA SaMD classification
- D-2 (ML Fundamentals): Training loops, loss functions, evaluation metrics
- D-4 (Foundation Models): Transformer architecture, tokenization, prompt engineering
- D-5 (RAG): Hybrid RAG + fine-tuning approaches

**Feeds into:**
- D-9 (Decisioning AI): Fine-tuned models power clinical decision support systems
- D-10 (AI Safety): RLHF concepts, evaluation frameworks, bias detection
- D-11 (Observability): Model versioning, performance monitoring, drift detection for fine-tuned models
- D-12 (Agentic Systems): Fine-tuned specialist models as tools within agent architectures
- D-13 (Capstone): Multi-model systems using domain-adapted models
