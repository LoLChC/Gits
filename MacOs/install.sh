#!/bin/bash

APP_NAME="gits"
INSTALL_DIR="/usr/local/bin"
CONFIG_DIR="$HOME/.gits"

echo "[*] $APP_NAME kurulumu başlatılıyor..."

# Python3 kontrol
if ! command -v python3 &> /dev/null; then
    echo "[-] Python3 bulunamadı, lütfen yükleyin."
    exit 1
fi

# Kurulum klasörünü oluştur
sudo mkdir -p "$INSTALL_DIR"

# Script'i indir
sudo curl -sL "https://raw.githubusercontent.com/LoLChC/Gits/main/gits.py" -o "$INSTALL_DIR/$APP_NAME"

# Çalıştırılabilir yap
sudo chmod +x "$INSTALL_DIR/$APP_NAME"

# Kullanıcı config klasörü oluştur
mkdir -p "$CONFIG_DIR"

echo "[+] Kurulum tamamlandı! Şimdi '$APP_NAME' komutunu kullanabilirsin."
