# Foundation Models and Prompt Engineering for Healthcare

## Overview

This domain covers the practical use of Large Language Models (LLMs) in healthcare contexts. It bridges ML fundamentals (D-2) and healthcare data foundations (D-1) with downstream domains including RAG systems (D-5), fine-tuning (D-8), AI safety (D-10), and production operations (D-11). The focus is on understanding transformer architecture at an applied level, mastering prompt engineering for clinical tasks, building PHI-safe LLM pipelines, and navigating the healthcare LLM landscape.

This is a critical pivot domain — it introduces the generative AI paradigm that underlies most subsequent domains in the roadmap.

---

## Key Concepts

### 1. Transformer Architecture Fundamentals
- **Self-Attention Mechanism**: Core innovation allowing models to weigh relationships between all tokens in a sequence simultaneously. Uses Query, Key, Value (QKV) projections to compute attention scores. Essential for understanding why LLMs can process long clinical notes effectively.
- **Multi-Head Attention**: Runs attention in parallel across multiple subspaces, allowing the model to capture different types of relationships (syntactic, semantic, referential) simultaneously.
- **Positional Encoding**: Injects sequence order information since transformers process all tokens in parallel (unlike RNNs). Variants include sinusoidal, learned, and rotary positional encodings (RoPE).
- **Encoder-Decoder Architecture**: The original transformer design. Encoder processes input into contextual representations; decoder generates output autoregressively. BERT uses encoder-only; GPT uses decoder-only; T5 uses full encoder-decoder.
- **Feed-Forward Networks, Residual Connections, Layer Normalization**: Standard components that stabilize training and refine representations within each transformer block.
- **Tokenization**: How text is converted to numerical input — BPE (Byte Pair Encoding), WordPiece, SentencePiece. Medical terminology often fragments into subword tokens, affecting prompt design.

*Prerequisite for*: D-5 (embeddings/RAG), D-8 (fine-tuning), D-12 (agentic systems)

### 2. Healthcare LLM Landscape
- **Med-PaLM / Med-PaLM 2 / Med-PaLM M** (Google): First AI to pass USMLE-style questions. Med-PaLM 2 achieved 86.5% on MedQA. Med-PaLM M is multimodal (images, genomics, clinical notes). Available via Google Cloud as MedLM.
- **BioGPT** (Microsoft Research): Generative pre-trained transformer trained on PubMed abstracts. Excels at biomedical Q&A, literature summarization, relationship extraction (drug-drug interactions, disease-gene associations).
- **GPT-4 / GPT-4o in Clinical Studies**: GPT-4o achieves ~90.4% on USMLE questions, outperforming medical students (59.3% average). Diagnostic accuracy of 92.7% in clinical skills assessments. Performance varies — weaker on image-based and pathology questions.
- **ClinicalBERT / BioBERT / PubMedBERT**: Encoder-only models fine-tuned on clinical/biomedical corpora. Best for classification, NER, and embedding tasks rather than generation.
- **GatorTron**: Large clinical language model trained on 90B+ words of clinical text from University of Florida Health.
- **Open-Source Healthcare LLMs**: OpenBioLLM-70B (Saama AI Labs), Hippocrates/Hippo models (Mistral/LLaMA-based), Aloe (BSC), BioMedLM (Stanford CRFM).
- **Small Language Models (SLMs)**: Emerging trend of smaller, efficient models optimized for resource-constrained clinical environments.

*Prerequisite for*: D-8 (knowing which models to fine-tune), D-10 (evaluating model safety)

### 3. Prompt Engineering Techniques for Clinical Tasks
- **Zero-Shot Prompting**: Direct instruction without examples. Works for straightforward tasks but unreliable for nuanced clinical output.
- **Few-Shot Prompting**: Providing 2-5 input-output examples in the prompt. Critical for clinical tasks where output format and clinical terminology must be precise. Example diversity matters more than quantity.
- **Chain-of-Thought (CoT) Prompting**: Instructing the model to show step-by-step reasoning. Significantly improves performance on clinical reasoning, differential diagnosis, and medication dosing calculations. Most effective with models >100B parameters.
- **Self-Consistency Prompting**: Generate multiple CoT paths and select the most frequent answer. Reduces variance in clinical outputs.
- **Generated Knowledge Prompting**: Have the LLM generate relevant medical knowledge before answering the actual clinical question.
- **Meta-Prompting / Automated Prompt Optimization**: Using LLMs to optimize prompts for other LLMs — Microsoft's Medprompt technique combines dynamic few-shot selection, self-generated CoT, and choice-shuffle ensembling.
- **Context Engineering**: Optimizing the entire context window — not just the instruction but what background information, guidelines, and constraints to include. Critical for production healthcare systems.
- **Safety Constraints in Prompts**: Explicit instructions to refuse harmful advice, cite uncertainty, defer to clinicians, and flag out-of-scope queries. Non-negotiable in healthcare.

