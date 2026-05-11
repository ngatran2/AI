# Requirement Traceability Matrix (RTM)
## Feature: UC-DM-10 Quản lý hãng bay
**Version:** v1.0
**Date:** 2026-05-11

| AC ID | Acceptance Criteria (Extracted) | Linked Test Cases | Status |
|---|---|---|---|
| BR-GUI-01 | Hiển thị màn hình, phân trang, icon thao tác | TC_UC-DM-10_GUI_01, TC_UC-DM-10_GUI_02, TC_UC-DM-10_FUNC_21 | Covered |
| BR-GUI-02 | Nút Khôi phục xóa text, đóng popup | TC_UC-DM-10_GUI_04 | Covered |
| BR-GUI-03 | Nút Đóng popup không xóa text | TC_UC-DM-10_GUI_03 | Covered |
| BR-FUNC-01 | Thêm mới thành công, thông báo chuẩn | TC_UC-DM-10_FUNC_01 | Covered |
| BR-FUNC-02 | Trùng mã hãng bay | TC_UC-DM-10_FUNC_03 | Covered |
| BR-FUNC-03 | Sửa thành công, mã read-only | TC_UC-DM-10_FUNC_06, TC_UC-DM-10_FUNC_07 | Covered |
| BR-FUNC-04 | Xóa thành công (Soft Delete) | TC_UC-DM-10_FUNC_08 | Covered |
| BR-FUNC-05 | Chặn xóa do đang sử dụng | TC_UC-DM-10_FUNC_09 | Covered |
| BR-INT-01 | Đồng bộ Thêm/Sửa/Xóa sang Dropdown | TC_UC-DM-10_FUNC_11, TC_UC-DM-10_FUNC_12, TC_UC-DM-10_FUNC_13 | Covered |
| BR-RBAC-01| Phân quyền Admin, View, Edit | TC_UC-DM-10_FUNC_16, TC_UC-DM-10_FUNC_17 | Covered |
| CMR-03 | Trim khoảng trắng | TC_UC-DM-10_FUNC_04 | Covered |
| CMR-07 | Validate trường bắt buộc | TC_UC-DM-10_FUNC_02 | Covered |
| CMR-08/09/10| Tìm kiếm, lọc | TC_UC-DM-10_FUNC_19, TC_UC-DM-10_FUNC_20, TC_UC-DM-10_GUI_05 | Covered |
| CMR-12 | Timeout / Mất mạng / Loading State | TC_UC-DM-10_FUNC_14, TC_UC-DM-10_FUNC_15 | Covered |
| EDGE-01 | Concurrency | TC_UC-DM-10_FUNC_10 | Covered |
| EDGE-02 | XSS Security | TC_UC-DM-10_FUNC_05 | Covered |
| EDGE-03 | API Security (403) | TC_UC-DM-10_FUNC_18 | Covered |

### Summary
AC Coverage: 100%
