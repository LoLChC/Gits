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
git add . && git commit -m "commit contents" && git push -u origin "branch name"
```

Gits ile kısa hâli / Short form with Gits:
```bash
Gits commit "commit içeriği(opsiyonel)" "branch ismi(opsiyonel)"
Gits commit "commit contents(optionel)" "branch name(optionel)"
```
Açıklama / Description: Bu komut commit işlemlerini kısa bir şekilde yapmanızı sağlar / This command allows you to perform commit operations in a shorter way.

---

### 2️⃣ Repo Komutu / Repo Command
Yeni bir projeyi GitHub’a bağlamak için uzun komut / Long command to connect a new project to GitHub:
```bash
echo "# New Repository" > README.md && git init && git add . && git commit -m "first commit" && git branch -M main && git remote add origin <URL> && git push -u origin main
```

Gits ile kısa / Short form with Gits:
```bash
Gits repo <URL>
```
Açıklama / Description: Bu komut yeni bir projeyi hızlı bir şekilde bir repository ile bağlamanızı sağlar / This command allows you to quickly connect a new project to a repository.

---

### 3️⃣ Create Komutu / Create Command
Kendi kısayol komutlarınızı oluşturabilirsiniz / You can create your own shortcut commands:
```bash
gits create komut_ismi "param1,param2" "işlev {param1} {param2}"
gits create command_name "param1,param2" "function {param1} {param2}"
```

#### Örnek / Example:
```bash
gits create selam_isim "isim" "echo Merhaba {isim}"
gits create hi_name "name" "echo Hello {name}"
```

Kullanım / Use:
```bash
gits selam_isim "Çağatay Han"
gits hi_name "Çağatay Han"
```

Çıktı / Output:
```text
Merhaba Çağatay Han
Hello Çağatay Han
```

Açıklama / Description: Bu komut, kullanıcı tarafından tanımlanan parametreleri alarak özel bir mesaj veya işlem yapmanızı sağlar / This command allows you to take user-defined parameters to perform a custom message or action.

---

### 4️⃣ Delete Komutu / Delete Command
Oluşturduğunuz kısayol komutlarını silmek için / To delete shortcut commands you created:
```bash
gits delete komut_ismi
gits delete command_name
```

Açıklama / Description: Bu komut, create ile oluşturduğunuz kısayol komutlarını silmenizi sağlar / This command allows you to delete shortcut commands created with create.

---

### 5️⃣ List Komutu / List Command
Tüm mevcut ve otomatik komutları görüntülemek için / To view all available and automatic commands:
```bash
gits list
```

Açıklama / Description: Bu komut mevcut tüm kısayol ve otomatik komutları listelemenizi sağlar / This command allows you to list all active and default commands.

---

## 🛠️ Kurulum / Installation

### Windows
Gits kurulum dosyasını indir / Download Gits installation file:
```link
https://github.com/LoLChC/Gits/raw/main/Windows/Gits_Setup.exe
```
Açıklama / Description: Windows için Gits'i kurmanızı sağlar / This allows you to install Gits on Windows.

### Linux
Kurulum için terminale yazın / Type in terminal for installation:
```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/LoLChC/Gits/main/Linux/install.sh)"
```
Açıklama / Description: Linux sistemlere Gits kurulumu için kullanılır / Used for installing Gits on Linux systems.

### MacOS (Denemedik / Not Tested)
```bash
curl -s https://raw.githubusercontent.com/LoLChC/Gits/main/MacOS/install.sh | bash
```
Açıklama / Description: MacOS için Gits kurulumunu sağlar (denenmedi) / Installs Gits on MacOS (not tested).

---

By **LoLChC**
