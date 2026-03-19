# Multi-Tenant Operations and Go-Live

## Overview

When integrating third-party software with the Epic Electronic Health Record (EHR) system, understanding multi-tenant architecture, configuration variability across organizations, version management, go-live processes, and IT governance is essential. Epic deployments vary significantly between organizations — each instance is uniquely configured, upgraded on different schedules, and governed by distinct policies. A software vendor or integration developer must design applications that gracefully handle this variability while meeting the rigorous requirements of healthcare go-live events.

This domain covers the operational reality of deploying and maintaining integrations across multiple Epic customers, each with their own instance, configuration, and governance structure.

---

## Key Concepts

### 1. Multi-Tenant Architecture in Healthcare

**Definition:** Multi-tenancy refers to a single software instance serving multiple customers (tenants), each with isolated data and potentially different configurations. In the Epic ecosystem, multi-tenancy operates at two levels:

- **Epic's own multi-tenant models:** Epic Community Connect (host health system extends its instance to affiliates) and Epic Garden Plot (Epic-hosted SaaS for independent groups).
- **Your application's multi-tenancy:** Third-party apps listed on Epic's Showroom typically serve many health systems, each representing a tenant with its own Epic instance, FHIR endpoints, and configuration.

**Key architectural decisions:**
- **Data isolation models:** Separate databases per tenant (strongest isolation), shared database with separate schemas, or shared schema with tenant ID filtering
- **Configuration isolation:** Each tenant may require different FHIR endpoint URLs, OAuth client credentials, custom mappings, and feature flags
- **Tenant identification:** URL-based routing, JWT claims with tenant context, or header-based tenant resolution

### 2. Epic Community Connect

A deployment model where a large health system (the "host") extends its Epic environment to smaller affiliated organizations ("tenants"). The host manages infrastructure, interfaces, support, and governance. Community Connect partners share the same Epic instance but operate with separate user groups, workflows, and access controls.

**Implications for integrators:**
- Multiple organizations may share the same FHIR base URL but have different organizational contexts
- Data access permissions vary by partner organization
- The host system controls integration approvals and governance

### 3. Epic Garden Plot

Launched in 2022, Garden Plot is Epic's SaaS offering for independent medical groups (typically 40+ providers). Epic handles hosting, configuration, updates, and support directly.

**Implications for integrators:**
- Epic controls the update schedule — your app must stay current
- Standardized configuration reduces variability but also limits customization
- Integration approval goes through Epic rather than individual health systems

### 4. Configuration Variability Across Epic Instances

Each Epic deployment is uniquely configured based on the organization's decisions about:

- **Modules activated:** EpicCare Ambulatory, Inpatient, ASAP (ED), OpTime (Surgery), Beaker (Lab), MyChart, Resolute (Billing), etc.
- **Custom build:** Order sets, clinical decision support rules, documentation templates, preference lists
- **FHIR R4 resources enabled:** Not all organizations enable the same FHIR resources or support the same search parameters
- **Terminology and coding:** Organizations may use different code systems, value sets, or local codes
- **Security configuration:** OAuth scopes, token lifetimes, IP allowlisting, and mutual TLS requirements vary

**Practical impact:** Your integration cannot assume uniform behavior. You must:
- Discover capabilities dynamically (FHIR CapabilityStatement)
- Handle missing or differently-structured data gracefully
- Maintain per-tenant configuration for endpoint URLs, credentials, feature toggles, and field mappings

### 5. Epic Version Differences and Upgrade Cadence

Epic releases updates on a quarterly schedule, with larger version upgrades periodically. Each organization chooses when to apply updates, creating version fragmentation across your customer base.

**Key considerations:**
- **API behavior changes:** New FHIR resources, modified search parameters, or deprecated endpoints may appear with upgrades
- **Breaking changes:** Quarterly releases can alter data formats, validation rules, or authentication flows
- **Version detection:** Use the FHIR CapabilityStatement and metadata endpoints to detect the Epic version and available features
- **Backward compatibility:** Design your integration to support at least 2–3 prior versions simultaneously
- **Upgrade coordination:** Communicate with customers before their Epic upgrades to verify integration compatibility

### 6. Go-Live Process

A go-live is the critical moment when an Epic system (or a new integration) transitions from testing to production use. For third-party integrations, go-live involves:

**Pre-Go-Live (4–8 weeks before):**
- Complete integration testing in the customer's non-production Epic environment
- Validate data flows end-to-end: FHIR reads, writes, webhooks, and subscriptions
- Conduct user acceptance testing (UAT) with clinical end-users
- Perform load testing to verify performance under realistic conditions
- Complete security review and HIPAA compliance validation
- Develop a go-live playbook: workflows, rollback procedures, escalation paths, communication plans

