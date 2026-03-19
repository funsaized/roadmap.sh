# App Orchard Showroom and Epic Distribution

## Overview

Epic's marketplace for third-party applications has evolved from the original **App Orchard** (launched 2016) through the **App Market** to the current **Epic Showroom** (launched early 2024). The Showroom is the centralized platform where healthcare organizations discover, evaluate, and activate third-party tools that integrate with Epic's EHR system. Understanding the Showroom listing process, the tiered product structure, security requirements, and legal obligations is essential for any vendor building software that integrates with Epic.

This domain covers the full lifecycle of getting your application listed and distributed through Epic's ecosystem — from initial Vendor Services enrollment through Connection Hub listing, Toolbox designation, security review, SOC 2 compliance, ONC certification alignment, and ongoing operational expectations.

---

## Key Concepts

### 1. Evolution: App Orchard → App Market → Showroom
- **App Orchard** (2016–2022): Original marketplace for Epic-integrated third-party apps
- **Connection Hub** (2022): Launched as a transitional directory for vendors with live Epic connections
- **Epic Showroom** (2024): Current unified marketplace replacing all prior platforms
- The technical developer portal remains **open.epic** (open.epic.com), which is separate from the Showroom

### 2. Showroom Product Tiers
The Showroom organizes products into distinct tiers reflecting depth of integration:

| Tier | Description | Requirements |
|------|------------|-------------|
| **Cornerstone Partners** | Technologies integral to Epic software | Deep co-development partnership with Epic |
| **Workshop** | Products with integrations under active co-development with Epic | Direct collaboration with Epic engineering; moves to Toolbox when mature |
| **Toolbox** | Products following Epic's recommended integration practices (Blueprint) | Adherence to Blueprint recommended practices for the product category |
| **Toolbox Under Construction** | Products in categories where Blueprint practices are still being defined | Active integration development in an emerging category |
| **Connection Hub** | Any vendor with a live connection to at least one Epic customer site | $500/year annual fee; at least one live customer connection |

### 3. Connection Hub
- **Entry-level listing**: Any vendor with a live connection to at least one Epic customer can join
- **Annual fee**: $500/year
- **Self-reported**: Vendors provide their own product descriptions and website links
- **Not a prerequisite**: Listing is optional marketing — customers can connect to your app without a Connection Hub listing
- **Discovery tool**: Epic customers browse the Connection Hub to find solutions; vendor-supplied information only

### 4. Blueprint and Toolbox Designation
- **Blueprint**: Epic's set of recommended connection practices for specific product categories (e.g., ambient documentation, patient engagement, clinical surveillance)
- **Toolbox designation**: Achieved by products that fully adhere to Blueprint practices
- Toolbox apps receive higher visibility and credibility in the Showroom
- Epic regularly evaluates new categories and products for Toolbox eligibility
- Blueprint adherence covers: technical compatibility, workflow alignment, security standards, data accuracy, and clinical value

### 5. Vendor Services Program
- **Cost**: $1,900/year (separate from Connection Hub fee)
- **Includes**: Expanded API specifications, direct Epic technical rep support, design consultation, troubleshooting, installation assistance, expanded testing sandboxes, configurable test data
- **Not required to build or deploy**: open.epic provides free self-service tools sufficient for development and go-live
- **Recommended for**: Vendors seeking deeper integration support, faster troubleshooting, or Toolbox designation

### 6. open.epic Developer Platform
- Free, self-service online resource at open.epic.com
- Provides: public API documentation, sandbox environments, app registration, client ID generation
- Supports: FHIR R4 APIs, CDS Hooks, SMART on FHIR, HL7v2 specs
- Vendor-neutral: no special relationship with Epic required
- fhir.epic.com is a subset focused on FHIR API documentation

### 7. Client ID Lifecycle and Go-Live Process
1. **Register application** on open.epic → generates production and non-production client IDs
2. **Develop and test** using Epic sandbox environments
3. **License to customer** → share client IDs with the healthcare organization
4. **Customer requests activation** → client IDs synced to their specific Epic instance
5. **Developer enables keys** for non-production first, then production
6. **Go live** → client ID active in customer's production Epic environment
7. **Optional**: List in Connection Hub/Showroom for broader visibility

