# Dự Án Dự Đoán Giá Nhà (House Price Prediction)

## Giới thiệu
Dự án này hướng đến việc thu thập dữ liệu nhà đất từ trang Meeyland (hoặc nguồn dữ liệu tương tự) và sử dụng các kỹ thuật Học máy (Machine Learning) để xây dựng mô hình dự đoán giá nhà. Thông qua việc phân tích và xử lý dữ liệu, dự án giúp đưa ra các gợi ý về giá bất động sản, hỗ trợ người dùng trong việc tham khảo, mua bán hoặc đầu tư nhà đất.

## Mục tiêu
- **Thu thập dữ liệu nhà đất** từ Meeyland bằng cách sử dụng Scrapy (hoặc công cụ crawl tương tự).
- **Tiền xử lý dữ liệu** và khám phá dữ liệu (EDA) nhằm làm sạch, chuẩn hóa và hiểu rõ đặc trưng của dữ liệu.
- **Xây dựng mô hình học máy** (ví dụ: Linear Regression, Random Forest, XGBoost, v.v.) để dự đoán giá nhà.
- **Đánh giá hiệu năng mô hình** và đề xuất cải thiện.

## Cấu trúc thư mục

```bash
HousePrice_Prediction/
│
├── Crawl_data/
│   ├── meeyland/
│   │   └── __pycache__/
│   ├── spiders/
│   │   ├── __pycache__/
│   │   ├── meeyland.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   └── settings.py
│   └── scrapy.cfg
│
├── data/
│   └── # Thư mục lưu trữ dữ liệu thô (raw data) hoặc dữ liệu sau khi crawl
│
├── houseprice_prediction.ipynb
│   # Notebook chính, bao gồm các bước:
│   # - Khám phá dữ liệu (EDA)
│   # - Xử lý, tiền xử lý dữ liệu
│   # - Xây dựng, huấn luyện mô hình dự đoán giá
│   # - Đánh giá và trực quan hóa kết quả
│
└── README.md
    # Hướng dẫn tổng quan về dự án
```

### 1. Thư mục `Crawl_data/`
- **meeyland/** và **spiders/**: 
  - Chứa các tệp tin Python định nghĩa **spider** dùng để thu thập dữ liệu từ website Meeyland.
  - Thư mục `__pycache__` tự động sinh ra khi chạy Python, không cần chỉnh sửa thủ công.
- **`meeyland.py`**: Định nghĩa lớp spider, mô tả cách duyệt qua các trang web, trích xuất dữ liệu (title, giá, diện tích, địa chỉ, thông tin liên hệ, v.v.).
- **`items.py`**: Khai báo các trường dữ liệu (fields) sẽ được lưu lại sau khi crawl.
- **`middlewares.py`** và **`pipelines.py`**: 
  - `middlewares.py` có thể dùng để xử lý request/response ở giữa quá trình crawl.
  - `pipelines.py` xử lý dữ liệu sau khi spider thu thập được (ví dụ: làm sạch dữ liệu, lưu vào CSDL).
- **`settings.py`**: Cài đặt các thông số cấu hình cho dự án Scrapy (như độ trễ giữa các request, số lượng concurrent requests, v.v.).
- **`scrapy.cfg`**: File cấu hình chung của dự án Scrapy, thường được tạo tự động khi khởi tạo dự án.

### 2. Thư mục `data/`
- Chứa dữ liệu thô (raw data) được thu thập từ quá trình crawl.
- Có thể bao gồm các file CSV, JSON hoặc các định dạng khác (tùy thuộc vào cấu hình `pipelines.py`).
- Thư mục này cũng có thể chứa dữ liệu đã được làm sạch hoặc xử lý để phục vụ cho quá trình huấn luyện mô hình.

### 3. Notebook `houseprice_prediction.ipynb`
Đây là file chính thực hiện các bước phân tích và xây dựng mô hình dự đoán giá nhà:
1. **Import thư viện**: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, v.v.
2. **Đọc dữ liệu**: Đọc file CSV hoặc JSON từ thư mục `data/`.
3. **Khám phá dữ liệu (EDA)**:
   - Kiểm tra các thông tin cơ bản về dữ liệu (kích thước, kiểu dữ liệu, thống kê mô tả).
   - Trực quan hóa mối quan hệ giữa các biến (giá, diện tích, vị trí, số phòng, v.v.).
   - Xử lý dữ liệu thiếu (missing values), dữ liệu ngoại lai (outliers).
4. **Tiền xử lý dữ liệu**:
   - Mã hóa (encoding) các biến phân loại (categorical variables).
   - Chuẩn hóa (scaling) các biến liên tục nếu cần.
5. **Xây dựng và huấn luyện mô hình**:
   - Áp dụng các mô hình hồi quy (Linear Regression, Random Forest, XGBoost, v.v.).
   - Chia dữ liệu thành tập huấn luyện (train set) và tập kiểm tra (test set).
   - Huấn luyện mô hình và điều chỉnh siêu tham số (hyperparameters).
6. **Đánh giá mô hình**:
   - Tính các chỉ số như MAE (Mean Absolute Error), RMSE (Root Mean Squared Error), R² (Coefficient of Determination).
   - So sánh kết quả giữa các mô hình và lựa chọn mô hình tối ưu.
7. **Trực quan hóa kết quả**:
   - Biểu đồ so sánh giá trị dự đoán và giá trị thực tế.
   - Biểu đồ phân bố sai số (residuals).

### 4. Hướng dẫn cài đặt và sử dụng
1. **Cài đặt môi trường ảo (khuyến nghị)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Trên Linux/Mac
   # hoặc .\venv\Scripts\activate (trên Windows)
   ```
2. **Cài đặt các thư viện cần thiết**:
   - Sử dụng file `requirements.txt` (nếu có) hoặc cài đặt thủ công:
     ```bash
     pip install scrapy
     pip install numpy pandas matplotlib seaborn scikit-learn plotly
     # ... và các thư viện khác nếu cần
     ```
3. **Chạy dự án crawl dữ liệu**:
   - Di chuyển vào thư mục `Crawl_data/`:
     ```bash
     cd Crawl_data
     scrapy crawl meeyland  # tên spider được định nghĩa trong meeyland.py
     ```
   - Dữ liệu sau khi crawl sẽ được lưu trong thư mục `data/` hoặc đường dẫn bạn cấu hình.
4. **Phân tích và dự đoán**:
   - Mở notebook `houseprice_prediction.ipynb` bằng Jupyter Notebook hoặc JupyterLab.
   - Chạy các cell theo thứ tự để thực hiện quá trình EDA, tiền xử lý, huấn luyện và đánh giá mô hình.

### 5. Kết quả
- **Kết quả**: 
  - Mô hình có thể dự đoán giá nhà với độ chính xác tương đối, hỗ trợ người dùng tham khảo giá thị trường.
  - Các biểu đồ và thống kê giúp nắm bắt xu hướng, yếu tố ảnh hưởng đến giá nhà (vị trí, diện tích, số phòng, v.v.).
