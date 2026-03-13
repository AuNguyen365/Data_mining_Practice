# BÁO CÁO YÊU CẦU 2: TÍNH TRUNG BÌNH VÀ ĐỘ LỆCH CHUẨN

**Sinh viên thực hiện:** Hoàng Sơn  
**Bài tập:** Phân tích Iris Dataset - Practice 1 EDA  
**Yêu cầu:** Tính trung bình, độ lệch chuẩn của từng đặc trưng

---

## 1. MỤC TIÊU

Yêu cầu 2 tập trung vào việc tính toán và phân tích các thống kê mô tả cơ bản của Iris Dataset, bao gồm:
- Tính trung bình (mean) của từng đặc trưng
- Tính độ lệch chuẩn (standard deviation) của từng đặc trưng
- Hiển thị thống kê mô tả chi tiết
- Trực quan hóa kết quả bằng biểu đồ

---

## 2. PHƯƠNG PHÁP THỰC HIỆN

### 2.1. Công cụ và thư viện sử dụng

```python
import pandas as pd
import matplotlib.pyplot as plt
```

- **pandas**: Xử lý và phân tích dữ liệu
- **matplotlib**: Vẽ biểu đồ trực quan

### 2.2. Các bước thực hiện

#### Bước 1: Trích xuất các đặc trưng
```python
features = df.drop("species", axis=1)
```
Loại bỏ cột nhãn (species) để chỉ làm việc với các đặc trưng số.

#### Bước 2: Tính trung bình
```python
means = features.mean()
```
Sử dụng hàm `mean()` của pandas để tính giá trị trung bình của mỗi cột.

#### Bước 3: Tính độ lệch chuẩn
```python
stds = features.std()
```
Sử dụng hàm `std()` của pandas để tính độ lệch chuẩn mẫu (sample standard deviation).

#### Bước 4: Thống kê mô tả chi tiết
```python
features.describe()
```
Hiển thị các thống kê mô tả bao gồm: count, mean, std, min, 25%, 50%, 75%, max.

#### Bước 5: Trực quan hóa
Vẽ 2 biểu đồ cột (bar chart) để so sánh:
- Trung bình của các đặc trưng
- Độ lệch chuẩn của các đặc trưng

---

## 3. KẾT QUẢ

### 3.1. Trung bình của từng đặc trưng

| Đặc trưng | Giá trị trung bình |
|-----------|-------------------|
| sepal length (cm) | 5.8433 |
| sepal width (cm) | 3.0573 |
| petal length (cm) | 3.7580 |
| petal width (cm) | 1.1993 |

### 3.2. Độ lệch chuẩn của từng đặc trưng

| Đặc trưng | Độ lệch chuẩn |
|-----------|---------------|
| sepal length (cm) | 0.8281 |
| sepal width (cm) | 0.4359 |
| petal length (cm) | 1.7653 |
| petal width (cm) | 0.7622 |

### 3.3. Thống kê mô tả đầy đủ

```
       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
count         150.000000        150.000000         150.000000        150.000000
mean            5.843333          3.057333           3.758000          1.199333
std             0.828066          0.435866           1.765298          0.762238
min             4.300000          2.000000           1.000000          0.100000
25%             5.100000          2.800000           1.600000          0.300000
50%             5.800000          3.000000           4.350000          1.300000
75%             6.400000          3.300000           5.100000          1.800000
max             7.900000          4.400000           6.900000          2.500000
```

---

## 4. PHÂN TÍCH VÀ NHẬN XÉT

### 4.1. Về giá trị trung bình

- **Sepal length** có giá trị trung bình cao nhất (5.84 cm), cho thấy đây là đặc trưng có kích thước lớn nhất
- **Petal width** có giá trị trung bình thấp nhất (1.20 cm), là đặc trưng nhỏ nhất
- Các giá trị trung bình nằm trong khoảng hợp lý cho kích thước hoa Iris

### 4.2. Về độ lệch chuẩn

- **Petal length** có độ lệch chuẩn cao nhất (1.77), cho thấy sự biến thiên lớn trong chiều dài cánh hoa
- **Sepal width** có độ lệch chuẩn thấp nhất (0.44), cho thấy chiều rộng đài hoa khá đồng đều
- Độ lệch chuẩn cao của petal length và petal width cho thấy 2 đặc trưng này có khả năng phân biệt tốt giữa các loài

### 4.3. Ý nghĩa thống kê

1. **Phân bố dữ liệu**: Các đặc trưng có phân bố khác nhau, với petal length và petal width có độ biến thiên cao hơn

2. **Khả năng phân loại**: Đặc trưng có độ lệch chuẩn cao (petal length, petal width) thường hữu ích hơn trong việc phân biệt các lớp

3. **Chuẩn hóa dữ liệu**: Do các đặc trưng có thang đo và độ biến thiên khác nhau, cần chuẩn hóa trước khi áp dụng các thuật toán học máy nhạy cảm với scale (KNN, SVM, Neural Networks)

---

## 5. BIỂU ĐỒ TRỰC QUAN

### 5.1. Biểu đồ trung bình
Biểu đồ cột màu xanh lam (#4ECDC4) hiển thị giá trị trung bình của 4 đặc trưng, giúp so sánh trực quan kích thước trung bình của các đặc trưng.

### 5.2. Biểu đồ độ lệch chuẩn
Biểu đồ cột màu đỏ (#FF6B6B) hiển thị độ lệch chuẩn, cho thấy mức độ phân tán của dữ liệu quanh giá trị trung bình.

---

## 6. KẾT LUẬN

Yêu cầu 2 đã được hoàn thành với các kết quả chính:

1. Tính toán thành công trung bình và độ lệch chuẩn cho 4 đặc trưng của Iris Dataset
2. Hiển thị thống kê mô tả đầy đủ với 8 chỉ số quan trọng
3. Trực quan hóa kết quả bằng biểu đồ cột dễ hiểu
4. Phân tích và rút ra nhận xét về đặc điểm phân bố của dữ liệu

Các thống kê này cung cấp nền tảng quan trọng cho:
- Hiểu rõ đặc điểm của dataset
- Lựa chọn phương pháp tiền xử lý phù hợp
- Đánh giá khả năng phân biệt của các đặc trưng
- Chuẩn bị cho các bước phân tích tiếp theo

---

## 7. TÀI LIỆU THAM KHẢO

- Pandas Documentation: https://pandas.pydata.org/docs/
- Iris Dataset: https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset
- Descriptive Statistics: https://en.wikipedia.org/wiki/Descriptive_statistics

---

**Ngày hoàn thành:** 14/03/2026  
**File code:** `iris_eda.ipynb`  
**Nhánh Git:** `HoangSon`
