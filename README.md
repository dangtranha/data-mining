### MỤC TIÊU CHÍNH CỦA PROJECT

| Phần                       | Mục tiêu                                               |
| -------------------------- | ------------------------------------------------------ |
| Phân cụm khách hàng        | Tìm hiểu nhóm hành vi người mua (unsupervised)         |
| Phân tích giỏ hàng         | Khai phá các tổ hợp sản phẩm thường được mua chung     |
| Dự đoán quay lại của khách | Ứng dụng học có giám sát (ANN hoặc model truyền thống) |

## CHAY FILE runscripts de load du data cho cac service con lai

### 1. Thu thập và tiền xử lý dữ liệu

* Loại bỏ dòng thiếu `CustomerID`
* Xử lý cột `InvoiceDate` → trích ngày tháng
* Loại bỏ đơn trả hàng (`InvoiceNo` chứa "C")
* Tạo `TotalPrice = Quantity * UnitPrice`
* Xử lý dupicated
* Xử lý outlier

### 2. EDA – Khám phá dữ liệu

* Tổng số khách hàng, sản phẩm, hóa đơn
* Phân phối `Quantity`, `UnitPrice`, `TotalPrice`
* Phát hiện outliers tiếp nếu có

### 3. Feature Engineering theo `CustomerID`

Tổng hợp hành vi khách hàng:

| Đặc trưng gợi ý    | Ý nghĩa                         |
| ------------------ | ------------------------------- |
| Recency            | Số ngày kể từ lần mua gần nhất  |
| Frequency          | Số lần mua hàng                 |
| Monetary           | Tổng số tiền đã chi tiêu        |
| AvgOrderValue      | Trung bình giá trị mỗi đơn hàng |
| UniqueProductCount | Số sản phẩm khác nhau đã mua    |
| ReturnRate         | Tỷ lệ đơn hàng bị trả lại       |

### 4. Phân nhóm khách hàng (Customer Segmentation) và dự đoán đơn hàng bị huỷ
Sử dụng các chỉ số như RFM (Recency, Frequency, Monetary) để phân loại khách hàng thành các nhóm như:
- Khách hàng trung thành
- Khách hàng tiềm năng
- Khách hàng đã không còn mua hàng,...

Giúp doanh nghiệp thiết kế chiến lược tiếp thị phù hợp cho từng nhóm.

---

### 5. Phân cụm khách hàng (Customer Clustering)
Ứng dụng thuật toán học máy (ví dụ: KMeans) để tự động chia khách hàng thành các cụm dựa trên hành vi mua sắm.
- Không cần xác định nhóm trước, các cụm được tạo ra từ dữ liệu.
- Hữu ích để khám phá các kiểu mẫu hành vi ẩn trong dữ liệu.

---

### 6. Phân tích giỏ hàng (Market Basket Analysis)
Sử dụng các thuật toán như Apriori hoặc FP-Growth để xác định các mẫu sản phẩm thường được mua cùng nhau.
- Giúp đề xuất sản phẩm, thiết kế combo bán hàng, tăng giá trị đơn hàng trung bình.
- Ví dụ: “Khách mua Cốc thường cũng mua Đĩa”.

---

### 7. Dự đoán khả năng quay lại của khách hàng (Customer Retention Prediction)
Sử dụng mô hình dự đoán như Logistic Regression, Random Forest,... để ước lượng khả năng khách hàng sẽ tiếp tục mua hàng hay rời bỏ.
- Cho phép doanh nghiệp giữ chân khách hàng hiệu quả, tăng doanh thu.
- Có thể kết hợp với RFM để xác định khách hàng có nguy cơ rời bỏ cao.

---

### 8. Trực quan và báo cáo

* Biểu đồ cho từng bước (EDA, Clustering, Rules)
* Scatter plot các nhóm khách hàng
* Luật giỏ hàng dễ hiểu (If A → B, Lift = 2.1)
* Báo cáo markdown hoặc word

---
