# Requirement Readiness Review: UC-DM-10: Quản lý danh mục hãng bay

**Phiên bản:** v6 (Integration Focus)
**Ngày thực hiện:** 2026-04-21
**Người thực hiện:** Antigravity (AI Agent)
**Trạng thái tổng quát:** ⚠️ **CONDITIONALLY READY** (Score: 85%)

---

## 0. Executive Summary (Feature Brief)
Bản Audit v6 tập trung vào các rủi ro tích hợp (Integration Risks). Mặc dù các luồng GUI và CRUD của Hãng bay đã rõ ràng, nhưng sự xuất hiện của thực thể "Loại thẻ" trong các thông báo lỗi và ràng buộc xóa cho thấy có một sự liên kết dữ liệu chưa được định nghĩa rõ ràng trong tài liệu này.

## 1. Functional Integration Analysis (MỚI)

### 1.1 Mối quan hệ Hãng bay - Loại thẻ
- **Quan sát:** Thông báo xóa nhắc đến "hãng bay và loại thẻ liên quan".
- **Vấn đề:** Tài liệu chưa mô tả danh mục "Loại thẻ" được quản lý ở đâu (UC nào?).
- **Rủi ro:** Khi xóa một hãng bay, các "loại thẻ liên quan" sẽ bị xử lý như thế nào (Xóa mềm đồng loạt hay chỉ vô hiệu hóa)? 

## 2. Unified Gap & Question Report (Bổ sung câu hỏi tích hợp)

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q-03 | **HIGH** | `“...xóa hãng bay và loại thẻ liên quan...”` | **Hãng bay có quan hệ như thế nào với Loại thẻ?** Danh mục Loại thẻ được quản lý ở module nào? | Không có Integration Flow, Tester không thể verify được việc "xóa các loại thẻ liên quan" có diễn ra đúng logic không. | **Open** |
| Q-04 | **HIGH** | `BR-10.6` | **Scanning session và Cấu hình điều kiện kiểm tra Hãng bay hay kiểm tra Loại thẻ?** Hay kiểm tra cả hai? | Cần làm rõ mức độ ảnh hưởng của ràng buộc để thiết kế Test Data phức hợp. | **Open** |

## 3. Detailed System Decomposition & Messages

*(Giữ nguyên các thông báo và logic từ v5)*

## 4. Testability Outlook
- **Integration Test:** Hiện tại **CHƯA THỂ TEST** phần liên quan đến loại thẻ vì thiếu tài liệu về Card Types.
- **Data Prep:** Cần DB schema hoặc tài liệu module Loại thẻ để chuẩn bị dữ liệu liên kết.

## 5. Summary & Verdict
Trạng thái hạ xuống **CONDITIONALLY READY**. QA có thể thiết kế các case GUI/CRUD cho Hãng bay, nhưng **KHÔNG THỂ** thiết kế các case Integration liên quan đến Loại thẻ, Scanning Session và Cấu hình điều kiện cho đến khi Q-03 và Q-04 được giải đáp.
