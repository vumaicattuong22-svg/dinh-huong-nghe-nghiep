<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Định Hướng Nghề Nghiệp AI</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
    <style>
        .hero-section { background: linear-gradient(135deg, #0d6efd 0%, #6610f2 100%); color: white; padding: 80px 0; }
        .feature-box { border-radius: 12px; transition: transform 0.3s; }
        .feature-box:hover { transform: translateY(-5px); }
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
        <div class="container">
            <a class="navbar-brand fw-bold" href="#"><i class="bi bi-robot me-2"></i>CareerAI</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link active" href="#">Trang chủ</a></li>
                    <li class="nav-item"><a class="nav-link" href="#tests">Trắc nghiệm</a></li>
                    <li class="nav-item"><a class="nav-link" href="#profile">Hồ sơ của tôi</a></li>
                    <li class="nav-item"><a class="nav-link" href="#roadmap">Lộ trình</a></li>
                    <li class="nav-item"><a class="btn btn-outline-light ms-lg-2" href="#">Đăng nhập</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section text-center">
        <div class="container">
            <h1 class="display-4 fw-bold">Khám Phá Bản Thân – Định Hướng Tương Lai</h1>
            <p class="lead my-4">Hệ thống phân tích tính cách, sở thích và năng lực bằng Trí tuệ Nhân tạo AI</p>
            <a href="#tests" class="btn btn-warning btn-lg fw-bold me-2">Làm Trắc Nghiệm Ngay</a>
        </div>
    </section>

    <!-- Features -->
    <section id="tests" class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center mb-5 fw-bold">Các Mục Trắc Nghiệm & Phân Tích</h2>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="card h-100 p-4 border-0 shadow-sm feature-box text-center">
                        <i class="bi bi-compass display-4 text-primary mb-3"></i>
                        <h4>Trắc Nghiệm Holland</h4>
                        <p class="text-muted">Xác định 6 nhóm sở thích nghề nghiệp chuẩn quốc tế.</p>
                        <button class="btn btn-outline-primary mt-auto">Bắt đầu</button>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card h-100 p-4 border-0 shadow-sm feature-box text-center">
                        <i class="bi bi-cpu display-4 text-success mb-3"></i>
                        <h4>Phân Tích AI Tự Do</h4>
                        <p class="text-muted">Nhập mô tả tính cách, sở thích để AI đưa ra gợi ý chi tiết.</p>
                        <button class="btn btn-outline-success mt-auto">Phân tích ngay</button>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card h-100 p-4 border-0 shadow-sm feature-box text-center">
                        <i class="bi bi-person-badge display-4 text-purple mb-3"></i>
                        <h4>Hồ Sơ & Lịch Sử</h4>
                        <p class="text-muted">Xem lại các báo cáo định hướng đã lưu trong tài khoản.</p>
                        <button class="btn btn-outline-dark mt-auto">Xem hồ sơ</button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
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
