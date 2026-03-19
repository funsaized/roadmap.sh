# OAuth 2.0 Security Standards and Epic Auth

## Overview

This domain covers the security layer that underpins all authenticated access to Epic's FHIR APIs. OAuth 2.0, augmented by SMART on FHIR profiles, OpenID Connect (OIDC), PKCE, and JWT-based backend authentication, forms the authorization backbone for every integration — whether it's a clinician-facing EHR-embedded app, a patient portal widget, or a headless data pipeline.

Mastering this domain is a prerequisite for D-6 (SMART on FHIR App Development), D-9 (Epic Interconnect/MyChart APIs), D-10 (Bulk Data), and D-12 (App Orchard Distribution), since every one of those surfaces requires valid OAuth tokens.

**Relationship to Prior Domains:** Builds on D-4 (FHIR R4) for understanding resource-level scopes, and D-2 (Regulatory/Compliance) for HIPAA audit-trail requirements that shape token handling.

---

## Key Concepts

### 1. OAuth 2.0 Core Framework (RFC 6749)

**What it is:** The foundational authorization delegation protocol. Defines four roles — resource owner, client, authorization server, resource server — and several grant types (authorization code, client credentials, implicit [deprecated], refresh token).

**Why it matters for Epic:** All Epic FHIR API access is gated by OAuth 2.0 tokens issued by Epic's authorization server. Understanding the framework is non-negotiable.

**Key elements:**
- Authorization endpoint vs. token endpoint
- Access tokens (short-lived) and refresh tokens (long-lived)
- Scopes as permission boundaries
- Bearer token usage (RFC 6750)
- Redirect URIs and the security implications of open redirectors

### 2. OAuth 2.0 Authorization Code Flow

**What it is:** The primary flow for user-facing applications. The client redirects the user to the authorization server, receives an authorization code at a registered redirect URI, then exchanges that code server-side for an access token.

**Epic-specific details:**
- Used for EHR Launch and Standalone Launch flows
- Epic returns an access token, optional refresh token, patient FHIR ID, and (if `openid` scope requested) an `id_token`
- Authorization codes are single-use and short-lived
- Token endpoint requires `client_id` (public clients) or client authentication (confidential clients)

### 3. SMART on FHIR Launch Framework

**What it is:** An HL7-standardized profile of OAuth 2.0 tailored to healthcare. Adds launch context, FHIR-aware scopes, and well-known configuration discovery.

**Two launch modes:**
- **EHR Launch:** App launched from within the EHR; receives a `launch` parameter containing opaque context
- **Standalone Launch:** App initiates the flow independently; requests context via `launch/patient` or `launch/encounter` scopes

**Discovery:** Apps retrieve `/.well-known/smart-configuration` from the FHIR server to find OAuth endpoints, supported scopes, and capabilities.

### 4. SMART Scopes and Granular Permissions

**What it is:** SMART defines a scope syntax for FHIR resource access:
- `patient/Observation.read` — read Observations for the in-context patient
- `user/MedicationRequest.cruds` — full CRUD on MedicationRequests accessible to the user
- `system/*.read` — system-level read (backend services)
- `openid fhirUser` — request OIDC identity token with FHIR user link
- `launch` / `launch/patient` — request EHR launch context
- `online_access` / `offline_access` — control refresh token behavior

**Epic nuances:** Epic may not support every SMART v2 granular scope. Always check the server's `.well-known/smart-configuration` for `scopes_supported`.

### 5. Proof Key for Code Exchange (PKCE) — RFC 7636

**What it is:** A security extension that prevents authorization code interception attacks. The client generates a random `code_verifier`, derives a `code_challenge` (SHA-256 hash), sends the challenge with the auth request, and proves possession of the verifier at the token endpoint.

**Why it matters:**
- **Mandatory** for all SMART apps (SMART App Launch IG v2 requires PKCE)
- Essential for public clients (SPAs, mobile apps) that cannot hold a client secret
- Now recommended even for confidential clients
- Epic supports `S256` challenge method

