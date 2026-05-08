# 📊 PROJECT MASTER DASHBOARD: JOYS QA AUTOMATION

> [!IMPORTANT]
> **Project Health:** 🟢 **Healthy**
> **Current Focus:** Step 3A/3B - Test Case Design for DM modules.
> **Quality Standard:** ERA Score ≥ 70 | AQG Score ≥ 80%

## 🏁 High-Level Summary
- **Overall Progress:** [███░░░░░░░] 30%
- **Total Use Cases:** 8
- **Requirement Audited:** 4/8
- **Scenarios Designed:** 4/8
- **Test Cases Designed:** 0/8
- **Execution Completed:** 0/8

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
      
      /* Task đã hoàn thành - Xanh lá đậm, chữ trắng để nổi bật */
      'doneTaskFill': '#2E7D32',
      'doneTaskBorderColor': '#1B5E20',
      'doneTaskContentColor': '#ffffff',
      
      /* Task đang làm - Vàng tươi, chữ đen để dễ đọc */
      'activeTaskFill': '#FFEB3B',
      'activeTaskBorderColor': '#FBC02D',
      'activeTaskContentColor': '#000000',
      
      /* Task chưa làm - Xanh dương nhạt, chữ đen */
      'taskFill': '#E3F2FD',
      'taskBorderColor': '#2196F3',
      'taskTextLightColor': '#000000',
      'taskContentColor': '#000000',

      /* Màu chữ của Section bên trái */
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

## 🗺️ QA Pipeline Flow (Refined)
```mermaid
graph TD
    %% Node Definitions
    START([Requirement Input]) --> AUDIT{Step 1: Audit}
    
    AUDIT -- "Fail" --> BA[BA Backlog]
    BA --> AUDIT
    
    AUDIT -- "Pass" --> SCE[Step 2: Scenario Design]
    
    SCE --> TC_BRANCH{Step 3: TC Type}
    
    TC_BRANCH -->|Fast| HL[3A: High-Level TC]
    TC_BRANCH -->|Full| DET[3B: Detail-Level TC]
    
    HL --> ERA{ERA Audit}
    DET --> ERA
    
    ERA -- "Score < 70" --> TC_BRANCH
    ERA -- "Score >= 70" --> EXEC[Step 4: Execution]
    
    EXEC --> AQG{AQG Quality Gate}
    
    AQG -- "Score < 80%" --> RETEST[[RE-TEST REQUIRED]]
    RETEST --> EXEC
    
    AQG -- "Score >= 80%" --> REPORT([Final Report])

    %% Styling for Light Theme
    classDef startEnd fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px;
    classDef process fill:#E3F2FD,stroke:#1565C0,stroke-width:1px;
    classDef decision fill:#FFFDE7,stroke:#FBC02D,stroke-width:2px;
    classDef alert fill:#FFEBEE,stroke:#C62828,stroke-width:2px;
    classDef success fill:#F1F8E9,stroke:#388E3C,stroke-width:2px;

    class START,REPORT success;
    class AUDIT,TC_BRANCH,ERA,AQG decision;
    class SCE,HL,DET,EXEC process;
    class RETEST,BA alert;
```

---

## 📝 Detailed Task Tracker
| UC-ID | Feature Name | Req Audit | Scenario | TC Type | TC Status | Execution | Latest Version |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **UC-DM-10** | Airline Cat. | ✅ v7 | ✅ v4 | DET | ⏳ Pending | - | v7 / v4 |
| **UC-DM-11** | Card Type | ✅ v4 | ✅ v2 | DET | 🔄 In Progress | - | v4 / v2 |
| **UC-DM-12** | Airport | ✅ v3 | ✅ v1 | HL | ⏳ Pending | - | v3 / v1 |
| **UC-DN-01** | Login (2FA) | ✅ v2 | ✅ v2 | HL | ⏳ Pending | - | v2 / v2 |
| **UC-BL-18** | (TBD) | 🔄 In Analysis | ⏳ Pending | - | ⏳ Pending | - | v1 |

---

## ⚠️ Risk & Notes
1. **AQG Threshold:** Lưu ý mọi kết quả thực thi phải được AI giải trình (Internal Note) và đạt trên 80% điểm tin cậy (không có False Positive, đủ evidence).
2. **HL vs DET:** Ưu tiên gen High-Level (HL) cho các module DN (Login) để test nhanh Sanity, và Detail (DET) cho các module DM (Danh mục) để phủ kín RBAC.
