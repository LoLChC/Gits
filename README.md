# 🚀 Gits

**Gits**, Git komutlarını kısaltmak ve kullanımını kolaylaştırmak için geliştirilmiş bir Python aracıdır.  
Ayrıca kullanıcıların kendi kısayol komutlarını (`shortcut`) tanımlayıp çalıştırmasına imkan tanır.

**Gits** is a Python tool designed to shorten Git commands and make them easier to use.  
It also allows users to create and run their own custom shortcut commands.

---

## ⚡ Hazır Kısa Yollar / Ready Shortcuts

### 1️⃣ Commit Komutu / Commit Command
Standart Git commit işlemi / Standard Git commit process:
```bash
git add . && git commit -m "commit içeriği" && git push -u origin "branch ismi"
```

Gits ile kısa hâli / Short form with Gits:
```bash
Gits commit "commit içeriği(opsiyonel)" "branch ismi(opsiyonel)"
```

---

### 2️⃣ Repo Komutu / Repo Command
Yeni bir projeyi GitHub’a bağlamak için uzun komut / Long command to connect a new project to GitHub:
```bash
echo "# New Repository" > README.md && git init && git add . && git commit -m "first commit" && git branch -M main && git remote add origin <URL> && git push -u origin main
```

Gits ile kısa / Gits ile kısa:
```bash
Gits repo <URL>
```

---

### 3️⃣ Create Komutu / Create Command
Kendi kısayol komutlarınızı oluşturabilirsiniz / You can create your own shortcut commands:
```bash
gits create komut_ismi "param1,param2" "işlev {param1} {param2}"
```

#### Örnek / Example:
```bash
gits create selam_isim "isim" "echo Merhaba {isim}"
```

Kullanım / Use:
```bash
gits selam_isim "Çağatay Han"
```

Çıktı / Output:
```bash
Merhaba Çağatay Han
```

---

### 4️⃣ Delete Komutu / Delete Command
Oluşturduğunuz kısayol komutlarını silmek için / To delete shortcut commands you created:
```bash
gits delete komut_ismi
```

Özel bir kısayolu silme / Delete a custom shortcut:
```bash
gits delete command_name
```

---

### 5️⃣ List Komutu / List Command
Tüm mevcut ve otomatik komutları görüntülemek için / To view all available and automatic commands:
```bash
gits list
```

Tüm etkin ve varsayılan komutları görün / See all active and default commands:
```bash
gits list
```

---

## 🛠️ Kurulum / Installation

### Windows
Gits kurulum dosyasını indir / Download Gits installation file:
```text
https://github.com/LoLChC/Gits/raw/main/Setup/Gits_Setup.exe
```

### Linux
Kurulum için terminale yazın / Type in terminal for installation:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/LoLChC/Gits/main/Linux/install.sh)"
```

### MacOS (Denemedik / Not Tested)
```bash
curl -s https://raw.githubusercontent.com/LoLChC/Gits/main/install.sh | bash
```

---

Made with ❤️ by **LoLChC**
