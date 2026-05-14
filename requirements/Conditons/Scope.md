Scope POC:

FE validate syntax (Required)
BE validate syntax (Required)



Tạo được rule 
Sử dụng 5-10 fields cùng với các toán tử thông dụng bao gồm <,>,=,!=,AND, OR,IN,NOT ...
Then: Set biến, If/else (1 hoặc nhiều lớp), Gọi 1 function (Gửi mail)
Tạo được rule set support ALL Matching, First Match, Sequential
Validate ngày hiệu lực và thời gian áp dụng cho Rule và Ruleset
CRUD cho rule và rule set (Chưa handle các edge cases)



API để scan -> Tạm thời compare trực tiếp dữ liệu truyền lên với điều kiện của phòng chờ -> Trả kết quả và thực thi Then (Note: Tạm thời nếu match nhiều rule -> Cộng dồn)


Các yêu cầu chính