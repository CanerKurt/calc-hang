import random
#Bu işlemÇöz fonksiyonu kullanıcının isteğine göre işlemi ve sayıları berlirledikten sonra
#işlem çözüp bonus puan ve genel puan kazanmasını sağlıyor. Ayrıca kullanıcı bir kez
#kullandığı işlemi bir daha kullanamıyor. Eğer işlemi doğru yaparsa 15 genel puan ve 1
#bonus puan kazanır. yanlış yaparsa 10 genel puan kaybeder.
def işlemÇöz(bonus, kullanılmayan_işlemler, puan, kelime_seçimi, gizli_kelime, hata_sayısı,
             islem=None, s1=None, s2=None, cevap=None):
    while True:

        if islem is None:
            işlem = input(f"İşlem türü \033[96m({'/'.join(kullanılmayan_işlemler)})\033[0m ya da '\033[96miptal\033[0m': ").strip().lower()
        else:
            işlem = islem

        if işlem == "iptal":
            print("işleminiz iptal edildi.\n")
            return bonus, puan, gizli_kelime, hata_sayısı

        if işlem not in kullanılmayan_işlemler:
            print("Geçersiz Giriş")
            if islem is not None:
                return bonus, puan, gizli_kelime, hata_sayısı
            continue
        break
    while True:

        if s1 is None:
            sayı1 = input("1. sayı (iptal için '\033[96miptal\033[0m'):").strip().lower()

            if sayı1 == "iptal":
                print("İşleminiz iptal edildi.\n")
                return bonus, puan, gizli_kelime, hata_sayısı

            else:
                try:
                    sayı1 = float(sayı1)
                    break
                except ValueError:
                    print("Geçersiz giriş")
                    continue
        else:
            try:
                sayı1 = float(s1)
                break
            except:
                return bonus, puan, gizli_kelime, hata_sayısı
    while True:

        if s2 is None:
            sayı2 = input("2. sayı (iptal için '\033[96miptal\033[0m'):").strip().lower()

            if sayı2 == "iptal":
                print("İşleminiz iptal edildi.\n")
                return bonus, puan, gizli_kelime, hata_sayısı

            else:
                try:
                    sayı2 = float(sayı2)
                    if işlem == "bölme" and sayı2 == 0:
                        print("0 ile bölme yapılamaz!")
                        return bonus, puan, gizli_kelime, hata_sayısı
                    break

                except ValueError:
                    print("Geçersiz giriş")
                    continue
        else:
            try:
                sayı2 = float(s2)
                if işlem == "bölme" and sayı2 == 0:
                    print("0 ile bölme yapılamaz!")
                    return bonus, puan, gizli_kelime, hata_sayısı
                break
            except:
                return bonus, puan, gizli_kelime, hata_sayısı

    sembol = ""
    sonuç = 0

    if işlem == "toplama":
        sonuç = sayı1 + sayı2
        sembol = "+"
    elif işlem == "çıkarma":
        sonuç = sayı1 - sayı2
        sembol = "-"
    elif işlem == "çarpma":
        sonuç = sayı1 * sayı2
        sembol = "*"
    elif işlem == "bölme":
        sonuç = sayı1 / sayı2
        sembol = "/"

    print(f"Soru: {sayı1} {sembol} {sayı2} = ?")

    try:
        if cevap is None:
            sonuç_tahmini = float(input("Cevabınız: "))
        else:
            sonuç_tahmini = float(cevap)
    except ValueError:
        hata_sayısı += 1
        puan -= 10
        print(f"Geçersiz giriş! | Cevap: {sonuç} | Hata sayısı + 1 | Genel puan -10\n")
        return bonus, puan, gizli_kelime, hata_sayısı

    if abs(sonuç_tahmini - sonuç) <= 1e-6:
        bonus += 1
        puan += 15
        print("\033[92mDoğru!\033[0m 🎉 | Bonus puan +1 | Genel puan +15")

        kapalı_indeksler = []
        for i in range(len(gizli_kelime)):
            if gizli_kelime[i] == "_":
                kapalı_indeksler.append(i)

        if len(kapalı_indeksler) > 0:
            rastgele_indeks = random.choice(kapalı_indeksler)
            gizli_kelime[rastgele_indeks] = kelime_seçimi[rastgele_indeks]
            print(f"\033[92m🎁 Bonus:\033[0m '{kelime_seçimi[rastgele_indeks]}' harfi açıldı!")
            print(f"Güncel bonus puanın: {bonus}\n")

    else:
        hata_sayısı += 1
        puan -= 10
        print(f"\033[91mYanlış!\033[0m ❌ | Cevap: {sonuç} | Hata sayısı +1 | Genel puan -10\n")

    kullanılmayan_işlemler.remove(işlem)
    return bonus, puan, gizli_kelime, hata_sayısı

