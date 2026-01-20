import re
import math
import random
import time
from time import sleep
sozluk = {
    "yaz": "print",
    "girdi": "input",
    "tamsayi": "int",
    "metin": "str",
    "Dogru": "True",
    "Yanlış": "False",
    "eger": "if",
    "eğer": "if",
    "egif": "elif",
    "degilse": "else",
    "değilse": "else",
    "icin": "for",
    "için": "for",
    "icinde": "in",
    "içinde": "in",
    "dongu": "while",
    "döngü": "while",
    "üzerinden": "from",
    "dene": "try",
    "hata": "except",
    "ve": "and",
    "veya": "or",
    "degil": "not",
    "tanimla": "def",
    "tanımla": "def",
    "durdur": "break",
    "dur": "break",
    "atla": "continue",
    "ver": "return",
    "ac": "open",
    "kapat": "close",
    "rastgele": "random.randint",
    "karekök": "math.sqrt",
    "mutlak": "abs",
    "yuvarla": "round",
    "pi_sayısı": "math.pi",
    "pisayısı": "math.pi",
    "pisayisi": "math.pi",
    "pi_sayisi": "math.pi",
    "bekle": "sleep",
    "zaman.bekle": "sleep",
    "getir": "import",
    "isimsiz": "lambda",
    "piton_komutları": "list(sozluk.keys())"
}

def baslat():
    dosya_adi = input("Dosya adı: ")
    if not dosya_adi.endswith(".txt"): dosya_adi += ".txt"

    # DOSYAYI UTF-8 OLARAK OKUMAK ÇOK ÖNEMLİ
    with open(dosya_adi, "r", encoding="utf-8") as f:
        turkce_kod = f.read()

    python_kodu = turkce_kod
    
    # Kelimeleri tam yakalayan ve Türkçe karakterleri bozmayan yöntem
    for tr, eng in sozluk.items():
        # Bu kod sayesinde 'içinde' kelimesindeki 'in'i gidip 'for' yapmaz!
        pattern = r'(?<![a-zA-ZçğıöşüÇĞİÖŞÜ])' + tr + r'(?![a-zA-ZçğıöşüÇĞİÖŞÜ])'
        python_kodu = re.sub(pattern, eng, python_kodu)

    # ... çeviri (re.sub) döngüsünün bittiği yer ...
    
    print("\n--- ÇALIŞTIRILIYOR ---\n")
    
    # BU SATIRLARIN BAŞINDAKİ BOŞLUKLARA DİKKAT ET! (Hepsi içeride)
    python_kodu = "piton_komutları = " + str(list(sozluk.keys())) + "\n" + python_kodu
    
    exec(python_kodu)

# Fonksiyon bittikten sonra en sola dayanarak çağırıyoruz
baslat()
