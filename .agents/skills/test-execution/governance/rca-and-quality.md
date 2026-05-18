# Quality Gate & RCA Analysis

Nghiệm thu toàn bộ kết quả sau khi chạy automation và phân tích lỗi.

## 1. Enterprise Leakage Detection (Rò rỉ Logic ngầm)
Đánh giá độ tin cậy bằng cách đối chiếu UI -> API -> DB. Nếu phát hiện "Pass giả" (Leakage), phải phân loại 4 cấp:
- **L1 (UI/API Mismatch):** UI Pass (màu xanh) nhưng Payload API trả về rỗng hoặc HTTP sai.
- **L2 (DB Persistence Failure):** API trả 200 nhưng DB hoàn toàn không ghi nhận record (mất data).
- **L3 (Replication/Async Delay):** Ghi nhận ở DB Master nhưng trễ ở Replica hoặc kẹt Queue.
- **L4 (Cross-service Inconsistency):** Lệch data giữa các microservices (VD: Trừ tiền thành công nhưng hóa đơn vẫn Pending).

## 2. Skipped Allowed Threshold
- Không chấp nhận Zero-Skip tuyệt đối, cho phép skip <= 3% tổng số TCs.
- **Điều kiện:** Phải có Reason Code hợp lệ (`ENV_DOWN`, `DATA_MISSING`...). Bỏ qua bừa bãi = Đánh sập (FAIL) toàn bộ Execution Run.

## 3. Evidence Correlation (Chống bằng chứng giả)
- Timestamp của Screenshot, API Network Log, DB Query Log **PHẢI ĐỒNG NHẤT** trong khung thời gian của Test Case. Lệch thời gian -> Kết quả hạ cấp thành `FAIL (Evidence Forged)`.

## 4. RCA (Root Cause Analysis) & Module Stability
Mọi TC bị FAIL phải gán một mã RCA:
- `[R1]` Actual Bug (Sai logic/code).
- `[R2]` Requirement Gap (Tài liệu sai).
- `[R3]` Infra/Environment (Môi trường sập).
- `[R4]` Script Flaw (Script automation dở).

**Tính điểm Module Stability (Weighted Defect Score):**
Nhân trọng số theo Severity (Critical x5, High x3, Medium x2, Low x1) trên mỗi 100 TCs.
- Green (Stable): Đủ chuẩn release.
- Yellow (At Risk): Cần test hồi quy (Regression) thêm.
- Red (Unstable): Nát, trả về code review toàn bộ.