**Flow additions:**
1. Generate cryptographically random `code_verifier` (43–128 characters)
2. Compute `code_challenge = BASE64URL(SHA256(code_verifier))`
3. Include `code_challenge` and `code_challenge_method=S256` in authorization request
4. Include `code_verifier` in token exchange request

### 6. OpenID Connect (OIDC) and Identity in FHIR

**What it is:** An identity layer on top of OAuth 2.0. When the `openid` scope is requested, the token response includes an `id_token` (a signed JWT) containing user identity claims.

**FHIR-specific claim — `fhirUser`:** When the `fhirUser` scope is requested alongside `openid`, the `id_token` includes a `fhirUser` claim — a URL pointing to the FHIR resource (Patient, Practitioner, or Person) representing the authenticated user.

**Use cases:**
- Identifying who launched the app
- Personalizing UI based on clinician vs. patient role
- Audit logging with traceable user identity

### 7. JWT-Based Backend Service Authentication (RFC 7523)

**What it is:** For applications that run without user interaction (data pipelines, analytics, population health tools), Epic supports the `client_credentials` grant type using JWT assertions.

**How it works:**
1. App generates a JWT with claims: `iss` (client ID), `sub` (client ID), `aud` (token endpoint URL), `jti` (unique ID), `exp` (max 5 minutes from now)
2. JWT is signed with the app's private key (RS384 recommended by Epic)
3. App POSTs to token endpoint with `grant_type=client_credentials`, `client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`, and `client_assertion=<signed JWT>`
4. Epic validates the JWT signature using the app's registered public key
5. Epic returns an access token

**Key constraints:**
- `exp` must be no more than 5 minutes in the future
- Non-production and production environments have separate client IDs
- System-level scopes only (e.g., `system/Patient.read`)

### 8. JSON Web Key Sets (JWKS) and Key Management

**What it is:** JWKS is a JSON structure (RFC 7517) containing one or more public keys. Used by Epic to verify JWT signatures from backend service clients.

**Two registration approaches:**
- **JWKS URL:** Register a publicly accessible URL that hosts your JWKS. Epic fetches keys dynamically. Enables key rotation without re-registration.
- **Static JWKS upload:** Upload the JWKS directly to Epic's developer portal. Simpler but requires manual update on rotation.

**Best practices:**
- Include `kid` (key identifier) in both the JWKS and JWT header so Epic can select the correct key
- Use RSA key pairs with minimum 2048-bit keys (RS384 signing algorithm)
- Rotate keys periodically (every 90–365 days)
- Never expose private keys; store in HSMs or secure vaults
- Host JWKS URL over HTTPS with valid TLS certificate
- Keep at least two keys in JWKS during rotation (old + new) for graceful rollover

### 9. TLS and Transport Security

**What it is:** All communication with Epic's FHIR APIs must occur over TLS 1.2 or higher.

**Requirements:**
- Valid X.509 certificates from trusted CAs
- No self-signed certificates in production
- Certificate pinning is not recommended (Epic may rotate certificates)
- Mutual TLS (mTLS) is not currently required by Epic but may be relevant for other healthcare integrations

### 10. Token Lifecycle Management

**What it is:** Operational discipline around token handling that directly impacts reliability and security.

**Concepts:**
- **Access token expiry:** Typically 5–60 minutes for Epic tokens
- **Refresh tokens:** Use `offline_access` scope; must be stored securely server-side
- **Token caching:** Cache access tokens and reuse until near-expiry; avoid requesting new tokens for every API call
- **Token revocation:** No standard revocation endpoint in SMART; rely on short expiry
- **Secure storage:** Tokens in memory only; never in logs, local storage, or databases without encryption

### 11. CSRF Protection and State Parameter

**What it is:** The `state` parameter in OAuth authorization requests prevents cross-site request forgery attacks.

**Implementation:**
- Generate a unique, unpredictable value per authorization request
- Store server-side (or in a signed cookie)
- Validate on redirect callback — reject if missing or mismatched

