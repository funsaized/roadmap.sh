# HL7v2 Interfaces and Integration Engines

## Overview

HL7 Version 2 (HL7v2) is the most widely deployed healthcare messaging standard in the world, used by 95% of U.S. healthcare organizations and adopted in over 35 countries. It defines a pipe-delimited, segment-based message format for exchanging clinical and administrative data between systems in real time. Despite the emergence of FHIR, HL7v2 remains the backbone of hospital integrations — particularly for ADT feeds, lab results, orders, scheduling, and document management.

This domain covers the HL7v2 message structure, the most common message types used in Epic integrations (ADT, ORM, ORU, SIU, MDM), the MLLP transport protocol, ACK/NAK acknowledgment patterns, and the integration engines that route and transform these messages.

---

## Key Concepts

### 1. HL7v2 Message Structure

HL7v2 messages are human-readable ASCII text with a hierarchical structure:

- **Message**: The complete unit of data exchange, composed of one or more segments
- **Segment**: A logical grouping of related fields, identified by a 3-character code (e.g., MSH, PID, PV1). Segments are separated by carriage returns (`\r`)
- **Field**: Data elements within a segment, separated by pipe characters (`|`)
- **Component**: Sub-parts of a field, separated by carets (`^`)
- **Sub-component**: Further subdivisions, separated by ampersands (`&`)
- **Repetition separator**: Tilde (`~`) separates repeating fields

**Example ADT^A01 Message:**
```
MSH|^~\&|EPIC|EPICADT|iFW|SMSADT|199912271408|CHARRIS|ADT^A04|1817457|D|2.5|
PID||0493575^^^2^ID 1|454721||DOE^JOHN^^^^|DOE^JOHN^^^^|19480203|M||B|254 MYSTREET AVE^^MYTOWN^OH^44123^USA||(216)123-4567|||M|NON|400003403~1129086|
PV1||O|168~219~C~PMA^^^^^^^^^||||277^ALLEN MYLASTNAME^BONNIE^^^^|||||||||||2688684|||||||||||||||||||||||||199912271408||||||002376853
```

### 2. Critical Segments

| Segment | Name | Purpose |
|---------|------|---------|
| **MSH** | Message Header | Mandatory first segment. Defines sender, receiver, message type (MSH-9), control ID (MSH-10), processing mode (MSH-11), HL7 version (MSH-12), and delimiter characters (MSH-1, MSH-2) |
| **PID** | Patient Identification | Patient demographics: name (PID-5), DOB (PID-7), sex (PID-8), address (PID-11), MRN (PID-3), account number (PID-18) |
| **PV1** | Patient Visit | Visit-specific data: patient class (PV1-2), location (PV1-3), attending doctor (PV1-7), admit date (PV1-44), discharge date (PV1-45) |
| **ORC** | Common Order | Order control information: order number, placer/filler IDs, order status |
| **OBR** | Observation Request | Details of the ordered observation/test: universal service ID, requested date, result status |
| **OBX** | Observation Result | Individual result values: observation ID, value type, actual value, units, reference range, abnormal flags |
| **SCH** | Schedule Activity | Scheduling details: appointment ID, event reason, timing, duration |
| **TXA** | Transcription Document Header | Document metadata: document type, activity date, unique document number, completion status |
| **IN1** | Insurance | Primary insurance information |
| **DG1** | Diagnosis | Diagnosis codes and descriptions |
| **NK1** | Next of Kin | Emergency contact and next-of-kin information |
| **AL1** | Allergy | Patient allergy information |
| **EVN** | Event Type | Trigger event details and timing |
| **MSA** | Message Acknowledgment | ACK status (AA/AE/AR) and reference to original message control ID |
| **ERR** | Error | Detailed error information in acknowledgment messages |

### 3. Common Message Types

#### ADT — Admission, Discharge, Transfer
The highest-volume message type in most hospitals. Communicates patient movement and administrative status changes.

| Trigger | Event |
|---------|-------|
| ADT^A01 | Patient Admit |
| ADT^A02 | Patient Transfer |
| ADT^A03 | Patient Discharge |
| ADT^A04 | Patient Registration |
| ADT^A05 | Pre-Admit |
| ADT^A08 | Update Patient Information |
| ADT^A11 | Cancel Admit |
| ADT^A12 | Cancel Transfer |
| ADT^A13 | Cancel Discharge |
| ADT^A28 | Add Person Information |
| ADT^A31 | Update Person Information |
| ADT^A40 | Merge Patient |

#### ORM — Order Message
Transmits orders for lab tests, radiology procedures, medications, and other services.

