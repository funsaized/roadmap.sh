# D-12: Agentic Systems for Healthcare

## Overview

Agentic AI systems represent the next evolution beyond simple chatbots and recommendation engines — they are autonomous, goal-directed systems that plan multi-step actions, use external tools, maintain state, and adapt to feedback. In healthcare, this means AI that doesn't just answer questions but actually *does things*: querying EHRs via FHIR APIs, orchestrating prior authorization workflows, routing cases to specialists, and escalating to humans when confidence is low.

The agentic AI in healthcare market was valued at ~$538.5M in 2024 and is projected to reach ~$5B by 2030 (CAGR ~45%). Key players (Epic, Oracle, Microsoft, AWS) are embedding agentic AI directly into EHR platforms and cloud health services. This domain covers how to build, evaluate, and safely deploy such systems.

---

## Key Concepts

### 1. Agent Architectures

**ReAct (Reason + Act)**
The foundational pattern for tool-using LLM agents. The model interleaves reasoning ("Thought:") with tool invocations ("Action:") and observation of results ("Observation:"), looping until a final answer is produced. In healthcare: an agent reasons about a patient query, calls a FHIR API to retrieve lab results, reasons about the results, then formulates a response or routes to a clinician.

**Plan-and-Execute (Planner-Executor)**
Separates planning from execution. A planner LLM produces a multi-step plan (e.g., "1. Retrieve patient demographics, 2. Check formulary, 3. Validate prior auth criteria, 4. Submit request"), and executor sub-agents carry out each step. Better for long-horizon clinical workflows where the plan can be audited before execution.

**Tool-Using Agents**
Agents equipped with function-calling / tool schemas (OpenAI function calling, Anthropic tool use). Tools in healthcare context:
- `get_patient_record(patient_id)` → FHIR Patient resource
- `search_medications(query)` → formulary lookup
- `submit_prior_auth(claim_data)` → payer portal API
- `schedule_appointment(patient_id, provider_id, time)` → EHR scheduling
- `query_clinical_guidelines(condition)` → evidence database

**Multi-Agent Systems**
Multiple specialized agents collaborate: an orchestrator agent routes tasks to specialist agents (imaging agent, medication agent, billing agent, documentation agent). Each agent has its own prompt, tools, and LLM. The orchestrator coordinates communication and handles inter-agent dependencies.

---

### 2. FHIR API Agents

FHIR (Fast Healthcare Interoperability Resources) R4/R5 is the standard for healthcare data exchange. Agents interact with FHIR via:

**Core FHIR Resources for Agents:**
- `Patient` — demographics, identifiers
- `Encounter` — visit/admission records
- `Observation` — lab results, vitals
- `Condition` — diagnoses (ICD-10 coded)
- `MedicationRequest` — prescriptions
- `DiagnosticReport` — structured reports
- `Claim` / `CoverageEligibilityRequest` — billing / prior auth
- `CarePlan` — longitudinal care coordination

**SMART on FHIR** — OAuth2-based authorization for FHIR APIs, enabling agents to authenticate securely against EHR systems (Epic, Cerner/Oracle, Allscripts).

**Agent FHIR patterns:**
```
1. Agent receives task: "Check if patient 12345 needs prior auth for drug X"
2. Tool call: GET /Patient/12345 → demographics
3. Tool call: GET /Condition?patient=12345 → diagnoses
4. Tool call: GET /MedicationRequest?patient=12345 → current meds
5. Tool call: query_payer_guidelines(drug=X, diagnoses=[...]) → criteria
6. Reasoning: Criteria met? → yes/no with confidence score
7. If confidence < threshold: route to human review queue
8. If confidence >= threshold: submit_prior_auth(structured payload)
```

---

### 3. LangChain / LangGraph / CrewAI for Healthcare

**LangChain**
The foundational framework for LLM application development. Provides tool-calling abstractions, memory management, chain composition. Used for single-agent healthcare apps (symptom checkers, EHR query assistants).
- Docs: https://python.langchain.com/docs/get_started/introduction

