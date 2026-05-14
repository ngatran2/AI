# Báo Cáo Kiểm Tra Mức Độ Sẵn Sàng Của Yêu Cầu (Readiness Review)
**Tính năng / Use Case:** Quản lý danh mục sân bay (UC-DM-12)
**Ngày đánh giá:** 2026-04-22
**Người đánh giá (Agent):** requirement-reviewer
**Trạng thái sẵn sàng:** ❌ **NOT READY**
**Điểm Readiness:** 54.5 / 100

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
- Trạng thái hiển thị của các nút (Xem, Sửa, Xóa, Thêm mới) hoàn toàn phụ thuộc vào phân quyền của Role đang đăng nhập. Nếu Role có quyền Sửa/Xóa thì nút Xem sẽ bị ẩn (ẩn để gộp trải nghiệm xem vào màn Sửa, hoặc click trực tiếp Sửa).
- Nút "Cập nhật" ở UI-12.4-a (Sửa sân bay) sẽ ở trạng thái Disabled nếu dữ liệu không có sự thay đổi nào so với ban đầu.

**UI/UX Feedback (Verbatim):**
- *[MISSING]* Thông báo thành công: Tài liệu chỉ ghi chung chung "hiển thị success toast message", chưa có nguyên văn thông báo (Ví dụ: "Thêm mới sân bay thành công" hay "Thêm mới [Mã sân bay] thành công").
- *[MISSING]* Lỗi trùng lặp (BR-12.2): Chưa có nguyên văn thông báo khi mã sân bay bị trùng.
- Lỗi Validation chung: Bôi đỏ input và hiển thị lỗi "{Tên field} là trường bắt buộc" (Theo CMR-07).
- Xác nhận Xóa: Popup confirm xóa theo CMR-03.

### 0.3. System Decomposition & Functional Logic (Phân rã hệ thống & Nghiệp vụ)
**Decomposition:**
- Sub-module 1: Xem và Tìm kiếm danh sách (UC-SB-12.1).
- Sub-module 2: Thêm mới sân bay (UC-SB-12.2).
- Sub-module 3: Xem chi tiết sân bay (UC-SB-12.3).
- Sub-module 4: Sửa sân bay (UC-SB-12.4).
- Sub-module 5: Xóa sân bay (UC-SB-12.5).

**Main Flows & Alternative Flows:**
- Luồng tìm kiếm: Hỗ trợ tìm kiếm từ khóa trên các cột, nhấn Enter để search. Giữ nguyên điều kiện search/phân trang sau khi Thêm mới thành công (BR-12.4).
- Luồng xem chi tiết: Có thể đi tới chức năng Sửa/Xóa trực tiếp từ màn hình chi tiết (UI-12.3-a).
- Xóa dữ liệu (UC-SB-12.5): *[MISSING BLOCKER]* Tài liệu không ghi rõ các ràng buộc khi xóa. (Ví dụ: Nếu sân bay đã được gán vào vé/phòng chờ thì có được xóa không? Nếu chặn xóa thì thông báo lỗi nguyên văn là gì?).

**Business Rules & Validations:**
- BR-12.2: Mã sân bay là duy nhất trên toàn danh mục.
- BR-12.3: Cho phép thêm mới mã sân bay trùng với mã đã bị xóa trước đó.
- Lịch sử thao tác: Ghi nhận log cụ thể khi thêm mới và cập nhật (Ví dụ: "Tạo mới sân bay [Mã sân bay] vào Danh mục sân bay").

### 0.4. Functional Integration Analysis (Tích hợp & Liên kết)
**RBAC Matrix:**
- Admin có quyền Thêm/Sửa/Xóa -> Nút Xem bị ẩn, chỉ hiện Thêm, Sửa, Xóa.
- View Role chỉ có quyền xem -> Chỉ hiện nút Xem, ẩn Thêm, Sửa, Xóa.