### 12. Epic's Token Format and Audience Validation

**What it is:** Epic may issue tokens as JWTs in some environments. The `aud` (audience) parameter in authorization requests specifies the FHIR server URL.

**Important caveats:**
- Do NOT decode Epic-issued JWTs unless `aud` matches your client ID
- Treat access tokens as opaque strings — rely on the authorization server for validation
- Token length may vary; do not impose fixed-size limits

---

## Learning Resources

### Documentation and Specifications (Primary)

1. **Epic on FHIR — OAuth 2.0 Documentation**
   - URL: https://fhir.epic.com/Documentation?docId=oauth2
   - Type: Official documentation
   - Covers: All Epic-supported OAuth flows, launch types, scopes, backend services
   - Essential: This is the canonical reference for Epic-specific OAuth behavior

2. **HL7 SMART App Launch Implementation Guide (v2)**
   - URL: https://build.fhir.org/ig/HL7/smart-app-launch/
   - Type: HL7 specification
   - Covers: Full SMART protocol including scopes, launch context, PKCE, backend services
   - Essential: The standard that Epic implements

3. **HL7 SMART App Launch — Scopes and Launch Context**
   - URL: https://build.fhir.org/ig/HL7/smart-app-launch/scopes-and-launch-context.html
   - Type: Specification section
   - Covers: Complete scope syntax, v1 vs v2 scope formats, launch parameters

4. **RFC 6749 — The OAuth 2.0 Authorization Framework**
   - URL: https://datatracker.ietf.org/doc/html/rfc6749
   - Type: IETF standard
   - Covers: Core OAuth 2.0 protocol

5. **RFC 7636 — Proof Key for Code Exchange (PKCE)**
   - URL: https://datatracker.ietf.org/doc/html/rfc7636
   - Type: IETF standard
   - Covers: PKCE specification

6. **RFC 7523 — JWT Profile for OAuth 2.0 Client Authentication**
   - URL: https://datatracker.ietf.org/doc/html/rfc7523
   - Type: IETF standard
   - Covers: JWT bearer assertions for client auth and grant type

7. **Epic on FHIR Developer Portal**
   - URL: https://fhir.epic.com/
   - Type: Developer portal
   - Covers: Client ID registration, sandbox access, API documentation

8. **open.epic Developer Resources**
   - URL: https://open.epic.com/DeveloperResources
   - Type: Developer portal
   - Covers: Overview of Epic integration technologies, developer onboarding

### Online Courses

9. **Firely HL7 FHIR Overview Course**
   - URL: https://fire.ly/training/hl7-fhir-overview-course/
   - Platform: Firely (online, instructor-led)
   - Duration: 3 days
   - Cost: Paid
   - Covers: FHIR fundamentals including security framework, SMART App Launch, OAuth2, OIDC, scopes
   - Relevance: Provides structured learning of SMART/OAuth in FHIR context

10. **Auth0 — Authorization Code Flow with PKCE**
    - URL: https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow-with-pkce
    - Platform: Auth0 (free documentation + interactive guides)
    - Duration: 1–2 hours
    - Covers: PKCE flow explanation with code samples and diagrams

11. **OAuth.com — Map of OAuth 2.0 Specs**
    - URL: https://www.oauth.com/oauth2-servers/map-oauth-2-0-specs/
    - Platform: Free web resource by Aaron Parecki
    - Duration: Self-paced reference
    - Covers: Navigation guide to all OAuth RFCs and how they relate

### Video Tutorials

12. **Epic EHR Integration: Exploring FHIR, OAuth 2.0 and Beyond (Mindbowser)**
    - URL: https://www.youtube.com/watch?v=mbjXXvsa5I8
    - Duration: ~45 minutes
    - Covers: Live demo of Epic FHIR integration with OAuth 2.0, front-end and backend flows

