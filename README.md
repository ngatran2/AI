# JOYS - Just Optimize Your Workforce

Dự án này là một không gian làm việc (workspace) dựa trên Agentic Frameworkm - tối ưu hóa "lao động" AI, được thiết kế để tự động hóa quy trình làm việc thực tế của QC, bao gồm từ  bước phân tích tài liệu nghiệp vụ, thiết kế và thiết kế kiểm thử. Hệ thống sử dụng các AI Agent chạy các luồng công việc (workflows) tuần tự để tự động đọc, phân tích tài liệu yêu cầu, và sinh ra kịch bản kiểm thử (Test Scenarios) cũng như ca kiểm thử chi tiết (Test Cases).

## 🚀 Điểm nhấn & Giá trị cốt lõi (Key Highlights)

Dành cho mục đích sharing và thấu hiểu nhanh sức mạnh của hệ thống:

### 1. Chiến lược Thiết kế Test Case (Smart Design Strategy)
*   **Phân cấp linh hoạt (HL vs DET):** Tùy chọn giữa tốc độ (High-level: 5-15 cases trọng yếu) và độ phủ (Detail-level: 30-80+ cases biên). Giúp tối ưu hóa chi phí token và thời gian chạy.
*   **Tiêu chuẩn "Bước Nguyên Tử" (Atomic Steps):** Mọi test case đều được viết theo chuẩn Action Keywords `[Click]`, `[Input]`, `[Verify]`. Điều này biến tài liệu Excel thành "mã nguồn" mà cả người và máy (Automation) đều hiểu thống nhất 100%.
*   **Xác thực 3 lớp (Triple-Layer Verification):** Không dừng lại ở việc check hiển thị (UI), AI bắt buộc phải đối soát dữ liệu (Database) và logic nghiệp vụ xuyên suốt.
*   **Phân quyền (RBAC) mặc định:** Tự động gen kịch bản cho ít nhất 5 Roles tiêu chuẩn, đảm bảo an toàn dữ liệu tuyệt đối.

### 2. Hệ thống Thực thi "Thông minh & Tin cậy" (Reliable Execution)
*   **ERA Audit (Quality Gate đầu vào):** Hệ thống sẽ từ chối chạy nếu bộ test case không đủ điểm chất lượng (>70). Đảm bảo không phí thời gian vào kịch bản sai.
*   **Antigravity Quality Gate (AQG - Hậu kiểm):** AI không chỉ báo Pass/Fail mà phải giải trình được logic (Internal Note) và cung cấp bằng chứng DOM/Clipboard/Logs. Loại bỏ hoàn toàn tình trạng báo cáo "Pass giả".
*   **Self-Healing & Tối ưu tốc độ:** Tự động sửa Locator bị hỏng và tái sử dụng Session/State, giúp tốc độ thực thi nhanh gấp 5 lần so với các luồng automation truyền thống.
*   **MCP Integration:** Kết nối trực tiếp vào "nội tạng" hệ thống (DB/Logs) để bắt lỗi tầng sâu thay vì chỉ nhìn bề mặt UI.

---

