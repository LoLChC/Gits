#!/bin/bash
# Gits kurulumu için otomatik script

set -e

echo "Gits kurulumu başlıyor..."

# 1. Gerekli bağımlılıkları kontrol et
if ! command -v python3 &> /dev/null; then
    echo "Python3 yüklü değil. Lütfen önce Python3'ü yükleyin."
    exit 1
fi

# 2. Ana dizini oluştur
INSTALL_DIR="/opt/gits"
BIN_PATH="/usr/local/bin/gits"

echo "Kurulum dizini oluşturuluyor: $INSTALL_DIR"
sudo mkdir -p "$INSTALL_DIR"

# 3. Python dosyasını oluştur
echo "Python dosyası oluşturuluyor..."
sudo tee "$INSTALL_DIR/gits.py" > /dev/null << 'EOF'
#!/usr/bin/env python3
import argparse
import subprocess
import json
import os
import sys
from typing import Dict, List, Any

# KURULUM DİZİNİ DEĞİŞTİ - /opt/gits olarak ayarlandı
BASE_DIR = "/opt/gits"
JSON_PATH = os.path.join(BASE_DIR, "shortcuts.json")

def ensure_json_file():
    """Ensure the shortcuts JSON file exists"""
    try:
        # Önce dizinin var olduğundan emin ol
        os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
        
        if not os.path.exists(JSON_PATH):
            with open(JSON_PATH, "w", encoding="utf-8") as f:
                json.dump({"shortcuts": []}, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"JSON dosyası oluşturulurken hata: {e}")
        # Ev dizininde yedek oluştur
        home_dir = os.path.expanduser("~")
        fallback_path = os.path.join(home_dir, ".gits_shortcuts.json")
        print(f"Yedek dosya oluşturuluyor: {fallback_path}")
        
        with open(fallback_path, "w", encoding="utf-8") as f:
            json.dump({"shortcuts": []}, f, ensure_ascii=False, indent=4)
        
        return fallback_path
    return JSON_PATH

def load_data() -> Dict[str, Any]:
    """Load shortcuts data from JSON file"""
    json_path = ensure_json_file()
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        # Boş bir veri yapısı döndür
        return {"shortcuts": []}

def save_data(data: Dict[str, Any]):
    """Save shortcuts data to JSON file"""
    try:
        json_path = ensure_json_file()
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Veri kaydedilirken hata: {e}")

# KODUN GERİ KALANI AYNEN KALDI (orijinal kodunuz)
# ... (run_dynamic_shortcut, commit, repo, create, delete, list_shortcuts fonksiyonları)
# ... (build_parser_with_dynamic_subcommands ve main fonksiyonları)
EOF

# 4. Dosya izinlerini ayarla
sudo chmod +x "$INSTALL_DIR/gits.py"

# 5. JSON dosyasını oluştur ve izinleri ayarla
echo "JSON dosyası oluşturuluyor..."
sudo touch "$INSTALL_DIR/shortcuts.json"
sudo chmod a+rw "$INSTALL_DIR/shortcuts.json"

# 6. Başlangıç içeriği ile JSON dosyasını doldur
echo '{"shortcuts": []}' | sudo tee "$INSTALL_DIR/shortcuts.json" > /dev/null

# 7. /usr/local/bin dizinine sembolik link oluştur
echo "Sembolik link oluşturuluyor..."
sudo ln -sf "$INSTALL_DIR/gits.py" "$BIN_PATH"

echo "Gits başarıyla kuruldu!"
echo "Artık terminalden 'gits' komutu ile çalıştırabilirsiniz."