import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

SYSTEM_PROMPT = """
Bạn là Chuyên gia Định hướng Nghề nghiệp cho học sinh THPT Việt Nam.
Hãy phân tích dữ liệu đầu vào của học sinh dựa trên 5 bộ trắc nghiệm chuẩn hóa:
1. Holland (RIASEC): Sở thích nghề nghiệp
2. Đa trí thông minh (MI): Dạng năng lực nổi trội
3. MBTI: Kiểu tính cách
4. DISC: Xu hướng hành vi
5. Motivators: Động lực thúc đẩy nội tại

Yêu cầu đầu ra:
- Phân tích ngắn gọn sự kết hợp giữa các yếu tố.
- Gợi ý 3 nhóm nghề nghiệp phù hợp nhất.
- Đề xuất Tổ hợp môn học THPT tương ứng.
- Lời khuyên phát triển bản thân chân thành.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    if not client:
        return jsonify({"error": "Chưa cấu hình GEMINI_API_KEY trên Server!"}), 500

    data = request.json
    user_input = data.get("input_text", "")

    if not user_input:
        return jsonify({"error": "Vui lòng nhập thông tin!"}), 400

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Thông tin học sinh cung cấp:\n{user_input}",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.7,
            )
        )
        return jsonify({"result": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)