**Integration Flow:**
- Dữ liệu sân bay được quản lý ở module này sẽ xuất hiện tại "các danh sách sân bay được sử dụng trên toàn hệ thống" (UC-SB-12.2 Post-condition).
- *[MISSING]* Cần làm rõ cụ thể các module/dropdown nào sẽ tiêu thụ dữ liệu này (ví dụ: màn hình tạo chuyến bay, màn hình phòng chờ).

### 0.5. Acceptance Criteria (AC) Synthesis
*(Synthesized based on standard quality rules, as explicit ACs are missing from the spec)*
- **UI:** Giao diện danh sách và popup phải hiển thị đầy đủ và tuân thủ các quy tắc trong CMR.
- **Function - Thêm mới/Cập nhật:** Validate được bắt buộc nhập, giới hạn 255 ký tự. Hệ thống báo lỗi đúng format khi trùng mã sân bay. Nút Lưu phải disabled nếu không có thay đổi (Sửa).
- **Function - Xóa:** Popup confirm xuất hiện. Xóa thành công sân bay nếu không vi phạm ràng buộc (cần làm rõ ràng buộc).
- **Integration:** Tài khoản Role chỉ có quyền View thì không thể thực hiện các thao tác bằng API Thêm/Sửa/Xóa. Thay đổi trên Danh mục Sân bay cập nhật đúng lên các drop-down sử dụng Sân bay ở hệ thống.

---

## 1. Audit Summary (Bảng chấm điểm)

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 10/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 10/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 5/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 0/10 | ❌ |
| 10 | Non-functional Requirements | 5 | 0/5 | ❌ |
| **Total** | | **110** | | **60/110 → 54.5/100** |

**Verdict:** ❌ **NOT READY** (Bị trượt do thiếu thông tin ở các vùng kiến thức mang tính chất Critical là Tiêu chí chấp nhận và Điều kiện ràng buộc khi Xóa).

---

## 2. Báo cáo Khoảng trống & Câu hỏi (Unified Gap & Question Report)

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High (Blocker) | N/A (Missing) | **Xác nhận điều kiện chặn xóa (Delete constraints).** Sân bay đã được gán vào vé máy bay, chuyến bay hoặc phòng chờ có được phép xóa không? Nếu không, hệ thống có cảnh báo gì (Verbatim message)? | Nếu QA không biết điều kiện ràng buộc này, kịch bản test sẽ bị lọt luồng lỗi nghiêm trọng liên quan đến Data Integrity. | Open |
| Q2 | High (Blocker) | N/A (Missing) | **Bổ sung Acceptance Criteria.** Đề nghị bổ sung các Tiêu chí chấp nhận rõ ràng và đo lường được cho UC này. | AC là căn cứ cao nhất để QA pass/fail một kịch bản test. | Open |
| Q3 | Medium | "Hệ thống hiển thị success toast message." | **Cung cấp nguyên văn (Verbatim) các Toast Message.** Thông báo thành công cụ thể là gì khi Thêm, Sửa, Xóa? (Ví dụ: "Thêm mới [Mã sân bay] thành công.") | Test Automation (Playwright) bắt buộc phải assert chính xác từng câu chữ trong Toast message. | Open |
| Q4 | Medium | "BR-12.2. Mã sân bay phải là duy nhất trên toàn danh mục." | **Cung cấp nguyên văn thông báo lỗi.** Nếu người dùng nhập trùng Mã sân bay (đang tồn tại) thì thông báo lỗi hiển thị dưới input là gì? | QA Automation cần chính xác text lỗi để làm kịch bản Negative test. | Open |
| Q5 | Medium | "Sân bay mới hiển thị ở các danh sách sân bay được sử dụng trên toàn hệ thống." | **Xác nhận Integration Linkage.** Cụ thể những màn hình/module nào trong hệ thống đang gọi tới/tiêu thụ dữ liệu Danh mục Sân bay này? | QA cần biết chính xác điểm đầu ra để test Data Sync (Tạo xong qua màn khác kiểm tra có xuất hiện trong Dropdown chưa). | Open |
| Q6 | Low | "Cập nhật dữ liệu vào DB (Disable nếu không có thay đổi)." | Khi người dùng nhập khoảng trắng (space) vào sau tên sân bay, input text sẽ tự động trim() theo CMR-03. Vậy trường hợp này nút Cập nhật có bị bật lên không (Enable) hay vẫn Disable? | Clarification cho case boundary validation. | Open |

