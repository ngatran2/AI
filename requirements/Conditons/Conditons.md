PHỤ LỤC 01: CHỨC NĂNG CẤU HÌNH ĐIỀU KIỆN KHÁCH VÀO PHÒNG CHỜ LINH HOẠT.
Yêu cầu nghiệp vụ
Chức năng cấu hình điều kiện khách vào phòng chờ linh hoạt là chức năng của hệ thống cho phép:
Tách biệt logic nghiệp vụ khỏi code ứng dụng
Người sử dụng có thể tạo, sửa, quản lý các business rules
Người sử dụng có thể thay đổi rules mà không cần deploy tại ứng dụng
Người sử dụng có thể đánh giá các rules một cách nhất quán và có thể kiểm tra được.
Yêu cầu kỹ thuật
Mục tiêu kỹ thuật
Mục tiêu
Yêu cầu
Đo lường
Hiệu năng
Đánh giá nhanh
< 500 ms cho 100 rules
Độ tin cậy
Kết quả nhất quán
100% deterministic
Linh hoạt
Thay đổi dễ dàng
Deploy rule < 5 phút
Khả năng mở rộng
Thêm rule không giới hạn
Hỗ trợ 500+ rules
Khả năng bảo trì
Dễ debug, dễ hiểu
Non-tech users quản lý được
Khả dụng
Hoạt động offline
99.9% uptime
Khả năng xử lý phức tạp
Xử lý được các yêu cầu nghiệp vụ phức tạp
Yêu cầu tech xử lý code


Các thành phần chính
STT
Tên
Mô tả
1
Rule repository
Lưu trữ và quản lý định nghĩa rules, version, metadata
2
Rule parser
Chuyển đổi rule definition thành cấu trúc có thể thực thi
3
Rule compiler
Tối ưu hóa rules để thực thi nhanh hơn
4
Execution engine
Đánh giá rules với dữ liệu đầu vào, trả về kết quả
5
Audit and Logging
Ghi lại mọi quyết định, hỗ trợ debug và compliance

Rule Repository
Chức năng
Rule Repository là nơi lưu trữ tất cả định nghĩa rules với các chức năng:
Lưu trữ:
Định nghĩa rule
Metadata (tên, mô tả, tác giả, ngày tạo)
Trạng thái lifecycle (draft, active)
Lịch sử versions
Quản lý:
Tạo, đọc, sửa, xóa rules
Tìm kiếm và lọc rules
Nhóm rules theo category
Quản lý dependencies giữa các rules
Đồng bộ:
Sync rules đến các edge devices
Đảm bảo consistency giữa các nodes
Hỗ trợ offline operation
  
Identity
Rule Id: Số định danh của rule
Rule Code: Mã định danh của rule
Rule Name: Tên Rule
Description: Mô tả
Category: Loại Counter, Point, …
Tags or Group: Dùng để tìm kiếm hoặc phân loại
Rule Logic:
Rule order (priority): Thứ tự ưu tiên xử lý của các rule
Conditions (WHEN clause)
Danh sách các thông tin được sử dụng được mô tả chi tiết tại mục 3
Các hàm logic (AND, OR, NOT, …)
Actions (THEN clause)
Assignments
Function calls
Control flow (Optional)
Alternative Actions (ELSE clause- optional)
Phạm vi và đối tượng áp dụng:
Các phòng chờ
Các đối tác
Các nguồn khác
Thời gian bắt đầu hiệu lực
Thời gian kết thúc hiệu lực
Các khoảng thời gian đặc biệt (ngày nghỉ, các ngày hoặc giờ được chọn)
Các thông tin khác phục vụ kiểm soát và theo dõi
Trạng thái của rules (active, inactive, Draft…)
Tạo bởi ai
Thời gian tạo
Chỉnh sửa bởi ai
Thời gian chỉnh sửa
Nội dung chỉnh sửa
Rules set (Optional)
Rules được nhóm thành Rule Sets để quản lý và thực thị
Các chế độ riêng rành cho Rule set
Mode
Mô tả
Use Case
ALL_MATCHING
Chạy tất cả các rule thỏa mãn trong set
Tìm các nguồn thỏa mãn
FIRST_MATCH
Dừng khi rule đầu tiên match
Theo nguồn được chọn
TOP_PRIORITY
Chỉ chạy rule được ưu tiên cao nhất
Tránh các conflict xảy ra
SEQUENTIAL
Chạy theo thứ tự tuần tự, rule sau có thể override lên rule trước
Dùng trong các trường hợp giảm giá, khuyến mại


