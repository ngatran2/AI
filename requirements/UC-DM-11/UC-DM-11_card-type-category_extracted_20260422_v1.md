# UC-DM-11: Card Type Category Management (Quản lý danh mục loại thẻ)

| Field       | Value                    |
|-------------|--------------------------|
| Source      | https://docs.google.com/document/d/1OfaNXQmPYw6p_aRSsWvWQ3mZ1b_VD-JMd1ZWZyXBrvc/edit?usp=sharing        |
| Extracted   | 2026-04-22              |
| Agent       | docs-reader               |
| UC-ID       | UC-DM-11                  |
| Version     | N/A |

## General Business Rules (Quy tắc nghiệp vụ chung)
*   **BR-11.3:** Within the same airline, the **Card ID** must be unique and cannot be duplicated. (Trong cùng một hãng bay, mã thẻ phải là duy nhất và không được phép lặp lại).
*   **BR-11.4:** It is possible to create a new Card ID that is identical to a previously deleted Card ID within the same airline. (Có thể thêm mới mã thẻ trùng với mã thẻ đã bị xóa trong cùng 1 hãng bay).
*   **BR-11.5:** Deleting a Card Type is not allowed if there is existing card data associated with that type in the system. (Không được phép xóa loại thẻ nếu đã có dữ liệu thẻ tương ứng với loại thẻ đó trong hệ thống).
*   **BR-11.6:** When a Card Type is deleted, the system performs a **soft delete**. (Khi xóa loại thẻ, hệ thống thực hiện xóa mềm).

## 2.2.11.1 UC-LT-11.1: View Card Type Category (Xem danh mục loại thẻ)
*   **Screen (UI-11.1-a):**
    *   **Airline (Hãng bay):** Combobox. Defaults to the first airline in the list.
    *   **Search (Tìm kiếm):** Textbox. Allows searching by Card Type Name or Card ID.
    *   **Add New (Thêm mới):** Button. Displayed only if the user has the "Add" permission.
*   **Data Table (Bảng danh sách):**
    *   Columns: No. (STT), Card ID (Mã thẻ), Card Type (Loại thẻ), Airline (Hãng bay).
    *   Actions: **View** (Xem), **Edit** (Sửa), **Delete** (Xóa).

## 2.2.11.2 UC-LT-11.2: Add Card Type (Thêm loại thẻ)
*   **Trigger:** Click the "Add New" button on the Category screen.
*   **Input Fields (UI-11.2-a Popup):**
    1.  **Airline (Hãng bay):** Combobox. Select the owning airline.
    2.  **Card ID (Mã thẻ):** 
        *   Textbox, maximum 30 characters.
        *   Allowed characters: English letters, numbers, and spaces.
        *   Automatic uppercase conversion.
        *   Mandatory field. Must be unique within the airline.
    3.  **Card Type (Loại thẻ):**
        *   Textbox, maximum 255 Unicode characters.
        *   Mandatory field.
*   **Audit Log:** Title: "Create New Card Type". Content: `[User Name] created card type [Card Type Name] for airline [Airline Name]`.

## 2.2.11.3 UC-LT-11.3: View Card Type Details (Xem chi tiết loại thẻ)
*   **Display:** Shows Card ID, Card Type, and Airline. All fields are **Read-only**.
*   **Action:** Close button to return to the list.

## 2.2.11.4 UC-LT-11.4: Edit Card Type (Sửa loại thẻ)
*   **Editable Fields:**
    *   **Card ID:** Read-only (Disable).
    *   **Airline:** Read-only (Disable).
    *   **Card Type:** Editable. Maximum 100 characters (as per the detail screen rule).
*   **Actions:** 
    *   **Update (Cập nhật):** Saves changes and shows success toast.
    *   **Delete (Xóa):** Triggers the delete process.
    *   **Close (Đóng):** Closes the popup without saving.

## 2.2.11.5 UC-LT-11.5: Delete Card Type (Xóa loại thẻ)
*   **Confirmation Popup:** "Are you sure you want to delete this card type?" (Bạn có chắc chắn muốn xóa loại thẻ này không?).
*   **Validation:** System checks **BR-11.5** before deleting. If there is associated data, the deletion is blocked.
*   **Result:** Soft delete performed; record no longer appears in active lists.
