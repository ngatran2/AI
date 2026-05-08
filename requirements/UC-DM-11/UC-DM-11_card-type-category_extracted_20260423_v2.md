# UC-DM-11: Quản lý danh mục loại thẻ

| Field       | Value                    |
|-------------|--------------------------|
| Source      | https://docs.google.com/document/d/1OfaNXQmPYw6p_aRSsWvWQ3mZ1b_VD-JMd1ZWZyXBrvc/edit?usp=sharing |
| Extracted   | 2026-04-23              |
| Agent       | docs-reader               |
| UC-ID       | UC-DM-11                  |
| Version     | v2 |

## 2.2.11 UC-DM-11: Quản lý danh mục loại thẻ
ID
	Use case
	Mô tả
	UC-DM-11
	Quản lý danh mục loại thẻ
	Màn hình Danh mục loại thẻ bao gồm các UC:
                           * UC-LT-11.1: Xem danh mục loại thẻ
* UC-LT-11.2: Thêm loại thẻ
                           * UC-LT-11.3: Xem chi tiết loại thẻ
                           * UC-LT-11.4: Sửa loại thẻ
                           * UC-LT-11.5: Xóa loại thẻ
	Người dùng đăng nhập vào hệ thống, chọn “Danh mục - Loại thẻ” tại sidebar để truy cập chức năng Quản lý danh mục loại thẻ hội viên của hệ thống
Trigger
Người dùng chọn  “Danh mục - Loại thẻ” tại sidebar
Pre-conditions
                           * Người dùng đăng nhập hệ thống thành công 
                           * Người dùng có quyền truy cập các chức năng quản lý danh mục loại thẻ tùy theo phân quyền của người dùng, cụ thể từng chức năng được mô tả chi tiết tại từng use case bên dưới
Post-conditions
Tùy theo phân quyền của người dùng, người dùng có thể:
                           * Xem được danh mục các loại thẻ có trong hệ thống và chi tiết từng loại
                           * Thêm được loại thẻ mới vào danh mục
                           * Sửa thông tin loại thẻ trong danh mục
                           * Xóa loại thẻ khỏi danh mục


## 2.2.11.1 UC-LT-11.1: Xem danh mục loại thẻ
ID
	Use case
	Mô tả
	UC-LT-11.1
	Xem danh mục loại thẻ
	Người dùng có thể xem và tìm kiếm trong danh mục các loại thẻ hội viên từng hãng bay có trong hệ thống
	Trigger
Người dùng chọn  “Danh mục - Loại thẻ” tại sidebar
Pre-conditions
                           * Người dùng đăng nhập hệ thống thành công 
                           * Người dùng có quyền truy cập chức năng Xem Danh mục - Loại thẻ
Post-conditions
                           * Người dùng được điều hướng tới màn UI-11.1-a: Danh mục loại thẻ 
                           * Người dùng xem được danh sách các loại thẻ hội viên của từng hãng bay trên hệ thống
Basic Flow
                           1. Người dùng chọn  “Danh mục - Loại thẻ” tại sidebar
                           2. Hệ thống điều hướng người dùng tới màn UI-11.1-a: Danh mục loại thẻ 
                           3. Hệ thống tải và hiển thị danh sách loại thẻ trong bảng Danh mục loại thẻ
Alternative flow
[Tìm kiếm loại thẻ trong bảng Danh mục loại thẻ]
                           4. Người dùng nhấn icon Search tại các cột của bảng Danh mục loại thẻ
                           5. Hệ thống mở Popup search (CMR-09) trên màn UI-11.1-a 
                           6. Người dùng nhập từ khóa tìm kiếm vào popup
                           7. Người dùng gõ phím Enter
                           8. Hệ thống thực hiện tìm kiếm dựa trên từ khóa đã nhập
                           9. Hệ thống tải và hiển thị danh sách loại thẻ tương ứng
[Không có dữ liệu hoặc không có kết quả tìm kiếm]
Hiển thị màn trống trong bảng Danh mục loại thẻ (CMR-08)