Yêu cầu về ngôn ngữ khi tạo rules
Ngôn ngữ sử dụng cho rule cần đáp ứng các tiêu chí sau:
Đối với người dùng nghiệp vụ
Dễ đọc, gần với ngôn ngữ tự nhiên
Không cần biết lập trình (optional)
Có thể dễ dàng training
Có phần chuyên sâu cho người dùng có kiến thức lập trình
Đối với hệ thống
Có cấu trúc rõ ràng, dễ hiểu
Có thể validate syntax
Có thể compile để check lỗi hoặc tối ưu (optional)
Có mô phỏng kết quả của rules phục vụ mục đích kiểm tra
Các dữ liệu đầu vào và các hàm thực thi 
Mô tả chi tiết tại bảng ở mục 3
Phần thực thi rules và trả kết quả
Luồng thực thi
INPUT: Các dữ liệu được mô tả ở mục 3
Step 1: Tổng hợp dữ liệu
Phân tích dữ liệu đầu vào
Xác thực các trường bắt buộc
Tra cứu dữ liệu bổ sung (các thông tin liên quan)\
Tính toán các trường dữ liệu
 Xây dựng các đối tượng để tính toán
Step 2: Kiểm tra rule set để lựa chọn
Xác định rule set cần chạy
Tải dữ liệu các rule thực thi từ cache
Lọc rules theo từng scope
Step 3: Đánh giá Rule
Đối với từng rule set:
Sắp xếp rules theo thứ tự ưu tiên
Đối với từng rule:
Đánh giá mệnh đề WHEN
Nếu khớp: Thực thi mệnh đề THEN
Không khớp: Thực thi mệnh đề ELSE hoặc các hành động khác (Optional)
Ghi nhận kết quả đánh giá
Áp dụng chế độ thực thi của rule set (ALL_MATCHING, FIRST_MATCH, …)
Step 4: Tổng hợp kết quả
Thu thập kết quả từ các rule
Giải quyết xung đột
Tính toán quyết định cuối
Tính toán các loại khuyến mại, quyền lợi.
Step 5: Kiểm tra và phản hồi
Có log ghi nhận quá trình thực thi
Ghi nhận quyết định để kiểm tra
Tạo đối tượng phản hồi
Trả kết quả cho người khởi tạo\
OUT PUT
Quyết định, quyền lợi, …
Cách đánh giá điều kiện trong mệnh đề WHEN
Đánh giá trật tự sắp xếp:
Phân tích điều kiện thành cây biểu thức (expression tree)
Đánh giá là các nodé lá đến rễ
Tạo đường tắt khi có thể (AND với false, OR với true)
Ví dụ:
Customer.is_active = true
AND customer.Age() >= 60
AND (flight.type = “INTERNATIONAL” OR customer.is_vip = true)
Đánh giá:
Step 1: Customer.is_active = true - TRUE
Step 2: AND customer.Age() >= 60 – TRUE
Step 3: flight.type = “INTERNATIONAL” – TRUE
Step 4: OR(TRUE,… ) – TRUE (đường tắt)
Step 5: AND(TRUE, TRUE, TRUE) – TRUE 
Kết quả: Điều kiện khớp
Quy tắc thực hiện đường tắt
AND: Dừng ngay khi gặp FALSE
OR: Dừng ngay khi gặp TRUE
Cách thực thi hành động trong mệnh đề THEN
Gán giá trị
Set result.eligible = true
Set guest.invite_free = 1
Gọi các hàm liên quan
Hàm thông báo cho HV hoặc gửi Message đến app
Hàm ghi nhận chấp nhận khách hợp lệ “ACCESS_GRANDTED”
Điều kiện trong thực thi
If guest.age < 12 THEN
    SET pricing.invite_guest = 0