**Go-Live Event (typically a weekend or holiday):**
- Cutover from test to production credentials and endpoints
- Execute smoke tests on production data
- Staff a command center with integration engineers, clinical informaticists, and vendor support
- Provide "at-the-elbow" (ATE) support for clinical users
- Monitor real-time dashboards for error rates, latency, and data integrity

**Post-Go-Live (2–6 weeks after):**
- Stabilization period with enhanced monitoring and rapid response
- Track adoption metrics, error rates, and user satisfaction
- Address workflow gaps and unexpected edge cases
- Transition from go-live support mode to steady-state operations
- Conduct lessons-learned retrospective

### 7. Go-Live Stakeholders

Successful integration go-lives require coordination across multiple stakeholder groups:

| Stakeholder | Role |
|---|---|
| **Executive Sponsor** | Secures budget, removes organizational barriers, champions the project |
| **Chief Medical Informatics Officer (CMIO)** | Bridges clinical practice and IT; validates clinical workflows; drives physician adoption |
| **Chief Nursing Informatics Officer (CNIO)** | Ensures nursing workflows are supported; trains nursing staff; validates documentation flows |
| **Epic Project Manager** | Coordinates timelines, manages dependencies, runs the command center |
| **Epic Application Analysts** | Configure Epic to support the integration (e.g., enabling FHIR resources, creating interface records) |
| **Integration/Interface Analysts** | Manage data flows between Epic and external systems; configure integration engines |
| **IT Security Team** | Reviews security posture, manages credentials, validates HIPAA compliance |
| **Clinical Champions/Super Users** | Departmental experts who provide frontline support and feedback |
| **Third-Party Vendor Team** | The integration developer team — provides technical support, monitoring, and issue resolution |
| **Revenue Cycle Specialists** | Validate billing and financial data flows if the integration affects charges or claims |
| **Change Management Lead** | Plans communication, manages resistance, promotes adoption |

### 8. Integration Testing Strategy

A comprehensive testing strategy for Epic integrations should include:

**Testing Levels:**
1. **Unit Testing:** Validate individual FHIR API calls, data transformations, and business logic
2. **Integration Testing:** Verify end-to-end data flows between your application and Epic's non-production environment
3. **System Integration Testing (SIT):** Test all interfaces together — FHIR, HL7v2, CDS Hooks, and any custom APIs
4. **User Acceptance Testing (UAT):** Clinical users validate workflows in realistic scenarios
5. **Performance/Load Testing:** Simulate production-level traffic to verify latency, throughput, and error handling
6. **Security Testing:** Penetration testing, vulnerability scanning, and compliance validation
7. **Regression Testing:** After Epic upgrades or application changes, verify all existing functionality still works

**Multi-Tenant Testing Considerations:**
- Maintain test environments for multiple Epic versions
- Test with different configuration profiles (different modules enabled, different terminology sets)
- Validate tenant isolation — ensure one tenant's data cannot leak to another
- Test failover and error handling per tenant

**Automation:**
- Automate regression tests against FHIR endpoints using tools like Postman collections, pytest, or custom test harnesses
- Use Epic's open test environments (available through the Showroom program) for continuous integration
- Implement contract testing to catch API changes before they reach production

### 9. IT Governance for Integrations

IT governance ensures that integrations are approved, secure, compliant, and well-managed throughout their lifecycle:

- **Integration Request Process:** Formal process for requesting, reviewing, and approving new integrations
- **Security Review Board:** Evaluates third-party applications for security posture, data handling practices, and compliance
- **Change Advisory Board (CAB):** Reviews and approves changes to production integrations, especially during Epic upgrade windows
- **Vendor Risk Assessment:** Evaluates vendors for financial stability, security practices, business continuity, and regulatory compliance
- **Software Bill of Materials (SBOM):** Increasingly required — documents all components and dependencies in the integration
- **Ongoing Monitoring:** Continuous logging, alerting, and periodic re-assessment of integration health and security

---

## Learning Resources

### Official Documentation and References

1. **Epic Showroom — Integration Specifications and Developer Resources**
   - URL: https://showroom.epic.com
   - Type: Official documentation
   - Description: Epic's marketplace for third-party integrations. Contains technical specifications, integration patterns, and listings of validated apps. Essential reference for understanding Epic's integration ecosystem.

2. **Epic Garden Plot Announcement**
   - URL: https://www.epic.com/epic/post/epic-launches-garden-plot-a-shared-environment-where-independent-medical-groups-can-grow/
   - Type: Official announcement
   - Description: Epic's official post introducing the Garden Plot SaaS model for independent medical groups. Explains the multi-tenant hosting model and its implications.

