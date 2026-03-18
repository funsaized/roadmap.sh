# Decisioning AI and Clinical Decision Support

## Overview

This domain covers the intersection of AI-driven decisioning systems and clinical decision support (CDS) in healthcare software. It spans two complementary paradigms: **rule-based CDS systems** (deterministic, guideline-driven) and **reinforcement learning / optimization-based systems** (adaptive, data-driven). A fullstack healthcare engineer must understand both approaches, when to apply each, and how to integrate them into EHR workflows using standards like CDS Hooks, CQL, and FHIR.

This is an **advanced** domain that builds on predictive AI (D-3), embeddings/RAG (D-5), and generative AI (D-6). It feeds forward into agentic systems (D-12) and the capstone architecture (D-13).

---

## Key Concepts

### 1. Clinical Decision Support (CDS) Fundamentals

**CDS System Types**
- **Knowledge-based CDS**: Uses explicit if/then rules, clinical guidelines, and evidence-based protocols. The traditional approach — deterministic, auditable, and easy to validate.
- **Non-knowledge-based CDS**: Uses ML/AI to derive patterns from data without explicit rule authoring. Includes predictive models, RL agents, and NLP-driven systems.
- **Hybrid CDS**: Combines rule-based guardrails with ML-driven recommendations. The most practical architecture for production healthcare systems.

**CDS Five Rights Framework (Osheroff)**
The foundational principle for effective CDS: deliver the *right information*, to the *right person*, in the *right format*, through the *right channel*, at the *right time* in the workflow. Every CDS implementation should be evaluated against these criteria.

**CDS Intervention Types**
- Alerts and reminders (drug-drug interactions, allergy checks)
- Order sets and protocol-driven workflows
- Diagnostic support and differential generation
- Therapeutic recommendations (dosing, treatment selection)
- Reference information and infobuttons
- Dashboards and data presentation

### 2. CDS Rules Engines

**Architecture Components**
- **Clinical Data Repository**: Patient data store (typically EHR/FHIR server) providing facts for rule evaluation.
- **Knowledge Base / Rule Base**: Repository of if/then rules encoding clinical guidelines. Rules are typically authored in a domain-specific language (CQL, Arden Syntax, or proprietary DSLs).
- **Inference Engine**: Core runtime that matches facts against rules using forward chaining (data-driven) or backward chaining (goal-driven) strategies.
- **Working Memory**: Temporary store of current facts and intermediate results during rule evaluation.
- **Integration Layer**: APIs connecting the rules engine to EHR systems, typically via CDS Hooks or HL7 messaging.

**Rule Authoring and Management**
- Rules lifecycle: authoring → testing → validation → deployment → monitoring → retirement
- Version control for clinical rules (critical for regulatory compliance)
- Conflict resolution when multiple rules fire simultaneously
- Rule priority and specificity ordering

**Common Rules Engine Technologies**
- **Drools** (Java-based, open source) — widely used in healthcare
- **OpenCDS** (open-source CDS platform, Apache 2 license) — standards-based, supports multiple knowledge module adapters
- **CQL Engine** (HL7 standard) — purpose-built for clinical quality and decision support logic
- **Custom FHIR-based engines** — emerging pattern using FHIR PlanDefinition and ActivityDefinition resources

### 3. Clinical Quality Language (CQL)

**What CQL Is**
An HL7 ANSI Normative Standard — a high-level, domain-specific language for expressing clinical logic that is both human-readable and machine-executable. CQL is the standard way to encode clinical decision rules in the FHIR ecosystem.

**Key CQL Concepts**
- **Libraries**: Reusable collections of CQL definitions and functions
- **Expressions**: Named logic that evaluates to a value (boolean, list, etc.)
- **Retrieve**: Queries against FHIR data (e.g., `[Condition: "Diabetes"]`)
- **Value Sets and Code Systems**: Standardized terminology references
- **Expression Logical Model (ELM)**: Machine-readable compiled form of CQL — what execution engines actually run

**CQL in Practice**
- Used for clinical quality measures (eCQMs), care gap identification, and CDS rules
- Integrates with FHIR resources (Patient, Condition, MedicationRequest, etc.)
- Executed by CQL engines (e.g., cqf-ruler, cql-execution on npm)
- Supports temporal logic — critical for clinical rules involving time-based criteria

