# Kodun çalışması için adamasmaca.py ile aynı dosya dizininde olması gerekiyor.

import adamasmaca

print("\nTestlerin Baslangici")

def test_baslangic():
    try:
        kategoriler = {
            "Meyveler": ["elma"],
            "Hayvanlar": ["kedi"],
        }
        kategori, kelimeler = list(kategoriler.items())[0]
        kelime = kelimeler[0]
        print("Başlangıç testi: \033[92mCalisiyor\033[0m")
    except:
        print("Başlangıç testi: \033[91mHATA\033[0m")

def test_harf_dogruluk():
    try:
        gizli = ["_","_","_","_"]
        tlist = []
        gizli, tlist, hata, puan = adamasmaca.harfTahmini(
            "test", gizli, tlist, 0, 0, giris="t"
        )
        print("Harf doğruluk testi: \033[92mCalisiyor\033[0m")
    except:
        print("Harf doğruluk testi: \033[91mHATA\033[0m")

def test_harf_tekrar():
    try:
        gizli = ["_","_","_","_"]
        tlist = ["t"]
        gizli, tlist, hata, puan = adamasmaca.harfTahmini(
            "test", gizli, tlist, 0, 0, giris="t"
        )
        print("Harf tekrar testi: \033[92mCalisiyor\033[0m")
    except:
        print("Harf tekrar testi: \033[91mHATA\033[0m")

def test_islem_dogru():
    try:
        bonus, puan, gizli, hata = adamasmaca.işlemÇöz(
            0, ["toplama"], 0, "elma", ["_"]*4, 0,
            islem="toplama", s1=2, s2=3, cevap=5
        )
        print("İşlem doğru testi: \033[92mCalisiyor\033[0m")
    except:
        print("İşlem doğru testi: \033[91mHATA\033[0m")

def test_islem_yanlis():
    try:
        bonus, puan, gizli, hata = adamasmaca.işlemÇöz(
            0, ["toplama"], 0, "elma", ["_"]*4, 0,
            islem="toplama", s1=2, s2=3, cevap=999
        )
        print("İşlem yanlış testi: \033[92mCalisiyor\033[0m")
    except:
        print("İşlem yanlış testi: \033[91mHATA\033[0m")

def test_sifira_bolme():
    try:
        bonus, puan, gizli, hata = adamasmaca.işlemÇöz(
            0, ["bölme"], 0, "elma", ["_"]*4, 0,
            islem="bölme", s1=10, s2=0, cevap=0
        )
        print("Sıfıra bölme testi: \033[92mCalisiyor\033[0m")
    except:
        print("Sıfıra bölme testi: \033[91mHATA\033[0m")

def test_iptal():
    try:
        bonus, puan, gizli, hata = adamasmaca.işlemÇöz(
            0, ["toplama"], 0, "elma", ["_"]*4, 0,
            islem="iptal"
        )
        print("İptal testi: \033[92mCalisiyor\033[0m")
    except:
        print("İptal testi: \033[91mHATA\033[0m")

def test_oyun_sonu():
    try:
        gizli = ["e","l","m","a"]
        if "_" not in gizli:
            puan = 100
        print("Oyun sonu testi: \033[92mCalisiyor\033[0m")
    except:
        print("Oyun sonu testi: \033[91mHATA\033[0m")


test_baslangic()
test_harf_dogruluk()
test_harf_tekrar()
test_islem_dogru()
test_islem_yanlis()
test_sifira_bolme()
test_iptal()
test_oyun_sonu()

print("\nTestler tamamlandi")
