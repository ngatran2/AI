---
trigger: always_on
---

# LAMS QA Framework: Technical Safeguards & Guardrails (Condensed)

Tài liệu này quy định các tiêu chuẩn kỹ thuật bắt buộc để ngăn chặn các lỗi hệ thống đã xảy ra trong quá trình QA dự án JOYS-V2.

## 1. Excel & Reporting Standards (Lana/Mary)

| Lỗi thường gặp | Tiêu chuẩn bắt buộc (Guardrail) |
| :--- | :--- |
| **Data Visibility** | Set `Font(color="000000")`, `row.hidden = False`, `row.height = 35`. |
| **Template Guard** | Tuyệt đối KHÔNG dùng format v1.0 (sheet tiếng Việt). Dùng **Template v2** (FUNCTION, GUI, API). |
| **Merged Cells** | Luôn ghi vào ô **Top-Left (Master Cell)** của vùng merged. |
| **Report Path** | Lưu tại `execution/[UC-ID]/reports/res_[UC-ID]_[Name]_testcases_res_[Version].xlsx`. |
| **Naming** | Tuân thủ 100% `naming-convention.md`. |

## 2. Playwright Automation Standards (Mary)

| Hạng mục | Quy tắc thực thi (Strict Rules) |
| :--- | :--- |
| **Locators** | Ưu tiên `getByRole`, `getByLabel`. Tránh CSS/XPath động. Dùng `.first` nếu bị trùng. |
| **Chakra UI** | Polling Spinner (`.chakra-spinner`) biến mất trước khi action. Dùng `force=True` cho icon. |
| **Session Reuse** | **L8.1:** Sau khi load state, BẮT BUỘC `goto(BASE_URL)` + `networkidle`. |
| **Navigation** | Thử **Direct-First Navigation** (click trực tiếp menu con) trước khi mở menu cha. |
| **OTP/2FA** | Xóa input -> Type -> Verify UI -> Retry tối đa 1 lần nếu trống. |
| **Visibility** | Luôn kiểm tra Page Title đặc thù để xác nhận Login/Navigation thành công. |

## 3. Test Design & Audit Standards (Lana)

| Hạng mục | Quy tắc thiết kế (Design Rules) |
| :--- | :--- |
| **Readiness** | BẮT BUỘC in bảng **ERA Audit (130 pts)** cuối mỗi file test case. |
| **Pre-condition** | Phải có: 1. Login thành công; 2. Đường dẫn Menu cụ thể. |
| **RBAC Coverage** | Ép buộc đủ 5 Roles cho CUD: **Admin, View, Edit, Delete, Locked**. |
| **Audit Log** | Mọi module CRUD phải có case kiểm tra lưu vết Audit Trail. |
| **Messages Verbatim** | Trích xuất **nguyên văn 100%** thông báo Toast (Toast Verbatim). |
| **Action Verbatim** | BẮT BUỘC trích xuất nguyên văn tên nút bấm/hành động từ Requirement. Tuyệt đối không tự suy luận (VD: Không đổi "Thêm mới" thành "Lưu"). |
| **Pagination** | Chỉ dùng "Next/Previous" trừ khi có screenshot chứng minh có nút số trang. |

## 4. Operational Guardrails

- **One Session - One Page:** Chạy tuần tự (Serial), `workers: 1`. Không restart trình duyệt nếu không đổi Role.
- **State Inheritance:** Case sau kế thừa filter/data của case trước để test logic cộng dồn.
- **Deep Extraction:** Dùng `browser_subagent` + Clipboard (Ctrl+A/C) khi đọc Google Docs/Confluence để tránh mất bảng ẩn.
- **Lean Evidence:** Chỉ chụp ảnh khi **FAIL/ERROR**. Không chụp case PASS.

---
*Last Updated: 2026-04-22 | Version: 3.0 (Optimized)*