### 4. CDS Hooks

**Specification Overview**
CDS Hooks is an HL7 specification that enables real-time, workflow-integrated clinical decision support. It defines a RESTful, JSON-based protocol for EHRs (CDS Clients) to invoke external CDS Services at specific workflow trigger points.

**Core Components**
- **Hooks**: Named workflow trigger points (e.g., `patient-view`, `order-select`, `order-sign`, `encounter-start`, `appointment-book`)
- **CDS Services**: External HTTP services that receive hook context and return recommendations
- **CDS Cards**: Response format — information, suggestions (with auto-applicable FHIR actions), or app links (launching SMART on FHIR apps)
- **Discovery Endpoint**: `GET /cds-services` — allows EHRs to discover available CDS services
- **Prefetch**: Service-specified FHIR queries that the EHR resolves and includes in the request, reducing round-trips

**Integration Patterns**
- **Synchronous decision support**: EHR calls service, waits for cards, displays inline
- **Suggestion actions**: Cards can include FHIR resources to create/update/delete (e.g., auto-populate an order)
- **SMART app launch**: Cards link to SMART on FHIR applications for complex interactions
- **Feedback**: Optional mechanism for EHRs to report whether clinicians accepted/overrode CDS recommendations

**Implementation Architecture**
```
EHR (CDS Client) → Hook triggered → HTTP POST to CDS Service
                                      ↓
                              CDS Service evaluates rules/models
                                      ↓
                              Returns CDS Cards (JSON)
                                      ↓
                        EHR renders cards in clinical workflow
```

### 5. Reinforcement Learning (RL) for Treatment Optimization

**RL Fundamentals in Healthcare Context**
- **Agent**: The AI system making treatment decisions
- **Environment**: The patient and their physiological state
- **State**: Current patient status (lab values, vitals, medications, history)
- **Action**: Treatment decision (drug selection, dose adjustment, procedure timing)
- **Reward**: Clinical outcome signal (improved biomarkers, survival, quality of life)
- **Policy**: The learned mapping from states to optimal actions

**Key RL Algorithms Used in Healthcare**
- **Q-Learning / Deep Q-Networks (DQN)**: Learn value of state-action pairs; used for discrete treatment decisions
- **Policy Gradient Methods**: Directly optimize the treatment policy; better for continuous action spaces (dose titration)
- **Actor-Critic Methods**: Combine value estimation and policy optimization
- **Batch/Offline RL**: Learn from historical patient data without real-time interaction — the dominant paradigm in healthcare (cannot experiment on patients)
- **Conservative Q-Learning (CQL)**: Offline RL variant that avoids overestimating value of unseen actions — important safety property for clinical use

**Dynamic Treatment Regimes (DTRs)**
Sequential decision rules that adapt treatment over time based on patient response. Core framework for RL in chronic disease management:
- Multi-stage treatment decisions (e.g., cancer chemotherapy cycles)
- Adaptive dosing protocols (insulin, warfarin, immunosuppressants)
- Treatment escalation/de-escalation strategies

**Specific Clinical Applications**
- **Insulin dosing optimization**: RL agents adjust basal/bolus insulin based on continuous glucose monitoring data, dietary patterns, and activity levels. Goal: maximize time-in-range while minimizing hypoglycemic events.
- **Warfarin dose titration**: RL optimizes warfarin maintenance doses to keep INR within therapeutic range (2.0–3.0), accounting for individual pharmacokinetic variation.
- **Sepsis management**: RL models recommend fluid resuscitation and vasopressor timing in ICU settings.
- **Chemotherapy planning**: RL optimizes drug selection, dosing, and cycle timing based on tumor response and side effects.

### 6. Scheduling and Resource Optimization

**Problem Types**
- **Staff scheduling**: Matching provider availability with patient demand, respecting certification requirements, labor laws, and preferences
- **Appointment optimization**: Reducing no-shows through predictive modeling, overbooking strategies, and smart waitlists
- **Operating room scheduling**: Mixed-integer programming for maximizing utilization while minimizing delays
- **Bed management**: Predictive models for admission/discharge timing to optimize bed allocation
- **Equipment allocation**: Ensuring critical resources (ventilators, imaging machines) are optimally distributed

