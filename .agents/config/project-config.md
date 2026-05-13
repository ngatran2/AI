# Project Configuration

This file serves as the configuration template for the actual project utilizing this Automated QC Framework. Fill in the specifics below so that BAs, QAs, and AI Agents understand the context, links, and environments of the project being tested.

| Field   | Value                             |
|---------|-----------------------------------|
| Project | [Insert Real Project Name]        |
| Created | [Insert Date]                     |
| Author  | [Insert Author Name]              |
| Version | v1                                |
| Requirement Link | https://docs.google.com/document/d/1OfaNXQmPYw6p_aRSsWvWQ3mZ1b_VD-JMd1ZWZyXBrvc/edit?usp=sharing |


---

## 1. Project Overview

> **Description:** [Provide a brief description of the actual project context, e.g., an E-commerce platform, a banking system, or internal tooling.]
> **Domain:** [E-commerce / Finance / Healthcare / etc.]
> **Target Audience:** [Internal users / Public consumers / B2B partners]

---

## 2. Associated Links & Resources

Provide all access links required for gathering context and documentation.

| Resource Type    | URL / Link                                      | Note / Access Requirement                |
|------------------|-------------------------------------------------|------------------------------------------|
| **Jira Board**   | `https://[company].atlassian.net/...`           | Sprint tracking, bug reporting           |
| **Confluence**   | `https://[company].atlassian.net/...`           | PRD, Architecture, API Specs             |
| **Figma / UI**   | `https://figma.com/file/...`                    | Design mockups and design system         |
| **Git Repo**     | `https://github.com/... / https://gitlab/...`   | Source code repository                   |
| **CI/CD Pipeline**| `https://jenkins... / https://github.com/...` | Deployment and pipeline tracking         |

| **Others**       | `https://lams-api.sotatek.works/document-json` | Raw Swagger/OpenAPI Spec (JSON)          |
| **Swagger UI**   | `https://lams-api.sotatek.works/document#/`     | API Documentation Interface     
---

## 3. Environments

List all deployment environments. This is crucial for test execution and manual testing context.

| Environment | URL Endpoint                  | Database (Optional)          | Purpose                           |
|-------------|-------------------------------|------------------------------|-----------------------------------|
| **STAGING** | `https://lams-api.sotatek.works` | `172.16.200.84:5432` (vna_lams_be) | API Staging Environment           |
| **DEV**     | `https://dev.api.project.com` | `dev-db.project.internal`    | Development & initial testing     |
| **QA / Staging** | `https://qa.api.project.com` | `qa-db.project.internal` | Primary environment for QA and UAT|
| **UAT**     | `https://uat.api.project.com` | `uat-db.project.internal`    | User Acceptance Testing by clients|
| **PROD**    | `https://api.project.com`     | `prod-db.project.internal`   | Live production system            |

---

## 4. Accounts & Credentials Structure

> **SECURITY WARNING:** NEVER STORE RAW PASSWORDS HERE. Describe the *types* of accounts available and how to request or retrieve credentials securely (e.g., via 1Password, internal Vault, etc.).

| Vai trò | Username / Email | Password | Secret key (OTP) |
| :--- | :--- | :--- | :--- |
| Admin | nga.tran2+100@sotatek.com | Linh@12345 | N54X2TBDGYSSYJLOOJOTU4KTPNQUO4ZW |
| Admin View | nga.tran2+50@sotatek.com | Linh@12345 | krasyq2ikbevkmr3jb4hcxjdofxwm3tt |
| Admin Delete | nga.tran2+51@sotatek.com | Linh@12345 | g5hee4lbnv5xulbyhzas6t3fijtvky3o |
| Admin Edit | huong.pham1@yopmail.com | tgNzNT!A3qN2Oe | MFQVWUS6J4QUOJJEJNOVOV2SF5KDIZZU |
| AdminLocked | nga.tran2+15@sotatek.com | Linh@12345 | G5HEE4LBNV5XULBYHZAS6T3FIJTVKY3O |

---

## 5. Third-Party Integrations / APIs

List external services or APIs that the project relies on, which might need special configurations or test data.

- **Payment Gateway:** [e.g., Stripe Sandbox endpoints]
- **Email Service:** [e.g., Mailgun (Testing keys)]
- **Authentication:** [e.g., Auth0, Firebase Auth]

---
---

# JOYS Internal Framework Settings

> *The sections below are internal constants for the AI Agents. Do not alter unless you are customizing the AI pipeline.*

## 6. Confluence / Jira API Authentication

To allow the `docs-reader` agent to access authenticated Confluence or Jira pages, provide a personal API token when prompted.

### How to Generate a Token
1. Go to: https://id.atlassian.com/manage-profile/security/api-tokens
2. Click **Create API token**
3. Name it (e.g., `JOYS-docs-reader`)
4. Copy the token immediately — it will not be shown again

### Security Rules
- **NEVER** paste your token into a requirement file, output file, or any other document.
- Tokens are **in-session only** — they are not stored or persisted anywhere.

---

## 7. Base Directory Paths

These paths define where the pipeline reads and writes files. Agents MUST use these paths.

| Role             | Path                          |
|------------------|-------------------------------|
| Requirements     | `requirements/[UC-ID]/`       |
| Scenarios        | `scenarios/[UC-ID]/`          |
| Test Cases       | `testcases/[UC-ID]/`          |
| Execution Report | `execution/[UC-ID]/`          |

---

## 8. Pipeline Settings

| Setting                    | Value                  |
|----------------------------|------------------------|
| Default language (output)  | English                |
| Default language (comms)   | Vietnamese             |
| Auto-proceed between steps | ❌ Disabled (User controls)|
| Overwrite finalized files  | ❌ Never (Create new version)|

---

## 9. Template Locations

| Template                     | Path                                                              |
|------------------------------|-------------------------------------------------------------------|
| UC Readiness Review Template | `.agents/skills/qc-uc-review/template/UC_readiness_review_template_v3.md` |
| Test Case Excel Template     | `.agents/skills/qc-tc-design/templates/Testcase_template.xlsx`       |

---

## 10. MCP Server Configuration (Optional)

> Cấu hình các MCP Server bên dưới để kích hoạt tính năng nâng cao trong quá trình Execute Test (xem `test-execution` SKILL.md Section 7). Nếu chưa cấu hình, Agent sẽ tự động sử dụng phương thức UI-only truyền thống.

| Component | MCP Server | Status | Purpose |
|---|---|---|---|
| **Database Access** | `postgres-mcp` | 🟢 Configured | host=172.16.200.84, db=vna_lams_be, user=lams_readonly (Layer 2 Verification) |
| **File System** | `[e.g., local-file-mcp]` | ❌ Not configured | Read/Write execution reports, evidence files |
| **Browser Control** | `[e.g., playwright-mcp]` | ❌ Not configured | UI test execution, DOM inspection |
| **API Testing** | `[e.g., fetch-mcp / rest-api-mcp]` | ❌ Not configured | API-based data preparation (Pre-conditions) |
| **Log Access** | `[e.g., log-reader-mcp]` | ❌ Not configured | Automated log extraction on test failure |

**Security Rules:**
- Database MCP MUST be configured with **READ-ONLY** access (`SELECT` only). No write permissions.
- Log MCP MUST NOT have delete or overwrite permissions.
- All MCP connections MUST target non-production environments only.