*Prerequisite for*: D-5 (RAG prompt design), D-10 (guardrails), D-12 (agent prompt orchestration)

### 4. Clinical Note Summarization
- **Discharge Summary Generation**: Condensing multi-day inpatient notes into structured discharge summaries. Key application of few-shot prompting with format templates.
- **Progress Note Summarization**: Extracting assessment and plan from daily clinical notes.
- **Radiology Report Summarization**: Generating impression sections from findings.
- **Context-Preserving Techniques**: Token filtering that preserves clinically important terms while reducing noise. Knowledge graph augmentation for maintaining clinical fidelity.
- **Evaluation Metrics**: ROUGE, BERTScore, clinical accuracy (human expert evaluation), factual consistency scoring. Automated metrics alone are insufficient — human clinical review is essential.

### 5. Medical Coding and Q&A with LLMs
- **ICD/CPT Code Suggestion**: Using LLMs to suggest diagnosis and procedure codes from clinical text. Prompt design must include coding guidelines context.
- **Clinical Question Answering**: Answering clinician queries about treatment protocols, drug interactions, clinical guidelines. Requires grounding in evidence-based sources.
- **MedDRA Coding**: Adverse event coding using standardized terminology. GPT-4 achieves F1 of 0.67-0.73, comparable to specialized NLP tools.

### 6. Structured Output Extraction from Clinical Text
- **JSON Schema Enforcement**: Constraining LLM output to conform to predefined JSON schemas. Tools: OpenAI function calling, Anthropic tool use, Instructor library.
- **FHIR Resource Generation**: Converting free-text clinical notes to HL7 FHIR resources (MedicationStatement, Condition, Procedure). FHIR-GPT achieved >90% exact match rates.
- **Named Entity Recognition (NER)**: Extracting medications, diagnoses, procedures, lab values from unstructured text. Prompt-based NER vs. traditional NER pipelines.
- **Relation Extraction**: Identifying relationships between entities (drug-condition, symptom-diagnosis).
- **Validation Pipelines**: Schema validation, FHIR conformance checking, clinical terminology verification (SNOMED CT, LOINC, RxNorm mapping).

*Prerequisite for*: D-5 (knowledge extraction for RAG), D-9 (CDS data pipelines)

### 7. PHI-Safe LLM Integration Patterns
- **Business Associate Agreements (BAAs)**: Non-negotiable before any PHI touches a third-party LLM API. Not all LLM providers offer BAAs.
- **HIPAA-Eligible Infrastructure**: Azure OpenAI Service, Google Cloud Vertex AI (with MedLM), AWS Bedrock — all offer BAA-covered LLM access. Consumer APIs (ChatGPT, Claude.ai) are NOT suitable for PHI.
- **De-identification Pipelines**: Removing/masking 18 HIPAA identifiers before sending to LLMs. Tools: John Snow Labs Healthcare NLP, AWS Comprehend Medical, Azure Text Analytics for Health, Presidio.
- **Metadata-First Design**: Keep raw PHI in secure boundaries. LLMs operate on de-identified data, codes, or aggregates. Include PHI in prompts only with documented need and compensating controls.
- **Data Minimization**: Only send the minimum necessary PHI for the specific task. Truncate irrelevant sections of clinical notes.
- **Prompt/Response Logging as PHI**: Audit logs containing prompts with clinical data are themselves PHI. Must be encrypted, access-controlled, and retention-managed.
- **Zero-Trust Architecture**: Deny-by-default, least-privilege access, continuous verification for every LLM API call.
- **No-Train Clauses**: Ensure LLM providers contractually agree not to use input data for model training.
- **Synthetic Data for Development**: Never use real PHI in dev/test environments. Use synthetic patient data generators (Synthea).

*Prerequisite for*: D-10 (safety), D-11 (production operations)

