# UC-BL-18: Blacklist Management (Quản lý danh mục Blacklist)

## 1. Overview
Managing members restricted from accessing specific lounges.

## 2. Use Cases
- UC-BL-18.1: View Blacklist
- UC-BL-18.2: View Blacklist Detail
- UC-BL-18.3: Add Member to Blacklist
- UC-BL-18.4: Edit Blacklist Member
- UC-BL-18.5: Remove Member from Blacklist

## 3. Business Rules
- **BR-18.3.1**: Error if Member Code doesn't exist.
- **BR-18.3.3**: "All Lounges" restricted hides individual selection.
- **BR-18.3.5**: Multiple blacklist records allowed for the same Member Code.
- **BR-18.4.1**: Member Code cannot be changed during edit.

## 4. Field Descriptions (UI-18.1-b)
1. Member Code
2. Restricted Access (All or count of lounges)
3. Effective Date
4. Expiry Date
5. Adder
6. Actions: View, Edit, Delete, Add Member

## 5. UI/UX Rules
- Pagination: 20 records per page.
- Lazy load for member dropdown.
- Toast Messages: "Thêm hội viên vào blacklist thành công".