Điều khiển luồng
STOP: Dừng rule set, không chạy tiếp
CONTINUE: Tiếp tục xử lý rule tiếp theo
RETURN value – Trả về giá trị và dừng
INDEPENDENCE: Hành động diễn ra độc lập 
Trật tự thực thi:
Các hành động được thực thi tuần tự từ trên xuống dưới
Kết quả của action trước có thể ảnh hưởng đến action sau hoặc độc lập tùy cấu hình của action
Giải quyết xung đột
Khi nhiều rules khớp, cần giải quyết xung đột giữa các rule
Các loại xung đột:
Khách có thể hợp lệ từ nhiều nguồn -> Chọn nguồn có quyền lợi tốt nhất
Một rule set hợp lệ, rule khác set không hợp lệ -> Chọn rule có ưu tiên cao hơn
Nhiều kết quả khuyến mãi trùng lặp -> Áp dụng theo chiến thuật tùy chọn (stack, best, first..) 
Mô phỏng kết quả của 1 Rules
Có chức năng mô phỏng kết quả 
Các thông tin dữ liệu đầu vào và các hàm thực thi
Các hàm thực thi
Các kiểu dữ liệu
Kiểu
Mô tả 
Ví dụ
Text
Chuỗi ký tự
“GOLD”, “Vietnam Airlines” 
Number
Số nguyên hoặc thập phân
100, 3.5, -10
Boolean
Đúng/Sai
True, false
Date
Ngày
2025-01-15
DateTime
Ngày và giờ
2025-01-15 14:30:00
Duration
Khoảng thời gian


List
Danh sách giá trị


Null






Các hàm so sánh
Toán tử
Mô tả
Ví dụ
=
Bằng
Customer.tier =”Gold”
!=
Không bằng
Flight.carrier != “VN”
>
Lớn hơn
Customer.Age > 25
>=
Lớn hơn hoặc bằng
Customer.Age >= 25
<
Nhỏ hơn
Time_to_departure < 4h
<=
Nhỏ hơn hoặc bằng
Customer.nominee_list.count <=12
InList
Trong danh sách
Ticket.Booking_class InList (‘A’,’B’,’C’)
LIKE
Khớp pattern
Flight.Numbẻ like “4****”
CONTAINS
Chứa giá trị










Các hàm logic
Toán tử
Mô tả 
Ví dụ
AND
Và
Condition 1 AND condition 2
OR
Hoặc
Condition 1 OR conditiion 2
NOT
Phủ định
NOT(customer.is_blacklisted)
()
Nhóm điều kiện
(a OR b) AND c


Các hàm số học
Toán tử
Mô tả
Ví dụ
+
Cộng


-
Trừ


*
Nhân


/
Chia


%
Chia lấy dư


IS NULL
Không có giá trị




Các hàm có sẵn
Hàm Date/Time:
Hàm
Mô tả
Ví dụ
NOW
Lấy thời gian hiện tại
Định dạng: DD/MM/YYYY HH:MM:SS


TODAY
Lấy ngày hiện tại
DD/MM/YYYY


ADD_TIME
Cộng trừ thời gian


YEAR
Trả về năm của biến thời gian


MONTH
Trả về tháng của biến thời gian


DAY
Trả về tháng của biến thời gian


DAY_OF_WEEK
Ngày trong tuần


HOUR
Trả về giờ của biến thời gian



     
Hàm xử lý chuỗi: 
Hàm
Mô tả
Ví dụ
UPPER
Chuyển ký tự thành ký tự in hoa


LOWER
Chuyển ký tự thành ký tự in thường


TRIM
Xóa khoảng trắng


LENGTH
Tính độ dài của chuỗi ký tự


SUBSTRING
Cắt chuỗi


CONCAT
Gộp chuỗi


COUNT
Đếm


SUM
Tổng


AVG
Trung bình


MIN
Lấy giá trị nhỏ nhất


MAX
Lấy giá trị lớn nhất


FIRST
Lấy phần tử đầu tiên trong list


LAST
Lấy phần tử cuối trong list




Hàm tiện ích
Hàm
Mô tả
Ví dụ
IF
Hàm điều kiện


COALESCE
Hàm chọn giá trị đầu tiên không bị null


ROUND
Làm tròn


FLOOR
Làm tròn xuống


CEIL
Làm tròn lên


ABS
Giá trị tuyệt đối




Các hàm build chuyên biệt
Hàm
Mô tả
Ví dụ
GET_LOUNGE
Lấy thông tin Lounge
GET_LOUNGE(lounge_id)
GET_FLIGHT_STATUS
Lấy trạng thái chuyến bay
GET_FLIGHT_STATUS(flight_number)
CHECK_BLACKLIST
Kiểm tra có trong blacklist
CHECK_BLACKLIST(passport)
GET_USAGE_COUNT
Đếm lượt sử dụng
GET_USAGE_COUNT(card, year)
CHECK_WHITELIST
Kiểm tra co trong whitelist
CHECK_WHITELIST(card)


