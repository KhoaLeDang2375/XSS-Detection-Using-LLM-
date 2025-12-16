# Hệ thống Phát hiện Tấn công XSS sử dụng Deep Learning (RoBERTa)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-green)
![AI Model](https://img.shields.io/badge/Model-RoBERTa-orange)

> Nhập môn bảo đảm và an ninh thông tin - IE105.Q11 - Demo khả năng phòng thủ XSS bằng mô hình ngôn ngữ lớn (LLM).

---

## 📖 Giới thiệu

Dự án này xây dựng một hệ thống Web demo có khả năng phát hiện và ngăn chặn các cuộc tấn công **Cross-Site Scripting (XSS)** trong thời gian thực bằng cách sử dụng mô hình ngôn ngữ (RoBERTa) đã được tinh chỉnh.

Hệ thống được thiết kế để chạy trên máy local hoặc deploy lên server, với giao diện web thuận tiện cho việc kiểm tra và minh họa cách mô hình phát hiện payload XSS.

---

## ✨ Tính năng chính

- 🕵️ **Phát hiện payload XSS** thông qua mô hình học sâu (RoBERTa).
- 🛡️ **Chặn và báo cáo** các payload độc hại trước khi lưu trữ.
- ⚡ **Dùng thử real-time** qua giao diện web.
- 📁 **Dễ cài đặt**: hướng dẫn rõ ràng để chạy local với virtual environment.

---

## 🔧 Yêu cầu (Prerequisites)

- Python 3.8+
- pip
- (Tùy chọn) Docker

---

## 🚀 Cài đặt & Chạy nhanh (Quick start)

1. Clone repository:

```bash
git clone https://github.com/KhoaLeDang2375/XSS-Detection-Using-LLM-.git
cd XSS-Detection-Using-LLM-
```

2. Tạo virtual environment và cài dependencies:

Windows (PowerShell):
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

Mở trình duyệt tại: http://127.0.0.1:5000

---

## 📦 Model (PLACEHOLDER)

**LINK DRIVE MODEL:** (https://drive.google.com/drive/folders/1PlhW0fxMgA1gZFXYmrsGxEQDbaJZ2_ir?usp=sharing)

Hướng dẫn: tải toàn bộ file model từ link Drive phía trên và đặt vào folder `saved_model/` trong repository (ví dụ: `saved_model/config.json`, `saved_model/tokenizer.json`, `saved_model/model.safetensors`, ...). Nếu bạn lưu model vào đường dẫn khác, đặt biến môi trường `MODEL_PATH` tương ứng.

Ví dụ trên Windows (PowerShell):
```powershell
$env:MODEL_PATH = "./saved_model"
```

---

## 🔎 Sử dụng & API

- Trang web demo: `GET /` (root)
- Endpoint dự đoán (ví dụ): `POST /predict` với payload JSON: `{ "input": "<user input>" }` => trả về kết quả phân loại và score.

---

## 🛠️ Cấu hình (Config)

- `requirements.txt` — chứa các thư viện cần cài.
- `config.py` — một số cấu hình (DB, secret keys, v.v.).
- `saved_model/` — nơi đặt model đã tải xuống.

---

## ✅ Kiểm tra (Testing)

- Có thể kiểm tra bằng cách gửi request qua Postman / curl tới `/predict`.
- Thực hiện test thủ công trên giao diện web để xác nhận hệ thống chặn payload XSS.

---

## 🤝 Đóng góp (Contributing)

1. Fork repository
2. Tạo branch feature: `git checkout -b feature/your-feature`
3. Commit thay đổi: `git commit -m "Mô tả thay đổi"`
4. Push lên branch và tạo Pull Request.

---

## 📝 License

Ghi rõ license của bạn ở đây (ví dụ MIT). Nếu bạn không chắc, tôi có thể thêm file `LICENSE` sau.

---

## ☎️ Liên hệ

Nếu bạn cần giúp điều chỉnh README hoặc muốn tôi chèn **link Drive model** vào chỗ chừa sẵn, nói cho tôi biết link hoặc cho phép tôi chèn giúp.

---