### 2.2.11.1.1 Mô hình hóa quy trình
Biểu đồ xx: Quy trình xem danh mục loại thẻ

### 2.2.11.1.2 Wireframe/UI
Danh sách UI 
UI Code
	Screen
	UI-11.1-a
	Danh mục loại thẻ


### 2.2.11.1.3 Mô tả màn hình và quy tắc nghiệp vụ
Màn hình UI-11.1-a: Danh mục loại thẻ
ID
	Field Name
	Field type
	Validation Rule / Behaviour
	1
	Danh mục loại thẻ
	Table
	Display rule:
                           * Refer CMR-08 
                           * Mặc định hiển thị danh sách được sắp xếp theo thời gian tạo giảm dần
                           * Khi không có dữ liệu loại thẻ, hiển thị màn trống (CMR-08)
	2
	Mã thẻ
	Text
	Display rule:
                           * Hiển thị mã thẻ tương ứng của từng loại thẻ hội viên của 1 hãng bay
                           * Giới hạn hiển thị: hiển thị đủ mã không giới hạn
	3
	Loại thẻ
	Text
	Display rule:
                           * Hiển thị tên loại thẻ thuộc danh mục
                           * Giới hạn hiển thị: 1 dòng
	4
	Hãng bay
	Text
	Display rule:
* Hiển thị tên hãng bay sở hữu loại thẻ hội viên đó
                           * Giới hạn hiển thị: 1 dòng
	5
	Xem
	Button
	Display rule:
                           * Không hiển thị nếu người dùng có thêm quyền sửa Danh mục loại thẻ (hiển thị nếu người dùng có quyền xem và không có quyền sửa)
Behavior:
                           * Khi nhấn nút, hệ thống thực thi chức năng UC-LT-11.3: Xem chi tiết loại thẻ
	6
	Sửa
	Button
	Display rule:
                           * Chỉ hiển thị nếu người dùng có quyền sửa Danh mục loại thẻ
Behavior:
                           * Khi nhấn nút, hệ thống thực thi chức năng UC-LT-11.4: Sửa loại thẻ
	7
	Xóa
	Button
	Display rule:
                           * Chỉ hiển thị nếu người dùng có quyền xóa Danh mục loại thẻ
Behavior:
                           * Khi nhấn nút, hệ thống thực thi chức năng UC-LT-11.5: Xóa loại thẻ
	8
	Thêm mới
	Button
	Display rule:
                           * Chỉ hiển thị nếu người dùng có quyền thêm Danh mục loại thẻ
Behavior:
                           * Khi nhấn nút, hệ thống thực thi chức năng UC-LT-11.2: Thêm loại thẻ


## 2.2.11.2 UC-LT-11.2: Thêm loại thẻ
ID
	Use case
	Mô tả
	UC-LT-11.2
	Thêm loại thẻ
	Người dùng thêm loại thẻ hội viên mới của một hãng bay vào danh mục loại thẻ của hệ thống
	Trigger
Người dùng nhấn nút “Thêm mới” trên màn UI-11.1-a: Danh mục loại thẻ
Pre-conditions
                           * Người dùng đăng nhập hệ thống thành công 
                           * Người dùng đang ở màn UI-11.1-a: Danh mục loại thẻ
                           * Người dùng có quyền truy cập chức năng Thêm Danh mục - Loại thẻ
Post-conditions
                           * Loại thẻ mới được thêm vào danh mục
                           * Hệ thống hiển thị success toast message
                           * Loại thẻ mới hiển thị ở các danh sách loại thẻ được sử dụng trên toàn hệ thống
                           * Hệ thống log lịch sử thực hiện hành động với nội dung sau: 
                           * Tiêu đề: Tạo thẻ mới
                           * Thời gian tạo: dd/mm/yyyy hh:mm:ss
                           * Người thực hiện: Account thực hiện tạo hãng thẻ mới
                           * Nội dung chi tiết: Tạo mới thẻ [Mã thẻ] vào Danh mục loại thẻ