**LangGraph**
Extends LangChain with *stateful graph-based workflows*. Nodes = agents/functions, Edges = transitions with conditional routing. Critical features for healthcare:
- **State persistence** — maintain conversation and patient context across steps
- **Conditional routing** — branch based on confidence scores, clinical rules, or tool results
- **Human-in-the-loop** — `interrupt_before` / `interrupt_after` to pause for clinician review
- **Subgraph composition** — modular clinical workflows (triage subgraph, prior-auth subgraph, documentation subgraph)
- Docs: https://langchain-ai.github.io/langgraph/

**CrewAI**
Role-based multi-agent framework. Define agents with roles ("Clinical Reviewer", "Prior Auth Specialist", "Documentation Writer"), tasks, and delegation rules. Orchestrates agents in sequential or hierarchical processes.
- Docs: https://docs.crewai.com/

**AutoGen (Microsoft)**
Conversation-based multi-agent framework where agents converse to complete tasks. Supports human-proxy agents (a human in the conversation loop). Used in clinical note validation and multi-disciplinary team simulations.
- Docs: https://microsoft.github.io/autogen/

---

### 4. Multi-Step Clinical Workflow Orchestration

#### Prior Authorization Workflow (End-to-End)
```
Trigger: New medication order in EHR
  ↓
[Data Extraction Agent]
  - FHIR: GET Patient, Condition, MedicationRequest, Coverage
  - Extract: diagnosis codes, clinical notes, current formulary
  ↓
[Criteria Validation Agent]
  - Query payer guidelines API
  - Check: clinical necessity, step therapy requirements, exclusions
  - Output: criteria_met=True/False, confidence=0.87, missing_docs=[...]
  ↓
[Confidence Router]
  - confidence >= 0.90 → auto-submit
  - 0.70 <= confidence < 0.90 → soft review queue (clinician validates)
  - confidence < 0.70 → hard escalation (block + human required)
  ↓
[Submission Agent] (if auto or after human approval)
  - Format CoverageEligibilityRequest FHIR resource
  - POST to payer FHIR endpoint
  - Poll for response (async)
  ↓
[Notification Agent]
  - Update EHR with authorization status
  - Alert prescriber via EHR message
  - Schedule follow-up if denied
```

#### Care Coordination Workflow
```
Trigger: Patient discharge planning initiated
  ↓
[Assessment Agent] — Pull active conditions, medications, social history
  ↓
[Care Plan Generator] — Draft CarePlan FHIR resource with:
  - Follow-up appointments (scheduling tool)
  - Medication reconciliation
  - Referrals to specialists
  ↓
[Transition Planning Agent] — Identify: SNF vs. home vs. rehab
  ↓
[Communication Agent] — Notify: PCP, specialists, patient
  ↓
[Documentation Agent] — Generate discharge summary
```

#### Clinical Documentation Workflow
```
[Audio Capture] → [Transcription Agent] → [NLP Structure Agent]
  → [ICD/CPT Coding Agent] → [Review Queue] → [EHR Write Agent]
```

---

### 5. Human-in-the-Loop (HITL) Patterns

HITL is not optional in clinical AI — it is a regulatory and safety requirement. Key patterns:

**Confidence-Based Routing**
```python
def route_task(result):
    if result.confidence >= HIGH_THRESHOLD:
        return "auto_execute"       # Agent acts autonomously
    elif result.confidence >= MED_THRESHOLD:
        return "soft_review"        # Human validates, agent pre-fills
    else:
        return "hard_escalation"    # Human required before any action
```

**Review Queue Pattern**
- Agent pre-populates a task card with recommendation + evidence
- Human reviewer sees: AI recommendation, supporting data, confidence, audit trail
- Human approves/modifies/rejects
- Agent learns from corrections (RLHF feedback loop)
- Queue SLA monitoring ensures tasks don't languish

**Interrupt Patterns in LangGraph**
```python
# Pause workflow before a critical action
graph.add_node("submit_auth", submit_prior_auth)
graph.add_edge("validate", "submit_auth", interrupt_before=True)

# When interrupted, human reviews state, then resumes:
# thread = {"configurable": {"thread_id": "patient-123"}}
# graph.invoke(Command(resume={"approved": True}), thread)
```

