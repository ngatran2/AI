# 🌌 JOYS - Just Optimize Your Workforce

Dự án này là một không gian làm việc (workspace) dựa trên **Agentic Framework** - tối ưu hóa "lao động" AI, được thiết kế để tự động hóa quy trình làm việc thực tế của QC, bao gồm từ bước phân tích tài liệu nghiệp vụ, thiết kế và thiết kế kiểm thử. Hệ thống sử dụng các AI Agent chạy các luồng công việc (workflows) tuần tự để tự động đọc, phân tích tài liệu yêu cầu, và sinh ra kịch bản kiểm thử (Test Scenarios) cũng như ca kiểm thử chi tiết (Test Cases).

---

## 🚀 Điểm nhấn & Giá trị cốt lõi (Key Highlights)

> [!TIP]
> **1. Chiến lược Thiết kế Test Case (Smart Design Strategy)**
> *   **Phân cấp linh hoạt (HL vs DET):** Tùy chọn giữa tốc độ (High-level: 5-15 cases trọng yếu) và độ phủ (Detail-level: 30-80+ cases biên). Giúp tối ưu hóa chi phí token và thời gian chạy.
> *   **Tiêu chuẩn "Bước Nguyên Tử" (Atomic Steps):** Mọi test case đều được viết theo chuẩn Action Keywords `[Click]`, `[Input]`, `[Verify]`. Điều này biến tài liệu Excel thành "mã nguồn" mà cả người và máy (Automation) đều hiểu thống nhất 100%.
> *   **Đối soát đa lớp linh hoạt (Flexible Multi-Layer):** AI hỗ trợ 3 chế độ xác thực tùy theo độ sẵn sàng của hệ thống: API-Only (Backend xong), UI+DB (Frontend xong) hoặc Triple-Link (UI -> API -> DB). Giúp phát hiện lỗi logic tầng sâu ngay từ giai đoạn sớm.
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
| **Extensions** | `Zixfel Extension` | Truy cập DOM, giải mã OTP/2FA runtime & cho phép nhấn Auto Run ở phần chat |
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
    *   **Technical Spec Sync:** AI chủ động rà soát và yêu cầu User cung cấp Input/Output API hoặc Data Schema nếu tài liệu còn thiếu để phục vụ thiết kế test case chi tiết.
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
    *   **Execution Mode Sync:** AI luôn hỏi User để chọn 1 trong 3 chế độ: 1. API-Only, 2. UI+DB, 3. Triple-Link (Full).
    *   **ERA Audit:** AI từ chối chạy nếu bộ Test Case < 70 điểm.
    *   **Self-Healing:** Tự động vá Locator hỏng qua Accessibility Tree.
    *   **Triple-Layer Verification:** Đối soát linh hoạt tùy theo Mode đã chọn.
    *   **Báo cáo bắt buộc:** Summary phải bao gồm phân loại lỗi **RCA (R1-R4)**, **Mật độ lỗi (DD%)** và **Điểm tin cậy (Reliability Score)** dựa trên bằng chứng đa lớp.
    *   **AQG Hậu kiểm:** AI giải trình logic Pass/Fail (Internal Note) và cung cấp Trace ID/Error Stack.

### 🛡️ Giao thức Retest & Độ ổn định (Step 4+)
*   **Đánh giá Độ ổn định (Stability Rating):**
    *   🟢 **Green (Stable):** DD% < 5%.
    *   🟡 **Yellow (At Risk):** DD% 5% - 15%.
    *   🔴 **Red (Unstable):** DD% > 15%.
*   **Điều kiện Re-run ngay lập tức:** Khi điểm **Reliability < 80%** do lỗi môi trường hoặc script (R3/R4).
*   **Điều kiện Full Regression:** Khi module bị đánh dấu **🔴 Red (Unstable)**, bắt buộc chạy lại toàn bộ bộ test sau khi fix.

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

## 💡 Mẹo làm việc hiệu quả với AI (AI Collaboration Tips)

Để tối ưu hóa chi phí token và đảm bảo AI hoạt động minh mẫn nhất, hãy áp dụng các mẹo sau:

1.  **Tóm tắt & Reset (Checkpointing):** Khi phiên chat quá dài hoặc tiêu thụ lượng Token lớn (thường trên 65% dung lượng), AI sẽ có hiện tượng "giảm trí nhớ" và trả lời kém chính xác hơn. Hãy yêu cầu AI tóm tắt trạng thái hiện tại thành một bản Checkpoint và sử dụng nó để bắt đầu một phiên chat mới nhằm khôi phục 100% khả năng tư duy.
2.  **Audit ngược (Self-Critique):** Sau khi AI hoàn thành task, hãy ra lệnh: *"Hãy đóng vai QC Lead khó tính, chỉ ra 3 điểm yếu trong kết quả này và cách khắc phục"*.
3.  **Tư duy trước khi làm (Chain-of-Thought):** Yêu cầu AI *"Giải thích logic thực hiện trước khi viết code"* để tránh sai sót ngay từ đầu.
4.  **Chia nhỏ task (Atomic Prompts):** Chia các yêu cầu lớn thành các bước nhỏ tuần tự để AI tập trung tối đa độ chính xác.
5.  **Negative Constraints:** Sử dụng lệnh phủ định như *"Tuyệt đối không ghi đè file X"* hoặc *"Bỏ qua các giải thích dài dòng, chỉ trả về kết quả JSON"*.
6.  **Cung cấp ví dụ (Few-shot Prompting):** AI học tốt nhất qua ví dụ. Nếu bạn muốn kết quả theo một style nhất định, hãy đưa cho nó 1-2 mẫu (ví dụ: *"Đây là mẫu Test Case tôi thích, hãy làm theo format này..."*).
7.  **Yêu cầu bằng chứng (Evidence-based):** Để tránh AI tự suy diễn (hallucination), hãy ra lệnh: *"Hãy trích dẫn số dòng hoặc tên file tài liệu cho mỗi lỗi logic bạn tìm thấy"*.
8.  **Xác nhận trước khi ghi (Safe-to-Run):** Với các task sửa đổi hàng loạt file, hãy bảo AI: *"Hãy liệt kê danh sách các file bạn định thay đổi và tóm tắt nội dung sửa trước khi thực hiện"*.

---

## 📚 Các mẫu câu lệnh phổ biến (Prompting Guide)

> [!IMPORTANT]
> **Lưu ý về xử lý yêu cầu phức tạp (Long/Complex Prompts):**
> Nếu bạn có một yêu cầu quá dài, nhiều ý tưởng hoặc cần nhiều đầu ra (outputs) cùng lúc, hãy xử lý theo 2 cách để đảm bảo hiệu quả cao nhất:
> 1. **Phân chia theo giai đoạn (Phasing):** Tự chia nhỏ yêu cầu thành `Phase 1: Yêu cầu 1, 2`, `Phase 2: Yêu cầu 3, 4` và ra lệnh tuần tự.
> 2. **Lập kế hoạch trước (Plan First):** Nhập hết yêu cầu và bảo AI: *"Hãy đề xuất một kế hoạch thực thi (Execution Plan) chi tiết cho các yêu cầu này"*. Sau khi bạn duyệt Plan, AI sẽ chạy từng bước.
>
> **Quy tắc vàng:** Tốt nhất là một prompt nên tập trung vào **01 Workflow** hoặc **01 Skill** cụ thể. Điều này giúp AI tập trung trí tuệ, tránh câu trả lời loãng, sơ sài hoặc thiếu chính xác.

Để tương tác hiệu quả với Antigravity, bạn nên sử dụng các mẫu câu lệnh (prompts) được phân loại theo mục đích dưới đây. Việc xác định đúng loại prompt giúp AI kích hoạt đúng "skill" và persona cần thiết.

### 1. Câu ra lệnh trực tiếp (Command / Action Prompt)
*Dùng khi cần AI thực hiện task cụ thể, thực thi mã nguồn hoặc chạy skill.*
*   **Mẫu prompt:** 
    *   `Analyze this repository structure.`
    *   `Review UC-101 và chỉ ra các điểm thiếu logic nếu có.`
    *   `Run test and fix failed cases.`
    *   `Generate API documentation for login module.`
    *   `Hãy thực hiện task X, nếu có gì chưa rõ hãy hỏi ngược lại tôi trước khi làm.`

### 2. Câu yêu cầu phân tích (Analysis Prompt)
*AI đóng vai Senior/Dev Lead để phân tích sâu về kiến trúc hoặc nguyên nhân gốc rễ.*
*   **Mẫu prompt:** 
    *   `Review architecture of this project.`
    *   `Phân tích tại sao luồng login 2FA hay bị timeout ở môi trường Staging.`
    *   `Compare Playwright vs Selenium for this specific system.`
    *   `Find security risks in the current authentication code.`