### 8. LLM Evaluation for Healthcare
- **Benchmarks**: MedQA, PubMedQA, MMLU (medical subset), MultiMedQA, USMLE practice exams.
- **Clinical Accuracy Assessment**: Expert physician review of LLM outputs for factual correctness, clinical appropriateness, and potential harm.
- **Hallucination Detection**: Techniques to identify when LLMs generate plausible but incorrect medical information. Critical safety concern.
- **Bias Evaluation**: Testing for demographic, geographic, and condition-specific biases in clinical outputs.
- **Red-Teaming**: Adversarial testing for jailbreaks, harmful medical advice generation, PHI leakage.

### 9. Production LLM Architecture Patterns
- **API Integration**: REST/streaming calls to LLM providers (OpenAI, Anthropic, Google) with retry logic, rate limiting, and fallback models.
- **Prompt Management**: Version-controlled prompt templates, A/B testing, prompt registries.
- **Caching and Cost Optimization**: Semantic caching for repeated queries, prompt compression, model routing (cheaper models for simple tasks).
- **Latency Considerations**: Streaming responses for real-time clinical workflows vs. batch processing for retrospective analysis.

---

## Learning Resources

### Online Courses

1. **ChatGPT Prompt Engineering for Developers** — DeepLearning.AI + OpenAI
   - Platform: DeepLearning.AI (free)
   - URL: https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
   - Duration: ~1 hour
   - Difficulty: Beginner
   - Covers: Prompt patterns, summarization, inferring, transforming text, building chatbots
   - *Relevance*: Foundational prompt engineering skills applicable to all clinical tasks

2. **AI for Medicine Specialization** — DeepLearning.AI / Coursera
   - Platform: Coursera
   - URL: https://www.deeplearning.ai/courses/ai-for-medicine-specialization/
   - Duration: ~3 months (suggested pace)
   - Difficulty: Intermediate
   - Covers: Medical diagnosis from images, prognosis prediction, NLP for medical data labeling
   - Cost: Coursera subscription (~$49/month)
   - *Relevance*: Healthcare-specific AI context; NLP module directly applicable

3. **Prompt Engineering Specialization** — Vanderbilt University / Coursera
   - Platform: Coursera
   - URL: https://www.coursera.org/specializations/prompt-engineering
   - Duration: ~2 months
   - Difficulty: Beginner-Intermediate
   - Covers: Prompt patterns, advanced techniques, security considerations
   - Cost: Coursera subscription

4. **Clinical Prompt Engineering for Physicians** — Physician Prompt Engineering
   - Platform: Self-paced online
   - URL: https://physicianpromptengineering.com/courses/clinical-prompt-engineering/
   - Duration: Self-paced
   - Difficulty: Beginner (clinician-focused)
   - Covers: Clinical documentation prompts, hypothetical patient scenarios, self-evaluation exercises
   - *Relevance*: Directly addresses clinical prompt engineering with practical exercises

5. **Prompt Engineering with Llama 2 & 3** — DeepLearning.AI
   - Platform: DeepLearning.AI (free)
   - URL: https://www.deeplearning.ai/short-courses/
   - Duration: ~1 hour
   - Difficulty: Intermediate
   - Covers: Few-shot, CoT prompting with open-source models
   - *Relevance*: Open-source model prompt techniques applicable to healthcare LLMs

### Video Tutorials and Lectures

6. **The Illustrated Transformer** — Jay Alammar (blog + video)
   - URL (blog): https://jalammar.github.io/illustrated-transformer/
   - URL (video course): https://www.deeplearning.ai/short-courses/how-transformer-llms-work/ (with Maarten Grootendorst)
   - Duration: Blog ~30min read; video course ~2 hours
   - Difficulty: Beginner-Intermediate
   - *Relevance*: Best visual explanation of transformer architecture — essential prerequisite

7. **Attention Is All You Need — Paper Explained** — Yannic Kilcher (YouTube)
   - URL: https://www.youtube.com/watch?v=iDulhoQ2pro
   - Duration: ~40 minutes
   - Difficulty: Intermediate
   - *Relevance*: Deep dive into the original transformer paper

8. **Stanford CS224N: NLP with Deep Learning** — Stanford Online
   - URL: https://www.youtube.com/playlist?list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4
   - Duration: Full course (~20 lectures)
   - Difficulty: Intermediate-Advanced
   - *Relevance*: Comprehensive NLP foundation including transformers, attention, and language models

### Books