**Techniques**
- Mixed-Integer Linear Programming (MIP) for deterministic scheduling
- Reinforcement learning for adaptive, real-time scheduling adjustments
- Discrete event simulation for modeling patient flow
- Queuing theory for emergency department and clinic wait times
- Predictive analytics for demand forecasting

### 7. Clinical Trial Matching

**The Problem**
80% of clinical trials fail to meet enrollment timelines. Manual screening of patients against trial eligibility criteria is labor-intensive and error-prone.

**AI-Driven Approach**
- **NLP for criteria extraction**: Parse complex eligibility criteria from trial protocols into computable logic
- **EHR data matching**: Map patient records against trial requirements using NLP, embeddings, and structured data queries
- **Real-time cohort identification**: Continuously scan patient populations for trial eligibility
- **Privacy-preserving pipelines**: Federated approaches that match patients without exposing PHI

**Integration Points**
- CDS Hooks (`patient-view` hook) to surface matching trials during chart review
- FHIR ResearchStudy and ResearchSubject resources
- ClinicalTrials.gov API integration

### 8. Prior Authorization Automation

**End-to-End Workflow**
1. **Determination**: AI checks payer rules to determine if prior auth is required for the ordered service
2. **Document assembly**: NLP extracts relevant clinical evidence from patient records; auto-populates auth request forms
3. **Submission**: Automated submission via payer portals or X12 278 transactions
4. **Tracking**: Real-time status monitoring with intelligent escalation
5. **Appeal handling**: AI-assisted appeal generation when initial requests are denied

**AI Components**
- **NLP/document extraction**: Pulling relevant clinical data from unstructured notes
- **Rules matching**: Comparing clinical evidence against payer-specific medical necessity criteria
- **Predictive analytics**: Forecasting approval likelihood and flagging potential denials before submission
- **Generative AI**: Drafting appeal letters and peer-to-peer preparation materials

**Standards and Integration**
- FHIR Da Vinci Prior Authorization Support Implementation Guide
- X12 278 Health Care Services Review transactions
- CRD (Coverage Requirements Discovery) CDS Hooks service
- DTR (Documentation, Templates, and Rules) SMART on FHIR app

### 9. Care Gap Closure

**What Care Gaps Are**
Discrepancies between recommended care (per quality measures like HEDIS, CMS Star Ratings) and care actually delivered to patients.

**AI-Driven Care Gap Systems**
- **Gap identification**: Automated scanning of patient records against quality measure logic (often encoded in CQL)
- **Risk stratification**: Prioritizing patients most likely to benefit from intervention
- **Personalized outreach**: AI-driven communication (text, voice, portal messages) tailored to patient engagement patterns
- **Workflow integration**: Surfacing care gaps in EHR via CDS Hooks during patient encounters
- **Monitoring**: Tracking gap closure rates and measure performance over time

**Key Quality Frameworks**
- HEDIS (Healthcare Effectiveness Data and Information Set) by NCQA
- CMS Star Ratings for Medicare Advantage
- MIPS (Merit-based Incentive Payment System) quality measures
- State-specific quality programs

### 10. Alert Fatigue Management

**The Problem**
72-99% of clinical alerts are overridden by clinicians. Excessive, low-value alerts lead to desensitization, missed critical warnings, and clinician burnout.

**AI-Driven Solutions**
- **Alert prioritization**: ML models that score alerts by clinical significance, patient context, and urgency
- **Contextual suppression**: Suppressing alerts that are clinically irrelevant given the specific patient's history and current situation
- **Clinician behavior modeling**: Predicting which alerts a clinician will override and adjusting presentation strategy
- **Tiered alerting**: Hard stops (cannot proceed without acknowledgment), soft alerts (informational), and silent logging
- **Alert analytics**: Dashboards tracking override rates, alert-to-action ratios, and potential patient safety events

