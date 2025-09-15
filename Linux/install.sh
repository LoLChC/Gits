# Mevcut kurulumu kaldır
sudo rm -f /usr/local/bin/gits
sudo rm -rf /opt/gits

# Ev dizininizde çalışacak şekilde yeniden kur
mkdir -p ~/.gits
echo '{"shortcuts": []}' > ~/.gits/shortcuts.json
chmod +w ~/.gits/shortcuts.json

# Python scriptini ev dizinine kopyala
curl -fsSL https://raw.githubusercontent.com/LoLChC/Gits/main/Linux/gits.py > ~/.gits/gits.py
chmod +x ~/.gits/gits.py

# PATH'e ekle (bash kullanıyorsanız)
echo 'export PATH="$HOME/.gits:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Veya zsh kullanıyorsanız
echo 'export PATH="$HOME/.gits:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Test et
~/.gits/gits.py list