### 8. Security Review Requirements
Epic's security expectations for vendors include:
- **Encryption**: TLS 1.2+ for all data in transit; AES-128+ for data at rest
- **Authentication**: OAuth 2.0 with PKCE for all API access
- **HIPAA compliance**: Full adherence to HIPAA Privacy and Security Rules
- **Vulnerability management**: Documented policies for identifying, evaluating, responding to, and disclosing security vulnerabilities
- **Access controls**: Granular access via FHIR API scopes; unique user IDs; need-to-know basis
- **Incident response**: Policies for informing customers of security incidents and privacy breaches
- **Product security**: Conformance to recognized industry standards for safety, security, and privacy
- Epic's security team conducts deep technical reviews of how applications manage PHI

### 9. SOC 2 Compliance
- **Not explicitly mandated by Epic** as an enrollment prerequisite
- **De facto industry standard**: Most health systems require SOC 2 Type 2 from their vendors
- **SOC 2 Type 2** evaluates operational effectiveness of security controls over time (vs. Type 1 point-in-time)
- **Trust Services Criteria**: Security (mandatory), Availability, Processing Integrity, Confidentiality, Privacy
- **Practical requirement**: Individual Epic customers will demand SOC 2 during procurement; achieving it before listing dramatically improves sales velocity
- Comprehensive documentation required: security policies, access control records, system configurations, risk assessments, vendor risk management

### 10. ONC Health IT Certification
- Apps must meet specified **ONC certification criteria** or provide public documentation of equivalent functionality
- Key standard: **170.315(g)(10)** — Standardized API for Patient and Population Services
- Required data standard: **USCDI v3** (mandatory from January 1, 2026; currently alongside v1/v2)
- API standard: **HL7 FHIR R4** (Release 4.0)
- Epic or community members may review ONC compliance documentation
- Non-compliance can result in app notification to users or suspension
- **HTI-1 Final Rule** (effective February 2024): Updated certification requirements, decision support criteria
- **HTI-2 Proposed Rule** (July 2024): Proposes USCDI v4 baseline by 2028, expanded public health certification

### 11. Legal Agreements and Developer Terms
Key legal obligations for developers in the Epic ecosystem:
- **open.epic Developer Terms**: Govern use of APIs, sandboxes, and development tools
- **Indemnification**: Developers must indemnify and hold harmless Epic for all claims related to their products
- **Sole responsibility**: Developers bear full liability for their products — including patient harm, data corruption, privacy breaches
- **Trademark usage**: Must follow Epic's Trademark Usage Guidelines
- **Vendor Services enrollment criteria**: Legal compliance, no sanctions, no IP infringement, confidentiality agreements with staff
- **12-month interface commitment**: Must plan to complete an Epic interface within 12 months of enrollment
- **No deceptive statements**: Cannot make inaccurate claims about Epic or its products

### 12. Epic's Federated Model and Distribution Implications
- Each Epic customer runs an independent instance — there is no central Epic endpoint
- Connections must be established directly with individual healthcare organizations
- This means distribution is inherently one-customer-at-a-time (though the process is standardized)
- Showroom/Connection Hub provides discovery, but activation is always per-customer
- Scaling across multiple Epic sites requires operational discipline in managing multiple client ID activations

---

## Learning Resources

### Official Documentation and Portals

1. **open.epic Developer Resources**
   - URL: https://open.epic.com/DeveloperResources
   - Type: Documentation portal
   - Description: Primary hub for all Epic developer documentation, API specs, sandbox access, and app registration. Starting point for any integration effort.
   - Cost: Free

2. **Epic Vendor Services FAQ**
   - URL: https://vendorservices.epic.com/FAQ/Index
   - Type: FAQ / Documentation
   - Description: Comprehensive FAQ covering enrollment criteria, supported standards, development tools, testing environments, and how to engage with Epic. Essential reading before starting the listing process.
   - Cost: Free to read; Vendor Services enrollment is $1,900/year

3. **Epic Showroom**
   - URL: https://showroom.epic.com
   - Type: Marketplace / Directory
   - Description: The live marketplace itself. Browse existing listings to understand how products are presented, which tiers they occupy, and what Blueprint categories exist.
   - Cost: Free to browse

