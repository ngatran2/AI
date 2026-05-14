---
description: "[DEPRECATED] This workflow has been split into two separate workflows. Use /design-testcases-hl for High-Level (Smoke/Sanity) or /design-testcases-det for Detail-Level (Full Regression)."
---

# /design-testcases — Test Case Generation (Router)

> [!WARNING]
> **This workflow has been split into two levels.** Please use the appropriate command below:

## Available Workflows

| Command | Level | Purpose | Case Count |
| :--- | :--- | :--- | :--- |
| `/design-testcases-hl` | High-Level (HL) | Smoke/Sanity — Happy Paths + Critical Errors only | 5–15 per UC |
| `/design-testcases-det` | Detail-Level (DET) | Full Regression — All 6 Phases, BVA, RBAC, Edge Cases | 30–80+ per UC |

## Quick Decision Guide

```
Do you need full regression coverage?
  ├── YES → /design-testcases-det
  └── NO
       ├── Hotfix / CI gate / Quick check? → /design-testcases-hl
       └── Unsure? → Start with /design-testcases-hl, upgrade to /design-testcases-det later
```

## Auto-Routing Rule

If the user invokes `/design-testcases` without specifying a level:
1. **ASK** the user: *"Bạn muốn sinh bộ test cases ở cấp độ nào? **High-level** (5–15 cases, kiểm tra nhanh) hay **Detail-level** (30–80+ cases, regression toàn diện)?"*
2. Wait for user response before proceeding.
3. Route to the appropriate workflow file.