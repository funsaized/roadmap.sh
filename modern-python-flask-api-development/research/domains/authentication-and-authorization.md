# Authentication and Authorization in Flask APIs

## Overview

Authentication and authorization are critical security layers for any Flask API. Authentication verifies *who* the user is, while authorization determines *what* they can do. This domain covers JWT-based authentication, OAuth 2.0 integration, API key management, password hashing, role-based access control (RBAC), and token lifecycle management — all essential for building production-ready Flask APIs.

This domain builds on **Request Handling and Data Validation (D-4)** and **Database Integration and ORMs (D-5)**, and feeds into **Background Tasks and Async Patterns (D-9)** and **Security Hardening (D-10)**.

---

## Key Concepts

### 1. Password Hashing and Storage
- **What:** Converting plaintext passwords into irreversible hashes before database storage
- **Algorithms:** bcrypt (adaptive cost factor), Argon2 (memory-hard, OWASP recommended), PBKDF2 (Werkzeug default)
- **Salting:** Random data added before hashing to prevent rainbow table attacks
- **Flask tools:** `werkzeug.security.generate_password_hash()` / `check_password_hash()`, Flask-Bcrypt, passlib (used by Flask-Security)
- **Best practice:** Argon2 is now the default in Flask-Security 5.5.0+; bcrypt remains widely used and secure
- **Prerequisite for:** All authentication flows, user registration endpoints

### 2. Session-Based Authentication
- **What:** Server stores session state; client holds a session cookie
- **Flask tools:** Flask-Login (session management, `login_user()`, `logout_user()`, `current_user` proxy)
- **When to use:** Traditional web apps with server-rendered pages
- **Limitations:** Stateful (harder to scale horizontally), not ideal for pure APIs
- **Relation:** Contrasts with stateless JWT approach; Flask-Login often used alongside RBAC

### 3. JSON Web Tokens (JWT) Authentication
- **What:** Stateless authentication using signed tokens containing user claims
- **Structure:** Header (algorithm + type) → Payload (claims: sub, exp, iat, custom) → Signature (HMAC or RSA)
- **Key library:** Flask-JWT-Extended
- **Token types:**
  - **Access tokens:** Short-lived (15–60 min), used for API access
  - **Refresh tokens:** Longer-lived (days/weeks), used only to obtain new access tokens
- **Token location:** Authorization header (`Bearer <token>`), HTTP-only cookies, or query parameters
- **Important:** JWTs are signed, not encrypted — don't put secrets in the payload
- **Prerequisite for:** Token refresh/rotation, RBAC via claims, Security Hardening (D-10)

### 4. Token Refresh and Rotation
- **What:** Mechanism to issue new access tokens without re-authentication, with security controls
- **Refresh flow:** Client sends expired access token → uses refresh token to get new pair → old refresh token invalidated
- **Rotation:** Every refresh issues a NEW refresh token and invalidates the old one
- **Reuse detection:** If an invalidated refresh token is presented, revoke ALL tokens for that session (indicates theft)
- **Token blocklisting:** Maintain a denylist of revoked tokens (Redis is common for speed)
- **Token freshness:** Flask-JWT-Extended supports "fresh" tokens for sensitive operations (password change, payment)
- **Prerequisite for:** Security Hardening (D-10), session management patterns

### 5. OAuth 2.0 and OpenID Connect
- **What:** Industry-standard protocol for delegated authorization (OAuth 2.0) and identity (OIDC)
- **Key flows:**
  - **Authorization Code Flow:** Most secure for server-side apps; involves redirect to auth server, callback with code, exchange for tokens
  - **Client Credentials Flow:** Machine-to-machine authentication
  - **Implicit Flow:** Deprecated for security reasons
- **OIDC:** Extension of OAuth 2.0 that adds identity layer (ID tokens with user info)
- **Flask library:** Authlib (recommended) — supports OAuth 1.0/2.0 client and server
- **Common providers:** Google, GitHub, Facebook, Auth0, Okta
- **Client registration:** App registers with provider, receives `client_id` and `client_secret`
- **Scopes:** Define what data/access is being requested (e.g., `openid`, `email`, `profile`)

### 6. API Key Authentication
- **What:** Simple authentication using unique secret strings assigned per client/application
- **Generation:** Use `uuid.uuid4().hex` or `os.urandom()` for cryptographic randomness
- **Storage:** Hash API keys before storing (like passwords); never store plaintext
- **Validation:** Custom decorator checks `Authorization` header or `X-API-Key` header
- **Use cases:** Service-to-service auth, rate limiting per client, public API access tiers
- **Limitations:** No built-in expiration, no user identity, less flexible than JWT/OAuth
- **Best practices:** Periodic rotation, IP allowlisting, per-key permission scoping

