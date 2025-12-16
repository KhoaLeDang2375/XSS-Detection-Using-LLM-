// Biến trạng thái
let isSafetyOn = false;

// 1. Xử lý nút Bật/Tắt chế độ an toàn
const toggle = document.getElementById('safety-toggle');
const statusText = document.getElementById('status-text');

// --- ĐỒNG BỘ TRẠNG THÁI KHI LOAD TRANG ---
document.addEventListener('DOMContentLoaded', () => {
    // Luôn tắt chế độ bảo vệ khi vừa vào trang
    toggle.checked = false; 
    updateStatusUI(false);
    
    // Gửi tín hiệu về server để ép biến SAFETY_MODE thành False
    syncSafetyMode(false);

    // Tải comment
    loadComments();
});

toggle.addEventListener('change', async function() {
    isSafetyOn = this.checked;
    statusText.innerText = isSafetyOn ? "Đang bật - An toàn" : "Đang tắt - Nguy hiểm";
    statusText.className = isSafetyOn ? "status-on" : "status-off";

    // Gửi tín hiệu về server
    await fetch('/toggle_safety', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ status: isSafetyOn })
    });
});

// Load comment từ server
async function loadComments() {
    const res = await fetch('/get_comments');
    const comments = await res.json();
    
    const list = document.getElementById('comment-list');
    list.innerHTML = ''; // Xóa cũ

    comments.forEach(c => {
        const div = document.createElement('div');
        div.className = 'comment-item';
        // NGUY HIỂM: Gán trực tiếp innerHTML để code XSS chạy được
        div.innerHTML = `<strong>User:</strong> ${c}`; 
        list.appendChild(div);
        
        // Đoạn này để kích hoạt thẻ <script> nếu trình duyệt chặn tự động
        // (Một số trình duyệt hiện đại không chạy script thêm bằng innerHTML)
        const scripts = div.getElementsByTagName("script");
        for(let script of scripts) {
            eval(script.innerText);
        }
    });
}

// Gửi comment
async function postComment() {
    const input = document.getElementById('comment-input');
    const content = input.value;
    
    if(!content) return;

    const res = await fetch('/post_comment', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ content: content })
    });
    
    const data = await res.json();
    
    if (data.status === 'blocked') {
        alert(data.message); // Thông báo chặn của Model
    } else {
        input.value = '';
        loadComments(); // Load lại để thấy kết quả (hoặc hậu quả)
    }
}

async function clearDB() {
    await fetch('/clear_db', { method: 'POST' });
    loadComments();
}

// Load comment ngay khi vào trang
loadComments();