# 📊 PROJECT MASTER DASHBOARD: JOYS QA AUTOMATION
**Dự án:** JOYS-V3 LAMS (Lounge Access Management System)
**Ngày cập nhật:** 2026-05-13
**Phiên bản:** v8

> [!IMPORTANT]
> **Project Health:** 🟢 **Healthy** | **Overall Progress:** [█░░░░░░░░░] 18%
> **Current Focus:** Performance Testing for UC-DM-11 & Functional Exec for UC-DN-01.
> **Quality Gate:** ERA Score ≥ 70 | AQG Score ≥ 80%

## 🔌 Integration Status
| Service | Status | Connection Type | Purpose |
| :--- | :--- | :--- | :--- |
| **Jira (ALM)** | 🔴 Disconnected | API Token | Auto-log Bug & Tracking |
| **Database** | 🟢 Connected | JDBC/Postgres | host=172.16.200.84 (vna_lams_be) |
| **MCP (Local)** | 🟢 Connected | Direct Access | Browser Recording & Evidence |

---

## 🏗️ Overall Project Pipeline
```mermaid
graph LR
    S1([1. Audit]) --> S2([2. Scenario]) --> S3([3. Test Case]) --> S4([4. Execute]) --> S5([5. AQG]) --> S6([6. Report])
    
    classDef done fill:#2E7D32,stroke:#1B5E20,color:#fff;
    classDef active fill:#FFEB3B,stroke:#FBC02D,color:#000;
    classDef pending fill:#ECEFF1,stroke:#B0BEC5,color:#90A4AE;

    class S1,S2,S3,S4 done;
    class S5,S6 active;
```

---

## 🏃 Sprint Information (Sprint 1)
- **Name:** Sprint 1 - Foundation & Master Data
- **Timeline:** 2026-05-04 to 2026-05-17
- **Current Status:** 🔄 **In Progress**
- **Tasks in Scope:**
    - [x] **UC-DM-10:** Quản lý danh mục hãng bay (Done)
    - [x] **UC-DM-12:** Quản lý danh mục sân bay (Done)
    - [ ] **UC-DM-11:** Quản lý loại thẻ (Performance Scripting)
    - [ ] **UC-DN-01:** Login 2FA (Ready for Execution)

---

## 📅 Project Timeline (Gantt)
```mermaid
gantt
    title JOYS QA Sprint 1 Progress
    dateFormat  YYYY-MM-DD
    section Core Data
    UC-DM-10 Airline Category :done, 2026-05-04, 2026-05-08
    UC-DM-12 Airport Category :done, 2026-05-06, 2026-05-09
    section Security & Perf
    UC-DM-11 Card Category    :active, 2026-05-09, 2026-05-15
    UC-DN-01 2FA Login        :2026-05-11, 2026-05-16
```

---

## 📋 Master Task & Traceability Matrix
| UC-ID | Feature Name | Status | Audit | Scenario | Test Case | Functional Exec | Performance |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **UC-DM-10** | Quản lý danh mục hãng bay | ✅ Completed | ✅ v7 | ✅ v4 | ✅ HL/DET | ✅ Executed | ⏳ Pending |
| **UC-DM-11** | Quản lý loại thẻ | 🔄 In Progress | ✅ v4 | ✅ v2 | ⏳ Pending | ⏳ Pending | 🔄 Scripting |
| **UC-DM-12** | Quản lý danh mục sân bay | ✅ Completed | ✅ v3 | ✅ v1 | ✅ HL/DET | ✅ Executed | ⏳ Pending |
| **UC-DN-01** | Login 2FA | ✅ Completed | ✅ v2 | ✅ v2 | ✅ HL/DET | ✅ Executed | ✅ Executed (v1) |
| **UC-BL-18** | UC-BL-18 | ⏳ Pending | ⏳ Pending | ⏳ Pending | ⏳ Pending | ⏳ Pending | ⏳ Pending |

---

## 📈 Execution & Reliability Metrics
| Module | Reliability (AQG) | Defect Density | Stability | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **UC-DM-12** | 85% (TRUSTED) | 0% | 🟢 Stable | 6 cases skipped due to Env. |
| **UC-DN-01** | 95% (HIGH) | 0% | 🟢 Stable | Full 2FA verification. |
| **UC-DM-10** | 78% (TRUSTED) | 12.5% | 🟡 At Risk | 1 FAIL (FUNC_05) due to data constraint. |

---

## 📅 Recent Activities & Log
- **2026-05-13:** Khởi tạo cấu trúc Dashboard v8 tích hợp Gantt chart và Sprint tracking.
- **2026-05-13:** Cập nhật Rule 6 (Pipeline) về tần suất cập nhật Dashboard hàng ngày.
- **2026-05-11:** Thực thi thành công UC-DM-10 (Airline Category) trên Staging environment.
- **2026-05-09:** Thực thi thành công UC-DM-12 (Airport Category).

---
**Antigravity QA Management** - *Real-time Project Oversight*