3. **HL7 FHIR Multi-Tenancy Design Guidance (Health Samurai)**
   - URL: https://www.health-samurai.io/articles/how-to-design-a-multi-tenant-fhir-api-for-an-existing-ehr-system
   - Type: Technical article
   - Description: Detailed guide on designing multi-tenant FHIR APIs for existing EHR systems. Covers tenant modeling, data isolation, and access control patterns.

### Guides and Best Practices

4. **Baker Tilly — From Planning to Performance: Epic Implementation Guide**
   - URL: https://www.bakertilly.com/insights/from-planning-to-performance
   - Type: Industry whitepaper
   - Description: Comprehensive guide covering Epic implementation planning, governance, go-live execution, and post-go-live optimization. Includes stakeholder alignment and testing strategies.

5. **Surety Systems — Epic Go-Live Tips and Tricks**
   - URL: https://www.suretysystems.com/insights/epic-go-live-tips-tricks-to-crush-epic-implementation/
   - Type: Best practices guide
   - Description: Practical advice for Epic go-live events covering training, command center setup, at-the-elbow support, and post-go-live stabilization.

6. **ClindCast — Step-by-Step Guide to Successful Epic Go-Live Support**
   - URL: https://www.clindcast.com/a-step-by-step-guide-to-successful-epic-go-live-support/
   - Type: Practitioner guide
   - Description: Detailed walkthrough of Epic go-live support strategy including real-time dashboards, issue resolution, and 24/7 coordination between onsite and remote teams.

7. **Optimum Healthcare IT — Are You Ready for Your Next Epic Upgrade?**
   - URL: https://optimumhit.com/insights/blog/ehr-implementation/are-you-ready-for-your-next-epic-upgrade/
   - Type: Blog/guide
   - Description: Practical guidance on preparing for Epic upgrades, including assessing technical infrastructure impact and managing integration compatibility.

### Technical Resources

8. **Medplum — Multi-Tenant Access Policy Documentation**
   - URL: https://www.medplum.com/docs/access/multi-tenant-access-policy
   - Type: Technical documentation
   - Description: Open-source FHIR server documentation showing how to implement multi-tenant access policies with practical code examples. Directly applicable to building multi-tenant healthcare applications.

9. **AWS — Building a Multi-Tenant FHIR Server with AWS HealthLake**
   - URL: https://aws.amazon.com/blogs/industries/building-a-multi-tenant-fhir-server-with-aws-healthlake/
   - Type: Technical tutorial
   - Description: AWS architecture guide for building multi-tenant FHIR infrastructure. Covers tenant isolation, access control, and scalability patterns using cloud services.

10. **Kodjin — Multi-Tenant FHIR API Design**
    - URL: https://kodjin.com/blog/multi-tenant-fhir-api/
    - Type: Technical article
    - Description: Explores multi-tenant FHIR API design patterns including tenant routing, data partitioning, and configuration management.

### Community and Industry Resources

11. **HCTec — Epic Community Connect Resource Center**
    - URL: https://hctec.com/resource-center/epic-community-connect/
    - Type: Resource hub
    - Description: Comprehensive overview of Epic Community Connect including governance models, operational considerations, and partner management strategies.

12. **Cloudticity — Epic EHR Hosting Options Comparison**
    - URL: https://blog.cloudticity.com/epic-ehr-hosting-options-comparison-which-is-right-for-you
    - Type: Comparison guide
    - Description: Compares Epic hosting models (self-hosted, Community Connect, Garden Plot) with analysis of multi-tenant implications for each option.

13. **Login VSI — Importance of Automated Testing in Epic**
    - URL: https://www.loginvsi.com/resources/blog/the-importance-of-automated-testing-in-epic/
    - Type: Technical blog
    - Description: Covers automated testing strategies for Epic environments including regression testing, performance validation, and continuous integration approaches.

---

## Learning Path

### Phase 1: Foundations (Week 1–2, ~10 hours)

1. **Understand Epic's deployment models**
   - Study Epic Community Connect architecture and governance
   - Learn about Epic Garden Plot SaaS model
   - Compare self-hosted vs. hosted vs. SaaS deployment options
   - Read resources #2, #11, #12

2. **Learn multi-tenant architecture principles**
   - Data isolation patterns (separate DB, shared schema, tenant ID)
   - Tenant identification and routing
   - Configuration management per tenant
   - Read resources #3, #8, #10

### Phase 2: Configuration and Version Management (Week 3, ~8 hours)