---

## 3. What's Good (Điểm cộng của tài liệu)
- ✅ Các điều kiện Pre-conditions và Post-conditions được mô tả chi tiết, rõ ràng từng Use Case.
- ✅ Bảng phân tích thành phần UI-UX rất tốt, chỉ ra được các behavior mapping trực tiếp với bộ nguyên tắc chung (CMR).
- ✅ Các quy tắc liên quan đến trải nghiệm (BR-12.4 - Giữ nguyên filter/search sau khi thêm thành công) được define chỉn chu.
- ✅ Phân quyền chức năng RBAC (Ẩn/Hiện nút) trên giao diện được mô tả khá tốt.

---

## 4. Testability Outlook (Tầm nhìn khả năng kiểm thử)

**Những hạng mục ĐÃ CÓ THỂ test ngay:**
- Kiểm tra giao diện danh sách, cột, sắp xếp mặc định, phân trang, layout.
- Kiểm tra validation chuẩn của form Thêm/Sửa (Maxlength 255 ký tự, require field).
- Kiểm tra luồng ẩn/hiện nút (Authorization View/Edit/Delete).
- Chức năng tìm kiếm cơ bản.

**Những hạng mục CHƯA THỂ test (Blocked by gaps):**
- Kiểm tra chức năng Xóa (UC-SB-12.5) với các bản ghi đang được sử dụng ở nơi khác (Ràng buộc nghiệp vụ đang bị Missing).
- Kiểm tra luồng Assertion cho Automation (Đang thiếu 100% nguyên văn các thông báo Success/Error message).
- Kiểm tra luồng Integration Test đa màn hình (Chưa rõ tác động của dữ liệu sân bay tới các màn khác cụ thể là màn nào).

**Gợi ý các luồng test chính (Sau khi giải quyết xong câu hỏi):**
- **Happy Path:** Thêm mới sân bay (A) -> Thấy ở màn hình danh sách và màn hình tiêu thụ -> Sửa tên (A) thành (A') -> Xóa (A').
- **Alternative Flow:** Thêm một mã sân bay đã từng bị xóa (BR-12.3) -> Cho phép. Cập nhật dữ liệu không thay đổi -> Nút Cập nhật disable.
- **Negative Flow:** Nhập trùng mã sân bay đang tồn tại. Xóa một sân bay đang có liên kết.
- **Integration/Authorization:** Role View vào màn hình, verify không có URL hay API nào có thể dùng để thực thi hành động Thêm/Sửa/Xóa.

---

## 5. Summary & Recommendation

**Tổng quan:** Tài liệu UC-DM-12 được cấu trúc khá tốt và đã liên kết nhiều tới các rule dùng chung (CMR). Tuy nhiên, về bản chất lõi để có thể triển khai Test QA (Đặc biệt là Automation) thì đang thiếu hai yếu tố mang tính sống còn: **Điều kiện ràng buộc chặn xóa** và **Nguyên văn thông báo (Verbatim Messages)**.

**Đề xuất:** ❌ **HOLD**. Trạng thái hiện tại chưa đủ điều kiện (NOT READY) để QA Engineer bắt tay vào viết Test Scenario hay Test Case (vì viết lúc này chắc chắn sẽ sai luồng hoặc thiếu thông báo lỗi). BA cần giải quyết các câu hỏi High và Medium trong phần Gap Report trước khi đưa lại cho QA xử lý ở bước tiếp theo.
