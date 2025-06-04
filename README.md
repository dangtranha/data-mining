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

### 4. Phân cụm khách hàng (Unsupervised)

Mục tiêu: phân nhóm khách theo hành vi

* Chuẩn hóa đặc trưng
* Áp dụng:

  * `KMeans` (kèm Elbow, Silhouette)
  * Hoặc thử `DBSCAN`, `Hierarchical`
* Trực quan:

  * PCA / t-SNE
  * Gán nhãn: VIP, trung thành, ngủ quên, vãng lai...


###  5. Phân tích giỏ hàng (Basket Analysis)

* Mục tiêu: tìm sản phẩm thường mua chung

* Biến hóa đơn thành dạng `Basket Matrix`
* Dùng:

  * `Apriori` hoặc `FP-Growth`
* Trích xuất luật kết hợp:

  * Confidence, Lift, Support
* Ví dụ:

  * Nếu mua **A + B**, thì mua thêm **C**?


### 6. Dự đoán khả năng quay lại của khách (Supervised)

* Tạo nhãn:

* `Returning = 1` nếu khách mua >1 lần trong một khoảng thời gian
* `Returning = 0` nếu chỉ mua một lần

Mô hình thử:

* `ANN (Keras)` – hoặc Logistic Regression, Random Forest

**Đánh giá:**

* Accuracy, F1, ROC AUC


### 7. Trực quan và báo cáo

* Biểu đồ cho từng bước (EDA, Clustering, Rules)
* Scatter plot các nhóm khách hàng
* Luật giỏ hàng dễ hiểu (If A → B, Lift = 2.1)
* Báo cáo markdown hoặc word

