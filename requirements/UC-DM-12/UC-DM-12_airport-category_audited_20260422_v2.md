# Báo Cáo Kiểm Tra Mức Độ Sẵn Sàng Của Yêu Cầu (Readiness Review)
**Tính năng / Use Case:** Quản lý danh mục sân bay (UC-DM-12)
**Ngày đánh giá:** 2026-04-22
**Phiên bản:** v2 (Cập nhật sau khi fix lỗi trích xuất dữ liệu bảng)
**Người đánh giá (Agent):** requirement-reviewer
**Trạng thái sẵn sàng:** ⚠️ **CONDITIONALLY READY**
**Điểm Readiness:** 86.4 / 100

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
- *[MISSING]* Cần làm rõ cụ thể các module/dropdown nào sẽ tiêu thụ dữ liệu này (ví dụ: màn hình tạo chuyến bay, màn hình phòng chờ).

### 0.5. Acceptance Criteria (AC) Synthesis
*(Synthesized based on explicitly detailed UI behavior, business rules, and validation messages. No formal AC section was provided, but testability is high).*
- **UI:** Giao diện hiển thị đủ cột, tính năng Search/Filter/Phân trang hoạt động đúng (CMR-08, CMR-09).
- **Thêm/Sửa:** Validation báo lỗi đúng nếu thiếu thông tin, vượt quá 255 ký tự. Báo lỗi đúng format khi trùng mã sân bay. Toast thành công đúng câu chữ.
- **Xóa:** Hệ thống chặn xóa và báo lỗi “Không thể xóa khi sân bay đang được sử dụng.” nếu vi phạm ràng buộc.
- **Integration:** Tài khoản View-only không thể thực hiện thao tác CUD. Sân bay mới thêm phải xuất hiện trên dropdown của hệ thống.

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
| 8 | Functional Integration Analysis | 10 | 5/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 5/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 0/5 | ❌ |
| **Total** | | **110** | | **95/110 → 86.4/100** |

**Verdict:** ⚠️ **CONDITIONALLY READY** (Có thể bắt đầu viết kịch bản Test Case. Các nguyên văn thông báo lỗi và thành công đã đầy đủ. Tuy nhiên, vẫn cần hỏi BA một số chi tiết nhỏ về Integration).

---

## 2. Báo cáo Khoảng trống & Câu hỏi (Unified Gap & Question Report)

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | Medium | "BR-12.2. Mã sân bay phải là duy nhất trên toàn danh mục." | **Cung cấp nguyên văn thông báo lỗi.** Nếu người dùng nhập trùng Mã sân bay (đang tồn tại) thì thông báo lỗi hiển thị dưới input là gì? | QA Automation cần chính xác text lỗi để làm kịch bản Negative test. | Open |
| Q2 | Medium | "Sân bay mới hiển thị ở các danh sách sân bay được sử dụng trên toàn hệ thống." | **Xác nhận Integration Linkage.** Cụ thể những màn hình/module nào trong hệ thống đang gọi tới/tiêu thụ dữ liệu Danh mục Sân bay này? | QA cần biết chính xác điểm đầu ra để test Data Sync (Tạo xong qua màn khác kiểm tra có xuất hiện trong Dropdown chưa). | Open |
| Q3 | Low | "Cập nhật dữ liệu vào DB (Disable nếu không có thay đổi)." | Khi người dùng nhập khoảng trắng (space) vào sau tên sân bay, input text sẽ tự động trim() theo CMR-03. Vậy trường hợp này nút Cập nhật có bị bật lên không (Enable) hay vẫn Disable? | Clarification cho case boundary validation. | Open |

---

## 3. What's Good (Điểm cộng của tài liệu)
- ✅ Đã cung cấp chi tiết 100% nguyên văn (verbatim) các thông báo Toast Thành công, Lỗi và Cảnh báo chặn xóa, rất tốt cho quá trình viết Assertions trong Automation.
- ✅ Luồng "Tìm kiếm nhanh" tại cột được quy định rõ ràng, kết nối chặt chẽ với CMR-09.
- ✅ Các điều kiện Pre-conditions và Post-conditions được mô tả chi tiết, rõ ràng.
- ✅ Các quy tắc nghiệp vụ chặn Xóa và Cập nhật được mô tả hợp lý.

---

## 4. Testability Outlook (Tầm nhìn khả năng kiểm thử)

**Những hạng mục ĐÃ CÓ THỂ test ngay:**
- Kiểm tra luồng Happy path cho Thêm/Sửa/Xóa với các Assertion chuẩn xác về mặt text ("Thêm mới [mã sân bay - sân bay] thành công.").
- Kiểm tra tính năng "Tìm kiếm nhanh" theo từng cột Mã sân bay và Tên sân bay.
- Kiểm tra validation chuẩn của form Thêm/Sửa (Maxlength, Require).
- Kiểm tra luồng cảnh báo chặn xóa khi sân bay đang được sử dụng.
- Kiểm tra luồng ẩn/hiện nút (Authorization View/Edit/Delete).

**Những hạng mục CHƯA THỂ test (Blocked by gaps):**
- Kiểm tra luồng Integration Test đa màn hình (Chưa rõ tác động của dữ liệu sân bay tới các màn khác cụ thể là màn nào).

**Gợi ý các luồng test chính:**
- **Happy Path:** Thêm mới -> Thấy ở màn hình danh sách -> Sửa tên -> Xóa.
- **Alternative Flow:** Thêm một mã sân bay đã từng bị xóa (BR-12.3) -> Cho phép. Tìm kiếm từ khóa tồn tại -> hiển thị đúng kết quả. Tìm kiếm từ khóa không tồn tại -> báo không có dữ liệu.
- **Negative Flow:** Nhập trùng mã sân bay đang tồn tại. Xóa một sân bay đang có liên kết -> Validate toast message chặn xóa.

---

## 5. Summary & Recommendation

**Tổng quan:** Tài liệu UC-DM-12 hiện tại đã đủ chi tiết, đặc biệt là sự xuất hiện của các Toast Messages và Logic Cảnh báo chặn xóa trong bảng Quy tắc nghiệp vụ.

**Đề xuất:** ⚠️ **CONDITIONALLY READY**. QA Engineer có thể tiến hành viết Test Scenarios và Test Cases. Một vài rủi ro nhỏ về Integration (Danh sách các module liên quan) có thể được gửi BA để làm rõ song song mà không làm chậm tiến độ thiết kế Test Case.

---
**Changelog:**
- **v2 (2026-04-22):** Bổ sung các thông báo Toast Message nguyên văn, logic Tìm kiếm nhanh và Ràng buộc xóa từ bảng Quy tắc nghiệp vụ. Cập nhật lại điểm Readiness từ 54.5 lên 86.4. Mở khóa tiến trình tạo Test Case.