### 7. Role-Based Access Control (RBAC)
- **What:** Restricting access based on user roles (admin, editor, viewer) and permissions
- **Database modeling:** User ↔ Role (many-to-many via join table), Role ↔ Permission (many-to-many)
- **Implementation patterns:**
  - **Custom decorators:** `@role_required(['admin'])` checking `current_user.roles`
  - **JWT claims:** Embed roles in token payload, check in decorator
  - **Flask extensions:** Flask-Security (comprehensive), Flask-Principal (identity/needs), Flask-RBAC (dedicated)
  - **External services:** Auth0, Permit.io, Cerbos, Oso (policy-as-code)
- **Granularity levels:** Route-level, resource-level, field-level
- **Prerequisite for:** Security Hardening (D-10), Advanced Architectural Patterns (D-13)

### 8. Flask Authentication Extensions Ecosystem
- **Flask-Login:** Session management, `@login_required`, user loader callbacks
- **Flask-JWT-Extended:** JWT creation, validation, refresh, blocklisting, fresh tokens
- **Flask-Security-Too:** All-in-one (login, registration, roles, password hashing, 2FA)
- **Authlib:** OAuth 2.0/OIDC client and server
- **Flask-Principal:** Identity and permission management (needs-based)
- **Flask-CORS:** Cross-origin configuration for API auth headers

### 9. Security Headers and CSRF Protection
- **CSRF:** Cross-Site Request Forgery protection (critical for cookie-based auth)
- **CORS:** Configuring allowed origins for API consumers
- **Security headers:** `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`
- **Cookie flags:** `HttpOnly` (no JS access), `Secure` (HTTPS only), `SameSite` (CSRF mitigation)
- **Prerequisite for:** Security Hardening (D-10)

### 10. Multi-Factor Authentication (MFA/2FA)
- **What:** Additional verification beyond password (TOTP, SMS, email codes)
- **Flask-Security-Too:** Built-in support for TOTP-based 2FA
- **Libraries:** PyOTP for TOTP generation/verification
- **Recovery codes:** Backup codes for account recovery when 2FA device is lost

---

## Learning Resources

### Online Courses

1. **REST APIs with Flask and Python in 2025** — Udemy (Jose Salvatierra/Teclado)
   - URL: https://www.udemy.com/course/rest-api-flask-and-python/
   - Duration: ~17 hours | Difficulty: Intermediate
   - Covers JWT auth with Flask-JWT-Extended, token refresh, user registration
   - Cost: Paid (~$15-20 on sale)

2. **Securing Flask Apps with JWT Authentication** — CodeSignal
   - URL: https://codesignal.com/learn/courses/securing-flask-apps-with-jwt-authentication
   - Duration: ~4 hours | Difficulty: Intermediate
   - Covers token generation, route protection, refresh token rotation
   - Cost: Free tier available

3. **How To Add Authentication to Your App with Flask-Login** — DigitalOcean
   - URL: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
   - Duration: ~2 hours (tutorial) | Difficulty: Beginner-Intermediate
   - Step-by-step guide for session-based auth with Flask-Login
   - Cost: Free

4. **JWT Authentication in Flask** — freeCodeCamp
   - URL: https://www.freecodecamp.org/news/jwt-authentication-in-flask/
   - Duration: ~1-2 hours (article) | Difficulty: Intermediate
   - Complete guide covering JWT concepts, Flask-JWT-Extended setup, protected routes
   - Cost: Free

### Video Tutorials

5. **JWT Authentication For Flask With Flask-JWT-Extended (2-Hour Crash Course)** — YouTube (Ssali Jonathan)
   - URL: https://www.youtube.com/watch?v=aX-ayOb_Aho
   - Duration: ~2 hours | Difficulty: Intermediate
   - Comprehensive: setup, registration, login, token refresh, error handling

6. **Flask JWT Authentication with MongoDB | Full Tutorial 2024** — YouTube
   - URL: https://www.youtube.com/watch?v=Bnlks26HU70
   - Duration: ~1 hour | Difficulty: Intermediate
   - JWT with MongoDB backend, registration, login, profile management

### Books

