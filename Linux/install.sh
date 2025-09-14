#!/bin/bash
# Gits kurulumu için otomatik script

set -e

# 1. Dosyaları indir ve geçici klasöre koy
TMP_DIR=$(mktemp -d)
echo "Geçici klasör: $TMP_DIR"

curl -fsSL https://raw.githubusercontent.com/LoLChC/Gits/main/Linux/gits.py -o "$TMP_DIR/gits.py"

# 2. Dosya formatını Linux uyumlu yap
sudo apt-get install -y dos2unix
dos2unix "$TMP_DIR/gits.py"

# 3. /usr/local/bin dizinine kopyala
sudo cp "$TMP_DIR/gits.py" /usr/local/bin/gits
sudo chmod +x /usr/local/bin/gits

# 4. Gerekli Python paketlerini yükle
python3 -m pip install --user requests pyinstaller

# 5. Temizle
rm -rf "$TMP_DIR"

echo "Gits başarıyla kuruldu! Artık terminalden 'gits' komutu ile çalıştırabilirsiniz."