| Trigger | Event |
|---------|-------|
| ORM^O01 | General Order (new, modify, cancel) |

Key segments: MSH, PID, PV1, ORC (order control), OBR (observation request)

#### ORU — Observation Result (Unsolicited)
Transmits clinical results — lab values, radiology reports, vital signs, EKG data.

| Trigger | Event |
|---------|-------|
| ORU^R01 | Unsolicited Observation Result |

Key segments: MSH, PID, PV1, OBR, OBX (one per result value)

#### SIU — Scheduling Information Unsolicited
Communicates appointment scheduling events.

| Trigger | Event |
|---------|-------|
| SIU^S12 | New Appointment Booking |
| SIU^S13 | Appointment Rescheduling |
| SIU^S14 | Appointment Modification |
| SIU^S15 | Appointment Cancellation |
| SIU^S17 | Appointment Deletion |
| SIU^S26 | Notification of Patient No-Show |

Key segments: MSH, SCH, PID, PV1, AIS (appointment information), AIG (general resource), AIL (location resource)

#### MDM — Medical Document Management
Notifies of new or updated clinical documents (discharge summaries, notes, reports).

| Trigger | Event |
|---------|-------|
| MDM^T01 | Original Document Notification |
| MDM^T02 | Original Document Notification with Content |
| MDM^T03 | Document Status Change Notification |
| MDM^T07 | Document Edit Notification |
| MDM^T11 | Document Cancel Notification |

Key segments: MSH, PID, PV1, TXA (document header), OBX (document content, often base64-encoded PDF/RTF)

### 4. MLLP — Minimal Lower Layer Protocol

MLLP is the standard transport protocol for HL7v2 messages over TCP/IP connections. It wraps each message with framing characters:

```
<SB> = Start Block (0x0B, vertical tab)
<EB> = End Block (0x1C, file separator)
<CR> = Carriage Return (0x0D)

Transmission format: <SB>HL7 Message<EB><CR>
```

**Key characteristics:**
- Synchronous, connection-oriented protocol over TCP
- Single message per frame
- Sender waits for ACK before sending next message
- No built-in encryption (TLS wrapper commonly added)
- Default port is often 2575 (but configurable)
- Persistent connections are typical; some implementations use per-message connections

### 5. ACK/NAK Acknowledgment Patterns

HL7v2 uses two acknowledgment modes:

#### Original Mode (most common)
1. Sender transmits message via MLLP
2. Receiver validates and processes message
3. Receiver returns ACK message with MSA segment

**MSA-1 Acknowledgment Codes:**
| Code | Meaning | Action |
|------|---------|--------|
| **AA** | Application Accept | Message processed successfully; sender can discard |
| **AE** | Application Error | Processing error; sender should investigate and may resend after correction |
| **AR** | Application Reject | Message rejected (invalid structure, unsupported type); sender must fix before resending |

#### Enhanced Mode
Separates commit acknowledgment (message received and stored) from application acknowledgment (message processed):
- **CA** / **CE** / **CR** — Commit Accept / Error / Reject
- Allows asynchronous processing after initial commit

**ACK message structure:**
```
MSH|^~\&|RECEIVING_APP|RECEIVING_FAC|SENDING_APP|SENDING_FAC|20240101120000||ACK^A01|ACK12345|P|2.5|
MSA|AA|1817457|
```

**Error handling patterns:**
- Retry with exponential backoff on AE
- Dead-letter queue for persistent AR failures
- Timeout handling when no ACK received (typically 30-60 seconds)
- Logging all failed messages for manual review

### 6. Integration Engines

Integration engines (also called interface engines) are middleware platforms that receive, transform, route, and monitor HL7v2 messages between systems.

