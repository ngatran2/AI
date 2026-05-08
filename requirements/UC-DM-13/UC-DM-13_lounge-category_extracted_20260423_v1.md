# UC-DM-13: Lounge Category Management (Quản lý danh mục phòng chờ)

## 1. Overview
The Lounge Category Management screen allows users to view, search, add, edit, and delete lounge categories.

## 2. Use Cases
- UC-PC-13.1: View Lounge Category
- UC-PC-13.2: Add Lounge
- UC-PC-13.3: View Lounge Detail
- UC-PC-13.4: Edit Lounge
- UC-PC-13.5: Delete Lounge

## 3. Business Rules
- **BR-13.2**: Lounge Code must be unique across the category.
- **BR-13.3**: Can reuse a deleted Lounge Code.
- **BR-13.4**: Persistence of filters/search after successful addition.
- **BR-13.5**: Runtime permission check (RBAC) at API level.
- **BR-13.6**: Cannot delete if used in an active scanning session or entry configuration.
- **BR-13.7**: Soft-delete integrity.

## 4. Field Descriptions (UI-13.1-a)
1. Lounge Code (Mã phòng chờ)
2. Airport Code (Mã sân bay)
3. Lounge Name (Tên phòng chờ)
4. Capacity (Sức chứa)
5. Description (Mô tả)
6. Room Type (Loại phòng: International/Domestic)
7. Actions: View, Edit, Delete, Add New

## 5. UI/UX Rules
- Default sort: Created time descending.
- Empty state: Show CMR-08.
- Toast Messages: Verbatim strings like "Thêm mới [mã phòng chờ - tên phòng chờ] thành công."