## 📊 Quản lý dự án (Project Management)
Tất cả tiến độ, sức khỏe dự án (Health Check) và ma trận truy vết (RTM) được cập nhật liên tục tại:
- **Master Dashboard:** [PROJECT_MASTER_DASHBOARD_20260508_v2.md](file:///d:/AI/Newtemplate/report/PROJECT_MASTER_DASHBOARD_20260508_v2.md)
> [!TIP]
> Hãy mở file này để có cái nhìn tổng quan về trạng thái của từng Use Case (Audit, Scenario, Test Case, Execute).

---

## 📂 Cấu trúc dự án

Dự án tuân thủ theo nguyên tắc phân chia thư mục rõ ràng, phục vụ chặt chẽ cho từng bước trong quy trình Pipeline.

### Thư mục hệ thống Agent

- **`.agents/`**: Trái tim của hệ thống, chứa toàn bộ cấu hình, quy tắc, kỹ năng và luồng làm việc của các AI Agent.

  - `agents/`: Nơi định nghĩa các persona của AI như `docs-reader` (đọc tài liệu), `requirement-reviewer` (đánh giá yêu cầu), `qa-engineer` (thiết kế test).
  - `rules/`: Chứa các quy tắc hệ thống bắt buộc chạy (workflow chính, chuẩn đặt tên file `naming-convention.md`, chuẩn đầu ra,...).
  - `skills/`: Chứa các kỹ năng chuyên biệt mà AI có thể thực hiện (ví dụ: `qc-uc-review`, `qc-scenario-design`, `qc-api-automation`, `performance-testing`, `pdf`, `qc-ask-ba`,...).
  - `workflows/`: Điểm kích hoạt các luồng công việc toàn diện theo dạng lệnh tắt (slash/command) như `/qc-review-uc`, `/qc-design-testcases-hl`, `/qc-design-testcases-det`, `/qc-api-test-gen`, `/execute-testcases`, `/performance-testing`.

### Thư mục làm việc theo Pipeline

- **`requirements/`**: Nơi lưu trữ tài liệu đặc tả yêu cầu (Use Case) đầu vào. Sau khi AI chạy quy trình review, các tài liệu "audited" (đã đánh giá xong) cũng sẽ được lưu trữ tại đây theo từng nhóm `UC-ID`.
- **`scenarios/`**: Chứa kịch bản kiểm thử (Test Scenarios) dưới dạng tệp tin Markdown. File sinh ra chứa các hướng kiểm thử tích cực (happy path) và tiêu cực (edge case).
- **`testcases/`**: Nơi lưu trữ bộ ca kiểm thử chi tiết (Test Cases) ở định dạng bảng tính Excel (`.xlsx`). Test case có các các bước step-by-step rõ ràng để Tester thực thi.
- **`execution/`**: Lưu trữ các báo cáo kiểm thử khi tiến hành kiểm thử thủ công/với trình duyệt ở bước thực thi.
- **`scratch/`** và một số file Python tạm (`scratch_*.py`): Không gian lưu các đoạn script Python (ví dụ để hỗ trợ gen ra file Excel) và tệp tạm trong quá trình AI tính toán và xử lý tự động hóa.

---

## Hướng dẫn sử dụng dự án

Tiến trình làm việc được chia thành các bước tuần tự một cách nghiêm ngặt. Hệ thống sẽ luôn hoạt động thông qua việc người dùng gọi lệnh `/slash_command` hoặc gõ prompt yêu cầu để hệ thống thực hiện nghiệp vụ.

### Bước 1: Phân tích & Đánh giá Yêu cầu (Requirement Audit)

*Mục đích: Đánh giá tính đầy đủ, minh bạch và phát hiện lỗi/lỗ hổng của tài liệu requirement hiện tại.*

- **Thực hiện:** Đặt tài liệu Yêu cầu (DOCX, PDF, URL...) vào thư mục mã dự án (ví dụ `requirements/UC-101/`).
- **Ra lệnh:** Sử dụng lệnh `/qc-review-uc` (Hoặc chat: *"Review requirement/uc cho file/link này..."*)
- **Kết quả:** Hệ thống đọc file (trích xuất nội dung từ url, hoặc gọi skill pdf nếu là file pdf) và sinh ra một bản báo cáo Đánh giá (`*_audited_*.md`).
- **Output:** Nếu kết quả review xuất hiện nhiều vấn đề/câu hỏi cần làm rõ từ phía BA, bạn có thể chạy tiếp lệnh tính năng: *"Hỏi BA các câu hỏi của [UC-ID]"* để AI trích xuất các thắc mắc từ file audited vào file question-backlog cho từng UC-ID (sử dụng skill `qc-ask-ba`), sau đó bạn gửi file này cho BA nhờ trả lời và confirm giúp các vấn đề.
- **Re-audit**: Sau khi có các câu trả lời của BA vào file question-backlog, bạn hãy gọi /review-uc Hãy re-audit lại UC-ID, AI sẽ đọc lại nội dung đã audited, đọc lại UC xem có thay đổi gì không, và đọc nội dung trả lời từ BA, tiến hành audit lại và tạo version mới.

### Bước 2: Thiết kế kịch bản kiểm thử (Scenario Design)

*Dựa trên file yêu cầu đã được làm sạch và chuẩn hóa ở bước một nhằm chuẩn bị chiến lược test.*

- **Thực hiện:** Đảm bảo file _audited_ hợp lệ.
- **Ra lệnh:** Gõ lệnh `/qc-design-scenarios` (Hoặc chat *"Hãy thiết kế scenario cho UC-101"*).
- **Kết quả:** Sinh ra một file kịch bản bao quát nằm ở thư mục `scenarios/[UC-ID]/`.

### Bước 3: Viết Ca kiểm thử chi tiết (Test Case Design)

*Mục đích: Đưa ra định dạng Excel cho file testcase, chia theo từng action một cách cụ thể, đầy đủ test data & expected result. Dự án hỗ trợ 2 cấp độ thiết kế tùy theo nhu cầu:*

- **Cấp độ 1: High-Level (HL) — Lệnh `/design-testcases-hl`**
    - **Mục tiêu:** Sinh bộ case rút gọn (5–15 cases) tập trung vào Happy Path và các lỗi Critical.
    - **Sử dụng khi:** Cần kiểm tra nhanh (Smoke/Sanity test), validate hotfix hoặc chạy trong CI/CD gate.
- **Cấp độ 2: Detail-Level (DET) — Lệnh `/design-testcases-det`**
    - **Mục tiêu:** Sinh bộ case đầy đủ (30–80+ cases) phủ kín 6 Phases, Edge Cases, BVA, RBAC và Logic nghiệp vụ phức tạp.
    - **Sử dụng khi:** Kiểm thử hồi quy toàn diện (Full Regression), nghiệm thu tính năng mới hoặc chuẩn bị release.

- **Tiêu chuẩn chất lượng & Cấu trúc (Harden Standard - Áp dụng cho cả 2 cấp độ):**
    - **Action Keywords & Atomic Steps:** Ép buộc sử dụng bộ động từ chuẩn hóa (VD: `[Input]`, `[Click]`, `[Verify]`) và mỗi dòng chỉ chứa duy nhất một bước nguyên tử.
    - **Object + Location & Explicit Data:** Định danh đối tượng qua vị trí cụ thể và bắt buộc sử dụng dữ liệu tường minh (không tự suy luận, sử dụng Dynamic Data Placeholders như `{{timestamp}}`).
    - **RBAC & CRUD Compliance:** Bắt buộc phủ kín các quyền tiêu chuẩn và luôn sinh case kiểm thử vết hệ thống (Audit Trail).
    - **Strict Verbatim & Template Guard:** Trích xuất nguyên văn 100% text thông báo, tuân thủ định dạng Template v2.
    - **Expected Result 3 lớp:** Xác thực đồng thời UI (Giao diện) -> Data (Dữ liệu/DB) -> Logic (Nghiệp vụ).
    - **API Testing Integration:** Nếu tài liệu đầu vào là Swagger/OpenAPI, hệ thống hỗ trợ lệnh `/qc-api-test-gen` để tự động sinh bộ Test Case API và các script automation (JSON/Python) với đầy đủ assertion logic.
    - **Anti-Hallucination:** Tuyệt đối không "bịa" dữ liệu. Các phần thiếu thông tin sẽ được đánh dấu `[TBD]`.

- **Kết quả:** File Excel sẽ được lưu tại `testcases/[UC-ID]/` với hậu tố tương ứng:
    - `*_testcases-hl_*.xlsx` (cho High-level)
    - `*_testcases-det_*.xlsx` (cho Detail-level)

### Bước 4: Thực thi kiểm thử (Test Execution)

*Mục đích: Thực hiện chạy các Test Case đã thiết kế trên môi trường thật (Manual hoặc Automation) và báo cáo kết quả.*

- **Thực hiện:** Đảm bảo đã có file Test Case Excel tại thư mục `testcases/`.
- **Ra lệnh:** Gõ lệnh `/execute-testcases` (Hoặc chat *"Chạy test cho UC-101"*).
- **Cơ chế đặc biệt (Advanced Features):**
    - **Execution Readiness Audit (ERA):** AI tự chấm điểm bộ Test Case (ERA Score). Nếu < 70 điểm (không đủ chất lượng để chạy), AI sẽ từ chối thực thi và yêu cầu sửa lại.
    - **Triple-Layer Defense System:** Tích hợp Zero-Skip (không được bỏ qua step), Deep Evidence (trích xuất DOM/Clipboard) và Fault Injection.
    - **Lean Evidence & Direct Navigation:** Chỉ chụp ảnh lưu bằng chứng khi FAIL/ERROR để làm nhẹ báo cáo; áp dụng Direct-First Navigation (truy cập URL trực tiếp) trước khi thao tác UI rườm rà.
    - **Self-Healing Loop:** Tự động phát hiện và vá lỗi Locator bị hỏng trong quá trình chạy Automation thông qua Snapshot DOM & Accessibility Tree (ưu tiên `getByRole`, `getByLabel`).
    - **MCP Integration (Optional):** Kết nối trực tiếp với Database/Logs để xác minh dữ liệu tầng sâu (Layer 2) và trích xuất Trace ID/Error Stack khi gặp lỗi.
    - **Session Reuse & State Inheritance:** Tái sử dụng phiên đăng nhập và kế thừa bộ lọc/state giữa các case tuần tự (workers: 1) giúp tăng tốc độ thực thi tự động hóa gấp 5 lần.
    - **Antigravity Quality Gate (AQG):** Khâu hậu kiểm bắt buộc sau khi chạy xong để đánh giá:
        - **Độ tin cậy (Reliability):** Loại bỏ False Positive thông qua việc đối chiếu chéo (Cross-check) giữa UI Evidence và API/DB Logs.
        - **Độ hiểu (Cognitive Validation):** AI phải cung cấp "Internal Note" giải thích logic tại sao Case đó Pass/Fail, chứng minh sự thấu hiểu nghiệp vụ thay vì chỉ so khớp text đơn thuần.
        - **Khả năng thực thi & Bằng chứng:** Đảm bảo mọi bước Fail đều có bằng chứng (Trace ID, Error Stack, Screenshot) tường minh, phục vụ việc tái hiện lỗi (reproducible) 100%.
- **Kết quả:** Báo cáo kết quả kiểm thử (Pass/Fail) cập nhật trực tiếp vào file Excel (kế thừa hậu tố `-hl` hoặc `-det`) và lưu tại thư mục `execution/[UC-ID]/functional-test/`.

### Bước 5: Kiểm thử Hiệu năng (Performance Testing)

*Mục đích: Đánh giá khả năng chịu tải, tính ổn định và xác định điểm nghẽn (bottlenecks) của hệ thống thông qua các kịch bản Load, Spike, Stress Test.*

- **Thực hiện:** Đảm bảo đã xác định được UC-ID hoặc cung cấp luồng API/số lượng người dùng mô phỏng.
- **Ra lệnh:** Gõ lệnh `/performance-testing` cho chức năng cụ thể.
- **Quy trình tương tác (Mandatory):** 
    1. Agent phân tích Requirement và **Yêu cầu User cung cấp thông số tải** (VUs, Duration, KPIs).
    2. Nếu User không có thông số cụ thể, Agent sẽ **Tự động Suggest** cấu hình tối ưu dựa trên môi trường (Staging/Prod).
    3. User xác nhận đề xuất -> Agent mới bắt đầu sinh Plan và Script.
- **Cơ chế đặc biệt (Advanced Features):**
    - **Tự động xử lý Dữ liệu Động (Dynamic Data Bypass):** Tự động phân tích requirement để xử lý các bài toán sinh mã OTP runtime (TOTP bằng Groovy), Extract Token, Bypass 2FA cho kịch bản Load Test.
    - **Sinh Script Native:** Tự động cung cấp các đoạn mã JSR223 Groovy (JMeter) hoặc JavaScript (k6) cùng hướng dẫn cấu hình chi tiết trên công cụ.
    - **Chuẩn bị Dữ liệu (Test Data Generation):** Tạo sẵn các file `.csv` chứa thông tin test user hợp lệ (Email, Pass, Secret Key) để đưa vào JMeter/k6.
- **Kết quả:** Sinh ra một bản Kế hoạch (Performance Test Plan) đầy đủ KPIs, kèm theo file script/data lưu tại `execution/[UC-ID]/performance-test/`.

### Bước 6: Quản trị Thay đổi & Hồi quy (Impact Analysis)

*Mục đích: Khoanh vùng chính xác khu vực cần kiểm thử lại (Mini-Regression Suite) khi có Change Request (CR) hoặc thay đổi logic lõi từ khách hàng, thay vì phải chạy lại toàn bộ hệ thống.*

- **Thực hiện:** Cung cấp file Requirement bản cũ (v[N-1]) và bản mới (v[N]), hoặc đoạn text mô tả sự thay đổi.
- **Ra lệnh:** Gõ lệnh `/impact-analysis`.
- **Cơ chế thông minh:**
  - **Delta Analysis:** Lọc độ nhiễu, tự động bỏ qua các thay đổi không cốt lõi như typo hay text UI.
  - **Dependency Traceability:** Dựa vào `Integration_flow.md` để dò tìm các module bị lây nhiễm (Ví dụ: Đổi logic API Login -> Tự động flag các Use Case đang xài hàm check Token).
- **Kết quả:** File báo cáo `Impact_Analysis_[YYYYMMDD].md` liệt kê đích danh các Test Cases/Scenarios của các module vệ tinh cần phải đưa vào chu kỳ chạy Regression.

---

## 📌 Các quy tắc người dùng cần nhớ

- Hãy chạy thử 1 task từ bước phân tích nghiệp vụ để đánh giá kết quả, bảo AI liệt kê các bước chi tiết AI đã thực hiện để hiểu về cách hoạt động của dự án.
- Bạn có thể dùng bất cứ model nào để hỏi-đáp, tìm hiểu, nhưng **để chạy tasks PHẢI dùng model có khả năng suy luận mạnh (như Claude 3.5 Sonnet hoặc Opus)** để đảm bảo kết quả ổn định và tuân thủ các logic QA phức tạp.
- Mọi file đầu ra của toàn bộ giai đoạn luôn chứa version `v1`, `v2`, v.v... Hệ thống đã được lập trình **KHÔNG ĐƯỢC PHÉP ghi đè** lên file cũ do AI sinh ra nhằm mục đích quản lý các thay đổi và soát xét lịch sử.
- Bạn luôn có toàn quyền để ngưng một quy trình (stop pipeline) nếu phát hiện tài liệu yêu cầu (Requirement) sơ sài, thiếu quá nhiều thông tin. Hãy yêu cầu sửa Requirements trước khi chuyển đến bước test design.
- **Security Note:** Tuyệt đối không lưu mật khẩu thật vào file `project-config.md`. Hãy sử dụng mô tả cách lấy credentials hoặc dùng biến môi trường.