9. **"Natural Language Processing with Transformers" (Revised Edition)** — Lewis Tunstall, Leandro von Werra, Thomas Wolf (O'Reilly, 2022)
   - Relevant Chapters: Ch 1-4 (Transformer architecture, text classification, NER), Ch 8 (Efficient transformers), Ch 11 (Training from scratch)
   - Difficulty: Intermediate
   - *Relevance*: Hands-on Hugging Face Transformers library — directly applicable to building healthcare NLP pipelines

10. **"Prompt Engineering for Generative AI" (Early Release)** — James Phoenix, Mike Taylor (O'Reilly, 2024)
    - Relevant Chapters: All — covers prompt patterns, structured output, chain-of-thought, evaluation
    - Difficulty: Beginner-Intermediate
    - *Relevance*: Comprehensive prompt engineering reference

11. **"Biomedical Natural Language Processing"** — Kevin Bretonnel Cohen, Dina Demner-Fushman (John Benjamins, 2014; updated coverage in newer surveys)
    - Difficulty: Intermediate-Advanced
    - *Relevance*: Foundational biomedical NLP concepts; pair with modern LLM resources for full picture

### Documentation and Reference Materials

12. **OpenAI API Documentation — Structured Outputs**
    - URL: https://platform.openai.com/docs/guides/structured-outputs
    - *Relevance*: Production patterns for enforcing JSON schema compliance in clinical output extraction

13. **Anthropic Prompt Engineering Guide**
    - URL: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering
    - *Relevance*: Best practices for safety-focused prompt design, applicable to healthcare constraints

14. **Microsoft Medprompt Technical Report**
    - URL: https://github.com/microsoft/promptbase
    - Related paper: "Can Generalist Foundation Models Outcompete Special-Purpose Tuning?" (arXiv:2311.16452)
    - *Relevance*: State-of-the-art prompt engineering strategy achieving specialist-level medical performance with generalist models

15. **Google Med-PaLM Research Page**
    - URL: https://sites.research.google/med-palm/
    - *Relevance*: Understanding Google's healthcare LLM approach and MedLM product offerings

16. **HL7 FHIR Specification**
    - URL: https://hl7.org/fhir/
    - *Relevance*: Understanding FHIR resource schemas for structured output extraction targets

### Research Papers

17. **"Large Language Models in Medicine" — Singhal et al. (Nature, 2023)**
    - URL: https://arxiv.org/abs/2305.09617
    - *Relevance*: Med-PaLM 2 paper — foundational reading for healthcare LLM capabilities

18. **"Capabilities of GPT-4 on Medical Challenge Problems" — Nori et al. (Microsoft, 2023)**
    - URL: https://arxiv.org/abs/2303.13375
    - *Relevance*: Benchmark study of GPT-4 on USMLE, demonstrating clinical reasoning capabilities

19. **"A Survey of Large Language Models for Healthcare" — He et al.**
    - URL: https://github.com/KaiHe-better/LLM-for-Healthcare
    - *Relevance*: Comprehensive survey of the healthcare LLM landscape with taxonomy

20. **"Prompt Engineering in Clinical Practice: Tutorial for Clinicians" — PMC (2024)**
    - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12439060/
    - *Relevance*: Practical clinical prompt engineering framework with real examples

### Interactive Exercises and Practice

21. **Healthcare Prompt Engineering Workshop** — KarinBrisker (GitHub)
    - URL: https://github.com/KarinBrisker/Healthcare-Prompt-Engineering-Workshop
    - Format: Hands-on exercises with evaluation tools
    - *Relevance*: Direct practice with medical prompt engineering scenarios

22. **DAIR.AI Prompt Engineering Guide** — (GitHub)
    - URL: https://github.com/dair-ai/Prompt-Engineering-Guide
    - Format: Comprehensive guide with examples and exercises
    - *Relevance*: Foundational prompt engineering techniques reference

23. **Clinical Summarization LLM Benchmarks** — (GitHub)
    - URL: https://github.com/1Krypt0/clinical-summarization-llm
    - Format: Code + benchmarks for discharge summary generation
    - *Relevance*: Hands-on practice with clinical note summarization using various LLMs

### GitHub Repositories and Open-Source Projects

24. **HPAI-BSC/prompt_engine** — Healthcare Prompt Engineering Framework
    - URL: https://github.com/HPAI-BSC/prompt_engine
    - *Relevance*: Evaluation framework for LLMs on medical benchmarks using various prompting techniques; includes Medprompt adaptation for open-source models

25. **Hippocrates — Open-Source Medical LLM Framework**
    - URL: https://cyberiada.github.io/Hippocrates/
    - *Relevance*: Open training data, code, and checkpoints for medical LLMs; Hippo 7B models

26. **healthylaife/ConTextual — Clinical Text Summarization**
    - URL: https://github.com/healthylaife/ConTextual
    - *Relevance*: Context-preserving clinical summarization using knowledge graphs and prompt design

27. **John Snow Labs Spark NLP for Healthcare**
    - URL: https://www.johnsnowlabs.com/spark-nlp-health/
    - *Relevance*: Production-grade de-identification, NER, and clinical NLP pipelines

### Community Resources

28. **r/HealthcareAI** — Reddit
    - URL: https://www.reddit.com/r/HealthcareAI/
    - *Relevance*: Community discussions on LLMs in healthcare

29. **r/PromptEngineering** — Reddit
    - URL: https://www.reddit.com/r/PromptEngineering/
    - *Relevance*: General prompt engineering techniques and discussions

30. **Hugging Face Healthcare/Medical Models Hub**
    - URL: https://huggingface.co/models?pipeline_tag=text-generation&sort=trending&search=medical
    - *Relevance*: Browse and experiment with open-source medical LLMs

---

## Learning Path

### Phase 1: Transformer Foundations (Week 1 — ~10 hours)

**Concepts**: Self-attention, multi-head attention, positional encoding, encoder-decoder architecture, tokenization

**Activities**:
1. Read Jay Alammar's "The Illustrated Transformer" blog post
2. Watch the "How Transformer LLMs Work" DeepLearning.AI course
3. Read Chapters 1-2 of "NLP with Transformers" (O'Reilly)
4. Optional deep dive: Watch Yannic Kilcher's paper walkthrough

**Milestone**: Can explain how a transformer processes a clinical note, what attention does, and why tokenization matters for medical terms.

### Phase 2: Healthcare LLM Landscape (Week 2 — ~8 hours)

**Concepts**: Med-PaLM, BioGPT, GPT-4 clinical studies, ClinicalBERT, BioBERT, GatorTron, open-source healthcare LLMs, model selection criteria

**Activities**:
1. Read the Med-PaLM 2 paper (Singhal et al.)
2. Read the GPT-4 medical benchmarks paper (Nori et al.)
3. Survey the LLM-for-Healthcare GitHub repository (He et al.)
4. Explore the Hugging Face medical models hub — download and test 1-2 models
5. Read the PMC survey on LLMs in healthcare challenges/ethics

**Milestone**: Can articulate the differences between Med-PaLM, BioGPT, GPT-4, and open-source alternatives; knows which model fits which use case; understands current benchmark performance.

### Phase 3: Prompt Engineering Fundamentals (Week 3 — ~12 hours)

**Concepts**: Zero-shot, few-shot, chain-of-thought, self-consistency, meta-prompting, safety constraints, context engineering

**Activities**:
1. Complete DeepLearning.AI "ChatGPT Prompt Engineering for Developers"
2. Study the DAIR.AI Prompt Engineering Guide (focus on CoT, few-shot, structured output sections)
3. Read the Anthropic prompt engineering documentation
4. Read the Medprompt paper and explore the promptbase repository
5. Practice: Write prompts for 5 different clinical tasks (summarization, coding, Q&A, NER, triage)

**Milestone**: Can apply zero-shot, few-shot, and CoT techniques; understands when each is appropriate; can write effective safety constraints.

### Phase 4: Clinical Applications (Week 4 — ~12 hours)

**Concepts**: Clinical note summarization, medical coding, clinical Q&A, structured output extraction, FHIR generation, NER

**Activities**:
1. Complete the Healthcare Prompt Engineering Workshop (GitHub)
2. Work through the Clinical Summarization LLM Benchmarks repo
3. Build a discharge summary generator using few-shot prompting
4. Build a FHIR MedicationStatement extractor from clinical notes using structured output (OpenAI function calling or equivalent)
5. Read the FHIR-GPT paper on clinical text to FHIR conversion
6. Practice medical coding prompts (ICD-10, CPT suggestion from clinical narratives)

**Milestone**: Has built working prototypes for clinical summarization and structured extraction; understands evaluation metrics (ROUGE, BERTScore, clinical accuracy).

### Phase 5: PHI-Safe Integration (Week 5 — ~10 hours)

**Concepts**: BAAs, HIPAA-eligible LLM infrastructure, de-identification pipelines, data minimization, prompt logging as PHI, zero-trust, synthetic data

**Activities**:
1. Review Azure OpenAI Service HIPAA documentation and BAA requirements
2. Review Google Cloud Vertex AI / MedLM HIPAA compliance documentation
3. Set up a de-identification pipeline using an open-source tool (Presidio or similar)
4. Design a complete PHI-safe LLM pipeline architecture diagram for a clinical summarization use case
5. Generate synthetic clinical data using Synthea for testing
6. Document a compliance checklist for LLM integration in a healthcare application

**Milestone**: Can design and document a HIPAA-compliant LLM integration architecture; understands BAA requirements; can implement de-identification.

### Phase 6: Evaluation and Production Readiness (Week 6 — ~8 hours)

**Concepts**: Benchmarking, hallucination detection, bias evaluation, red-teaming, prompt management, cost optimization

**Activities**:
1. Run evaluations on medical QA benchmarks (MedQA, PubMedQA) using the HPAI-BSC prompt_engine
2. Design a red-teaming protocol for a clinical LLM application
3. Create a prompt versioning and A/B testing strategy
4. Calculate cost estimates for different LLM providers at clinical scale
5. Review production architecture patterns (caching, fallback, streaming)

**Milestone**: Can evaluate LLM performance on clinical tasks, identify hallucinations, estimate costs, and design a production-ready prompt management system.

**Total Estimated Time: 6 weeks (~60 hours)**

---

## Practical Exercises

### Exercise 1: Clinical Note Summarizer (Beginner)
Build a prompt that takes a multi-paragraph clinical progress note and produces a structured summary with: Chief Complaint, Assessment, Plan, and Medications. Use few-shot prompting with 3 example note/summary pairs. Evaluate using synthetic notes from Synthea.

### Exercise 2: ICD-10 Code Suggester (Intermediate)
Create a prompt pipeline that reads a clinical encounter note and suggests the top 3 ICD-10 codes with confidence levels and supporting evidence from the note. Use chain-of-thought prompting to show the reasoning path.

### Exercise 3: FHIR Resource Extractor (Intermediate)
Build a structured output pipeline that converts a free-text medication list into FHIR MedicationStatement resources (JSON). Use OpenAI function calling or Instructor library for schema enforcement. Validate output against the FHIR spec.

### Exercise 4: PHI-Safe Pipeline Design (Intermediate)
Design and implement a complete pipeline: (1) receive a clinical note, (2) de-identify it, (3) send to LLM for summarization, (4) re-identify the output, (5) log the transaction. Use Presidio for de-identification and a HIPAA-eligible LLM API.

### Exercise 5: Medical Q&A with Medprompt (Advanced)
Implement Microsoft's Medprompt technique: dynamic few-shot selection from a medical Q&A corpus, self-generated chain-of-thought, and choice-shuffle ensembling. Evaluate on a subset of MedQA. Compare with vanilla few-shot and zero-shot baselines.

### Exercise 6: Red-Teaming a Clinical LLM (Advanced)
Design and execute a red-teaming protocol for a clinical Q&A system. Attempt to: (1) extract harmful medical advice, (2) cause hallucinated drug interactions, (3) bypass safety guardrails, (4) extract training data. Document findings and design mitigations.

---

## Connections to Other Domains

| Domain | Connection |
|--------|-----------|
| **D-1: Healthcare Data Foundations** | FHIR, HIPAA, medical terminologies (SNOMED, LOINC, RxNorm) are prerequisites for structured output extraction |
| **D-2: ML Fundamentals** | Neural network basics, training concepts needed to understand transformer architecture |
| **D-3: Predictive AI** | LLMs can complement traditional predictive models; understanding when to use each |
| **D-5: Embeddings & RAG** | Prompt engineering + embedding retrieval = RAG; this domain provides the prompt layer |
| **D-6: Generative AI** | Builds on prompt engineering for content generation applications |
| **D-8: Fine-Tuning** | When prompt engineering isn't enough — understanding the boundary between prompting and fine-tuning |
| **D-9: Clinical Decision Support** | LLM-powered CDS requires prompt engineering + structured output + safety guardrails |
| **D-10: AI Safety** | Safety constraints, red-teaming, hallucination detection all originate here |
| **D-11: Production Operations** | Prompt management, cost optimization, monitoring patterns introduced here |
| **D-12: Agentic Systems** | Multi-agent prompt orchestration builds on single-prompt engineering skills |