**Override and Correction Patterns**
- Clinician overrides AI recommendation → logged for audit + retraining signal
- High override rates on a specific decision type → flag for model retraining or threshold adjustment
- Override UI shows reasoning transparency to reduce inappropriate overrides

**Escalation Tiers (Tiered Agentic Oversight - TAO)**
Mimics clinical hierarchies:
- Tier 1: Nurse-level agent (routine tasks, clear protocols)
- Tier 2: Physician-level agent (complex clinical decisions)
- Tier 3: Specialist-level agent (subspecialty questions)
- Each tier can escalate to human counterparts

---

### 6. Agent Safety Boundaries for Clinical Agents

**Scope Constraints**
- Agents must have explicit tool allowlists — an EHR data agent should NOT have billing submission tools
- Task-specific agents > general-purpose agents for safety
- Principle of least privilege: request only minimum FHIR scopes needed

**Guardrail Patterns**
```python
class ClinicalGuardrails:
    PROHIBITED_ACTIONS = [
        "prescribe_medication",       # Prescribing = physician only
        "modify_diagnosis",           # Diagnosis = physician only
        "discharge_patient",          # Discharge = care team only
    ]
    
    def validate_action(self, proposed_action):
        if proposed_action.type in self.PROHIBITED_ACTIONS:
            raise GuardrailViolation("Action requires human clinician")
        if proposed_action.patient_impact == "HIGH":
            return self.escalate_to_human(proposed_action)
```

**Audit and Traceability**
- Every agent action must be logged: timestamp, agent_id, tool_called, inputs, outputs, confidence
- LangSmith (LangChain) and LangFuse provide agent tracing
- HIPAA-compliant audit logs with PHI masking

**Hallucination Mitigation**
- Ground all clinical facts in retrieved FHIR data, not LLM memory
- Use structured outputs (Pydantic models) to constrain responses
- Confidence calibration: agents should output "I don't know" rather than guess
- Citation requirement: clinical recommendations must cite source (FHIR resource ID, guideline URL)

---

### 7. Testing Frameworks for Clinical Agents

**Unit Testing Agents**
- Mock FHIR endpoints with synthetic patient data (Synthea-generated)
- Test each tool call in isolation
- Test routing logic with boundary confidence values
- Use pytest + LangChain testing utilities

**Integration Testing**
- End-to-end workflow tests against FHIR sandbox (HAPI FHIR test server)
- Simulate payer API responses (success, denial, pending, error)
- Test human review interruption and resume flows

**Safety Testing**
- **MedSentry** benchmark: 5,000 adversarial medical prompts across 25 threat categories
- **Promptfoo medical plugin**: tests for fabricated medical facts, incorrect drug dosing, hallucinated studies
- Red teaming scenarios: dangerous dosing requests, authority impersonation, emergency misdirection
- NOHARM framework: physician-to-specialist consultation cases evaluating if AI recommendations could cause harm

**Evaluation Frameworks**
- **QUEST** (Stanford): Quality, Understanding, Expression, Safety, Trust — 5-principle human evaluation
- **MedHELM** (Stanford): Holistic evaluation against real-world clinical scenarios
- **RWE-LLM** (Hippocratic AI): Real-world evaluation with licensed clinician reviewers
- **MEDIC**: Medical reasoning, Ethics, Data understanding, In-context learning, Clinical safety

**Performance Metrics**
- Task completion rate (successful end-to-end workflows %)
- Human escalation rate (% of tasks requiring human intervention)
- Override rate (% of AI recommendations overridden — safety signal)
- Latency per workflow step (SLA compliance)
- False positive/negative rates for routing decisions

---

### 8. Multi-Model Architectures

**Mixture of Experts Routing**
- Small, fast model handles triage and routing decisions
- Specialized models handle subspecialty domains (radiology, pathology, cardiology)
- Large general model handles complex reasoning and documentation
- Cost optimization: use cheapest model that meets accuracy threshold

**Cascade Architecture**
```
Input → Small model (confidence check) 
  → If confidence < threshold → Medium model 
  → If still uncertain → Large model + human review
```