Các dữ liệu theo fact model
Model
Trường dữ liệu
Mô tả
Data types
Ticket


PRI_DOCNUM
Mã định danh của vé hoặc EMD
Text


CJT_DOCNUM
Mã định danh của vé nối
Text


PNR
Mã định danh cho mã đặt chỗ
Text


TICKET_TYPE
Loại chứng từ (TICKET, EMD_ASSOCIATED, EMD_STANDALONE)
Ví dụ: "TICKET"
Text


NUMBER_OF_BOOKLETS
Thứ tự của vé nối hoặc EMD trong chứng từ
Text


STATUS
Trạng thái của vé. Theo chuẩn của IATA PADIS Code List for data element 4405
enum (EXCHANGED, FLOWN, EXCHANGED_TO_FIM, COUPON_NOTIFICATION, OPEN_FOR_USE, REFUNDED, SUSPENDED, VOID, CLOSED, REVOKED, PRINTED, PRINT_EXCHANGE, NOT_AVAILABLE, BOARDED, IRREGULAR_OPERATIONS, ORIGINAL_ISSUE, CHECKED_IN, AIRPORT_CONTROL, UNAVAILABLE, REFUND_TAXES_AND_FEES, PAPER_TICKET)
Ví dụ: "EXCHANGED"
Text


FARE_BASIS_CODE
Mã giá
Text


ISSUE_DATE
Ngày xuất vé
Date


SCHEDULE_DEPARTURE_DATE
Ngày bay dự kiến
Text


DEPARTURE_DATE
Ngày bay thực tế
Text


FF_AIRLINE_CODE
Mã của hãng bay mà khách hàng thường xuyên được thêm vào
Ví dụ “VN”
Text


FF_NUMBER
Mã định danh khách hàng thường xuyên – mã trên thẻ hội viên
Ví dụ “6X090807061234”
Text


MARKETING_CARRIER_CODE
Mã của airlines/ hãng vận chuyển bán vé
Text


MARKETING_CARRIER_NUMBER	
Mã chuyến bay của airlines/ hãng vẫn chuyển bán vé
Text


OPERATING_CARRIER_CODE
Mã của airlines/ Hãng vận chuyển thực hiện chuyến bay
Text


OPERATING_CARRIER_NUMBER
Mã chuyến bay vận chuyển
Text


ORIGIN
Mã IATA của sân bay xuất phát 1 hành trình
Text


DESTINATION
Mã IATA của sân bay đến trong 1 hành trình
Text


PAX_TYPE
Loại khách
Các giá trị: ADT, CHD,
INF, INS, UNA
Text


PAX_FIRST_NAME
Tên khách
Text


PAX_LAST_NAME
Họ của khách
Text


CABIN_CLASS
Mã Cabin của chuyến bay
Text


BOOKING_CLASS
Mã đặt chỗ
Text


ENDORSEMENT
Trường bổ sung định nghĩa hoặc comments, rules được áp dụng cho vé hoặc EMD
Text


TOUR_CODE
Mã Tour hoặc hợp đồng giá đặc biệt 
Text


COUPONS
Số coupon của vé 
Text


RFIC
Mã bán dịch vụ 
Text


SERVICE_REMARK
Remark cho dịch vụ mà EMD đính kèm
Text


SAC
Mã có trên coupon dùng để xác thực việc thanh toán/đối soát toàn bộ các khoản phí bằng tiền của coupon
Text


POI
Địa điểm xuất vé
Text


IOID
Mã đại lý xuất vé
Text


EQIV
Equivalent fare giá cước quy đổi




SECTOR_STATUS


Text


TOTAL_TAX
Tổng tiền thuế, phí và phụ phí hàng không
Text


FARE
Giá cước
Text


TOTAL
Tổng cộng
Text


FARE_CAL
Mã tính giá
Text


FOP
Hình thức thanh toán
Text


IS_ARNK
Chặng mặt đất
Boolean


NVB
Not valid before – Có giá trị từ
Date


NVA
Not valid after – Có giá trị đến
Text


BAGGAGE ALLOWANCE
Số lượng hành lý miễn cước
Text
FLIGHT


DEPARTURE_DATE
Ngày bay thực tế
Text


FLIGHT_CARRIER_CODE
Mã của airlines/ Hãng vận chuyển thực hiện chuyến bay
Text


FLIGHT_NUMBER
Mã chuyến bay vận chuyển
Text


