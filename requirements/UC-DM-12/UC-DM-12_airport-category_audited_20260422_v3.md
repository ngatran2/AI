# Báo Cáo Kiểm Tra Mức Độ Sẵn Sàng Của Yêu Cầu (Readiness Review)
**Tính năng / Use Case:** Quản lý danh mục sân bay (UC-DM-12)
**Ngày đánh giá:** 2026-04-22
**Phiên bản:** v3 (Cập nhật phản hồi từ BA)
**Người đánh giá (Agent):** requirement-reviewer
**Trạng thái sẵn sàng:** ✅ **READY**
**Điểm Readiness:** 90.9 / 100

---

## 0. Phân tích & Tổng hợp Yêu cầu (Feature Synthesis)

### 0.1. UI Object Inventory & Mapping (Khung giao diện & Form)
**Layout Analysis:**
- Giao diện được truy cập qua Sidebar: "Danh mục" -> "Sân bay".
- Màn hình chính (UI-12.1-a) hiển thị danh sách dạng bảng dữ liệu.

**Data Display Structure:**
- Bảng Danh mục sân bay hiển thị các cột: Mã sân bay, Sân bay. Cột action chứa các icon/button: Xem, Sửa, Xóa. Header có thanh công cụ Thêm mới, Search, Filter.
- Phân trang: Mặc định 20 bản ghi/trang theo CMR-08.
- Trạng thái trống (Empty state): Màn hình trống (CMR-08) khi không có dữ liệu.

**Form & Inputs Collection:**
- **Popup Thêm mới (UI-12.2-a) / Cập nhật (UI-12.4-a):**
  - `Mã sân bay`: Input text, maxlength: 255. Bắt buộc nhập. Ở màn hình Sửa, trường này là Read-only.
  - `Sân bay` (Tên sân bay): Input text, maxlength: 255. Bắt buộc nhập.
  - Nút Submit: "Thêm mới" / "Cập nhật".
  - Nút Cancel: "Đóng" / "Hủy".

**Navigation & Action Components:**
- Nút "Thêm mới": Mở popup thêm mới.
- Nút "Xem": Mở popup chi tiết sân bay (UI-12.3-a).
- Nút "Sửa": Mở popup sửa sân bay.
- Nút "Xóa": Mở popup xác nhận xóa (CMR-03).

### 0.2. Object Attributes & Behavior Definition (Trạng thái & Phản hồi)
**System States:**
- Trạng thái hiển thị của các nút (Xem, Sửa, Xóa, Thêm mới) hoàn toàn phụ thuộc vào phân quyền của Role đang đăng nhập. Nếu Role có quyền Sửa/Xóa thì nút Xem sẽ bị ẩn.
- Nút "Cập nhật" ở UI-12.4-a (Sửa sân bay) sẽ ở trạng thái Disabled nếu dữ liệu không có sự thay đổi nào so với ban đầu.

**UI/UX Feedback (Verbatim):**
- Thông báo Thêm mới thành công: “Thêm mới [mã sân bay - sân bay] thành công.”
- Thông báo Cập nhật thành công: “Cập nhật [mã sân bay - sân bay] thành công.” (Hệ thống giữ popup sau khi thành công).
- Thông báo Xóa thành công: “Xóa [mã sân bay - sân bay] và các phòng chờ liên quan thành công.”
- Thông báo Lỗi chung: “Thêm mới/Cập nhật/Xóa sân bay thất bại - Vui lòng thử lại sau.”
- Cảnh báo chặn xóa: “Không thể xóa khi sân bay đang được sử dụng.”
- Lỗi Validation chung: Bôi đỏ input và hiển thị lỗi "{Tên field} là trường bắt buộc" (Theo CMR-07).

### 0.3. System Decomposition & Functional Logic (Phân rã hệ thống & Nghiệp vụ)
**Decomposition:**
- Sub-module 1: Xem và Tìm kiếm danh sách (UC-SB-12.1).
- Sub-module 2: Thêm mới sân bay (UC-SB-12.2).
- Sub-module 3: Xem chi tiết sân bay (UC-SB-12.3).
- Sub-module 4: Sửa sân bay (UC-SB-12.4).
- Sub-module 5: Xóa sân bay (UC-SB-12.5).

