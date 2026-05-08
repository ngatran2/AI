# Requirement Readiness Review: UC-DM-10: Quản lý danh mục hãng bay

**Phiên bản:** v1
**Ngày thực hiện:** 2026-04-21
**Người thực hiện:** Antigravity (AI Agent)
**Trạng thái tổng quát:** ❌ **NOT READY** (Score: 65%)

---

## 0. Executive Summary (Feature Brief)
Module này quản lý danh mục Hãng hàng không (Airlines). Đây là một module quản lý danh mục cơ bản (CRUD) nhưng có ràng buộc dữ liệu (BR-01) liên quan đến Quản lý chuyến bay, cần đảm bảo tính toàn vẹn dữ liệu khi xóa.

## 1. Completness Score (0-100%)
- **Score:** 65%
- **Lý do:** Thiếu trầm trọng mô tả về giao diện danh sách (Search/Filter/Pagination) và các kịch bản validation chi tiết.

## 2. Audit Findings (Gaps & Questions)

| ID | Section | Issue Description | Severity | Suggestion |
| :--- | :--- | :--- | :--- | :--- |
| G-01 | List Screen | Chưa mô tả màn hình danh sách có những cột nào, có Search hay Phân trang không. | HIGH | Bổ sung bảng định nghĩa các cột trên List và các trường Search. |
| G-02 | RBAC | Chưa định nghĩa các Role (Admin, View, Edit) có quyền hạn như thế nào. | MEDIUM | Xác định quyền truy cập cho từng hành động. |
| G-03 | UI Detail | Thiếu Screenshot hoặc mô tả Layout (Popup hay trang riêng). | MEDIUM | Bổ sung Figma link hoặc mô tả Layout. |
| Q-01 | Validation | Khi nhập trùng "Mã hãng bay", thông báo lỗi cụ thể hiển thị ở đâu (Toast hay Inline)? | LOW | Làm rõ cơ chế hiển thị lỗi. |
| Q-02 | Delete | BR-01 nói về "xóa mềm" hay "xóa cứng"? | LOW | Xác định cơ chế xóa trong DB. |

## 3. Detailed Audit (10 Sections)

### 3.1 Basic Information & Flow (Score: 8/10)
- Đầy đủ luồng Thêm/Sửa/Xóa cơ bản.

### 3.2 Data Fields & Constraints (Score: 7/10)
- Các trường cơ bản đã có, nhưng thiếu quy định về định dạng Tên hãng bay (có cho phép ký tự đặc biệt không?).

### 3.3 UI & UX (Score: 2/10)
- Hoàn toàn thiếu mô tả về vị trí nút bấm và trạng thái Loading/Success.

### 3.4 Business Rules & Logic (Score: 8/10)
- Các quy tắc ràng buộc xóa (BR-01) và khóa mã (BR-02) rất rõ ràng.

## 4. Testability Outlook
- Module này có thể tự động hóa (Automation) dễ dàng nếu bổ sung đầy đủ Locator (ID/Class) hoặc mô tả UI rõ hơn.
- Cần chú ý test case Negative cho phần trùng Mã hãng bay.

## 5. Summary & Verdict
Tài liệu hiện tại **CHƯA ĐỦ ĐIỀU KIỆN** để thiết kế Test Case chi tiết do thiếu phần mô tả màn hình Danh sách và Tìm kiếm. QA Engineer cần BA làm rõ các điểm trong danh sách Gap trước khi tiến hành.
