# 📊 PROJECT MASTER DASHBOARD: JOYS QA AUTOMATION

> [!IMPORTANT]
> **Project Health:** 🟢 **Healthy** | **Overall Progress:** [███░░░░░░░] 30%
> **Current Focus:** Step 3A/3B - Test Case Design for DM modules.
> **Quality Gate:** ERA Score ≥ 70 | AQG Score ≥ 80%

## 🔌 Integration Status
| Service | Status | Connection Type | Purpose |
| :--- | :--- | :--- | :--- |
| **Jira (ALM)** | 🔴 Disconnected | API Token | Auto-log Bug & Tracking |
| **Database** | 🔴 Disconnected | JDBC/SQL | Layer 2 Data Verification |
| **MCP (Local)** | 🟢 Connected | Direct Access | DOM & Clipboard Evidence |

---

## 🏗️ Overall Project Pipeline
```mermaid
graph LR
    S1([1. Audit]) --> S2([2. Scenario]) --> S3([3. Test Case]) --> S4([4. Execute]) --> S5([5. AQG]) --> S6([6. Report])
    
    classDef done fill:#2E7D32,stroke:#1B5E20,color:#fff;
    classDef active fill:#FFEB3B,stroke:#FBC02D,color:#000;
    classDef pending fill:#ECEFF1,stroke:#B0BEC5,color:#90A4AE;

    class S1,S2 done;
    class S3 active;
    class S4,S5,S6 pending;
```

---

## 📋 Master Task & Traceability Matrix
| UC-ID | Feature Name | Status | Audit | Scenario | Test Case (Type) | RTM Coverage | Latest |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **UC-DM-11** | Card Type | 🔵 Design | ✅ v4 | ✅ v2 | 🔄 DET | ✅ Covered | Audit v4 |
| **UC-DM-12** | Airport | ⏳ Pending | ✅ v3 | ✅ v1 | ⏳ HL | ✅ Covered | Audit v3 |
| **UC-DN-01** | Login (2FA) | ⏳ Pending | ✅ v2 | ✅ v2 | ⏳ HL | ✅ Covered | Audit v2 |
| **UC-DM-10** | Airline Cat. | ⏳ Pending | ✅ v7 | ✅ v4 | ⏳ DET | ✅ Covered | Audit v7 |
| **UC-BL-18** | (TBD) | 🔄 Analysis | 🔄 v1 | ⏳ | - | ❌ Gap | v1 |

**Legend:** 🟢 Done | 🔵 Active | 🔄 In Progress | ⏳ Pending | ✅ Covered | ❌ Gap

---

## 📈 Timeline Progress (Gantt Chart)
```mermaid
%%{
  init: {
    'theme': 'default',
    'gantt': {
      'titlePadding': 20,
      'barHeight': 30,
      'barGap': 8,
      'topPadding': 50,
      'leftPadding': 150,
      'gridLineStartPadding': 20,
      'fontSize': 14,
      'numberSectionStyles': 4
    },
    'themeVariables': {
      'primaryColor': '#ffffff',
      'doneTaskFill': '#2E7D32',
      'doneTaskBorderColor': '#1B5E20',
      'doneTaskContentColor': '#ffffff',
      'activeTaskFill': '#FFEB3B',
      'activeTaskBorderColor': '#FBC02D',
      'activeTaskContentColor': '#000000',
      'taskFill': '#E3F2FD',
      'taskBorderColor': '#2196F3',
      'taskTextLightColor': '#000000',
      'taskContentColor': '#000000',
      'sectionBGFill': '#f4f4f4',
      'sectionBGFill2': '#ffffff'
    }
  }
}%%
gantt
    title JOYS QA Pipeline Timeline (High Contrast)
    dateFormat  YYYY-MM-DD
    axisFormat  %d/%m
    
    section Requirement Audit
    UC-DM-10 (Airline)      :done,    audit1, 2026-04-21, 2026-05-08
    UC-DM-11 (Card Type)    :done,    audit2, 2026-04-22, 2026-05-08
    UC-DM-12 (Airport)      :done,    audit3, 2026-04-22, 2026-05-08
    UC-DN-01 (Login)        :done,    audit4, 2026-04-21, 2026-05-08

    section Scenario Design
    UC-DM-10 Scenarios      :done,    sce1, 2026-04-21, 2026-05-08
    UC-DM-11 Scenarios      :done,    sce2, 2026-05-04, 2026-05-08
    UC-DM-12 Scenarios      :done,    sce3, 2026-04-22, 2026-05-08
    UC-DN-01 Scenarios      :done,    sce4, 2026-04-21, 2026-05-08

    section TC Design (HL/DET)
    UC-DM-11 Detail TC     :active,  tc1, 2026-05-08, 3d
    UC-DM-12 High-Level TC :         tc2, 2026-05-09, 2d
```

---

## ⚠️ Risk & Notes
1. **AQG Threshold:** Kết quả thực thi phải đạt trên 80% điểm tin cậy (AQG Score) để Pass.
2. **ERA Audit:** Test Cases phải đạt ERA Score ≥ 70 trước khi thực thi.
3. **Traceability:** File RTM chi tiết (từng AC) nằm trong folder `testcases/[UC-ID]/`.

---

## 📚 Appendix: QA Methodology Flow
```mermaid
graph TD
    START([Requirement]) --> AUDIT{1. Audit}
    AUDIT -- "Pass" --> SCE[2. Scenario Design]
    
    SCE --> TC_TYPE{3. TC Type Selection}
    TC_TYPE -->|Fast/Smoke| HL[3A. High-Level TC]
    TC_TYPE -->|Full/Regression| DET[3B. Detail-Level TC]
    
    HL --> ERA{ERA Audit}
    DET --> ERA
    
    ERA -- "Score < 70" --> TC_TYPE
    ERA -- "Score >= 70" --> EXEC[4. Execute Step]
    
    EXEC --> AQG{AQG Gate: Usability/Reliability}
    
    AQG -- "Score < 80%" --> RETEST[[RE-TEST REQUIRED]]
    RETEST --> EXEC
    
    AQG -- "Score >= 80%" --> REPORT([Final Report])

    %% Styling for Light Theme
    classDef process fill:#E3F2FD,stroke:#1565C0,stroke-width:1px;
    classDef decision fill:#FFFDE7,stroke:#FBC02D,stroke-width:2px;
    classDef alert fill:#FFEBEE,stroke:#C62828,stroke-width:2px;
    classDef success fill:#F1F8E9,stroke:#388E3C,stroke-width:2px;

    class HL,DET,SCE,EXEC process;
    class AUDIT,TC_TYPE,ERA,AQG decision;
    class RETEST alert;
    class REPORT success;
```
