#!/bin/bash
# Tek satırlık kurulum için script

# 1. Dosyayı indir
curl -L -o gits https://github.com/LoLChC/Gits/raw/main/Linux/dist/gits

# 2. Çalıştırılabilir yap
chmod +x gits

# 3. Sistemde global olarak kullanılabilir hale getir
sudo mv gits /usr/local/bin/gits

# 4. Kurulum tamamlandı mesajı
echo "Gits başarıyla kuruldu! Artık terminalden 'gits' komutu ile çalıştırabilirsiniz."