Basic Flow
                           1. Người dùng nhấn nút “Thêm mới” ở màn UI-11.1-a: Danh mục loại thẻ
                           2. Hệ thống hiển thị màn UI-11.2-a: Popup thêm loại thẻ 
                           3. Người dùng nhập các trường thông tin
                           4. Người dùng nhấn nút “Thêm mới” trên popup
                           5. Hệ thống kiểm tra các trường
                           6. [Nếu các trường hợp lệ] Hệ thống đóng popup và thêm 1 bản ghi mới ở csdl.
                           7. Hệ thống hiển thị success toast message: “Thêm mới [mã thẻ - loại thẻ] thành công.”
Alternative flow
[Nếu các trường không hợp lệ]
                           6. Hệ thống hiển thị thông báo lỗi tương ứng - Xem chi tiết tại mô tả màn hình
[Nếu người dùng chọn “Đóng” trên Popup]
                           4. Người dùng chọn “Đóng” trên Popup
                           5. Hệ thống đóng popup, đưa người dùng trở lại màn UI-11.1-a: Danh mục loại thẻ, và không thực hiện tạo loại thẻ hội viên mới vào csdl
[Nếu access token hết hạn trước khi nhấn “Thêm mới”]
                           6. Người dùng nhấn nút “Thêm mới” trên popup
                           7. Logout người dùng và hiển thị error toast message: “Thêm mới thẻ thất bại - Vui lòng thử lại sau.”
Business rule
BR-11.2: Mã thẻ không cần là duy nhất trên toàn danh mục
BR-11.3: Trong cùng một hãng bay, mã thẻ phải là duy nhất và không được phép lặp lại
BR-11.4: Có thể thêm mới mã thẻ trùng với mã thẻ đã bị xóa trong cùng 1 hãng bay
BR-11.5: Trong trường hợp người dùng đang áp dụng filter và/hoặc search trên màn hình danh sách và thực hiện thêm mới bản ghi thành công, hệ thống phải:
- Giữ nguyên các điều kiện filter và search hiện tại
- Giữ nguyên vị trí người dùng trên màn hình danh sách (bao gồm trang hiện tại/pagination)
- Nếu bản ghi mới thỏa điều kiện filter/search hiện tại, bản ghi mới được hiển thị trong danh sách theo quy tắc sắp xếp mặc định
- Nếu bản ghi mới không thỏa điều kiện filter/search hiện tại:
  + Bản ghi không hiển thị trong danh sách
  + Hệ thống vẫn hiển thị thông báo tạo mới thành công
BR-11.6: Trong trường hợp người dùng đã bị xóa, bị vô hiệu hóa hoặc bị thu hồi quyền truy cập trong khi vẫn còn session đang hoạt động:
- Hệ thống phải kiểm tra trạng thái và quyền của người dùng tại thời điểm xử lý mỗi API
- Không cho phép thực hiện các thao tác tạo/sửa/xóa dữ liệu


### 2.2.11.2.1 Mô hình hóa quy trình
Biểu đồ xx: Quy trình thêm loại thẻ vào danh mục

### 2.2.11.2.2 Wireframe/UI
Danh sách UI 
UI Code
	Screen
	UI-11.2-a
	Popup thêm loại thẻ

### 2.2.11.2.3 Mô tả màn hình và quy tắc nghiệp vụ
Màn hình UI-11.2-a: Popup thêm loại thẻ
ID
	Field Name
	Field type
	Validation Rule / Behaviour
	1
	Mã thẻ
	Text field
	Display rule:
                           * Placeholder: Nhập mã thẻ