3. **Map configuration variability**
   - Understand how Epic instances differ (modules, FHIR resources, terminology, security)
   - Learn to use FHIR CapabilityStatement for capability discovery
   - Design tenant-specific configuration schemas for your application
   - Read resource #7

4. **Understand Epic's upgrade cadence**
   - Study quarterly release process and version differences
   - Learn how upgrades affect integrations (API changes, new resources, deprecations)
   - Develop a version compatibility strategy for your application
   - Read resource #7

### Phase 3: Go-Live Planning (Week 4–5, ~12 hours)

5. **Master the go-live process**
   - Study pre-go-live, go-live event, and post-go-live phases
   - Learn about command centers, at-the-elbow support, and escalation procedures
   - Understand the role of each stakeholder
   - Read resources #4, #5, #6

6. **Develop testing strategy**
   - Design multi-level testing approach (unit → integration → SIT → UAT → performance → security)
   - Plan for multi-tenant and multi-version testing
   - Learn automated testing tools and contract testing patterns
   - Read resources #9, #13

### Phase 4: Governance and Operations (Week 6, ~6 hours)

7. **IT governance frameworks**
   - Integration request and approval processes
   - Security review and vendor risk assessment
   - Change advisory board procedures
   - SBOM requirements and compliance monitoring

8. **Operational readiness**
   - Develop a go-live playbook template
   - Create runbooks for common integration issues
   - Establish monitoring and alerting baselines
   - Plan for ongoing version compatibility maintenance

**Total estimated time: ~36 hours over 6 weeks**

---

## Practical Exercises

### Exercise 1: Multi-Tenant Configuration Design
**Difficulty:** Intermediate | **Time:** 3–4 hours

Design a tenant configuration schema for a hypothetical SMART on FHIR application that serves multiple Epic customers. Your schema should include:
- FHIR base URL and OAuth endpoints per tenant
- Feature flags for optional functionality
- Custom field mappings for tenant-specific terminology
- Version compatibility settings

Deliverable: A JSON/YAML configuration file with at least 3 tenant profiles showing realistic variation.

### Exercise 2: Go-Live Playbook
**Difficulty:** Intermediate | **Time:** 4–5 hours

Create a go-live playbook for deploying your integration at a new Epic customer site. Include:
- Pre-go-live checklist (20+ items)
- Go-live day timeline (hour-by-hour)
- Escalation matrix with stakeholder contacts
- Rollback procedure
- Post-go-live monitoring dashboard specification

### Exercise 3: Version Compatibility Testing
**Difficulty:** Advanced | **Time:** 4–6 hours

Using Epic's open FHIR sandbox:
1. Query the CapabilityStatement from the sandbox
2. Write automated tests that verify your application handles different resource availability
3. Simulate a version upgrade by modifying expected API responses
4. Implement graceful degradation when expected resources are unavailable

Tools: Postman, pytest, or any HTTP testing framework.

### Exercise 4: Tenant Isolation Audit
**Difficulty:** Advanced | **Time:** 3–4 hours

For a multi-tenant FHIR application:
1. Set up a local FHIR server (e.g., HAPI FHIR or Medplum) with two tenants
2. Create patient resources in each tenant
3. Attempt cross-tenant data access and verify isolation
4. Document the isolation mechanisms and any gaps found

### Exercise 5: Stakeholder Communication Plan
**Difficulty:** Beginner | **Time:** 2–3 hours

Draft a stakeholder communication plan for an integration go-live at a 500-bed hospital:
- Identify all stakeholder groups and their information needs
- Create a communication timeline (12 weeks before go-live through 4 weeks after)
- Draft template emails for key milestones (kick-off, UAT start, go/no-go decision, go-live announcement, stabilization complete)

---

## Connections to Other Domains

- **D-4 (FHIR R4):** CapabilityStatement is your primary tool for discovering tenant-specific FHIR capabilities
- **D-5 (OAuth 2.0 / Epic Auth):** Each tenant has unique OAuth endpoints and client credentials; multi-tenant auth management is critical
- **D-6 (SMART on FHIR):** SMART launch context varies by tenant; your app must handle different EHR launch parameters
- **D-7 (HL7v2):** Some tenants may use HL7v2 interfaces alongside or instead of FHIR; your integration strategy must accommodate both
- **D-9 (Epic Interconnect / MyChart):** Interconnect configuration differs per instance; MyChart-facing features may vary by tenant
- **D-12 (App Orchard / Showroom):** Showroom listing and distribution mechanisms determine how your multi-tenant app reaches Epic customers
- **D-14 (Production Operations):** Go-live transitions directly into production operations; monitoring and reliability patterns build on go-live infrastructure