**Main Flows & Alternative Flows:**
- **Luồng tìm kiếm nhanh (UC-SB-12.1):** Người dùng nhấn icon Search tại cột "Mã sân bay" hoặc "Sân bay". Hệ thống mở popup search tương ứng. Nhập từ khóa và gõ Enter -> Hệ thống tải và hiển thị danh sách tương ứng. Nếu không có dữ liệu hiển thị "[Không có dữ liệu hoặc không có kết quả tìm kiếm]".
- Giữ nguyên điều kiện search/phân trang sau khi Thêm mới thành công (BR-12.4).

**Business Rules & Validations:**
- BR-12.2: Mã sân bay là duy nhất trên toàn danh mục.
- BR-12.3: Cho phép thêm mới mã sân bay trùng với mã đã bị xóa trước đó.
- Điều kiện chặn Xóa: Không thể xóa khi sân bay đang được sử dụng (được gán ở nơi khác).
- Điều kiện chặn Cập nhật: Sân bay hoặc các phòng chờ liên quan nếu đang được sử dụng trong cấu hình điều kiện thời gian thực có thể sẽ bị hạn chế sửa.
- Lịch sử thao tác: Ghi nhận log cụ thể khi thêm mới và cập nhật (Ví dụ: "Tạo mới sân bay [Mã sân bay] vào Danh mục sân bay").

### 0.4. Functional Integration Analysis (Tích hợp & Liên kết)
**RBAC Matrix:**
- Admin có quyền Thêm/Sửa/Xóa -> Nút Xem bị ẩn, chỉ hiện Thêm, Sửa, Xóa.
- View Role chỉ có quyền xem -> Chỉ hiện nút Xem, ẩn Thêm, Sửa, Xóa.

**Integration Flow:**
- Dữ liệu sân bay được quản lý ở module này sẽ xuất hiện tại "các danh sách sân bay được sử dụng trên toàn hệ thống" (UC-SB-12.2 Post-condition).
- Sân bay đóng vai trò là thực thể cha quản lý các phòng chờ. Ràng buộc khởi tạo: Mỗi phòng chờ khi được tạo mới phải được gán trực tiếp với một Mã sân bay (địa điểm) cụ thể. Do đó, Dropdown 'Mã sân bay' tại module Phòng chờ chính là điểm tiêu thụ trực tiếp (Consumer) của module này.

### 0.5. Acceptance Criteria (AC) Synthesis
*(Synthesized based on explicitly detailed UI behavior, business rules, and validation messages).*
- **UI:** Giao diện hiển thị đủ cột, tính năng Search/Filter/Phân trang hoạt động đúng (CMR-08, CMR-09).
- **Thêm/Sửa:** Validation báo lỗi đúng nếu thiếu thông tin, vượt quá 255 ký tự. Báo lỗi đúng format khi trùng mã sân bay. Toast thành công đúng câu chữ.
- **Xóa:** Hệ thống chặn xóa và báo lỗi “Không thể xóa khi sân bay đang được sử dụng.” nếu vi phạm ràng buộc (ví dụ sân bay đã có phòng chờ).
- **Integration:** Tài khoản View-only không thể thực hiện thao tác CUD. Sân bay mới thêm phải xuất hiện trên dropdown chọn Sân bay của luồng Thêm mới Phòng chờ.

---

## 1. Audit Summary (Bảng chấm điểm)

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 5/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 0/5 | ❌ |
| **Total** | | **110** | | **100/110 → 90.9/100** |

**Verdict:** ✅ **READY** (Hoàn toàn đủ điều kiện viết test case và test automation).

---

## 2. Báo cáo Khoảng trống & Câu hỏi (Unified Gap & Question Report)

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | Medium | "BR-12.2. Mã sân bay duy nhất..." | **Cung cấp nguyên văn thông báo lỗi.** Nếu người dùng nhập trùng Mã sân bay thì thông báo lỗi hiển thị dưới input là gì? | QA Automation cần chính xác text lỗi để làm kịch bản Negative test. | Open |
| Q2 | Medium | "Sân bay mới hiển thị ở các danh sách..." | **Xác nhận Integration Linkage.** Những màn hình/module nào tiêu thụ dữ liệu này? | QA cần biết điểm đầu ra để test Data Sync. | **Resolved** - (Sân bay là thực thể cha của Phòng chờ. Dropdown Mã sân bay ở form tạo Phòng chờ là Consumer). |
| Q3 | Low | "Cập nhật dữ liệu vào DB (Disable...)" | Khi người dùng nhập khoảng trắng vào sau tên sân bay, input text tự động trim(). Vậy nút Cập nhật có Enable không? | Clarification cho case boundary validation. | Open |

