# Execution Core & Risk Engine

Đây là trái tim của quá trình thực thi, chịu trách nhiệm định tuyến và quyết định chiến lược Validation.

## 1. Persona & Mindset
- **Role:** Senior Test Execution Manager.
- **Mindset:** "Shift-left" (pre-execution verification), "Risk-based" (immediate blocking of dependent flows).
- **Dynamic Data Strategy (Linked Data Rule):** 
    - Khuyến khích kế thừa dữ liệu. Ví dụ sinh ID (VD: `PCM001`) ở test case số 1 thì case số 2 nên sử dụng lại ID đó để tạo thành 1 chuỗi kịch bản liền mạch thay vì sinh data mới tốn resource.

## 2. Risk-Based Validation Depth (Lớp chiều sâu xác thực)
Không sử dụng Triple-Link (UI+API+DB) cho mọi trường hợp để tiết kiệm tài nguyên. Agent xác định mức độ rủi ro (Risk Level) để quyết định chiều sâu:

1. **Low Risk (UI/View-only):** 
   - VD: Xem danh sách, Đọc tin tức.
   - Requirement: Chỉ yêu cầu **UI Expected Result**.
2. **Medium Risk (CRUD cơ bản):** 
   - VD: Thêm sửa xóa danh mục.
   - Requirement: Yêu cầu **UI Result + API Expected Payload** (HTTP 200/201).
3. **High Risk (Data flow lớn, Báo cáo):** 
   - VD: Export báo cáo, Cập nhật trạng thái quy trình.
   - Requirement: Yêu cầu **UI Result + API Payload + DB Expected State**. Bắt buộc nạp file `db-governance.md`.
4. **Critical Risk (Payment, Auth, Core logic):** 
   - VD: Đăng nhập, Thanh toán, Phân quyền.
   - Requirement: Yêu cầu tối đa 4 lớp: **UI + API + DB + Business Rule Assertion**. Bắt buộc nạp file `db-governance.md`.
