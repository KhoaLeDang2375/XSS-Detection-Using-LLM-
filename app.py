import mysql.connector 
from flask import Flask, request, jsonify, render_template, make_response
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

app = Flask(__name__)

# --- CẤU HÌNH KẾT NỐI MYSQL ---
db_config = {
    'host': 'localhost',
    'user': 'root',          
    'password': 'Thanhdan@1402',         
    'database': 'xss_demo_db' 
}

# Hàm lấy kết nối (Mở xong nhớ đóng)
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# --- CẤU HÌNH MODEL ---
MODEL_PATH = "./saved_model"
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    model.eval()
    print("Load model thành công!")
except Exception as e:
    print(f"Lỗi load model: {e}")

# --- BIẾN TRẠNG THÁI ---
SAFETY_MODE = False 

# --- LOGIC DỰ ĐOÁN ---
def check_xss(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)
    predicted_class_id = torch.argmax(probs, dim=-1).item()
    return predicted_class_id == 1

# --- ROUTES ---

@app.route('/')
def home():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('SecretToken', 'DayLaMatKhauNganHangCuaUser123')
    return resp

@app.route('/toggle_safety', methods=['POST'])
def toggle_safety():
    global SAFETY_MODE
    data = request.json
    SAFETY_MODE = data.get('status', False)
    return jsonify({'status': 'success', 'safety_mode': SAFETY_MODE})

@app.route('/get_comments', methods=['GET'])
def get_comments():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Lấy comment mới nhất lên đầu
        cursor.execute("SELECT content FROM comments ORDER BY id DESC")
        comments = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        conn.close()
        return jsonify(comments)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/post_comment', methods=['POST'])
def post_comment():
    content = request.json.get('content', '')
    
    if not content:
        return jsonify({'error': 'Nội dung rỗng'}), 400

    # 1. Kiểm tra an toàn nếu Mode đang BẬT
    if SAFETY_MODE:
        is_xss = check_xss(content)
        if is_xss:
            return jsonify({
                'status': 'blocked', 
                'message': 'CẢNH BÁO: Hệ thống phát hiện mã độc! Comment bị chặn.'
            })
    
    # 2. Lưu vào MySQL (nếu tắt Safe Mode hoặc Model thấy sạch)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = "INSERT INTO comments (content) VALUES (%s)"
        cursor.execute(sql, (content,))
        
        conn.commit() 
        cursor.close()
        conn.close()
        
        return jsonify({'status': 'success', 'message': 'Đã đăng bình luận thành công!'})
    except Exception as e:
        print("Lỗi Database:", e)
        return jsonify({'error': 'Lỗi Database'}), 500

@app.route('/clear_db', methods=['POST'])
def clear_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM comments") 
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'status': 'cleared'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)