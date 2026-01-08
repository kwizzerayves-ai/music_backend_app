from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<filename>')
def serve_file(filename):
    # Müzik dosyalarını sun
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
        print("Site adresi: http://localhost:5000")
        print("\nKullanım:")
        print("  1. 'Hadi Dinle' butonuna tıklayın")
        print("  2. Müzik otomatik başlayacak ve buton kaybolacak")
        print("  3. Şarkı sözleri ay ışığı efektiyle görünecek")
        print("  4. İlk 5 satır hızlı, sonrası yavaş geçecek")
        print("  5. Arka planda %35 sesle yağmur efekti çalacak")
        print("\nGizli kontroller:")
        print("  - Boşluk (Space) tuşu: Müziği başlat")
        print("  - ESC tuşu: Sayfayı yenile")
        
        # Flask sunucusunu başlat
        app.run(debug=True, port=5000)