**Specialist Model Selection**
- Imaging reports → radiology-fine-tuned model
- Medication queries → pharmacy/formulary-tuned model
- Clinical notes → general clinical LLM (clinical BERT, MedPaLM)
- Administrative tasks → GPT-4o-mini / fast models

**Azure Healthcare Agent Orchestrator Pattern (Microsoft)**
- Orchestrator agent receives clinical task
- Routes to specialist agents based on task type (imaging, EHR, genomics)
- Aggregates results into unified clinical view
- FHIR Integration layer handles all EHR reads/writes

---

## Learning Resources

### Online Courses

**1. AI Agents in LangGraph** — DeepLearning.AI (Free)
- URL: https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/
- Instructors: Harrison Chase (LangChain founder), Rotem Weiss (Tavily)
- Topics: Build agents from scratch, LangGraph workflows, persistence, human-in-the-loop
- Duration: ~4 hours | Difficulty: Intermediate
- Why: The canonical hands-on intro to LangGraph; directly applicable to healthcare agent patterns

**2. AI Agents in Healthcare and Capstone** — Coursera (IBM)
- URL: https://www.coursera.org/learn/ai-agents-in-healthcare-and-capstone
- Topics: Agentic AI in healthcare automation, decision-making, system optimization; capstone project
- Duration: ~20 hours | Cost: Coursera subscription or audit free
- Why: Healthcare-specific agentic AI with practical project

**3. Multi AI Agent Systems with CrewAI** — DeepLearning.AI (Free)
- URL: https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/
- Topics: Role-based multi-agent design, task delegation, crew composition
- Duration: ~2 hours | Difficulty: Intermediate
- Why: Best intro to multi-agent systems; patterns transfer directly to healthcare

**4. Agentic AI with LangChain and LangGraph** — Coursera
- URL: https://www.coursera.org/learn/agentic-ai-with-langchain-and-langgraph
- Topics: Stateful workflows, self-improving agents, LangGraph deep dive
- Duration: ~15 hours | Cost: Coursera subscription

**5. AI Agentic Design Patterns with AutoGen** — DeepLearning.AI (Free)
- URL: https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/
- Topics: Conversation-based multi-agent, human-proxy agents, HITL patterns
- Duration: ~3 hours | Why: AutoGen's human-proxy pattern is ideal for clinical review queues

**6. Agentic AI in Practice** — IBM Training
- URL: https://www.ibm.com/training/learning-path/agentic-ai-in-practice-1058
- Topics: Agentic workflow design with LangGraph, healthcare assistants, production patterns
- Cost: IBM subscription

### Documentation & Reference

**7. LangGraph Official Documentation**
- URL: https://langchain-ai.github.io/langgraph/
- Topics: Graph construction, state management, HITL interrupts, persistence, multi-agent architectures
- Why: Primary reference for building healthcare workflow orchestration

**8. LangGraph How-To Guides: Human-in-the-Loop**
- URL: https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/
- Topics: `interrupt_before`, `interrupt_after`, `Command(resume=...)`, approval workflows
- Why: Direct implementation patterns for clinical review queues

**9. FHIR R4 Specification — HL7**
- URL: https://hl7.org/fhir/R4/
- Topics: All FHIR resource types, search parameters, RESTful API, SMART on FHIR
- Why: The authoritative spec for building FHIR API agents

**10. SMART on FHIR Developer Documentation**
- URL: https://docs.smarthealthit.org/
- Topics: OAuth2 authorization for FHIR apps, app launch, scopes
- Why: Required for building agents that authenticate against real EHRs

**11. AWS Blog: Prior Authorization with AI Agents**
- URL: https://aws.amazon.com/blogs/industries/transform-healthcare-prior-authorization-with-ai-agents/
- Topics: End-to-end prior auth workflow, agent architecture, AWS Bedrock integration
- Why: Production-level walkthrough of one of the most common healthcare agentic use cases

### GitHub Repositories

**12. Azure Healthcare Agent Orchestrator** — Microsoft
- URL: https://github.com/Azure-Samples/healthcare-agent-orchestrator
- Topics: Multi-agent healthcare orchestration, FHIR integration, tumor board workflow, Azure AI
- Stars: Active, Microsoft-maintained
- Why: The most comprehensive production-quality reference for healthcare multi-agent systems