**Implementation Strategies**
- Retrospective analysis of alert override patterns to identify candidates for suppression
- A/B testing of alert presentation strategies
- Feedback loops: capturing clinician responses to improve future alerting
- Regular governance review of active alert rules (alert stewardship committees)

---

## Concept Relationships

```
CDS Rules Engines ←→ CQL (rules authored in CQL)
CDS Rules Engines ←→ CDS Hooks (rules triggered via hooks)
CDS Hooks ←→ SMART on FHIR (app launch from cards)
CDS Hooks ←→ Prior Auth (CRD service uses hooks)
CQL ←→ Care Gaps (quality measures encoded in CQL)
RL ←→ Treatment Optimization (insulin, warfarin, sepsis)
RL ←→ Scheduling Optimization (adaptive scheduling)
Alert Fatigue ←→ CDS Rules Engines (alert management)
Alert Fatigue ←→ ML Models (prioritization)
Clinical Trial Matching ←→ NLP + CDS Hooks (surfacing matches)
All concepts → Agentic Systems (D-12) (autonomous clinical agents)
All concepts → Capstone (D-13) (multi-modal architecture)
```

---

## Learning Resources

### Online Courses

1. **Clinical Decision Support Systems (CDSS 4)** — University of Glasgow via Coursera
   - URL: https://www.coursera.org/learn/cdss4
   - Platform: Coursera
   - Duration: ~8 hours
   - Level: Intermediate
   - Cost: Free to audit, paid certificate
   - Covers: CDS evaluation, bias/calibration/fairness in ML models, decision curve analysis, human-centered CDS

2. **Health Informatics for Healthcare Professionals** — Northeastern University via Coursera
   - URL: https://www.coursera.org/learn/health-informatics-for-healthcare-professionals
   - Platform: Coursera
   - Duration: ~20 hours
   - Level: Beginner-Intermediate
   - Cost: Free to audit
   - Covers: Health IT systems, CDS integration, data standards, reinventing CDS

3. **Reinforcement Learning Specialization** — University of Alberta via Coursera
   - URL: https://www.coursera.org/specializations/reinforcement-learning
   - Platform: Coursera
   - Duration: ~4 months (10 hrs/week)
   - Level: Intermediate-Advanced
   - Cost: Subscription
   - Covers: MDPs, temporal-difference learning, policy gradient methods, function approximation

4. **Stanford CS234: Reinforcement Learning** — Stanford Online
   - URL: https://online.stanford.edu/courses/xcs234-reinforcement-learning
   - Platform: Stanford Online
   - Duration: ~10 weeks
   - Level: Advanced
   - Cost: Paid
   - Covers: Exploration, policy search, batch RL — strong foundation for healthcare RL applications

5. **Informed Clinical Decision Making using Deep Learning Specialization** — University of Glasgow via Coursera
   - URL: https://www.coursera.org/specializations/informed-clinical-decision-making-using-deep-learning
   - Platform: Coursera
   - Duration: ~3 months
   - Level: Intermediate
   - Covers: Deep learning for clinical decision support, CDSS design and evaluation

### Video Tutorials and Talks

6. **David Silver's Reinforcement Learning Course** — DeepMind/UCL
   - URL: https://www.youtube.com/watch?v=2pWv7GOvuf0
   - Platform: YouTube (10 lectures)
   - Duration: ~20 hours total
   - Level: Intermediate-Advanced
   - The canonical RL lecture series. Covers MDPs, Q-learning, policy gradients — essential foundation before healthcare RL.

7. **FHIR CDS Hooks Tutorial: Create A CDS Service in 10 mins**
   - URL: https://www.youtube.com/watch?v=9hu8OTmTd-I
   - Platform: YouTube
   - Duration: ~10 minutes
   - Level: Beginner
   - Practical walkthrough of building a CDS Hooks service in Node.js and testing with the sandbox.

8. **CDS Hooks Integration into FHIR Application** — Darena Solutions
   - URL: https://www.youtube.com/watch?v=o2CCoSUMZEI
   - Platform: YouTube
   - Level: Intermediate
   - Demonstrates integrating CDS Hooks into a FHIR application with source code.

### Books