13. **EPIC FHIR OAuth2.0 with NextJS Part 1**
    - URL: https://www.youtube.com/watch?v=8P9gzKLW3to
    - Duration: ~30 minutes
    - Covers: Hands-on standalone launch with Epic FHIR and OAuth in NextJS

14. **Health Data Sharing — OAuth, SMART on FHIR, and Friends (ONC)**
    - URL: https://www.youtube.com/watch?v=OVLKIKRXkNk
    - Duration: ~60 minutes
    - Covers: OAuth 2.0 and SMART on FHIR overview with Epic MyChart demo, policy perspective

15. **SMART on FHIR: OAuthServer Setup (Auth0/Okta)**
    - URL: https://www.youtube.com/watch?v=rkOAGBY1yUw
    - Duration: ~20 minutes
    - Covers: Setting up an OAuth 2.0 server for SMART on FHIR with Auth0/Okta

### Books

16. **OAuth 2 in Action** — Justin Richer & Antonio Sanso (Manning, 2017)
    - URL: https://www.manning.com/books/oauth-2-in-action
    - Difficulty: Intermediate
    - Relevant chapters: Authorization code flow, JWT/JOSE, client authentication, token management
    - Note: Best general OAuth 2.0 book; not healthcare-specific but essential for understanding the protocol deeply

17. **OpenID Connect in Action** — Prabath Siriwardena (Manning)
    - Difficulty: Intermediate
    - Relevant chapters: OIDC fundamentals, ID tokens, claims, identity federation
    - Note: Complements OAuth 2 in Action with identity layer focus

### GitHub Repositories and Code Examples

18. **epic-on-fhir-backend-app** (Node.js backend service example)
    - URL: https://github.com/callum-anderson/epic-on-fhir-backend-app
    - Language: Node.js
    - Demonstrates: Client credentials flow with JWT assertion against Epic sandbox

19. **example-fhir-app** (Express.js SMART launch)
    - URL: https://github.com/donzacharias/example-fhir-app
    - Language: Node.js/Express
    - Demonstrates: SMART on FHIR EHR launch with OAuth 2.0

20. **epic-fhir-kitchensink** (Node.js full example)
    - URL: https://github.com/sudheerchekka/epic-fhir-kitchensink
    - Language: Node.js
    - Demonstrates: OAuth 2.0 with public/private keys, JWT, patient data access

21. **OncoKB-FHIR-Auth** (Node.js EHR auth)
    - URL: https://github.com/oncokb/OncoKB-FHIR-Auth
    - Language: Node.js
    - Demonstrates: Full FHIR authentication process for EHR integration

22. **epic-api-client** (Python package)
    - URL: https://pypi.org/project/epic-api-client/
    - Language: Python
    - Demonstrates: Modular Epic FHIR API interaction with OAuth 2.0 JWT client credentials

### Articles and Tutorials

23. **Building Backend OAuth 2.0 App for JWT Assertions (Medium)**
    - URL: https://medium.com/onebyte-llc/building-backend-oauth-2-0-app-for-jwt-assertions-acf1af784920
    - Covers: Step-by-step backend service OAuth with Epic

24. **How to Integrate with Epic EHR Using Python and SMART on FHIR APIs (Spritle)**
    - URL: https://www.spritle.com/blog/how-to-integrate-with-epic-ehr-using-python-and-smart-on-fhir-apis/
    - Covers: Python implementation of Epic FHIR integration with OAuth

25. **Implementing Configurable SMART on FHIR Authentication with Node.js (ToTheNew)**
    - URL: https://www.tothenew.com/blog/implementing-configurable-smart-on-fhir-authentication-with-node-js/
    - Covers: Multi-EHR SMART auth supporting both Epic and Cerner

26. **Building a SMART on FHIR App with Flask and OAuthLib (Medium)**
    - URL: https://medium.com/@fmoralcaballero/building-a-smart-on-fhir-application-with-pythons-flask-and-oauthlib-1217a49d1529
    - Covers: Python Flask SMART on FHIR implementation

### Community Resources

