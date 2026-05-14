## ✅ Detail-Level Test Design Complete

| Artifact | File | Count |
|---|---|---|
| Test Cases (DET) | UC-DM-12_airport-category_testcases-det_20260509_v1.xlsx | 25 cases (5 GUI / 20 FUNC) |
| RTM Report | UC-DM-12_airport-category_rtm_20260509_v1.md | AC coverage: 100% |

### Requirement Traceability Matrix (RTM)
| AC ID | Acceptance Criteria / Business Rule | Linked Test Cases | Status |
|---|---|---|---|
| REQ-12.1 | Xem danh mục (Hiển thị, Phân trang, Search) | TC_UCDM12_GUI_01, TC_UCDM12_GUI_02, TC_UCDM12_FUNC_12, TC_UCDM12_FUNC_13 | Covered |
| REQ-12.2 | Thêm sân bay (Boundary, Dup, Validations) | TC_UCDM12_FUNC_01, TC_UCDM12_FUNC_02, TC_UCDM12_FUNC_03, TC_UCDM12_FUNC_04, TC_UCDM12_FUNC_05, TC_UCDM12_FUNC_07, TC_UCDM12_FUNC_20 | Covered |
| BR-12.3 | Cho phép thêm sân bay bị xóa | TC_UCDM12_FUNC_06 | Covered |
| BR-12.4 | Giữ nguyên filter sau thao tác | TC_UCDM12_FUNC_14 | Covered |
| REQ-12.3 | Xem chi tiết | TC_UCDM12_GUI_02 (Nút xem) | Covered |
| REQ-12.4 | Sửa sân bay (Read-only, Disable Lưu, Update) | TC_UCDM12_GUI_03, TC_UCDM12_GUI_04, TC_UCDM12_FUNC_08, TC_UCDM12_FUNC_09 | Covered |
| REQ-12.5 | Xóa sân bay (Thành công, Chặn xóa) | TC_UCDM12_FUNC_10, TC_UCDM12_FUNC_11 | Covered |
| REQ-INT | Tích hợp dữ liệu Sân bay sang Phòng chờ | TC_UCDM12_FUNC_15, TC_UCDM12_FUNC_16 | Covered |
| REQ-RBAC | Phân quyền truy cập | TC_UCDM12_FUNC_18 | Covered |
| CMR-12,13 | Global Rules (Timeout, Concurrency 404) | TC_UCDM12_FUNC_17, TC_UCDM12_FUNC_19 | Covered |
| CMR-08 | Pagination & Default | TC_UCDM12_GUI_02 | Covered |

### Self-Review Results
| # | Weakness Found | Action Taken |
|---|---|---|
| 1 | Chưa có testcase kiểm tra Loading State | Đã thêm TC_UCDM12_FUNC_19 cho trường hợp timeout (CMR-12) |
| 2 | Thiếu Data Integrity Test với Emoji/Unicode | Thêm TC_UCDM12_FUNC_20 kiểm tra Unicode |
| 3 | Logic nút Cập nhật khi text rỗng chưa rõ ràng | Đã thêm TC_UCDM12_FUNC_09 xử lý theo chuẩn Trim Space (CMR-03) |