Validation:
                           * Refer CMR-03
                           * Cho phép nhập tối đa 30 ký tự, không cho phép nhập thêm khi đã đủ
                           * Chỉ cho phép điền chữ (tiếng anh), số và ký tự space
                           * Tự động hiển thị chữ hoa khi nhập chữ thường
                           * Mã thẻ là trường bắt buộc (CMR-07)
                           * Khi người dùng nhập mã thẻ trùng với mã thẻ đã tồn tại của cùng hãng bay và nhấn nút “Thêm mới”, hệ thống hiển thị thông báo lỗi bên dưới trường: "Mã thẻ đã tồn tại trong hãng bay này."
	2
	Loại thẻ
	Text field
	Display rule: 
                           * Placeholder: Nhập loại thẻ
Validation:
                           * Refer CMR-03 
                           * Tối đa 100 ký tự. Không cho phép nhập thêm khi đã đủ.
	3
	Hãng bay
	Dropdown
	Display rule: 
                           * Placeholder: Chọn hãng bay
                           * Hiển thị danh sách tất cả hãng bay trong bảng Danh mục hãng bay
Validation:
                           * Refer CMR-02 
                           * Hãng bay là trường bắt buộc (CMR-07)
	4
	Đóng
	Button
	Behavior
                           * Nút luôn được enable
                           * Khi nhấn nút, đóng popup và đưa người dùng trở lại màn UI-11.1-a: Danh mục loại thẻ
                           * Hệ thống không tạo loại thẻ mới trong danh mục
	5
	Thêm mới
	Button
	Behavior:
                           * Nút luôn được enable
                           * Khi click, hệ thống kiểm tra các trường dữ liệu đã nhập và hiện validation rule tương ứng
                           * Nếu dữ liệu hợp lệ: 
                           * Đóng popup
                           * Thêm bản ghi mới ở csdl
                           * Hiện toast message "Thêm mới [mã thẻ - loại thẻ] thành công."
	6
	Close
	Button
	Behavior
                           * Khi nhấn nút, đóng popup và đưa người dùng trở lại màn UI-11.1-a: Danh mục loại thẻ
                           * Hệ thống không tạo loại thẻ mới trong danh mục


## 2.2.11.3 UC-LT-11.3: Xem chi tiết loại thẻ
ID
	Use case
	Mô tả
	UC-LT-11.3
	Xem chi tiết loại thẻ
	Người dùng có thể xem chi tiết của từng loại thẻ hội viên trong Danh mục loại thẻ
	Trigger
Tùy vào phân quyền người dùng, người dùng xem chi tiết của từng loại thẻ bằng cách nhấn nút 1 trong 2 nút:
* Nút Xem    ở dòng chứa loại thẻ hội viên muốn xem trên Danh mục loại thẻ (nút hiển thị nếu người dùng có quyền xem và không có quyền sửa Danh mục loại thẻ)
                           * Nút Sửa   ở dòng chứa loại thẻ hội viên muốn xem trên Danh mục loại thẻ (nút hiển thị nếu người dùng có quyền xem và quyền sửa Danh mục loại thẻ)
Pre-conditions
                              * Người dùng đăng nhập hệ thống thành công 
                              * Người dùng đang ở màn UI-11.1-a: Danh mục loại thẻ
                              * Người dùng có quyền truy cập chức năng Xem Danh mục - Loại thẻ
Post-conditions
                              * Người dùng được điều hướng tới màn UI-11.3-a: Popup chi tiết thẻ
                              * Người dùng xem được thông tin chi tiết của một loại thẻ hội viên của 1 hãng bay
Basic Flow
                              1. Người dùng nhấn nút Xem của một loại thẻ trên Danh mục
                              2. Hệ thống mở màn UI-11.3-a: Popup chi tiết thẻ 
Alternative flow
[Người dùng có quyền sửa Danh mục loại thẻ]
                              1. Người dùng nhấn nút Sửa của một loại thẻ trên Danh mục

### 2.2.11.3.1 Mô hình hóa quy trình
Biểu đồ xx: Quy trình xem chi tiết loại thẻ

### 2.2.11.3.2 Wireframe/UI
Danh sách UI 
UI Code
	Screen
	UI-11.3-a
	Popup chi tiết thẻ