9. **"Clinical Decision Support Systems: Theory and Practice"** — Eta S. Berner (3rd Edition, Springer)
   - Level: Intermediate-Advanced
   - The canonical CDS textbook. Covers CDS theory, system design, implementation challenges, evaluation methods.
   - Relevant chapters: All — this is a CDS-focused textbook.

10. **"Improving Outcomes with Clinical Decision Support: An Implementer's Guide"** — Jerome A. Osheroff et al. (2nd Edition, HIMSS, 2012)
    - Level: Intermediate
    - Practical guide to CDS implementation in healthcare organizations. Covers the "CDS Five Rights" framework, governance, and optimization.

11. **"Reinforcement Learning: An Introduction"** — Richard S. Sutton & Andrew G. Barto (2nd Edition, MIT Press, 2018)
    - URL: http://incompleteideas.net/book/the-book-2nd.html (free online)
    - Level: Intermediate-Advanced
    - The definitive RL textbook. Chapters on MDPs, temporal-difference learning, policy gradient methods, and function approximation are directly applicable to treatment optimization.

12. **"Statistical Methods for Dynamic Treatment Regimes"** — Bibhas Chakraborty & Eric B. Moodie (Springer, 2013)
    - Level: Advanced
    - Focused specifically on DTRs — the statistical framework underlying RL-based treatment optimization.

### Documentation and Reference Materials

13. **CDS Hooks Official Specification**
    - URL: https://cds-hooks.org/specification/current/
    - The primary specification document. Essential reading for any CDS Hooks implementation.

14. **CDS Hooks Quick Start Guide**
    - URL: https://cds-hooks.org/quickstart/
    - Step-by-step guide to implementing your first CDS Hook (`patient-view`).

15. **CDS Hooks Sandbox**
    - URL: http://sandbox.cds-hooks.org
    - Interactive testing environment for CDS services.

16. **HL7 Clinical Quality Language (CQL) Specification**
    - URL: https://cql.hl7.org/
    - Official CQL specification from HL7. Reference for all CQL syntax and semantics.

17. **HL7 CQL GitHub Repository**
    - URL: https://github.com/HL7/cql
    - Source for the CQL specification and related tools.

18. **FHIR Clinical Reasoning Module**
    - URL: https://www.hl7.org/fhir/clinicalreasoning-module.html
    - FHIR specification for PlanDefinition, ActivityDefinition, and other CDS-relevant resources.

19. **Da Vinci Prior Authorization Support (PAS) Implementation Guide**
    - URL: https://build.fhir.org/ig/HL7/davinci-pas/
    - FHIR implementation guide for automating prior authorization workflows.

20. **eCQI Resource Center — CDS Hooks**
    - URL: https://ecqi.healthit.gov/tool/cds-hooks
    - ONC resource on CDS Hooks for electronic clinical quality improvement.

### Interactive Exercises and Labs

21. **CDS Hooks Tutorial (UW FHIR)**
    - URL: https://github.com/uw-fhir/CDS-Hooks-Tutorial
    - Hands-on tutorial: set up a CDS service, register with the sandbox, process hooks, return cards.

22. **OpenAI Gym / Gymnasium for RL**
    - URL: https://gymnasium.farama.org/
    - Standard RL training environment. Use to build RL foundations before applying to healthcare simulations.

23. **MIMIC-III Clinical Database**
    - URL: https://mimic.mit.edu/
    - Real ICU patient data (free with credentialing). Used extensively for RL research in sepsis management and treatment optimization.

### GitHub Repositories and Open-Source Projects

24. **CDS Hooks Documentation & Spec**
    - URL: https://github.com/cds-hooks/docs
    - Source for the CDS Hooks specification website.

25. **SMART on FHIR CDS Services (SRDC)**
    - URL: https://github.com/srdc/smart-on-fhir-cds
    - Example CDS Hooks services with SMART on FHIR integration. Includes QRISK and SCORE cardiovascular risk prediction.

26. **OpenCDS**
    - URL: https://opencds.org/
    - Code: https://bitbucket.org/opencds/opencds
    - Open-source, standards-based CDS engine (Apache 2 license). Supports pluggable knowledge modules and multiple rules engines.

