from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<filename>')
def serve_file(filename):
    allowed_files = ['Sevgilim.mp3', 'yağmur.mp3']
    if filename in allowed_files:
        return send_from_directory('.', filename)
    else:
        return "Dosya bulunamadı", 404


if __name__ == '__main__':
    # Gerekli dosyaların kontrolü
    required_files = ['Sevgilim.mp3', 'yağmur.mp3']
    missing_files = []

    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)

    if missing_files:
        print("Eksik dosyalar:")
        for file in missing_files:
            print(f"  - {file}")
        print("\nLütfen bu dosyaları index.html ve backend.py ile aynı klasöre koyun.")
    else:
        print("Sunucu başlatılıyor...")

    # 🔥 RENDER İÇİN KRİTİK KISIM
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
  )
