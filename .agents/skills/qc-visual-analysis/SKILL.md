---
name: qc-visual-analysis
description: Đọc và phân tích thông tin từ các ảnh báo cáo (Performance reports, Automation dashboards, Screenshots) để trích xuất số liệu, đánh giá KPIs và đưa ra nhận xét/insight. Trigger khi user nói "đọc báo cáo từ ảnh", "phân tích biểu đồ này", "đánh giá kết quả test từ screenshot".
---
# Visual Report Analysis Skill

## Purpose
Sử dụng khả năng thị giác (Vision) để đọc các tài liệu báo cáo dưới dạng hình ảnh, trích xuất các thông số kỹ thuật (Response Time, Error Rate, Throughput, Pass/Fail rate) và thực hiện đánh giá so với KPIs hoặc đưa ra các nhận xét chuyên môn.

## Khi nào kích hoạt?
Khi người dùng:
- Cung cấp ảnh chụp dashboard (JMeter Dashboard, Grafana, Playwright Report).
- Yêu cầu: "Phân tích ảnh báo cáo này giúp tôi".
- Yêu cầu: "Đọc số liệu từ bảng trong ảnh và đánh giá xem có đạt KPI không".

## Quy trình thực hiện (Workflow)

### Phase 1: Trích xuất Dữ liệu (Extraction)
1. **Xác định loại báo cáo:** Nhận diện đây là báo cáo Performance, Automation, hay UI Audit.
2. **Quét các chỉ số chính (Key Metrics):**
   - **Performance:** Avg/Min/Max Response Time, P95/P99, Throughput (TPS), Error %.
   - **Automation:** Total Tests, Passed, Failed, Flaky, Duration.
   - **UI:** Visual discrepancies, Console errors (nếu có trong ảnh).
3. **Lập bảng số liệu:** Chuyển đổi dữ liệu từ ảnh sang bảng Markdown để dễ theo dõi.

### Phase 2: Đánh giá & So sánh (Evaluation)
1. **Đối chiếu KPI:** Nếu người dùng cung cấp KPI (ví dụ: P95 < 2s), hãy thực hiện so sánh trực tiếp.
2. **Xác định xu hướng (Trends):** Nếu có biểu đồ, nhận xét về xu hướng (ổn định, tăng đột biến, hay đi xuống).
3. **Phát hiện điểm bất thường (Anomalies):** Chỉ ra các vùng có Error cao hoặc Response Time tăng vọt (Spikes).

### Phase 3: Đưa ra nhận xét (Insights & Recommendation)
1. **Kết luận:** Đạt hay Không đạt (Pass/Fail).
2. **Nguyên nhân tiềm năng (RCA):** Dựa trên số liệu, phỏng đoán nguyên nhân (ví dụ: TPS tăng làm Response Time tăng -> Nghẽn cổ chai).
3. **Hành động tiếp theo:** Đề xuất re-test, tối ưu hóa code, hay scale hệ thống.

## Tiêu chí đánh giá (Evaluation Criteria)
1. **Accuracy (Độ chính xác):** Số liệu trích xuất phải khớp 100% với chữ/số hiển thị trong ảnh.
2. **Structured Output:** Báo cáo phải có bảng dữ liệu rõ ràng.
3. **Actionable Insights:** Không chỉ liệt kê số, phải nói rõ số đó có ý nghĩa gì đối với chất lượng hệ thống.

## Output Contract
- Báo cáo phân tích (.md) bao gồm:
  - Bảng số liệu trích xuất.
  - Phần đánh giá Pass/Fail so với KPI.
  - Danh sách các Insight và Khuyến nghị.
