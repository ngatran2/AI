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

## 5. Report Integrity Guardrails (Prevention of Missing Info)

| Hạng mục | Quy tắc bắt buộc (Guardrail) |
| :--- | :--- |
| **ID Matching** | Luôn gọi `.strip()` và sử dụng Regex hoặc chứa chuỗi (contains) để khớp TC ID, tránh lỗi do sai tiền tố (ví dụ: UCDN01 vs UC2FA05). |
| **Zero-Gap Rule** | Tuyệt đối không để trống cột Status. Các case không chạy phải được điền `SKIPPED` hoặc `PENDING` kèm lý do. |
| **Post-Write Audit** | Bắt buộc chạy lệnh Read-back để kiểm tra 3 cột (Status, Actual, Note) đã có dữ liệu trước khi báo cáo hoàn thành cho User. |
| **Row Height** | Luôn set `row.height = 70-100` và `wrap_text = True` để đảm bảo nội dung Actual Result dài không bị che khuất. |

## 6. Cleanup & Zero-Clutter Policy

| Hạng mục | Quy tắc bắt buộc (Guardrail) |
| :--- | :--- |
| **Post-Execution Cleanup** | Sau khi hoàn thành và lưu Report, BẮT BUỘC xóa các file tạm/nháp tại: `execution/[UC-ID]/scripts/`, `execution/[UC-ID]/logs/`, và thư mục `scratch/`. |
| **Persistence Rule** | Chỉ giữ lại: 1. File Test Case gốc, 2. Báo cáo kết quả (.xlsx), 3. Báo cáo Audit (.md), 4. Ảnh chứng minh FAIL. |

---
*Last Updated: 2026-05-15 | Version: 3.2 (Cleanup Policy Added)*
