# Playwright POM & Automation Standard

## 1. Architecture & Locators
- **DOM Recon First:** Bắt buộc phải mờ trình duyệt/DOM ra để lấy thông tin thực tế. Tuyệt đối không đoán selector bừa.
- **Assertion Boundary:** Lệnh Assert (`expect()`) chỉ được nằm trong Test File. Page Object File (POM) chỉ chứa Locator và các hành động (Action).
- **Deterministic Locator Fallback Chain:**
  Khi Element Not Found, áp dụng theo trình tự:
  1. `getByRole` (Ưu tiên số 1 - Accessibility).
  2. `getByLabel` / `getByPlaceholder` (Ưu tiên 2).
  3. `getByTestId` (`data-testid` nếu có).
  4. Parent-scoped text locator (VD: `page.locator('.parent').filter(has_text='Submit')`).
  5. Semantic XPath (Tuyệt đối KHÔNG dùng XPath vị trí tuyệt đối như `/div[1]/div[2]`).
- **Self-Healing Validation:** Nếu tự dùng Fallback tìm ra element mới, phải xác minh thuộc tính của nó trước khi click để tránh click nhầm rác UI.

## 2. Session & State Inheritance (Lesson 8 & 11)
- **Session Reuse:** Chỉ tạo mới Browser Context khi chuyển đổi Role. Khi chạy luồng dài cho cùng 1 Role, tải lại `storage_state` (auth) để tiết kiệm thời gian Login.
- **Parallel by Namespace:** Hỗ trợ chạy song song (Parallel) nhưng BẮT BUỘC cách ly Namespace. VD: `Worker_1` thao tác trên `User_A`, `Worker_2` trên `User_B`. Tuyệt đối không song song trên cùng 1 record (Parallel Data Conflict).
- **State Inheritance (Kế thừa trạng thái):** Các testcase trong cùng nhóm (VD: Lọc, Tìm kiếm) không được tự ý gọi lại `goto()` hay làm mới trang, mà phải kế thừa kết quả filter của testcase trước.

## 3. Synchronization Guards
- Phải Wait `hidden` cho các `.chakra-skeleton`.
- **Spinner Polling:** Sử dụng vòng lặp kiểm tra `.chakra-spinner` cho đến khi nó biến mất.
- Bắt buộc kiểm tra `Toast Message`, hoặc `URL Change` để verify điều hướng. Không dùng Sleep cứng (`waitForTimeout`).
