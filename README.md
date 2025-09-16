# Gits

**Gits**, Git komutlarını kısaltarak daha pratik hale getirmek için geliştirilmiş bir Python aracıdır.  
Ayrıca kullanıcıların kendi kısayol komutlarını (`shortcut`) tanımlayıp çalıştırabilmesini sağlar.

**Gits** is a Python tool developed to shorten Git commands and make them easier to use.  
It also allows users to create and run their own shortcut commands.

---

## Hazır Kısa Yollar / Ready Shortcuts
1. ```bash
   git add . && git commit -m "commit içeriği" && git push -u origin "branch ismi"
   ```

   Commit işlemlerini kısa bir hale getirmek için aşağıdaki komutu kullanabilirsiniz:

   ```bash
   Gits commit "commit içeriği(opsionel)" "branch ismi(opsionel)"
   ```

   To shorten commit operations, you can use the following command:

   ```bash
   Gits commit "commit content(optionel)" "branch name(optionel)"
   ```

<br>

2. ```bash
   echo "# New Repository" > README.md && git init && git add . && git commit -m "first commit" && git branch -M main && git remote add origin <URL> && git push -u origin main
   ```
   
   Yeni bir projeyi bir depoya bağlarken bu uzun komuta ihtiyacınız yok, aşağıdaki komutu kullanabilirsiniz:

   ```bash
   Gits repo <URL>
   ```

   When connecting a new project to a repository, you don't need this long command; you can use the following command:

   ```bash
   Gits repo <URL>
   ```

<br>

3. Create Komutu / Create Command:

   ### Windows için: / For Windows:

      İhtiyaçlarınıza özel oluşturmanız kısayollar ile üst üste çok fazla komut yazmanıza gerek yok:

      ```bash
      gits create komut_ismi "parametre1, parametre2" "işlev {parametre1} {parametre2}"
      ```

      Örnek:

      ```bash
      gits create selam_isim "isim" "echo Merhaba {isim}
      ```

      #### Kullanım:

      ```bash
      gits selam_isim "Çağatay Han"
      ```

      #### Çıktı
         ```bash
         Merhaba Çağatay Han
         ```
      
      You don't need to type too many commands over and over again with shortcuts you create specifically for your needs:

      ```bash
      gits create command_name "param1, param2" "task {param1} {param2}"
      ```
      
      Example:

      ```bash
      gits create hi_name "name" "echo Hello {name}
      ```

## 🚀 Kurulum / Installation
1. Kurulum dosyasını indir Windows / Download the installation file for Windows:
   ```bash
   https://github.com/LoLChC/Gits/raw/main/Setup/Gits_Setup.exe

2. Kurulum dosyasını indirin Linux / Download the installation file for Linux:
   ```bash
   bash -c "$(curl -fsSL https://raw.githubusercontent.com/LoLChC/Gits/main/Linux/install.sh)"

3. Kurulum dosyasını indirin MacOs / Download the installation file for MacOs
   ```bash
   curl -s https://raw.githubusercontent.com/LoLChC/Gits/main/install.sh