### 3. Câu đánh giá (Evaluation / Review Prompt)
*AI đưa nhận xét, scoring, ưu nhược điểm và chỉ ra các vi phạm tiêu chuẩn.*
*   **Mẫu prompt:** 
    *   `Evaluate code quality of the performance script.`
    *   `Review bộ Test Cases này như một Senior QC Lead.`
    *   `Is this API design good for scalability?`
    *   `Đánh giá file audited này đã đủ độ tin cậy để chuyển sang bước Design chưa?`

### 4. Câu hỏi "Nên hay không nên" (Decision / Recommendation Prompt)
*Hỗ trợ ra quyết định dựa trên các yếu tố ràng buộc như thời gian, ngân sách, nhân sự.*
*   **Mẫu prompt:** 
    *   `Với hotfix này, tôi nên chạy bộ test HL hay DET để tối ưu thời gian?`
    *   `Should we automate this complex UI flow or keep it manual?`
    *   `Nên ưu tiên kiểm thử API hay UI cho module này để phát hiện lỗi logic nhanh nhất?`
    *   *Mẹo: Hãy cung cấp thêm team size, deadline để AI tư vấn sát hơn.*

### 5. Câu Brainstorming & Đề xuất (Solutioning Prompt)
*Khai phá ý tưởng mới hoặc tìm giải pháp cho các vấn đề kỹ thuật khó.*
*   **Mẫu prompt:** 
    *   `Suggest ways to improve test execution speed.`
    *   `Brainstorm giúp tôi 10 edge cases cực khó cho tính năng thanh toán.`
    *   `How can we improve test coverage without increasing token cost?`
    *   `Suggest a monitoring strategy for this microservice system.`

### 6. Câu giả lập vai trò (Role Simulation / Persona)
*Bắt AI đóng vai cụ thể để có góc nhìn chuyên gia.*
*   **Mẫu prompt:** 
    *   `Act as a senior DevOps engineer and review the CI/CD pipeline.`
    *   `Hãy đóng vai một ISTQB Advanced Tester để đánh giá chiến lược test này.`
    *   `Act as a security reviewer to find vulnerabilities in the DB connection.`

### 7. Câu quy trình đa bước (Multi-step Workflow)
*Yêu cầu AI thực hiện một chuỗi hành động liên tiếp, tự động hóa pipeline.*
*   **Mẫu prompt:** 
    *   `Read logs → Detect root cause → Suggest fix → Generate test cases.`
    *   `Thực hiện audit UC-101 → Design scenarios → Generate testcase-hl.`
    *   `Read repository → Identify critical modules → Generate test plan.`

### 8. Cấu trúc Prompt tối ưu cho Coding Agent
*Để nhận được kết quả tốt nhất (Best Practice), hãy soạn prompt theo cấu trúc:*
1.  **Goal:** Mục tiêu cuối cùng là gì?
2.  **Context:** Bối cảnh, file liên quan, môi trường.
3.  **Constraints:** Ràng buộc (không ghi đè file, không dùng thư viện ngoài...).
4.  **Expected Output:** Định dạng kết quả (JSON, Markdown, Code...).
5.  **Priority:** Ưu tiên tính năng nào trước.

*   **Ví dụ:** 
    > **Goal:** Optimize API performance.
    > **Context:** API Login đang phản hồi > 2s ở file `auth.js`.
    > **Constraints:** Không sửa đổi cấu trúc Database.
    > **Expected Output:** Đoạn code đã tối ưu và báo cáo so sánh performance.

---

## 📌 Các quy tắc người dùng cần nhớ

1.  **Chạy thử & Đánh giá:** Hãy bảo AI liệt kê chi tiết các bước đã thực hiện để hiểu cách vận hành.
2.  **Model Selection:** Ưu tiên dùng model có khả năng suy luận mạnh (Claude 3.5 Sonnet/Opus) cho các task QA phức tạp.
3.  **Zero-Overwrite:** Mọi file đầu ra luôn chứa version (`v1`, `v2`,...). AI **KHÔNG ĐƯỢC PHÉP** ghi đè file cũ.
4.  **Audit First:** Luôn có quyền ngưng pipeline nếu Requirement quá sơ sài. Hãy yêu cầu sửa tài liệu trước khi test design.
5.  **Security:** Tuyệt đối không lưu mật khẩu thật vào `project-config.md`.

---
*Last Updated: 2026-05-14 | Powered by JOYS Framework*