ORIGIN
Mã IATA của sân bay xuất phát 1 hành trình
Text


DESTINATION
Mã IATA của sân bay đến trong 1 hành trình
Text


IS_CODESHARE
Check đúng chuyến bay codeshare hay không?
Boolean
CUSTOMER


CUSTOMER_ID
Mã định danh của khách
Text


CUSTOMER_TYPE
Loại khách được xác định:
SKT, VIP, CIP, FFP, OTHER, NON-SKT
Text


FFP_CARD
Số thẻ của hội viên
Text


FFP_CARRIER
Hãng phát hành thẻ
Text


TITLE
Title của khách
Text


CUS_FIRST_NAME
Tên của khách
Text


CUS_LAST_NAME
Họ của khách
Text


FFP_TIER
Hạng của hội viên
Text


FFP_EMAIL
Email của hội viên
Text


FFP_PHONE
Số điện thoại
Text


FFP_COUNTRY
Quốc gia của hội viên
Text


VALID_UNTIL
Thời hạn trên thẻ của hội viên
Text


IS_HOUSEHOLD
Thành viên gia đình
Text


IS_MAIN_ACC
Là chủ hộ
Text


IS_SEND_INVITE
Là người send lời mời
Text


CUSTOMER_DOB
Ngày sinh
Text


CUSTOMER_AGE
Tuổi
Text


CUSTOMER_DOC_TYPE
Loại giấy tờ tùy thân
Text


CUSTOMER_DOC_NUM
Số giấy tờ tùy thân
Text


IS_GUEST
Là khách mời
Boolean


INVITED_BY
Được mời bởi
Text


IS_BLACKLISTED
Có trong blacklist 
Boolean


IS_WHITELISTED
Có trong whitelist
Boolean


CUS_ATT1
Trường dữ liệu trống trong trường hợp cần dùng
Text


CUS_ATT2
Trường dữ liệu trống trong trường hợp cần dùng
Text


CUS_ATT3
Trường dữ liệu trống trong trường hợp cần dùng
Text


CUS_ATT4
Trường dữ liệu trống trong trường hợp cần dùng
Text


CUS_ATT5
Trường dữ liệu trống trong trường hợp cần dùng
Text
BOARDING_PASS


IS_VALID
Hợp lệ 
Text


BARCODE_TYPE
Loại Barcode: QR, loại …
Text


BARCODE_DATA
Barcode data
Text
PARTNER


PARTNER_ID
Số mã đối tác
Text


PARTNER _CODE
Mã của đối tác
Text


PARTNER _LOCATION
Địa điểm
Text


LOCATION_TYPE
Loại địa điểm
Text


PARTNER _COUNTRY
Quốc gia
Text


PARTNER _ADDRESS
Địa chỉ
Text


AIRPORT
Thuộc airport nào
Text


PARTNER_TYPE
Loại đối tác
Text


CAPACITY
Số lượng giới hạn
Text


STATUS
Trạng thái của partner
Active, Inactive
Text


CONTACT_PHONE
Số điện thoại liên hệ
Text


CONTACT_EMAIL
Email liên hệ
Text
PNR




Text


PNR
Mã định danh cho mã đặt chỗ
Text


BOOKING_DATE
Ngày tạo mã đặt chỗ
Text


OO_ID
Mã đại lý tạo mã 
Text


REMARKS
Remark
Text


SSR
Dịch vụ đặc biệt, dịch vụ bổ trợ
Text


SVC
Dịch vụ đặc biệt, dịch vụ bổ trợ
Text


SK
Special keyword
Text


OSI
Các dịch vụ khác
Text


FLIGHT
Chuyến bay
Text


TRAVELLER_ID
Mã hội viên
Text
BAGGAGE




Text


BAGTAG_LICPLATE
Số thẻ hành lý
Text


CB_ID
Mã định danh hành lý
Text


BAG_TYPE
Loại hành lý
Text


BAGTAG_ISSCARR
Ngày tạo số thẻ hành lý
Text


BAGTAG_FINALDES
Địa điểm cuối của hành lý
Text


OWNER_ID
Mã định danh người sở hữu
Text


CB_COUNT
Số kiện
Number


CB_WEIGHTVALUE
Số cân
Number


CB_WEIGHTUNIT
Đơn vị
Text


HB_COUNT
Số kiện hành lý xách tay
Number


HB_WEIGHTVALUE
Số cân
Number


HB_WEIGHTUNIT
Đơn vị
Text