27. **SMART on FHIR Google Group**
    - URL: https://groups.google.com/g/smart-on-fhir
    - Active community for SMART implementation questions

28. **r/healthIT on Reddit**
    - URL: https://www.reddit.com/r/healthIT/
    - General health IT discussions including Epic integration

29. **Stack Overflow — [epic] [fhir] [oauth-2.0] tags**
    - URL: https://stackoverflow.com/questions/tagged/epic+fhir
    - Practical Q&A on Epic FHIR OAuth issues

---

## Learning Path

### Phase 1: OAuth 2.0 Foundations (5–7 hours)

**Goal:** Understand OAuth 2.0 as a protocol before applying it to healthcare.

1. Read RFC 6749 Sections 1–4 (or use oauth.com as a friendlier reference)
2. Study the authorization code grant flow in detail
3. Understand roles: resource owner, client, authorization server, resource server
4. Learn token types: access tokens, refresh tokens, bearer tokens
5. Watch an OAuth explainer video (many excellent ones on YouTube)

**Milestone:** Can whiteboard the authorization code flow from memory, explain each step and what security properties it provides.

### Phase 2: PKCE and Modern OAuth Security (3–4 hours)

**Goal:** Understand why PKCE exists and how to implement it.

1. Read RFC 7636
2. Study the Auth0 PKCE documentation (resource #10)
3. Implement a minimal PKCE flow in a test app (any OAuth provider)
4. Understand `code_verifier`, `code_challenge`, and `S256` method

**Milestone:** Can explain the authorization code interception attack and how PKCE prevents it. Have implemented PKCE in code.

### Phase 3: SMART on FHIR Authorization (6–8 hours)

**Goal:** Understand how OAuth 2.0 is profiled for healthcare via SMART.

1. Read the SMART App Launch IG (resource #2), focusing on:
   - App Launch Framework
   - Scopes and Launch Context
   - `.well-known/smart-configuration` discovery
2. Read Epic's OAuth 2.0 documentation (resource #1)
3. Understand EHR Launch vs. Standalone Launch
4. Study SMART scope syntax (`patient/`, `user/`, `system/`, CRUD permissions)
5. Watch the ONC SMART on FHIR video (resource #14)

**Milestone:** Can describe both EHR and standalone launch flows, list the scopes your app would request, and explain how `.well-known/smart-configuration` works.

### Phase 4: OpenID Connect and Identity (2–3 hours)

**Goal:** Understand how OIDC adds identity to OAuth in the FHIR context.

1. Study OIDC basics: `id_token`, claims, `openid` scope
2. Understand the `fhirUser` claim and how it maps to FHIR resources
3. Learn `id_token` validation (signature, issuer, audience, expiry)

**Milestone:** Can decode an `id_token`, explain each standard claim, and describe what `fhirUser` provides.

### Phase 5: JWT Backend Service Authentication (4–6 hours)

**Goal:** Master the machine-to-machine auth flow for Epic.

1. Read RFC 7523
2. Study Epic's backend services documentation
3. Generate an RSA key pair and create a JWKS
4. Build a JWT with correct claims (`iss`, `sub`, `aud`, `jti`, `exp`)
5. Sign the JWT and exchange it for an access token against Epic's sandbox
6. Study the Medium article on backend OAuth (resource #23)

**Milestone:** Have a working backend service that obtains an access token from Epic's sandbox using JWT assertion.

### Phase 6: Key Management and JWKS Operations (3–4 hours)

**Goal:** Understand production-grade key management.

1. Study JWKS structure (RFC 7517)
2. Implement a JWKS endpoint that serves your public keys
3. Practice key rotation: add new key, update JWKS, transition signing, remove old key
4. Understand `kid` matching between JWT header and JWKS
5. Learn about HSMs and secret management (AWS KMS, Azure Key Vault, HashiCorp Vault)

**Milestone:** Can rotate keys without downtime, host a JWKS URL, and explain the security implications of key compromise.

### Phase 7: Integration Practice with Epic Sandbox (4–6 hours)

**Goal:** End-to-end practical application.

1. Register an app on fhir.epic.com
2. Implement EHR Launch flow against Epic's sandbox
3. Implement Standalone Launch flow
4. Implement Backend Services flow
5. Test token refresh
6. Explore the Launchpad at open.epic.com/launchpad

**Milestone:** Have three working auth flows against Epic's sandbox — EHR launch, standalone, and backend service.

**Total estimated time: 27–38 hours**

---

## Practical Exercises

### Exercise 1: OAuth 2.0 Flow Diagram (Beginner, 1 hour)
Draw sequence diagrams for: (a) authorization code flow, (b) authorization code flow with PKCE, (c) client credentials with JWT assertion. Label every HTTP request/response, every parameter, and every security check.

### Exercise 2: PKCE Implementation (Beginner–Intermediate, 2 hours)
Build a minimal web app that performs an OAuth authorization code flow with PKCE against a public OAuth provider (Auth0, Okta, or Google). Verify the `code_verifier` → `code_challenge` relationship manually.

### Exercise 3: SMART Configuration Discovery (Intermediate, 1 hour)
Write a script that fetches `/.well-known/smart-configuration` from Epic's sandbox FHIR server, parses the response, and extracts the authorization endpoint, token endpoint, and supported scopes. Compare with the SMART App Launch IG requirements.

### Exercise 4: Epic Standalone Launch (Intermediate, 3 hours)
Register a public client on fhir.epic.com. Build a web app that performs a standalone launch: discovers SMART config, redirects to Epic's authorization endpoint with PKCE, handles the callback, exchanges the code for tokens, and reads a Patient resource.

### Exercise 5: JWT Assertion Builder (Intermediate, 2 hours)
Write a program that: (a) generates an RSA-2048 key pair, (b) creates a JWKS containing the public key, (c) builds a JWT with Epic-required claims, (d) signs it with RS384, and (e) prints the signed JWT. Verify the signature using the JWKS.

### Exercise 6: Backend Service Auth with Epic Sandbox (Advanced, 3 hours)
Register a confidential backend service app on fhir.epic.com. Upload your JWKS. Implement the full `client_credentials` flow: build JWT assertion, POST to token endpoint, receive access token, use it to read FHIR resources with `system/` scopes.

### Exercise 7: JWKS Key Rotation Simulation (Advanced, 2 hours)
Implement a JWKS endpoint that serves your public keys. Simulate key rotation: add a new key, update JWKS, sign new JWTs with the new key while old tokens are still valid, then retire the old key. Verify that both old and new JWTs validate correctly during the transition period.

### Exercise 8: Token Lifecycle Manager (Advanced, 2 hours)
Build a token management module that: caches access tokens, tracks expiry, automatically refreshes before expiry (for user-facing flows), and re-authenticates (for backend flows). Include proper error handling for expired tokens, revoked tokens, and network failures.

### Exercise 9: Multi-Flow Test Harness (Expert, 4 hours)
Build a comprehensive test application that supports all three Epic auth flows (EHR launch, standalone, backend service) with a single codebase. Include proper PKCE, state parameter validation, token caching, and structured logging of the entire auth flow for debugging.

---

## Connections to Other Domains

| Domain | Connection |
|--------|-----------|
| D-4: FHIR R4 | Scopes reference FHIR resource types; token responses include FHIR patient IDs |
| D-6: SMART on FHIR | Direct prerequisite — SMART is the OAuth profile used by Epic |
| D-8: CDS Hooks | CDS Hooks services receive FHIR authorization tokens for data access |
| D-9: Epic APIs | MyChart and Interconnect APIs use the same OAuth infrastructure |
| D-10: Bulk Data | Bulk FHIR export uses backend service auth with system-level scopes |
| D-12: App Orchard | App Orchard certification requires proper OAuth implementation |
| D-13: Multi-Tenant | Each Epic instance has its own authorization server and token endpoint |
| D-14: Production Ops | Token management, key rotation, and auth monitoring are operational concerns |