#Bu harfTahmini fonksiyonu kullanıcının harf tahmini seçeneğini seçtikten sonra rastgele
#seçilen kelimedeki harfleri tahmin etmeye çalışmasını sağlar. Eğer doğru tahmin ederse
#10 genel puan kazanır. Yanlış tahmin ederse 5 genel puan kaybeder ve hata sayısı 1 artar.
def harfTahmini(kelime_secimi, gizli_kelime, tahmin_edilenler, hata_sayısı, puan, giris=None):

    if giris is None:
        harf = input("Harf Tahmini: ").strip().lower()
    else:
        harf = giris.lower()

    rakamlar = "0123456789"
    if len(harf) != 1 or harf in rakamlar:
        print("Lütfen bir harf giriniz!\n")
        return gizli_kelime, tahmin_edilenler, hata_sayısı, puan

    if harf in tahmin_edilenler:
        print("Bu harfi zaten girdiniz!\n")
        return gizli_kelime, tahmin_edilenler, hata_sayısı, puan

    tahmin_edilenler.append(harf)

    if harf in kelime_secimi:
        for i in range(len(kelime_secimi)):
            if kelime_secimi[i] == harf:
                gizli_kelime[i] = harf
        puan += 10
        print("\033[92mDoğru!\033[0m | Genel puan +10\n")
    else:
        hata_sayısı += 1
        puan -= 5
        print(f"\033[91mYanlış Harf:\033[00m '{harf}' | Hata sayısı +1 | Genel puan -5\n")

    return gizli_kelime, tahmin_edilenler, hata_sayısı, puan