**13. Agentic Healthcare AI** — amitpuri
- URL: https://github.com/amitpuri/agentic-healthcare-ai
- Topics: CrewAI + AutoGen healthcare agents, FHIR API Gateway, SMART on FHIR, React UI
- Why: Shows full-stack FHIR agent implementation with multiple frameworks

**14. FHIR AI Hackathon Kit** — InterSystems Community
- URL: https://github.com/intersystems-community/FHIR-AI-Hackathon-Kit
- Topics: FHIR server setup, LangChain agentic tools, vector search on clinical data, "Making it Agentic" tutorial
- Why: Step-by-step tutorial from FHIR basics to agentic tool-calling

**15. ZenML: Building an Agentic AI System for Healthcare Support with LangGraph**
- URL: https://www.zenml.io/llmops-database/building-an-agentic-ai-system-for-healthcare-support-using-langgraph
- Topics: End-to-end LangGraph healthcare agent with ZenML MLOps pipeline
- Why: Shows how to productionize LangGraph agents with proper MLOps

### Research Papers & Academic Resources

**16. MedSentry: Understanding and Mitigating Safety Risks in Medical LLM Multi-Agent Systems**
- URL: https://www.researchgate.net/publication/392134013_MedSentry_Understanding_and_Mitigating_Safety_Risks_in_Medical_LLM_Multi-Agent_Systems
- Topics: 25 adversarial threat categories, multi-agent safety benchmarking, mitigation strategies
- Why: The most comprehensive safety testing framework for clinical multi-agent systems

**17. Agentic AI in Healthcare (PMC/NIH)**
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11848050/
- Topics: Systematic review of agentic AI applications, clinical workflow automation, safety considerations
- Why: Peer-reviewed academic overview; credible foundation for clinical AI work

**18. QUEST Framework for Human Evaluation of LLMs in Healthcare (JAMIA)**
- URL: https://academic.oup.com/jamia/article/31/11/2730/7776823
- Topics: 5-principle evaluation framework (Quality, Understanding, Expression, Safety, Trust)
- Why: Rigorous methodology for evaluating clinical agent outputs

### Video Content

**19. Building Healthcare AI Agents with LangGraph — YouTube/Winfully Digital**
- URL: https://winfully.digital/healthcare/building-an-agentic-ai-care-coordinator-for-home-health-using-langgraph/
- Topics: Home health care coordinator agent, patient care plan generation, EHR updates
- Why: Detailed walkthrough of a real healthcare agentic use case

**20. Healthcare Agent Orchestrator Demo — Microsoft YouTube**
- URL: https://www.youtube.com/watch?v=0tu3AWzQZAo
- Topics: Live demo of Azure Healthcare Agent Orchestrator, multi-agent tumor board workflow
- Duration: ~30 min | Why: Visual demonstration of production-grade multi-agent healthcare system

**21. How to Build Care Coordination Workflows with AI Agents using LangGraph — Medium/Dev.to**
- URL: https://medium.com/@JossGuarnelli/how-to-build-a-care-coordination-workflow-with-ai-agents-using-langgraph-0dfb9e561290
- Topics: Care coordination step-by-step, LangGraph nodes/edges, conditional routing

### Tools & Frameworks Documentation

**22. Promptfoo Medical Red Teaming Plugin**
- URL: https://www.promptfoo.dev/docs/red-team/plugins/medical/
- Topics: Automated adversarial testing for medical AI, dosing safety, hallucination detection
- Why: Practical tool for safety-testing clinical agents before deployment

**23. AWS Step Functions for Clinical AI Workflows**
- URL: https://aws.amazon.com/blogs/industries/orchestrating-clinical-generative-ai-workflows-using-aws-step-functions/
- Topics: Serverless clinical workflow orchestration, state machines, async FHIR operations
- Why: Alternative to LangGraph for production cloud-native clinical workflows

---

## Learning Path

### Phase 1: Agent Foundations (Week 1–2, ~15 hours)