4. **open.epic Developer Terms**
   - URL: https://open.epic.com/Home/DeveloperTerms
   - Type: Legal documentation
   - Description: The binding terms all developers agree to when using open.epic. Must-read for understanding liability, indemnification, and ONC certification obligations.
   - Cost: Free

5. **Epic FHIR Documentation**
   - URL: https://fhir.epic.com
   - Type: Technical documentation
   - Description: Detailed documentation on Epic's FHIR API support, including OAuth2 flows, client ID management, and sandbox testing.
   - Cost: Free

### Industry Analysis and Guides

6. **Fierce Healthcare: Epic Launches New Showroom Website**
   - URL: https://www.fiercehealthcare.com/health-tech/epic-launches-new-showroom-website-3rd-party-apps-services
   - Type: Industry news article
   - Description: Journalistic analysis of the Showroom launch, tier structure, and implications for vendors. Good for understanding the strategic context.
   - Cost: Free

7. **AHA: Epic Revamps App Market with Connection Hub**
   - URL: https://www.aha.org/aha-center-health-innovation-market-scan/2022-12-20-epic-revamp-its-app-market-connection-hub
   - Type: Industry analysis
   - Description: American Hospital Association's analysis of the Connection Hub transition. Provides the health system buyer's perspective on Epic's marketplace changes.
   - Cost: Free

8. **Lifebit: Epic App Store Integration Guide**
   - URL: https://lifebit.ai/blog/epic-app-store-integration/
   - Type: Blog / Practitioner guide
   - Description: Detailed vendor perspective on integrating with Epic's marketplace, covering security review, listing process, and practical lessons learned.
   - Cost: Free

### Compliance and Certification Resources

9. **ONC Health IT Certification Program — Cures Act Final Rule**
   - URL: https://healthit.gov/regulations/cures-act-final-rule/
   - Type: Government regulatory documentation
   - Description: The foundational regulation governing health IT certification, information blocking, and API requirements. Essential for understanding ONC certification obligations.
   - Cost: Free

10. **AICPA SOC 2 Overview**
    - URL: https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
    - Type: Professional standards documentation
    - Description: Official AICPA resource on SOC 2 framework, Trust Services Criteria, and audit requirements. Essential for planning your SOC 2 compliance journey.
    - Cost: Free

### Video and Multimedia

11. **Epic UserWeb and UGM Presentations** (requires Epic UserWeb access)
    - URL: https://userweb.epic.com
    - Type: Conference presentations / Video
    - Description: Epic's annual User Group Meeting (UGM) presentations include sessions on Showroom, vendor integration best practices, and new API capabilities. Access requires Epic customer or vendor credentials.
    - Cost: Requires UserWeb access (available to Vendor Services members)

12. **CHIME/HIMSS Conference Sessions on Epic Integration**
    - Type: Conference talks / Video
    - Description: Annual healthcare IT conferences feature sessions on Epic marketplace strategy, vendor integration experiences, and interoperability best practices.
    - Cost: Conference registration required; some recordings available online

---

## Learning Path

### Phase 1: Understand the Landscape (3–5 hours)
1. **Browse the Epic Showroom** — Visit showroom.epic.com and explore existing listings across all tiers. Note how products are categorized and presented.
2. **Read the Vendor Services FAQ** — Understand enrollment criteria, supported standards, and the distinction between open.epic (free) and Vendor Services (paid).
3. **Read the Fierce Healthcare and AHA articles** — Get the industry context for why Epic restructured its marketplace.

### Phase 2: Developer Platform and Legal Framework (4–6 hours)
4. **Study open.epic Developer Terms** — Understand your legal obligations, indemnification clauses, and ONC certification requirements.
5. **Walk through the Client ID tutorial** — Register a test application on open.epic and understand the client ID lifecycle.
6. **Review Epic's data sharing playbooks** — Understand the security, privacy, and data integrity expectations before designing your integration.