7. **The New and Improved Flask Mega-Tutorial** — Miguel Grinberg (2025)
   - Publisher: Pragmatic Programmers
   - URL: https://pragprog.com/titles/d-mgflask/the-new-and-improved-flask-mega-tutorial/
   - Relevant chapters: User management, secure password handling, logins, user profiles
   - Difficulty: Beginner-Intermediate
   - The canonical Flask learning resource, regularly updated

8. **Mastering Flask Web Development (Second Edition)** — Daniel Gaspar, Jack Stouffer
   - Publisher: Packt
   - URL: https://www.packtpub.com/en-us/product/mastering-flask-web-development-9781788995405
   - Relevant chapters: JWT authentication, REST APIs, role-based access with LDAP/OAuth/OpenID
   - Difficulty: Intermediate-Advanced

9. **Secure APIs: Design, Build, and Implement** — José Haro Peralta (2025)
   - Publisher: Manning
   - URL: https://www.simonandschuster.com/books/Secure-APIs/Jose-Haro-Peralta/9781633436633
   - Relevant: OWASP Top 10 API risks, API hardening, Python examples
   - Difficulty: Intermediate-Advanced

### Documentation and Reference

10. **Flask-JWT-Extended Official Documentation**
    - URL: https://flask-jwt-extended.readthedocs.io/en/stable/
    - Covers: Basic usage, refresh tokens, token blocklisting, custom claims, fresh tokens
    - Essential reference for JWT implementation

11. **Flask-JWT-Extended — Refreshing Tokens**
    - URL: https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens.html
    - Specific guide on token refresh patterns and implicit refreshing

12. **Authlib Documentation — Flask OAuth Client**
    - URL: https://docs.authlib.org/en/latest/client/flask.html
    - Official guide for OAuth 2.0/OIDC integration in Flask

13. **Flask-Security-Too Documentation**
    - URL: https://flask-security-too.readthedocs.io/en/stable/
    - Comprehensive auth extension: roles, password hashing (Argon2/bcrypt), 2FA

14. **Auth0 Flask API RBAC Code Sample**
    - URL: https://developer.auth0.com/resources/code-samples/api/flask/basic-role-based-access-control
    - Working example of RBAC with Auth0 and Flask

15. **OWASP Authentication Cheat Sheet**
    - URL: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
    - Industry-standard security guidelines for authentication

16. **JWT.io — Introduction to JSON Web Tokens**
    - URL: https://jwt.io/introduction
    - Visual explanation of JWT structure, interactive debugger

### Interactive Exercises and Practice

17. **Teclado REST APIs Course — Token Refreshing Section**
    - URL: https://rest-apis-flask.teclado.com/docs/flask_jwt_extended/token_refreshing_flask_jwt_extended/
    - Hands-on walkthrough with code examples

18. **Teclado — API Key Authentication with Flask**
    - URL: https://blog.teclado.com/api-key-authentication-with-flask/
    - Practical tutorial on implementing API key auth

### GitHub Repositories

19. **flask-rbac-jwt-api** — Pranjalm-23
    - URL: https://github.com/Pranjalm-23/flask-rbac-jwt-api
    - Flask API with JWT + RBAC, MongoDB, admin/user roles, CRUD operations

20. **flask-permission-manager** — justitsi
    - URL: https://github.com/justitsi/flask-permission-manager
    - Role-based permission management microservice with JWT

21. **vimalloc/flask-jwt-extended** (library source)
    - URL: https://github.com/vimalloc/flask-jwt-extended
    - Source code of Flask-JWT-Extended; excellent for understanding internals

22. **lepture/authlib** (library source)
    - URL: https://github.com/lepture/authlib
    - Source code of Authlib; OAuth 2.0/OIDC reference implementation

### Community Resources

23. **r/flask** — Reddit
    - URL: https://www.reddit.com/r/flask/
    - Active community; search for authentication-related threads

24. **Stack Overflow — [flask] [authentication] tags**
    - URL: https://stackoverflow.com/questions/tagged/flask+authentication
    - Thousands of Q&A on Flask auth patterns

---

## Learning Path

### Phase 1: Foundations (3–4 hours)
**Concepts:** Password hashing, session-based auth basics
- Study password hashing algorithms (bcrypt, Argon2, PBKDF2)
- Implement Flask-Login with Werkzeug password hashing
- Build a simple login/logout flow with session cookies
- **Milestone:** Working Flask app with user registration, login, logout, and hashed passwords