**Goal:** Understand ReAct, tool-calling, and single-agent systems before applying to healthcare.

1. **DeepLearning.AI: AI Agents in LangGraph** (4 hrs) — Start here. Build agents from scratch.
2. **LangGraph official docs: Quickstart + Concepts** (3 hrs) — Read State, Nodes, Edges, Checkpointers.
3. **DeepLearning.AI: Multi AI Agent Systems with CrewAI** (2 hrs) — Understand multi-agent patterns.
4. **Milestone:** Build a simple 3-node LangGraph agent that: (1) receives a query, (2) calls a mock API, (3) returns structured output with confidence score.

### Phase 2: FHIR and EHR Integration (Week 3, ~10 hours)

**Goal:** Learn FHIR APIs and how to build tool-calling agents on top of them.

1. **FHIR R4 Spec** — Read Patient, Observation, Condition, MedicationRequest, Claim resources (3 hrs)
2. **SMART on FHIR docs** — Understand OAuth2 authorization flow (2 hrs)
3. **FHIR AI Hackathon Kit** (GitHub) — Work through Steps 1-4, reaching the agentic step (3 hrs)
4. **AWS Blog: Prior Auth with AI Agents** — Read architecture walkthrough (1 hr)
5. **Milestone:** Build a LangGraph agent with 3 FHIR tools (patient lookup, condition query, medication query) against HAPI FHIR test server.

### Phase 3: Clinical Workflow Orchestration (Week 4–5, ~12 hours)

**Goal:** Implement multi-step clinical workflows with proper state management and routing.

1. **Azure Healthcare Agent Orchestrator** (GitHub) — Clone, read, run locally (4 hrs)
2. **ZenML LangGraph Healthcare Tutorial** — End-to-end system walkthrough (2 hrs)
3. **LangGraph How-To: Human-in-the-Loop** — Implement interrupt/resume pattern (2 hrs)
4. **AWS Step Functions for Clinical Workflows** blog (1 hr)
5. **Milestone:** Implement a 5-step prior authorization workflow: data extraction → criteria validation → confidence routing → human review queue → submission.

### Phase 4: Multi-Agent Systems and Multi-Model Routing (Week 6, ~8 hours)

**Goal:** Build specialized agent teams and implement multi-model routing.

1. **DeepLearning.AI: AI Agentic Design Patterns with AutoGen** (3 hrs)
2. **Microsoft Healthcare Agent Orchestrator demo video** (1 hr)
3. **LangGraph multi-agent documentation** (2 hrs)
4. **Milestone:** Build a 3-agent healthcare system: Orchestrator + ClinicalDataAgent + DocumentationAgent with confidence-based routing between agents.

### Phase 5: Safety, Testing, and Production (Week 7–8, ~12 hours)

**Goal:** Test, red-team, and safely deploy clinical agents.

1. **Promptfoo Medical Red Teaming Plugin** — Run adversarial tests on your agent (3 hrs)
2. **MedSentry paper** — Understand threat taxonomy and mitigations (2 hrs)
3. **QUEST Framework paper (JAMIA)** — Read and implement human eval methodology (2 hrs)
4. **Implement production guardrails**: audit logging, HIPAA PHI masking, scope constraints (3 hrs)
5. **Milestone:** Complete safety test suite for your prior auth agent: 20+ adversarial prompts, audit log verification, HITL override test, false confidence injection test.

---

## Practical Exercises