### Phase 3: Security and Compliance Preparation (8–12 hours)
7. **Map Epic's security requirements** — Document how your application meets each requirement (TLS 1.2+, OAuth 2.0 PKCE, encryption at rest, vulnerability management).
8. **Begin SOC 2 preparation** — Even if Epic doesn't mandate it, your customers will. Understand the Trust Services Criteria and begin documenting your security controls.
9. **Assess ONC certification** — Determine which 170.315 criteria apply to your application. Prepare public documentation of compliance or equivalence.

### Phase 4: Listing and Distribution (4–6 hours)
10. **Evaluate Vendor Services enrollment** — Decide whether the $1,900/year is worth it for your use case (expanded sandbox, direct support, Toolbox path).
11. **Prepare Connection Hub listing** — Draft your product description, screenshots, and marketing materials for the $500/year listing.
12. **Plan multi-customer scaling** — Design your operational process for managing client ID activations across multiple Epic sites.

### Phase 5: Advanced — Toolbox and Workshop (Ongoing)
13. **Understand Blueprint for your category** — If a Blueprint exists for your product category, study the recommended practices and align your integration.
14. **Engage with Epic for Toolbox designation** — Work with your Vendor Services rep to get evaluated for Toolbox status.
15. **Explore Workshop co-development** — If your product pushes beyond current standards, explore direct co-development with Epic engineering.

**Total estimated time: 20–30 hours** (excluding SOC 2 audit, which is a multi-month organizational effort)

---

## Practical Exercises

### Exercise 1: Showroom Competitive Analysis
- Browse showroom.epic.com and identify 5 products in your target category
- Document their tier (Connection Hub vs. Toolbox), listed integrations, and positioning
- Analyze what differentiates Toolbox-tier products from Connection Hub listings
- **Deliverable**: Competitive landscape document with positioning strategy for your product

### Exercise 2: Client ID Registration and Sandbox Testing
- Register a new application on open.epic.com
- Obtain production and non-production client IDs
- Execute API calls against the Epic sandbox using your client ID
- Test the OAuth 2.0 PKCE flow end-to-end
- **Deliverable**: Working sandbox integration with documented client ID lifecycle

### Exercise 3: Security Compliance Gap Analysis
- Create a compliance matrix mapping Epic's security requirements to your current controls
- Identify gaps in: encryption, authentication, vulnerability management, incident response
- Draft a remediation plan with timelines for each gap
- **Deliverable**: Security compliance matrix and remediation roadmap

### Exercise 4: SOC 2 Readiness Assessment
- Map the five Trust Services Criteria to your organization's current practices
- Identify which criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy) are relevant to your Epic integration
- Document existing controls and identify gaps
- Create a SOC 2 preparation timeline
- **Deliverable**: SOC 2 readiness assessment with gap analysis

### Exercise 5: Mock Connection Hub Listing
- Draft a complete Connection Hub listing: product description, integration summary, target audience, screenshots
- Review Epic's listing guidelines and formatting requirements
- Get feedback from clinical stakeholders on whether the listing resonates
- **Deliverable**: Publication-ready Connection Hub listing draft

### Exercise 6: Multi-Customer Activation Simulation
- Design a process for onboarding a new Epic customer: from initial contact through client ID activation to production go-live
- Document the steps, responsible parties, and expected timelines
- Create templates for: customer onboarding checklist, client ID request form, go-live verification
- **Deliverable**: Customer activation playbook with templates

---

## Connections to Other Domains

- **D-5 (OAuth 2.0 / Epic Auth)**: Client ID management and OAuth 2.0 PKCE flows are the technical foundation for Showroom-listed applications
- **D-6 (SMART on FHIR)**: Most Showroom applications use SMART on FHIR as their primary integration pattern
- **D-4 (FHIR R4)**: FHIR APIs are the primary data exchange mechanism for Showroom applications; ONC certification requires FHIR R4
- **D-2 (Regulatory Compliance)**: HIPAA, ONC certification, and information blocking rules directly govern what's required for Showroom listing
- **D-11 (Clinical Workflow Embedding)**: Toolbox-tier applications typically embed into clinical workflows using patterns covered in D-11
- **D-9 (Epic Interconnect / MyChart)**: Proprietary APIs available through Vendor Services complement the FHIR APIs used by Showroom applications