#Oyunun genel kısımları bu AdamAsmaca fonksiyonunda yer alıyor. kategoriler sözlüğünden
#rastgele bir kategori seçiliyor ve kelime seçiminde de o kategoriler içinden rastgele
#bir kelime seçiliyor. Adam asmaca görselini çizdirmek için hata sayısı indeks olarak
#alınarak görsel değişkeninin içindeki görseller bastırılıyor. While döngüsü gizli
#kelime tamamlanana kadar veya hata sayısı dolana kadar devam ediyor. Kullanıcının
#girdiği harfler tahmin edilenler listesi içine eklenip yazdırılıyor. Kullanıcı 'h'
#girerse harfTahmini fonksiyonu, 's' girerse işlemÇöz fonksiyonu çalışıyor. 'i' girerse
#ipucu veriliyor ve 'ç' girerse program sonlandırılıyor.
def adamAsmaca():
    print("\033[97m=== Calc & Hang: İşlem Yap, Harfi Kurtar! ===\033[0m\n")
    kategoriler = {
        "Meyveler": ["elma", "armut", "çilek", "karpuz", "kivi", "erik", "mandalina", "portakal", "hindistancevizi"],
        "Hayvanlar": ["inek", "kaplan", "aslan", "goril", "zürafa", "gergedan", "ayı", "köpek", "kedi"],
        "Teknoloji": ["telefon", "televizyon", "oyunkonsolu", "bilgisayar", "kulaklık", "tablet"]
    }

    kategori_adı, kategori_secimi = random.choice(list(kategoriler.items()))

    kelime_secimi = random.choice(kategori_secimi)
    kirmizirenk = '\033[91m'
    defaultrenk = '\033[00m'
    görsel = [
f"""
    +---+
    |   |
        |
        |
        |
        |
 ==========
""",
f"""
    +---+
    |   |
{kirmizirenk}    O   {defaultrenk}|
        |
        |
        |
 ==========
""",
f"""
    +---+
    |   |
{kirmizirenk}    O   {defaultrenk}|
{kirmizirenk}    |   {defaultrenk}|
        |
        |
 ==========
""",
f"""
    +---+
    |   |
{kirmizirenk}    O   {defaultrenk}|
{kirmizirenk}    |\\  {defaultrenk}|
        |
        |
 ==========
""",
f"""
    +---+
    |   |
{kirmizirenk}    O   {defaultrenk}|
{kirmizirenk}   /|\\  {defaultrenk}|
        |
        |
 ==========
""",
f"""
    +---+
    |   |
{kirmizirenk}    O   {defaultrenk}|
{kirmizirenk}   /|\\  {defaultrenk}|
{kirmizirenk}     \\  {defaultrenk}|
        |
 ==========
""",
f"""
    +---+
    |   |
{kirmizirenk}    O   {defaultrenk}|
{kirmizirenk}   /|\\  {defaultrenk}|
{kirmizirenk}   / \\  {defaultrenk}|
        |
 ==========
"""]

    kullanılmayan_işlemler = ["toplama", "çıkarma", "çarpma", "bölme"]
    bonus = 0
    puan = 0
    hata_sayısı = 0
    maks_hata = len(görsel) - 1
    tahmin_edilenler = []

    gizli_kelime = ["_"] * len(kelime_secimi)

    while "_" in gizli_kelime and hata_sayısı < maks_hata:
        print("\033[92m--- Yeni Tur ---\033[0m")
        print(görsel[hata_sayısı])
        print("\n\033[95mKelime: ", " ".join(gizli_kelime), "\033[0m")
        print("\033[97mTahmin edilen harfler:\033[0m", ", ".join(tahmin_edilenler))
        print(f"\033[97mBonus puan:\033[0m {bonus}")
        print(f"\033[97mGenel puan:\033[0m {puan}")
        print(f"\033[97mKalan hata hakkı:\033[00m {(maks_hata - 1) - hata_sayısı}")
        print("\033[97mSeçenekler:\033[0m Harf Tahmini\033[96m(h)\033[0m | Soru Çöz\033[96m(s)\033[0m |"
              " İpucu\033[96m(i)\033[0m | Çıkış\033[97m(ç)\033[0m")

        seçim = input("Seçiminiz: ").strip().lower()

        if seçim == "ç":
            print("Program Sonlandırılıyor...👋")
            return

        elif seçim == "s":
            bonus, puan, gizli_kelime, hata_sayısı = işlemÇöz(bonus, kullanılmayan_işlemler, puan, kelime_secimi, gizli_kelime, hata_sayısı)

        elif seçim == "i":
            if bonus > 0:
                print(f"Kelimenin kategorisi: {kategori_adı}\n")
                bonus -= 1
            else:
                print("⚠️ Bonus puanınız yok, ipucu alamazsınız!\n")

        elif seçim == "h":
            gizli_kelime, tahmin_edilenler, hata_sayısı, puan = harfTahmini(kelime_secimi, gizli_kelime, tahmin_edilenler, hata_sayısı, puan)

        else:
            print("Geçersiz Giriş!\n")

    print(görsel[hata_sayısı])
    print("\033[97mTahmin edilen harfler:\033[0m", ", ".join(tahmin_edilenler))

    if "_" not in gizli_kelime:
        puan += 50
        print("\033[92mTebrikler! Kelimeyi bildiniz.\033[0m 🎉 | Genel puan:", puan)
        print(f"\033[97mKelime: \033[95m{kelime_secimi}\033[0m")
    else:
        puan -= 20
        print("\033[91mKaybettiniz!\033[0m 😔 | Genel puan:", puan)
        print(f"\033[97mKelime: \033[95m{kelime_secimi}\033[0m")

if __name__ == "__main__":
    adamAsmaca()