### Exercise 1: ReAct Agent for Patient Data Retrieval
**Difficulty:** Beginner | **Time:** 3–4 hours
- Set up HAPI FHIR test server (https://hapi.fhir.org/baseR4)
- Load synthetic patient data (Synthea output)
- Build a LangChain/LangGraph ReAct agent with 4 FHIR tools
- Test: "What medications is patient John Smith currently taking, and are there any drug interactions?"
- Validate: Agent correctly chains multiple FHIR calls before answering

### Exercise 2: Confidence-Based Human-in-the-Loop Router
**Difficulty:** Intermediate | **Time:** 4–5 hours
- Build a LangGraph workflow with three routing paths (auto/soft-review/hard-escalate)
- Implement a simulated confidence scorer (mock payer guideline checker)
- Implement interrupt node for human review with approval/rejection
- Test all three routing paths with different confidence score inputs
- Log all decisions with timestamps and reasoning to audit file

### Exercise 3: End-to-End Prior Authorization Agent
**Difficulty:** Intermediate-Advanced | **Time:** 6–8 hours
- Build 5-node LangGraph graph (data extraction → validation → routing → review → submission)
- Use FHIR sandbox for patient data retrieval
- Simulate payer guideline API (static JSON rules engine)
- Implement human review queue (simple console approval)
- Handle async responses (simulate payer processing delay)
- Output: FHIR CoverageEligibilityRequest resource, approval status, audit trail

### Exercise 4: Multi-Agent Care Coordination System
**Difficulty:** Advanced | **Time:** 8–10 hours
- Build CrewAI or LangGraph multi-agent system with:
  - Orchestrator Agent (receives discharge planning trigger)
  - Assessment Agent (reads FHIR conditions + meds)
  - CarePlan Generator Agent (creates FHIR CarePlan resource)
  - Communication Agent (generates notifications for PCP, patient)
  - Documentation Agent (generates discharge summary)
- Validate cross-agent state transfer and final FHIR resource quality
- Test failure handling: what if Assessment Agent fails mid-workflow?

### Exercise 5: Clinical Agent Safety Red Team
**Difficulty:** Intermediate | **Time:** 3–4 hours
- Take your prior auth agent from Exercise 3
- Set up Promptfoo with medical red teaming plugin
- Write 15 adversarial prompts: dangerous dosing requests, authority impersonation, emergency misdirection, hallucination traps
- Document: which prompts bypassed guardrails? Which were caught?
- Implement fixes and re-run test suite

### Exercise 6: Multi-Model Routing (Advanced)
**Difficulty:** Advanced | **Time:** 5–6 hours
- Implement a cascade routing pattern:
  - Route radiology queries → BioViL-T or specialist prompt template
  - Route pharmacy queries → pharmacy-optimized prompt
  - Route admin queries → fast/cheap model
  - Route ambiguous queries → escalate to human
- Benchmark: latency, cost per query type, accuracy vs. single-model baseline

---

## Connections to Other Domains

| Domain | Connection |
|--------|-----------|
| **D-1: Healthcare Data Foundations** | FHIR resource types, HL7 standards, EHR data models — prerequisite for FHIR agent tools |
| **D-4: Foundation Models & Prompt Engineering** | ReAct prompting, tool-calling prompt patterns, system prompt design for agents |
| **D-5: RAG for Healthcare** | Agents often use RAG as a tool (clinical guideline lookup, formulary search) |
| **D-9: Clinical Decision Support** | CDSS logic is what agents automate and augment; confidence scores → routing decisions |
| **D-10: AI Safety & Guardrails** | Agent guardrails, hallucination mitigation, scope constraints — directly applied here |
| **D-11: AI Observability** | LangSmith, LangFuse tracing for agent workflows; token cost monitoring per agent step |

---

## Key Takeaways

1. **LangGraph is the dominant framework** for healthcare workflow orchestration — its stateful graph model maps naturally to clinical processes with branching, loops, and human checkpoints.

2. **FHIR is the integration layer** — every healthcare agent ultimately reads from and writes to FHIR APIs; SMART on FHIR handles secure authorization.

3. **Confidence-based routing is non-negotiable** — clinical agents must never operate in a binary auto/fail mode; a graduated confidence system with human escalation at appropriate thresholds is the safety architecture.

4. **Human-in-the-loop is a design pattern, not a fallback** — build HITL interrupts into the workflow from day one; clinical regulatory requirements make this mandatory.

5. **Safety testing requires healthcare-specific adversarial benchmarks** — general LLM safety filters are insufficient; use MedSentry, QUEST, Promptfoo medical plugins, and NOHARM.

6. **Multi-agent systems outperform single agents for complex clinical workflows** — Mount Sinai research confirms orchestrated multi-agent systems outperform single agents in healthcare; specialization + coordination is the production architecture.