27. **cqf-ruler (CQL FHIR Evaluation Engine)**
    - URL: https://github.com/DBCG/cqf-ruler
    - HAPI FHIR-based server with CQL evaluation capabilities. Essential for executing CQL-based CDS rules.

28. **AI Clinician (RL for Sepsis)**
    - URL: https://github.com/matthieukomorowski/AI_Clinician
    - Implementation of the landmark RL paper for sepsis treatment optimization using MIMIC-III data.

### Podcasts and Audio

29. **The Clinical AI Podcast**
    - Topics frequently cover CDS, AI in clinical workflows, and regulatory considerations.
    - Available on major podcast platforms.

30. **Healthcare AI Podcast by Deepgram**
    - Covers practical AI applications in healthcare including decision support and automation.

### Community Resources

31. **HL7 CDS Work Group**
    - URL: https://confluence.hl7.org/display/CDS
    - The standards body governing CDS Hooks and CQL. Meeting minutes, discussions, and specification development.

32. **r/healthIT** (Reddit)
    - URL: https://www.reddit.com/r/healthIT/
    - Active community discussing EHR integration, CDS implementation, and health informatics.

33. **AMIA (American Medical Informatics Association)**
    - URL: https://amia.org/
    - Professional organization for health informatics. Annual symposium features CDS research.

34. **OHDSI (Observational Health Data Sciences and Informatics)**
    - URL: https://ohdsi.org/
    - Open community for health data analytics, including standardized cohort definitions and quality measures.

---

## Learning Path

### Phase 1: CDS Foundations (2–3 weeks)

**Week 1–2: CDS Concepts and Rules Engines**
- Study CDS Five Rights framework (Osheroff book, chapters 1-3)
- Understand CDS intervention types and when to use each
- Learn rules engine architecture (knowledge base, inference engine, working memory)
- Read: Berner textbook, chapters on CDS system design

**Week 2–3: CQL and Clinical Logic**
- Work through CQL specification (start with authoring guide at cql.hl7.org)
- Write sample CQL expressions against FHIR resources
- Set up cqf-ruler locally and execute CQL libraries
- Milestone: Author a CQL library that identifies diabetic patients overdue for HbA1c testing

### Phase 2: CDS Hooks Integration (2 weeks)

**Week 4: CDS Hooks Specification**
- Read the full CDS Hooks specification at cds-hooks.org
- Complete the Quick Start guide
- Watch the "CDS Service in 10 mins" YouTube tutorial
- Explore the CDS Hooks sandbox

**Week 5: Build a CDS Hooks Service**
- Complete the UW FHIR CDS Hooks Tutorial
- Build a CDS Hooks service (Node.js or Python) that:
  - Responds to `patient-view` hook
  - Queries FHIR for patient data
  - Returns cards with clinical recommendations
- Study SMART on FHIR integration patterns (app link cards)
- Milestone: Working CDS Hooks service registered in the sandbox returning contextual clinical recommendations

### Phase 3: Reinforcement Learning for Healthcare (3–4 weeks)

**Week 6–7: RL Fundamentals**
- Complete David Silver's RL lectures (or first 2 courses of Alberta RL specialization)
- Study Sutton & Barto chapters 1-6 (MDPs, dynamic programming, TD learning)
- Practice with OpenAI Gymnasium — implement Q-learning and policy gradient agents

**Week 8–9: RL in Clinical Applications**
- Study the AI Clinician paper and code (RL for sepsis)
- Understand offline/batch RL and why it's essential in healthcare (cannot experiment on patients)
- Study DTR framework — read Chakraborty & Moodie selected chapters
- Explore insulin and warfarin dosing RL literature
- Milestone: Reproduce a simplified RL treatment optimization experiment using MIMIC-III or synthetic data

### Phase 4: Applied Decisioning (2–3 weeks)

**Week 10: Prior Authorization Automation**
- Study the Da Vinci PAS Implementation Guide
- Understand X12 278 transaction structure
- Learn CRD (Coverage Requirements Discovery) CDS Hooks pattern
- Map end-to-end prior auth workflow: determination → document assembly → submission → tracking → appeal
- Milestone: Design a prior auth automation architecture diagram with all integration points

