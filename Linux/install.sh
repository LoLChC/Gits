#!/bin/bash

# Kurulum dizini
INSTALL_PATH="/usr/local/bin"
APP_NAME="gits"
PY_FILE="${APP_NAME}.py"
URL="https://raw.githubusercontent.com/LoLChC/Gits/main/Linux/gits.py"

# Python3 kontrol
if ! command -v python3 &> /dev/null
then
    echo "Python3 bulunamadı! Lütfen yükleyin."
    exit 1
fi

# Dosya indirme
echo "Gits indiriliyor..."
curl -fsSL "$URL" -o "/tmp/$PY_FILE" || { echo "İndirme başarısız!"; exit 1; }

# Shebang ekle
sed -i '1i #!/usr/bin/env python3' "/tmp/$PY_FILE"

# Taşı ve çalıştırılabilir yap
sudo mv "/tmp/$PY_FILE" "$INSTALL_PATH/$APP_NAME"
sudo chmod +x "$INSTALL_PATH/$APP_NAME"

echo "Kurulum tamamlandı! Artık terminalden '$APP_NAME' komutu ile çalıştırabilirsiniz."
