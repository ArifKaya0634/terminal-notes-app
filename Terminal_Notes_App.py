import os
klasor = "notes"
klasor = os.path.join(os.getcwd(), "notes")
if not os.path.exists(klasor):
    os.mkdir(klasor)
print(klasor)
while True:
    print("Terminal günlük/not app'ine hoşgeldiniz.")
    print("""
    === TERMINAL NOTES APP ===
    
    1 - Yeni dosya oluştur
    2 - Dosya seç
    3 - Çıkış
    """)
    seçim = input("Seçim: ")
    if seçim == "1":
     yeni_dosya = input("Dosya ismini girin: ")

     if yeni_dosya == "":
        print("Boş kalamaz!")

     else:
        yeni_dosya = f"{yeni_dosya}.txt"

        dosya_yolu = f"{klasor}/{yeni_dosya}"

        with open(dosya_yolu, "w") as file:
            pass
     print("Dosya oluşturuldu ✅")
    elif seçim == "2":
        dosyalar = os.listdir(klasor)
        txt_dosyalar = []
        for dosya in dosyalar:
         if dosya.endswith(".txt"):
          txt_dosyalar.append(dosya)
        if txt_dosyalar == []:
            print("Henüz dosyanız yok.")
            continue
        else:
         dosyalar = os.listdir(klasor)
         for index, dosya in enumerate(txt_dosyalar):
          if dosya.endswith(".txt"):
            print(index,dosya)
            
        dosya_secim = int(input("Dosya seç: "))
        secilen_dosya = dosyalar[dosya_secim]
        print(f"Aktif dosya: {secilen_dosya}")
        print("""
        1 - Not ekle
        2 - Notları oku
        3 - Geri dön
        """)
        dosya_yolu_2 = f"{klasor}/{secilen_dosya}"
        not_secim = int(input("Aktif Dosya ile ne yapılacağını seçin: "))
        if not_secim == 1:
         not_içerik = input("Notunuzu girin: ").strip()
         with open(dosya_yolu_2,"a") as file1:
            file1.write(not_içerik + "\n")
         print ("Not eklendi.")
        elif not_secim == 2:
         with open(dosya_yolu_2,"r") as file2:
            içerik = file2.read()
            if içerik == "":
                print("Henüz not yok")
            else:
                print("\n=== Notlarınız ===\n")
                print(içerik)
        elif not_secim == 3:
            continue
        else:
            print("Hatalı giriş")
    elif seçim == "3":
        break
    else:
        print("Hatalı seçim")   