### 2.2.11.3.3 Mô tả màn hình và quy tắc nghiệp vụ
Màn hình UI-11.3-a: Popup chi tiết thẻ
ID
	Field Name
	Field type
	Validation Rule / Behaviour
	1
	Mã thẻ
	Text field
	Display rule:
                              * Trường disable, không cho chỉnh sửa
                              * Hiển thị mã thẻ đã nhập khi tạo
	2
	Loại thẻ
	Text field
	Display rule: 
                              * Trường enable, cho phép chỉnh sửa
Validation:
                              * Refer CMR-03 
                              * Tối đa 100 ký tự. Không cho phép nhập thêm khi đã đủ.
	3
	Hãng bay
	Dropdown
	Display rule: 
                              * Trường disable, không cho phép chỉnh sửa
                              * Hiển thị danh sách tất cả hãng bay trong bảng Danh mục hãng bay
Validation:
                              * Refer CMR-02 
                              * Hãng bay là trường bắt buộc (CMR-07)
	4
	Xóa
	Button
	Display rule:
                              * Nút luôn được enable
                              * Chỉ hiển thị nếu người dùng có quyền Xóa danh mục loại thẻ
Behavior:
                              * Khi nhấn nút, hệ thống thực thi chức năng UC-LT-11.5: Xóa loại thẻ
	5
	Cập nhập
	Cập nhập
	Display rule:
                              * Disable khi chưa có thay đổi trong bản ghi
                              * Chỉ hiển thị nếu người dùng có quyền Sửa danh mục loại thẻ
Behavior:
                              * Khi nhấn nút, hệ thống cập nhập dữ liệu trường loại thẻ và trường hãng bay mới vào csdl
	6
	Close
	Button
	Behavior:
                              * Khi nhấn nút, hệ thống đóng popup và đưa người dùng trở lại màn UI-11.1-a: Danh mục loại thẻ
                              * Hệ thống không cập nhập thông tin bản ghi đó trong csdl

## 2.2.11.4 UC-LT-11.4: Sửa loại thẻ
ID
	Use case
	Mô tả
	UC-LT-11.4
	Sửa loại thẻ
	Người dùng chỉnh sửa một bản ghi loại thẻ đã tạo bằng cách nhấn nút Sửa
	Trigger
Người dùng nhấn nút Sửa    ở dòng chứa loại thẻ muốn thay đổi trên bảng Danh mục loại thẻ
Pre-conditions
                              * Người dùng đăng nhập hệ thống thành công 
                              * Người dùng đang ở màn UI-11.1-a: Danh mục loại thẻ
                              * Người dùng có quyền truy cập chức năng Sửa Danh mục - Loại thẻ
Post-conditions
                              * Hệ thống cập nhập dữ liệu bản ghi loại thẻ đó vào csdl
* Hệ thống hiển thị dữ liệu mới của bản ghi đó trên toàn bộ các danh mục loại thẻ được sử dụng trên toàn hệ thống
                              * Người dùng xem được thông tin mới chỉnh sửa tại màn UI-11.3-a: Popup chi tiết thẻ 
                              * Hệ thống log lịch sử thực hiện hành động với nội dung sau: 
                              * Tiêu đề: Chỉnh sửa thông tin thẻ
                              * Thời gian thực hiện: dd/mm/yyyy hh:mm:ss
                              * Người thực hiện: Account thực hiện cập nhật thông tin thẻ
                              * Nội dung chi tiết:
                              * Thay đổi thông tin thẻ [Mã thẻ]
[Tên trường] : Giá trị trước ==> [Tên trường]: Giá trị sau
Basic Flow
                              1. Người dùng nhấn nút Sửa ở dòng chứa loại thẻ muốn sửa
                              2. Hệ thống điều hướng người dùng tới màn UI-11.3-a: Popup chi tiết thẻ 
                              3. Người dùng chỉnh sửa các trường thông tin 
                              4. Người dùng nhấn nút “Cập nhập”
                              5. Hệ thống cập nhập dữ liệu mới vào csdl
                              6. Hệ thống giữ popup và hiển thị success toast message: “Cập nhập [mã loại thẻ - loại thẻ] thành công.”