**Week 11: Care Gaps and Quality Measures**
- Study HEDIS measure specifications (pick 3-5 common measures)
- Encode a quality measure in CQL
- Build a care gap identification pipeline using CQL + FHIR
- Milestone: Working care gap detection for one HEDIS measure against synthetic patient data

**Week 12: Alert Fatigue and Clinical Trial Matching**
- Study alert override literature and ML-based prioritization approaches
- Design an alert scoring model architecture
- Explore clinical trial matching pipelines (NLP + FHIR ResearchStudy)
- Milestone: Design document for an AI-driven alert fatigue management system

### Phase 5: Integration and Capstone (1–2 weeks)

**Week 13–14: Putting It All Together**
- Build a comprehensive CDS architecture that combines:
  - Rule-based CDS (CQL) for guideline adherence
  - ML-based alert prioritization
  - CDS Hooks integration with EHR workflow
  - Care gap identification and closure workflow
- Review scheduling optimization approaches
- Connect to agentic systems concepts (D-12 preview)
- Milestone: Architecture document for a production CDS platform integrating rule-based and AI-driven decisioning

**Total estimated time: 10–14 weeks**

---

## Practical Exercises

### Exercise 1: Build a Drug-Drug Interaction CDS Hooks Service (Beginner)
- Create a CDS Hooks service that responds to `order-select`
- Check new medication orders against a drug interaction database
- Return warning cards with severity levels
- Test in the CDS Hooks sandbox

### Exercise 2: CQL Quality Measure Implementation (Intermediate)
- Pick a HEDIS measure (e.g., Breast Cancer Screening, Diabetes HbA1c Control)
- Write CQL to identify patients with care gaps
- Execute against synthetic FHIR data using cqf-ruler
- Build a simple dashboard showing gap closure rates

### Exercise 3: RL Medication Dosing Agent (Advanced)
- Use the MIMIC-III dataset (or a synthetic diabetes simulator)
- Implement a Q-learning agent for insulin dose recommendation
- Compare RL policy against a simple rules-based dosing protocol
- Evaluate using clinically relevant metrics (time-in-range, hypoglycemia events)

### Exercise 4: Alert Fatigue Reduction Model (Advanced)
- Analyze a dataset of CDS alert firings and clinician responses
- Build a classifier predicting alert override probability
- Design a tiered alerting strategy based on model scores
- Calculate the projected reduction in alert volume while maintaining safety

### Exercise 5: Prior Auth Automation Prototype (Advanced)
- Design a prior auth determination service using CDS Hooks CRD pattern
- Implement NLP extraction of clinical evidence from sample clinical notes
- Match extracted evidence against sample payer criteria
- Measure accuracy of automated determination vs. manual review

### Exercise 6: End-to-End CDS Platform Architecture (Expert)
- Design a complete CDS platform architecture including:
  - CDS Hooks API gateway
  - CQL execution service
  - ML model serving layer
  - Alert management and prioritization
  - Care gap monitoring
  - Analytics and feedback pipeline
- Document data flows, security considerations (HIPAA), and scalability approach
- Present as a technical design document suitable for engineering review

---

## Connections to Other Domains

### Prerequisites (what you need before this domain)
- **D-3 Predictive AI**: Understanding of predictive models is essential for risk scoring, alert prioritization, and outcome prediction in CDS
- **D-5 Embeddings/RAG**: Knowledge retrieval patterns used in clinical trial matching and evidence retrieval for prior auth
- **D-6 Generative AI**: NLP capabilities used in prior auth document extraction and appeal generation

### What this domain enables
- **D-12 Agentic Systems**: CDS services are a building block for autonomous clinical agents that can take actions in EHR workflows
- **D-13 Capstone Architecture**: Decisioning AI is a core modality in any multi-modal healthcare AI system, combining with predictive, generative, and perception AI

### Cross-cutting concerns
- **D-10 AI Safety**: CDS requires rigorous evaluation — false negatives (missed alerts) and false positives (alert fatigue) both cause patient harm
- **D-11 Observability**: Production CDS systems need comprehensive monitoring of alert firing rates, override patterns, and clinical outcomes
