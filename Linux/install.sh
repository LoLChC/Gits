#!/bin/bash
# =========================================
# Gits Linux Global Kurulum Scripti
# =========================================

# Mevcut kurulumu kaldır
sudo rm -f /usr/local/bin/gits
sudo rm -rf /opt/gits

# /opt/gits dizinini oluştur
sudo mkdir -p /opt/gits

# Python scriptini indir
sudo curl -fsSL https://raw.githubusercontent.com/LoLChC/Gits/main/gits.py -o /opt/gits/gits.py
sudo chmod +x /opt/gits/gits.py

# Boş JSON dosyası oluştur
sudo touch /opt/gits/shortcuts.json
sudo chmod 666 /opt/gits/shortcuts.json  # Tüm kullanıcılar yazabilir

# Global komut oluştur
echo -e '#!/bin/bash\npython3 /opt/gits/gits.py "$@"' | sudo tee /usr/local/bin/gits > /dev/null
sudo chmod +x /usr/local/bin/gits

echo "Kurulum tamamlandı! Artık terminalden 'gits' komutunu kullanabilirsiniz."
echo "Örnek kullanım: gits list"