Alternative flow
[Nếu người dùng chọn “Đóng” trên Popup]
                              4. Người dùng chọn “Đóng” trên Popup
                              5. Hệ thống đóng popup, đưa người dùng trở lại màn UI-11.1-a: Danh mục loại thẻ, và không thực hiện cập nhập bản ghi đó vào csdl
[Nếu access token hết hạn trước khi nhấn “Cập nhập”]
                              4. Người dùng nhấn nút “Cập nhập” trên popup
                              5. Logout người dùng và hiển thị error toast message: “Cập nhập thẻ thất bại - Vui lòng thử lại sau.”
[Nếu loại thẻ đang được sử dụng trong 1 scanning session]
                              4. Người dùng nhấn nút “Cập nhập” trên popup
                              5. Hệ thống không cập nhập bản ghi trong csdl và hiển thị error toast message: “Không thể cập nhập khi loại thẻ đang được sử dụng.”
Business rule
BR-11.4: Nếu loại thẻ đang được sử dụng trong một scanning session (runtime), hệ thống không cho phép chỉnh sửa và hiển thị thông báo lỗi.
BR-11.5: Nếu loại thẻ đang được sử dụng trong cấu hình điều kiện vào phòng chờ (configuration), hệ thống vẫn cho phép chỉnh sửa loại thẻ. Sau khi cập nhật, các thay đổi sẽ được hiển thị tại các màn hình cấu hình điều kiện và các master data đang tham chiếu đến loại thẻ đó.
BR-11.6: Hãng bay liên kết với loại thẻ là thông tin định danh và không được phép chỉnh sửa sau khi loại thẻ được tạo. Trong trường hợp cần thay đổi hãng bay, người dùng phải xóa loại thẻ hiện tại (nếu thỏa điều kiện) và tạo mới một loại thẻ khác.

### 2.2.11.4.1 Mô hình hóa quy trình
Biểu đồ xx: Quy trình sửa loại thẻ trong danh mục

## 2.2.11.5 UC-LT-11.5: Xóa loại thẻ
ID
	Use case
	Mô tả
	UC-LT-11.5
	Xóa loại thẻ
	Người dùng xóa một loại thẻ hội viên khỏi Danh mục loại thẻ
	Trigger
Người dùng nhấn nút Xóa ở 1 trong 2 màn sau:
                              *   Màn UI-11.1-a: Danh mục loại thẻ, trên dòng chứa loại thẻ muốn xóa khỏi bảng Danh mục loại thẻ
                              *    Màn UI-11.3-a: Popup chi tiết thẻ, của loại thẻ muốn xóa
Pre-conditions
                                 * Người dùng đăng nhập hệ thống thành công 
                                 * Người dùng đang ở 1 trong 2 màn 
                                 * UI-11.1-a: Danh mục loại thẻ
                                 * UI-11.3-a: Popup chi tiết thẻ
* Người dùng có quyền truy cập chức năng Xóa Danh mục - Loại thẻ
Post-conditions
                                 * Hệ thống xóa loại thẻ đó khỏi tất cả các danh mục loại thẻ được sử dụng trên toàn hệ thống
                                 * Bản ghi Hãng bay gắn với Loại thẻ đó được giữ nguyên
                                 * Hệ thống log lịch sử thực hiện hành động với nội dung sau: 
                                 * Tiêu đề: Xóa loại thẻ
                                 * Thời gian thực hiện: dd/mm/yyyy hh:mm:ss
                                 * Người thực hiện: Account thực hiện xóa thẻ
                                 * Nội dung chi tiết: Xóa thẻ [Mã thẻ] khỏi Danh mục loại thẻ
                                 * Người dùng có thể thêm mới Loại thẻ có cùng mã thẻ với thẻ bị xóa