### Phase 2: JWT Authentication (4–5 hours)
**Concepts:** JWT structure, access tokens, route protection
- Understand JWT structure (header/payload/signature) using jwt.io
- Install and configure Flask-JWT-Extended
- Implement login endpoint that returns JWT
- Protect routes with `@jwt_required()` decorator
- Handle JWT errors and custom claims
- **Milestone:** API with JWT login, protected endpoints, and meaningful error responses

### Phase 3: Token Lifecycle Management (3–4 hours)
**Concepts:** Refresh tokens, token rotation, blocklisting, fresh tokens
- Implement refresh token endpoint
- Add token rotation (new refresh token on each refresh)
- Set up token blocklisting (in-memory or Redis)
- Implement "fresh" tokens for sensitive operations
- Add reuse detection for compromised refresh tokens
- **Milestone:** Complete token lifecycle with refresh, rotation, revocation, and logout

### Phase 4: OAuth 2.0 Integration (3–4 hours)
**Concepts:** OAuth 2.0 flows, OIDC, Authlib
- Study OAuth 2.0 Authorization Code flow
- Register app with Google/GitHub as OAuth provider
- Implement OAuth login with Authlib
- Handle callback, token exchange, and user info retrieval
- Store OAuth user data and link to local accounts
- **Milestone:** "Login with Google/GitHub" working alongside JWT auth

### Phase 5: API Keys and RBAC (4–5 hours)
**Concepts:** API key generation/validation, RBAC modeling, permission decorators
- Implement API key generation, hashing, and validation
- Design User-Role-Permission database models (many-to-many)
- Build custom `@role_required` decorator
- Embed roles in JWT claims for stateless RBAC
- Test authorization with different user roles
- **Milestone:** API supporting multiple auth methods with role-based route protection

### Phase 6: Integration and Hardening (2–3 hours)
**Concepts:** CSRF, CORS, security headers, MFA introduction
- Configure CORS for API consumers
- Add CSRF protection for cookie-based auth
- Set security headers
- Explore Flask-Security-Too for all-in-one solution
- **Milestone:** Production-ready auth system with multiple auth methods and proper security headers

**Total estimated time: 19–25 hours**

---

## Practical Exercises

### Exercise 1: Basic Auth System (Beginner)
Build a Flask API with:
- User registration with Argon2 password hashing
- Login endpoint returning JWT access + refresh tokens
- Protected `/profile` endpoint
- Logout with token blocklisting

### Exercise 2: Token Refresh Service (Intermediate)
Extend Exercise 1:
- Implement `/refresh` endpoint with token rotation
- Add reuse detection (revoke all tokens if old refresh token is reused)
- Use Redis for token blocklist storage
- Add "fresh" token requirement for password change endpoint

### Exercise 3: OAuth Social Login (Intermediate)
Add to your API:
- "Login with GitHub" using Authlib
- Link OAuth accounts to local user accounts
- Support both JWT auth and OAuth sessions
- Handle account linking when email already exists

### Exercise 4: RBAC System (Intermediate-Advanced)
Build a content management API:
- Define roles: admin, editor, viewer
- Implement User-Role-Permission models with SQLAlchemy
- Create `@role_required` and `@permission_required` decorators
- Admin can manage users/roles; editor can create/edit content; viewer can only read
- Embed roles in JWT claims for stateless checks

### Exercise 5: Multi-Auth API Gateway (Advanced)
Build an API that supports:
- JWT Bearer token authentication
- API key authentication (for service-to-service)
- OAuth 2.0 (for third-party integrations)
- Rate limiting per API key
- Unified RBAC across all auth methods

---

## Connections to Other Domains

| Domain | Connection |
|--------|-----------|
| **D-4: Request Handling** | Auth decorators wrap request handlers; validated input needed for login/registration |
| **D-5: Database Integration** | User/Role/Permission models stored in database; password hashes in user table |
| **D-7: API Design** | Auth schemes documented in OpenAPI specs; API key in headers |
| **D-8: Testing** | Auth fixtures, testing protected endpoints, mocking JWT |
| **D-9: Background Tasks** | Token cleanup jobs, session expiration, async email for password reset |
| **D-10: Security Hardening** | HTTPS enforcement, rate limiting on auth endpoints, input validation against injection |
| **D-11: Deployment** | Secret management (JWT keys, OAuth secrets), HTTPS termination |
| **D-13: Advanced Patterns** | Microservice auth (service mesh, API gateway), centralized auth services |
