# QA Shared Glossary (Từ điển Thuật ngữ Dùng chung)

Tài liệu này định nghĩa các thuật ngữ kỹ thuật và quy chuẩn đánh giá bắt buộc phải dùng chung cho toàn bộ Agent (Requirement Reviewer, QA Designer, Test Executor) để tránh phân mảnh ngữ cảnh.

## 1. Mức độ Rủi ro & Chiều sâu Xác thực (Risk-Based Validation Depth)
Quyết định mức độ khắt khe khi kiểm tra một Test Case:
- **Low Risk:** Chỉ yêu cầu UI Expected Result (Check hiển thị giao diện).
- **Medium Risk:** Yêu cầu UI + API Expected Payload.
- **High Risk:** Yêu cầu UI + API + DB Expected State.
- **Critical Risk (Payment, Auth):** Yêu cầu tối đa 4 lớp (UI + API + DB + Business Rule Assertion).

## 2. Rò rỉ Logic (Enterprise Leakage Detection)
Hiện tượng "Pass Giả" - Giao diện báo thành công nhưng bên dưới hệ thống bị lỗi hoặc ghi nhận sai. Phân loại theo 4 cấp (L1-L4):
- **L1 (UI/API Mismatch):** UI báo Pass nhưng mã HTTP hoặc Payload API trả về sai.
- **L2 (DB Persistence Failure):** API báo Pass (200/201) nhưng Database không ghi nhận record hoặc ghi dở dang (Partial write).
- **L3 (Replication / Async Delay):** DB Master đã ghi nhận nhưng DB Replica chưa đồng bộ, hoặc Event bị kẹt trong Queue xử lý.
- **L4 (Cross-service Inconsistency):** Lệch data giữa các Microservices (VD: Payment báo Success nhưng số dư Wallet không đổi).

## 3. Phân loại Lỗi & Ổn định (RCA & Stability)
- **Flaky Test:** Lỗi chập chờn không do logic code mà do môi trường, infra, xung đột dữ liệu (Parallel Conflict) hoặc độ trễ UI (Timing). Biểu hiện: Chạy lần 1 Fail, chạy lần 2 Pass.
- **RCA (Root Cause Analysis) R1-R4:**
  - `[R1] Actual Bug`: Lỗi thực sự do Code sai so với Requirement.
  - `[R2] Req Gap`: Tài liệu thiếu/sai/lỗi thời khiến Test fail.
  - `[R3] Infra/Env`: Lỗi do môi trường sập, mạng lag, hết hạn Auth.
  - `[R4] Script Flaw`: Lỗi do script automation (locator hỏng, sleep cứng).
- **Weighted Defect Score:** Điểm độ nát của hệ thống được tính theo trọng số: Critical (x5), High (x3), Medium (x2), Low (x1).

## 4. Các thuật ngữ Automation
- **Correlation ID (Trace ID):** Khóa định danh duy nhất (VD: Transaction ID) dùng để truy vết xuyên suốt vòng đời từ UI -> API -> DB để đối chiếu bằng chứng (Evidence Correlation).
- **Parallel by Namespace:** Chạy song song nhiều worker nhưng bắt buộc cách ly tập dữ liệu/tài khoản hoàn toàn để tránh đụng độ (Parallel Conflict).
- **Commit Stability Window:** Quãng thời gian trễ có chủ ý (Wait 3-5s hoặc Polling) trước khi Query DB đối với các hệ thống Queue/Async để chống False-fail do ghi nhận chậm.