Basic Flow
                                 1. Người dùng nhấn nút Xóa trên dòng chứa loại thẻ muốn xóa trên bảng Danh mục loại thẻ
                                 2. Hệ thống hiển thị màn UI-11.5-a: Popup xóa loại thẻ 
                                 3. Người dùng chọn “Xác nhận”
                                 4. Hệ thống xóa loại thẻ khỏi Danh mục loại thẻ 
                                 5. Hệ thống đóng popup và đưa người dùng trở lại màn UI-11.1-a: Danh mục loại thẻ
                                 6. Hệ thống hiển thị Toast message: “Xóa [mã thẻ - loại thẻ] thành công."
Alternative flow
[Người dùng nhấn Xóa ở màn Chi tiết loại thẻ]
                                 1. Người dùng nhấn nút Xóa ở popup Chi tiết thẻ của loại thẻ muốn xóa
[Nếu người dùng chọn “Đóng” trên Popup]
                                 3. Người dùng chọn “Đóng” trên Popup
                                 4. Hệ thống đóng popup, đưa người dùng trở lại màn UI-11.1-a: Danh mục loại thẻ, và không thực hiện xóa loại thẻ khỏi danh mục loại thẻ
[Nếu access token hết hạn trước khi nhấn “Xóa”]
                                 3. Người dùng nhấn nút “Xóa” trên popup
                                 4. Logout người dùng và hiển thị error toast message: “Xóa thẻ thất bại - Vui lòng thử lại sau.”
[Nếu bản ghi đang được sử dụng trong 1 scanning session hoặc đang được sử dụng trong cấu hình điều kiện]
                                 3. Người dùng nhấn nút “Xóa” trên popup
                                 4. Hệ thống không cập nhập bản ghi trong csdl và hiển thị error toast message: “Không thể xóa khi loại thẻ đang được sử dụng.”
Business rule
BR-11.6: Không cho phép xóa loại thẻ nếu loại thẻ đó đang được sử dụng trong:
- Một scanning session đang hoạt động (runtime scan processing), hoặc
- Cấu hình điều kiện cho phép khách vào phòng chờ.
BR-11.7: Trong trường hợp xóa thành công, hệ thống sẽ:
- Xóa loại thẻ khỏi danh mục quản lý
- Không cho phép lựa chọn bản ghi đã xóa trong các cấu hình hoặc thao tác phát sinh mới
Dữ liệu đã phát sinh trước thời điểm xóa (ví dụ: lịch sử scan, báo cáo, thông tin tham chiếu master data) vẫn được phép hiển thị để phục vụ mục đích tra cứu và báo cáo.
BR-11.8: Sau khi loại thẻ bị xóa, hệ thống không cho phép sử dụng bản ghi này trong quá trình mapping dữ liệu khi thực hiện scan mới.

### 2.2.11.5.1 Mô hình hóa quy trình
Biểu đồ xx: Quy trình xóa loại thẻ khỏi danh mục

### 2.2.11.5.2 Wireframe/UI
Danh sách UI 
UI Code
	Screen
	UI-11.5-a
	Popup xóa loại thẻ

### 2.2.11.3.3 Mô tả màn hình và quy tắc nghiệp vụ
Màn hình UI-11.5-a: Popup xóa loại thẻ
ID
	Field Name
	Field type
	Validation Rule / Behaviour
	1
	Đóng
	Button
	Behavior:
                                 * Nút luôn được enable
                                 * Khi nhấn nút: 
                                 * Hệ thống đóng popup
* Không thực hiện xóa loại thẻ khỏi danh mục loại thẻ
	2
	Xác nhận
	Button
	Behavior:
                                 * Nút luôn được enable
                                 * Khi nhấn nút:
                                 * Hệ thống đóng popup
                                 * Xóa loại thẻ khỏi tất cả các danh mục loại thẻ hiện tại trên toàn hệ thống
                                 * Hiển thị toast message "Xóa [mã thẻ - loại thẻ] thành công." 
