# Hệ thống Phát hiện Tấn công XSS sử dụng Deep Learning (RoBERTa)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![AI Model](https://img.shields.io/badge/Model-RoBERTa-orange)

> Nhập môn bảo đảm và an ninh thông tin - IE105.Q11 - Demo khả năng phòng thủ XSS bằng mô hình ngôn ngữ lớn (LLM).

---

## 📖 Giới thiệu

Dự án này xây dựng một hệ thống Web demo có khả năng phát hiện và ngăn chặn các cuộc tấn công **Cross-Site Scripting (XSS)** trong thời gian thực bằng cách sử dụng mô hình ngôn ngữ **RoBERTa** đã được tinh chỉnh.

Hệ thống được thiết kế để chạy trên máy local hoặc deploy lên server, với giao diện web thuận tiện cho việc kiểm tra và minh họa cách mô hình phát hiện payload XSS.

---

## 🎥 Video Demo

👉 **Demo hệ thống phát hiện XSS (YouTube):**
[https://youtu.be/QTv_XW1y7Is](https://youtu.be/QTv_XW1y7Is)

Video minh họa cách hệ thống hoạt động, giao diện web, và cách mô hình RoBERTa phát hiện cũng như chặn payload XSS trong thời gian thực.

---

## 📊 Kaggle Notebooks (Huấn luyện & Xử lý dữ liệu)

Dự án sử dụng các notebook trên Kaggle cho quá trình xử lý dữ liệu và fine-tuning mô hình:

* 🔁 **Tăng cường dữ liệu (Data Augmentation):**
  [https://www.kaggle.com/code/thoandanh/t-ng-c-ng-d-li-u-xss](https://www.kaggle.com/code/thoandanh/t-ng-c-ng-d-li-u-xss)

* 🎯 **Fine-tuning mô hình RoBERTa cho XSS Detection:**
  [https://www.kaggle.com/code/thoandanh/xss-detection](https://www.kaggle.com/code/thoandanh/xss-detection)

Các notebook này bao gồm các bước tiền xử lý dữ liệu, tăng cường dữ liệu XSS/Benign, huấn luyện và đánh giá mô hình.

---

## ✨ Tính năng chính

* 🕵️ **Phát hiện payload XSS** thông qua mô hình học sâu (RoBERTa).
* 🛡️ **Chặn và báo cáo** các payload độc hại trước khi lưu trữ.
* ⚡ **Dùng thử real-time** qua giao diện web.
* 📁 **Dễ cài đặt**: hướng dẫn rõ ràng để chạy local với virtual environment.

---

## 🔧 Yêu cầu (Prerequisites)

* Python 3.8+
* pip
* (Tùy chọn) Docker

---

## 🚀 Cài đặt & Chạy nhanh (Quick start)

1. Clone repository:

```bash
git clone https://github.com/KhoaLeDang2375/XSS-Detection-Using-LLM-.git
cd XSS-Detection-Using-LLM-
```

2. Tạo virtual environment và cài dependencies:

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

3. **Tải model**: Sau khi tải, giải nén/đặt các file model vào thư mục `saved_model/` (hoặc đường dẫn bạn muốn) và cấu hình biến môi trường `MODEL_PATH` nếu cần.

4. Khởi động ứng dụng:

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
flask run
```

Mở trình duyệt tại: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 Model

**LINK GOOGLE DRIVE MODEL:**
[https://drive.google.com/drive/folders/1PlhW0fxMgA1gZFXYmrsGxEQDbaJZ2_ir?usp=sharing](https://drive.google.com/drive/folders/1PlhW0fxMgA1gZFXYmrsGxEQDbaJZ2_ir?usp=sharing)

### Hướng dẫn sử dụng model

* Tải toàn bộ file model từ link Google Drive phía trên
* Đặt các file vào thư mục `saved_model/` trong repository, ví dụ:

  * `saved_model/config.json`
  * `saved_model/tokenizer.json`
  * `saved_model/model.safetensors`

Nếu bạn lưu model ở đường dẫn khác, hãy thiết lập biến môi trường `MODEL_PATH`.

**Ví dụ (Windows PowerShell):**

```powershell
$env:MODEL_PATH = "./saved_model"
```

---

## 🔎 Sử dụng & API

* 🌐 **Trang web demo:** `GET /`
* 🤖 **API dự đoán:** `POST /predict`

**Payload mẫu:**

```json
{
  "input": "<script>alert('XSS')</script>"
}
```

API trả về nhãn dự đoán (XSS / Benign) kèm theo score xác suất.

---

## 🛠️ Cấu hình (Config)

* `requirements.txt` — danh sách thư viện Python cần thiết.
* `config.py` — cấu hình hệ thống (nếu có).
* `saved_model/` — thư mục chứa mô hình đã fine-tune.

---

## ✅ Kiểm tra (Testing)

* Kiểm tra API bằng **Postman** hoặc **curl** thông qua endpoint `/predict`.
* Thử nhập trực tiếp payload trên giao diện web để xác nhận hệ thống chặn XSS.

---

## 🤝 Đóng góp (Contributing)

1. Fork repository
2. Tạo branch mới: `git checkout -b feature/your-feature`
3. Commit thay đổi: `git commit -m "Mô tả thay đổi"`
4. Push và tạo Pull Request

---

## 📚 Ghi chú

Dự án mang tính học thuật và demo cho mục đích nghiên cứu – giảng dạy môn **Nhập môn Bảo đảm và An ninh Thông tin**. Không khuyến nghị sử dụng trực tiếp trong môi trường production mà không qua kiểm thử và đánh giá bảo mật bổ sung.
