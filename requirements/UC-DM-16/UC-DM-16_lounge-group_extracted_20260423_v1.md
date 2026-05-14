# UC-DM-16: Lounge Group Management (Quản lý danh mục nhóm phòng chờ)

## 1. Overview
Grouping lounges for bulk access control or reporting.

## 2. Use Cases
- UC-PC-16.1: View Lounge Group List
- UC-PC-16.2: View Lounge Group Detail
- UC-PC-16.3: Add Lounge Group
- UC-PC-16.4: Edit Lounge Group
- UC-PC-16.5: Delete Lounge Group

## 3. Business Rules
- **BR-16.1.4**: Max 55 lounges per group.
- **BR-16.3.1**: Unique Group Code.
- **BR-16.3.5**: Error if adding beyond 55 lounges.
- **BR-16.3.6**: Check lounge availability (not deleted) during group assignment.

## 4. Field Descriptions (UI-16.1-b)
1. Group Code
2. Group Name
3. Number of Lounges
4. Description
5. Status
6. Actions: View Detail, Edit, Delete, Add New

## 5. UI/UX Rules
- Multi-tab UI: "Group Info" and "Lounges in Group".
- Search/Filter persistence in session storage.
- Toast Messages: "Thêm nhóm phòng chờ thành công".
