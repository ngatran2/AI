# 🌌 JOYS - Just Optimize Your Workforce

Dự án này là một không gian làm việc (workspace) dựa trên **Agentic Framework** - tối ưu hóa "lao động" AI, được thiết kế để tự động hóa quy trình làm việc thực tế của QC, bao gồm từ bước phân tích tài liệu nghiệp vụ, thiết kế và thiết kế kiểm thử. Hệ thống sử dụng các AI Agent chạy các luồng công việc (workflows) tuần tự để tự động đọc, phân tích tài liệu yêu cầu, và sinh ra kịch bản kiểm thử (Test Scenarios) cũng như ca kiểm thử chi tiết (Test Cases).

---

## 🚀 Điểm nhấn & Giá trị cốt lõi (Key Highlights)

> [!TIP]
> **1. Chiến lược Thiết kế Test Case (Smart Design Strategy)**
> *   **Phân cấp linh hoạt (HL vs DET):** Tùy chọn giữa tốc độ (High-level: 5-15 cases trọng yếu) và độ phủ (Detail-level: 30-80+ cases biên). Giúp tối ưu hóa chi phí token và thời gian chạy.
> *   **Tiêu chuẩn "Bước Nguyên Tử" (Atomic Steps):** Mọi test case đều được viết theo chuẩn Action Keywords `[Click]`, `[Input]`, `[Verify]`. Điều này biến tài liệu Excel thành "mã nguồn" mà cả người và máy (Automation) đều hiểu thống nhất 100%.
> *   **Xác thực 3 lớp (Triple-Layer Verification):** AI bắt buộc phải đối soát chéo giữa Giao diện (UI) -> API -> Cơ sở dữ liệu (PostgreSQL). Điều này giúp phát hiện các lỗi logic ngầm mà chỉ nhìn UI không thể thấy được.
> *   **Phân quyền (RBAC) mặc định:** Tự động gen kịch bản cho ít nhất 5 Roles tiêu chuẩn (Admin, View, Edit, Delete, Locked), đảm bảo an toàn dữ liệu tuyệt đối.

> [!IMPORTANT]
> **2. Hệ thống Thực thi "Thông minh & Tin cậy" (Reliable Execution)**
> *   **ERA Audit (Quality Gate đầu vào):** Hệ thống sẽ từ chối chạy nếu bộ test case không đủ điểm chất lượng (>70). Đảm bảo không phí thời gian vào kịch bản sai.
> *   **Antigravity Quality Gate (AQG - Hậu kiểm):** AI không chỉ báo Pass/Fail mà phải giải trình được logic (Internal Note) và cung cấp bằng chứng DOM/Clipboard/Logs. Loại bỏ hoàn toàn tình trạng báo cáo "Pass giả".
> *   **Self-Healing & Tối ưu tốc độ:** Tự động sửa Locator bị hỏng và tái sử dụng Session/State, giúp tốc độ thực thi nhanh gấp 5 lần so với các luồng automation truyền thống.
> *   **MCP Integration:** Kết nối trực tiếp vào "nội tạng" hệ thống (DB/Logs) để bắt lỗi tầng sâu thay vì chỉ nhìn bề mặt UI.

---

## 📊 Quản lý Dự án (Project Management)

Tất cả tiến độ, sức khỏe dự án (Health Check) và ma trận truy vết (RTM) được cập nhật liên tục tại:

| Tài liệu | Đường dẫn / Link | Ghi chú |
| :--- | :--- | :--- |
| **📌 Master Dashboard** | [PROJECT_MASTER_DASHBOARD_v11.md](file:///d:/AI/Newtemplate/report/PROJECT_MASTER_DASHBOARD_20260513_v11.md) | Tổng quan trạng thái từng Use Case |
| **🐞 Daily Bug Snapshot** | [daily-bug-notification_20260514.md](file:///d:/AI/Newtemplate/report/daily-bug-notification_20260514.md) | Báo cáo quét Jira hằng ngày |

---

## 🔌 Kết nối Hệ thống (System Integrations)

| Hệ thống | Chi tiết kết nối | Mục đích |
| :--- | :--- | :--- |
| **Jira** | `https://jira.sotatek.com` (Key: `LAMS`, Filter: `BOARD_767`) | Quản lý Bug & Theo dõi Sprint |
| **Database** | `172.16.200.84:5432` (PostgreSQL) | Xác thực dữ liệu tầng sâu (Layer 2) |
| **Extensions** | `Zixfel Extension` | Truy cập DOM & Giải mã OTP/2FA runtime |
| **Protocol** | `MCP (Model Context Protocol)` | Cầu nối bảo mật DB/File/Logs |

---

## 📂 Cấu trúc Dự án (Project Structure)

### 🤖 Thư mục hệ thống Agent (`.agents/`)
*   **agents/**: Nơi định nghĩa các persona (docs-reader, requirement-reviewer, qa-engineer).
*   **rules/**: Chứa các quy tắc hệ thống bắt buộc (`primary-workflow.md`, `naming-convention.md`).
*   **skills/**: Chứa các kỹ năng chuyên biệt (`qc-uc-review`, `performance-testing`, `pdf`, `qc-ask-ba`).
*   **workflows/**: Điểm kích hoạt các lệnh tắt (`/qc-review-uc`, `/execute-testcases`, `/performance-testing`).

### 🛠 Thư mục làm việc theo Pipeline
*   **requirements/**: Tài liệu đặc tả yêu cầu (Use Case) & báo cáo `audited`.
*   **scenarios/**: Kịch bản kiểm thử (Markdown) bao gồm Happy Path & Edge Case.
*   **testcases/**: Bộ ca kiểm thử chi tiết ở định dạng Excel (.xlsx).
*   **execution/**: Lưu trữ báo cáo thực thi, bằng chứng (Screenshots) & Logs.

---

## 📑 Hướng dẫn Quy trình Pipeline (Manual & Automation)

### 🟢 Bước 1: Phân tích & Đánh giá Yêu cầu (Requirement Audit)
*   **Mục đích:** Đánh giá tính đầy đủ, minh bạch và phát hiện lỗi/lỗ hổng của tài liệu requirement.
*   **Thực hiện:** Đặt tài liệu (DOCX, PDF, URL...) vào thư mục `requirements/[UC-ID]/`.
*   **Ra lệnh:** Sử dụng lệnh `/qc-review-uc`.
*   **Kết quả:** Sinh ra báo cáo Đánh giá (`*_audited_*.md`).
*   **Tính năng bổ sung:** 
    *   **Hỏi BA:** Dùng skill `qc-ask-ba` để trích xuất thắc mắc vào file `question-backlog`.
    *   **Re-audit:** Gọi `/review-uc` để AI đọc lại phản hồi từ BA và cập nhật version mới cho bản Audit.

### 🟡 Bước 2: Thiết kế kịch bản kiểm thử (Scenario Design)
*   **Mục đích:** Xây dựng chiến lược test bao quát Happy Path & Edge Case.
*   **Ra lệnh:** Lệnh `/qc-design-scenarios`.
*   **Kết quả:** File kịch bản Markdown tại thư mục `scenarios/[UC-ID]/`.

### 🔵 Bước 3: Viết Ca kiểm thử chi tiết (Test Case Design)
Hệ thống hỗ trợ 2 cấp độ thiết kế:
*   **Cấp độ 1 (High-Level):** Lệnh `/design-testcases-hl`. Sinh bộ case rút gọn (5–15 cases) cho Smoke/Sanity test.
*   **Cấp độ 2 (Detail-Level):** Lệnh `/design-testcases-det`. Sinh bộ case đầy đủ (80+ cases) phủ kín 6 Phases, BVA, RBAC.
*   **Tiêu chuẩn Harden:** Bắt buộc dùng Action Keywords, Atomic Steps, State-based ER (UI/API/DB) và 100% AC Coverage (Traceability Matrix).

### 🔴 Bước 4: Thực thi kiểm thử (Test Execution)
*   **Mục đích:** Chạy Test Case trên môi trường thật và báo cáo kết quả.
*   **Ra lệnh:** Lệnh `/execute-testcases`.
*   **Tính năng nâng cao:** 
    *   **ERA Audit:** AI từ chối chạy nếu bộ Test Case < 70 điểm.
    *   **Self-Healing:** Tự động vá Locator hỏng qua Accessibility Tree.
    *   **Triple-Layer Verification:** Đối soát UI -> API -> DB PostgreSQL.
    *   **AQG Hậu kiểm:** AI giải trình logic Pass/Fail (Internal Note) và cung cấp Trace ID/Error Stack.

### ⚡ Bước 5: Kiểm thử Hiệu năng (Performance Testing)
*   **Lệnh:** `/performance-testing`.
*   **Quy trình:** Agent đề xuất thông số tải (VUs, Duration) -> User xác nhận -> Sinh Script (JMeter/k6).
*   **Đặc biệt:** Tự động xử lý Dữ liệu Động (Token/OTP) và sinh mã TOTP bằng Groovy.

### 🔍 Bước 6: Quản trị Thay đổi (Impact Analysis)
*   **Lệnh:** `/impact-analysis`.
*   **Mục đích:** Khoanh vùng chính xác khu vực cần kiểm thử lại khi có Change Request (CR).
*   **Kết quả:** Liệt kê các Test Cases bị ảnh hưởng dựa trên ma trận phụ thuộc.

---

## ⏰ Tự động hóa Báo cáo (Jira Automation)

> [!CAUTION]
> **Cấu hình Token (Bắt buộc)**
> nạp API Token vào biến môi trường Windows để AI có quyền truy cập Jira:
> ```powershell
> [System.Environment]::SetEnvironmentVariable('JIRA_API_TOKEN', 'Mã_Token_Của_Bạn', 'User')
> ```

*   **Chạy thủ công:** `python .agents/scripts/jira_daily_cron.py`
*   **Thiết lập lịch (9:00 AM hằng ngày):**
    ```powershell
    schtasks /create /tn "JOYS_JiraDailyReport" /tr "python %CD%\.agents\scripts\jira_daily_cron.py" /sc daily /st 09:00 /f
    ```

---

## 🚀 Lệnh Git cơ bản (Git Workflow)

| Hành động | Lệnh thực thi |
| :--- | :--- |
| **Tạo nhánh** | `git checkout -b feature/UC-XXX-name` |
| **Commit** | `git commit -m "feat(UC-XXX): mô tả nội dung"` |
| **Đẩy code** | `git push origin [branch-name]` |
| **Hoàn tác** | `git reset --soft HEAD~1` |

---

## 📌 Các quy tắc người dùng cần nhớ

1.  **Chạy thử & Đánh giá:** Hãy bảo AI liệt kê chi tiết các bước đã thực hiện để hiểu cách vận hành.
2.  **Model Selection:** Ưu tiên dùng model có khả năng suy luận mạnh (Claude 3.5 Sonnet/Opus) cho các task QA phức tạp.
3.  **Zero-Overwrite:** Mọi file đầu ra luôn chứa version (`v1`, `v2`,...). AI **KHÔNG ĐƯỢC PHÉP** ghi đè file cũ.
4.  **Audit First:** Luôn có quyền ngưng pipeline nếu Requirement quá sơ sài. Hãy yêu cầu sửa tài liệu trước khi test design.
5.  **Security:** Tuyệt đối không lưu mật khẩu thật vào `project-config.md`.

---
*Last Updated: 2026-05-14 | Powered by JOYS Framework*