#### Mirth Connect / NextGen Connect
- **Type**: Open-source (versions < 4.6 under Mozilla Public License 2.0; v4.6+ commercial)
- **Architecture**: Channel-based — each channel defines source connector, filters, transformers, and destination connectors
- **Key features**: JavaScript scripting, HL7-to-XML transformation, message viewer/debugger, database connectors, REST/SOAP support
- **Supported standards**: HL7v2, HL7v3, FHIR, CDA, DICOM, X12, custom formats
- **GitHub**: [nextgenhealthcare/connect](https://github.com/nextgenhealthcare/connect)
- **Best for**: Small-to-medium organizations, development/testing environments, organizations with technical staff

#### Rhapsody Integration Engine
- **Type**: Commercial (by Rhapsody Health)
- **Key features**: Graphical IDE with drag-and-drop, AI-powered integration assistant (Axon), high throughput, comprehensive protocol support
- **Supported standards**: HL7v2, FHIR, EDIFACT, NCPDP, X12, custom formats
- **Deployment**: On-premises or cloud (Rhapsody-as-a-Service / RaaS)
- **Best for**: Large enterprises, public health, high-volume production environments

#### InterSystems Health Connect
- **Type**: Commercial (by InterSystems)
- **Key features**: Built on IRIS data platform, deep FHIR support, ensemble-based routing, cloud-native
- **Supported standards**: HL7v2, FHIR, IHE profiles, CDA
- **Deployment**: On-premises, cloud, or managed service
- **Best for**: Large health systems, complex multi-facility environments

#### Epic Bridges
- **Type**: Proprietary (Epic Systems)
- **Key features**: Native to Epic EHR, handles inbound/outbound HL7v2 interfaces, Space Bridge tool for message transformations
- **Documentation**: [open.epic.com/Interface/HL7v2](https://open.epic.com/Interface/HL7v2) (public specs), Epic UserWeb (restricted, detailed guides)
- **Best for**: Organizations running Epic EHR

### 7. HL7v2 Parsing Libraries

| Library | Language | License | URL |
|---------|----------|---------|-----|
| **HAPI HL7v2** | Java | Open Source | [hapifhir.github.io/hapi-hl7v2](https://hapifhir.github.io/hapi-hl7v2/) |
| **python-hl7** | Python | Open Source | [github.com/johnpaulett/python-hl7](https://github.com/johnpaulett/python-hl7) |
| **nHapi** | .NET/C# | Open Source | [github.com/nHapiNET/nHapi](https://github.com/nHapiNET/nHapi) |
| **node-hl7-complete** | Node.js | Open Source | [github.com/MatthewVita/node-hl7-complete](https://github.com/MatthewVita/node-hl7-complete) |
| **Simple-HL7v2** | Java | Open Source | [github.com/jessepav/simple-hl7v2](https://github.com/jessepav/simple-hl7v2) |

### 8. Z-Segments (Custom Segments)

HL7v2 allows custom segments prefixed with "Z" (e.g., ZPD, ZPI) for organization-specific data not covered by the standard. These are common in Epic integrations and must be documented in interface specifications. They require agreement between sending and receiving systems.

### 9. Message Profiles and Conformance

- **Conformance profiles** define which segments, fields, and values are required, optional, or not used for a specific interface
- HL7v2 is highly flexible — the same message type can vary significantly between implementations
- Epic publishes interface specifications that serve as conformance profiles for each integration point
- Testing tools validate messages against these profiles

---

## Learning Resources

### Online Courses

1. **HL7 Fundamentals Course** (HL7 International)
   - URL: [https://www.hl7fundamentals.org/](https://www.hl7fundamentals.org/)
   - Format: 12-week asynchronous, instructor-led online workshop
   - Covers: V2, CDA, FHIR through guided exercises
   - Cost: Paid (member/non-member pricing)
   - Difficulty: Beginner to Intermediate

2. **Core Essentials Live: HL7 v2 Interface Protocol — The Basics** (SIIM)
   - URL: [https://siim.org/learning/hl7-v2-interface-protocol/](https://siim.org/learning/hl7-v2-interface-protocol/)
   - Format: Virtual-live, 3 modules
   - Covers: Versioning, compatibility, message structure, segments, trigger events
   - Cost: Paid
   - Difficulty: Beginner

3. **Curizent HL7 V2.x Training**
   - URL: [https://curizent.com/product/hl7-v2/](https://curizent.com/product/hl7-v2/)
   - Format: Classroom (6 days) or online (5 weeks)
   - Covers: Basic to advanced V2.x, conformance profiles, prepares for HL7 V2.8 certification
   - Cost: Paid
   - Difficulty: Beginner to Advanced

### Video Tutorials

4. **HL7 v2.x: The Developer's Complete Guide** (TechVariable, YouTube)
   - URL: [https://www.youtube.com/watch?v=xm5bZsmax1U](https://www.youtube.com/watch?v=xm5bZsmax1U)
   - Covers: Message structure, parsing logic, MSH/ADT/ORM/ORU messages, delimiters, best practices
   - Cost: Free
   - Difficulty: Beginner to Intermediate

5. **Integrating with Epic using HL7 v2** (6B Health, YouTube)
   - URL: [https://www.youtube.com/watch?v=djcqKxehxf0](https://www.youtube.com/watch?v=djcqKxehxf0)
   - Covers: Epic-specific HL7v2 integration patterns
   - Cost: Free
   - Difficulty: Intermediate

### Documentation and References

6. **Epic Open HL7v2 Interface Specifications**
   - URL: [https://open.epic.com/Interface/HL7v2](https://open.epic.com/Interface/HL7v2)
   - Covers: Incoming and outgoing HL7v2 interface specs for Epic (ADT, orders, results, scheduling, documents)
   - Cost: Free
   - Difficulty: Intermediate to Advanced

7. **HL7 V2 Official Specification** (HL7.org)
   - URL: [https://www.hl7.eu/HL7v2x/v24/std24/ch02.htm](https://www.hl7.eu/HL7v2x/v24/std24/ch02.htm)
   - Covers: Detailed specification of message components, data types, processing rules
   - Cost: Free (mirrored)
   - Difficulty: Advanced

8. **Caristix HL7v2 Segment/Message Reference**
   - URL: [https://hl7-definition.caristix.com/v2/HL7v2.7/Segments](https://hl7-definition.caristix.com/v2/HL7v2.7/Segments)
   - Covers: Browsable reference for all HL7v2 segments, fields, data types across versions
   - Cost: Free
   - Difficulty: All levels

9. **Interfaceware HL7 Tutorials and Guides**
   - URL: [https://www.interfaceware.com/hl7-message-structure](https://www.interfaceware.com/hl7-message-structure)
   - Covers: Message structure, ADT, ORM, ORU, SIU, MDM, ACK — individual guides for each
   - Cost: Free
   - Difficulty: Beginner to Intermediate

10. **Integration Soup — Free HL7 Tutorials**
    - URL: [https://www.integrationsoup.com/hl7tutorials.html](https://www.integrationsoup.com/hl7tutorials.html)
    - Covers: HL7 basics, message structure, MSH segment, Mirth Connect relay tutorials
    - Cost: Free
    - Difficulty: Beginner

11. **NIH Health Data Standards Tutorial — HL7 Version 2**
    - URL: [https://www.nlm.nih.gov/oet/ed/healthdatastandards/03-300.html](https://www.nlm.nih.gov/oet/ed/healthdatastandards/03-300.html)
    - Covers: Overview of V2 as an exchange standard, common message types, message profiles
    - Cost: Free
    - Difficulty: Beginner

### Books

12. **"Health Information Exchange: Navigating and Managing a Network of Health Information Systems"** by Brian Dixon, Charles Jajeh
    - Covers HL7v2, integration engines, and practical implementation patterns
    - Difficulty: Intermediate

### Open-Source Projects and Repos

13. **HAPI HL7v2 (Java Parser)**
    - URL: [https://hapifhir.github.io/hapi-hl7v2/](https://hapifhir.github.io/hapi-hl7v2/)
    - Includes TestPanel tool for editing/sending/validating HL7v2 messages
    - Difficulty: Intermediate

14. **NextGen Connect (Mirth Connect) — GitHub**
    - URL: [https://github.com/nextgenhealthcare/connect](https://github.com/nextgenhealthcare/connect)
    - Open-source integration engine (pre-4.6 versions), with examples at [connect-examples](https://github.com/nextgenhealthcare/connect-examples)
    - Difficulty: Intermediate

15. **Smile Digital Health — HL7 V2 Walkthrough**
    - URL: [https://www.smiledigitalhealth.com/hl7-v2-walkthrough](https://www.smiledigitalhealth.com/hl7-v2-walkthrough)
    - Covers: Ingesting V2 messages and mapping to FHIR bundles
    - Difficulty: Intermediate to Advanced

### Community Resources

16. **Mirth Connect Community Forum / GitHub Discussions**
    - URL: [https://github.com/nextgenhealthcare/connect/discussions](https://github.com/nextgenhealthcare/connect/discussions)
    - Active community for integration engine questions

17. **r/healthIT** (Reddit)
    - URL: [https://www.reddit.com/r/healthIT/](https://www.reddit.com/r/healthIT/)
    - Discussions on integration engines, HL7, and healthcare IT

---

## Learning Path

### Phase 1: HL7v2 Message Fundamentals (Week 1–2)
**Goal:** Understand the HL7v2 message format and be able to read/parse any message by hand.

1. Start with Integration Soup free tutorials for basic concepts
2. Study the MSH segment in depth — understand every field
3. Learn PID and PV1 segments thoroughly
4. Practice reading real HL7v2 messages using the Caristix reference
5. Complete the NIH Health Data Standards tutorial on V2

**Milestone:** Given a raw HL7v2 message, identify the message type, patient, visit, and all segment boundaries.

### Phase 2: Message Types Deep Dive (Week 2–3)
**Goal:** Understand the five core message types and their trigger events.

1. Study ADT messages and all major trigger events (A01–A40)
2. Study ORM/ORU for the order-result workflow
3. Study SIU for scheduling workflows
4. Study MDM for document management
5. Use Interfaceware guides for each message type
6. Watch the TechVariable YouTube tutorial

**Milestone:** Construct valid sample messages for each of the five types by hand.

### Phase 3: Transport and Acknowledgment (Week 3–4)
**Goal:** Understand MLLP framing and ACK/NAK patterns.

1. Learn MLLP framing characters and TCP connection patterns
2. Study original vs. enhanced acknowledgment modes
3. Understand AA/AE/AR codes and error handling
4. Learn retry patterns, dead-letter queues, and timeout handling
5. Practice with HAPI TestPanel — send messages and observe ACK responses

**Milestone:** Set up a local MLLP listener, send a test message, and receive an ACK.

### Phase 4: Integration Engines (Week 4–6)
**Goal:** Set up and configure an integration engine to route HL7v2 messages.

1. Install Mirth Connect (NextGen Connect) locally
2. Create a channel: TCP Listener source → File Writer destination
3. Add message transformations (field mapping, segment manipulation)
4. Add message filtering (route by message type)
5. Configure error handling and retry logic
6. Study Epic Bridges documentation on open.epic.com
7. Explore Rhapsody and InterSystems documentation for comparison

**Milestone:** Build a multi-channel Mirth setup that receives ADT messages, transforms them, and routes to different destinations based on trigger event.

### Phase 5: Epic-Specific Integration (Week 6–7)
**Goal:** Understand how HL7v2 interfaces work specifically with Epic.

1. Review Epic's public HL7v2 interface specifications on open.epic.com
2. Study Epic Bridges architecture and Space Bridge transformations
3. Understand Epic's inbound vs. outbound interface categories
4. Learn about Z-segments commonly used in Epic implementations
5. Study the V2-to-FHIR transformation pathway (Smile Digital Health walkthrough)

**Milestone:** Design an interface specification for a hypothetical Epic integration (e.g., outbound ADT feed to an external analytics system).

---

## Practical Exercises

### Exercise 1: Parse HL7v2 Messages by Hand
Take 5 sample HL7v2 messages (ADT, ORM, ORU, SIU, MDM) and manually identify:
- Message type and trigger event
- Patient name, MRN, DOB
- Every segment and its purpose
- All components and sub-components in complex fields

### Exercise 2: Build an HL7v2 Parser
Using HAPI (Java), python-hl7 (Python), or nHapi (.NET):
- Parse a sample ADT^A01 message
- Extract patient demographics from PID
- Extract visit information from PV1
- Generate a valid ACK response
- Handle encoding/decoding of special characters

### Exercise 3: MLLP Communication
- Set up a TCP MLLP listener (using HAPI TestPanel or a simple socket server)
- Send HL7v2 messages with proper MLLP framing
- Implement ACK handling — return AA for valid messages, AE for processing errors, AR for invalid structure
- Test timeout and retry scenarios

### Exercise 4: Mirth Connect Integration Channel
- Install Mirth Connect locally
- Create an inbound channel that receives ADT messages via TCP/MLLP
- Add transformers to: extract patient name, map gender codes, add a timestamp
- Route to a file destination (write transformed XML)
- Add a second channel for ORU messages with different routing rules
- Monitor the dashboard for message flow and errors

### Exercise 5: Design an Epic Interface Specification
- Choose one Epic HL7v2 interface from open.epic.com
- Document: message flow direction, trigger events, required segments, field mappings
- Define custom Z-segments if needed
- Write sample messages and expected ACK responses
- Create an error handling matrix (what happens for each failure scenario)

### Exercise 6: V2-to-FHIR Mapping
- Take an ADT^A01 message and map it to FHIR resources:
  - MSH → MessageHeader
  - PID → Patient
  - PV1 → Encounter
- Document field-by-field mappings
- Implement the transformation using Smile CDR walkthrough or HAPI FHIR

---

## Connections to Other Domains

- **D-1 (Healthcare Interoperability Foundations)**: HL7v2 is the original interoperability standard; understanding its limitations motivates FHIR adoption
- **D-4 (FHIR R4)**: Many organizations are mapping V2 messages to FHIR resources; understanding both is essential for modern integrations
- **D-6 (SMART on FHIR)**: SMART apps may consume data that originates from V2 interfaces
- **D-3 (Terminology and Coding Systems)**: HL7v2 messages carry coded values (ICD, CPT, LOINC, SNOMED) in OBX, DG1, and other segments
- **D-2 (Regulatory Compliance)**: HIPAA security requirements apply to all HL7v2 message transport (encryption, access controls, audit logging)