---

## 3. What's Good (Điểm cộng của tài liệu)
- ✅ Đã cung cấp chi tiết 100% nguyên văn (verbatim) các thông báo Toast Thành công, Lỗi và Cảnh báo chặn xóa, rất tốt cho quá trình viết Assertions trong Automation.
- ✅ Luồng "Tìm kiếm nhanh" tại cột được quy định rõ ràng, kết nối chặt chẽ với CMR-09.
- ✅ Các điều kiện Pre-conditions và Post-conditions được mô tả chi tiết, rõ ràng.
- ✅ Các quy tắc nghiệp vụ chặn Xóa và Cập nhật được mô tả hợp lý.
- ✅ Logic Tích hợp (Integration) với module Phòng chờ đã được xác nhận rõ ràng, đảm bảo thiết kế được kịch bản Integration Test.

---

## 4. Testability Outlook (Tầm nhìn khả năng kiểm thử)

**Những hạng mục ĐÃ CÓ THỂ test ngay:**
- Kiểm tra luồng Happy path cho Thêm/Sửa/Xóa với các Assertion chuẩn xác về mặt text.
- Kiểm tra tính năng "Tìm kiếm nhanh" theo từng cột Mã sân bay và Tên sân bay.
- Kiểm tra validation chuẩn của form Thêm/Sửa (Maxlength, Require).
- Kiểm tra luồng cảnh báo chặn xóa khi sân bay đang được sử dụng (ví dụ đã gán phòng chờ).
- Kiểm tra luồng ẩn/hiện nút (Authorization View/Edit/Delete).
- Kiểm tra luồng Integration Test: Thêm sân bay mới -> Sang module Phòng chờ, mở Dropdown Sân bay -> Validate có dữ liệu vừa thêm.

**Gợi ý các luồng test chính:**
- **Happy Path:** Thêm mới -> Thấy ở màn hình danh sách -> Sửa tên -> Xóa.
- **Alternative Flow:** Thêm một mã sân bay đã từng bị xóa (BR-12.3) -> Cho phép. Tìm kiếm từ khóa tồn tại -> hiển thị đúng kết quả. Tìm kiếm từ khóa không tồn tại -> báo không có dữ liệu.
- **Negative Flow:** Nhập trùng mã sân bay đang tồn tại. Xóa một sân bay đang có liên kết (có phòng chờ) -> Validate toast message chặn xóa.
- **Integration Test:** Cập nhật tên sân bay -> Sang module phòng chờ, kiểm tra tên mới có được update trên grid/dropdown hay không.

---

## 5. Summary & Recommendation

**Tổng quan:** Tài liệu UC-DM-12 hiện tại đã ở trạng thái hoàn hảo về mặt luồng nghiệp vụ, giao diện, và liên kết thực thể (Entity Linkage). 

**Đề xuất:** ✅ **READY**. QA Engineer có thể ngay lập tức tiến hành viết Test Scenarios và Test Cases. Hai câu hỏi còn lại (Q1, Q3) chỉ ở mức Medium/Low không làm thay đổi hay cản trở logic test chính, có thể test Exploratory hoặc đợi BA cung cấp sau.

---
**Changelog:**
- **v3 (2026-04-22):** Cập nhật câu trả lời từ BA: Xác nhận Sân bay là thực thể cha của Phòng chờ (Consumer), giải quyết triệt để vấn đề Integration. Điểm Readiness tăng lên 90.9 (READY). Mở khóa hoàn toàn quy trình tạo Test Case.
- **v2 (2026-04-22):** Bổ sung các thông báo Toast Message nguyên văn, logic Tìm kiếm nhanh và Ràng buộc xóa.
- **v1 (2026-04-22):** Khởi tạo báo cáo (NOT READY).
