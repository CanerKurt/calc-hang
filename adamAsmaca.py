import random


# işlemÇöz fonksiyonu kullanıcının isteğine göre işlemi ve sayıları berlirledikten sonra
# işlem çözüp bonus puan ve genel puan kazanmasını sağlıyor. Ayrıca kullanıcı bir kez
# kullandığı işlemi bir daha kullanamıyor. Eğer işlemi doğru yaparsa 15 genel puan ve 1
# bonus puan kazanır. yanlış yaparsa 10 genel puan kaybeder.
def işlemÇöz(bonus, kullanılmayan_işlemler, puan, kelime_seçimi, gizli_kelime, hata_sayısı,
             islem=None, s1=None, s2=None, cevap=None):
    while True:

        if islem is None:
            işlem = input(
                f"İşlem türü \033[96m({'/'.join(kullanılmayan_işlemler)})\033[0m ya da '\033[96miptal\033[0m': ").strip().lower()
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

    sembol = ""
    sonuç = 0

    if işlem == "toplama":
        sayı1 = random.randint(0, 999)
        sayı2 = random.randint(0, 999)
        sonuç = sayı1 + sayı2
        sembol = "+"
    elif işlem == "çıkarma":
        sayı1 = random.randint(0, 999)
        sayı2 = random.randint(0, 999)
        sonuç = sayı1 - sayı2
        sembol = "-"
    elif işlem == "çarpma":
        sayı1 = random.randint(0, 99)
        sayı2 = random.randint(0, 99)
        sonuç = sayı1 * sayı2
        sembol = "*"
    elif işlem == "bölme":
        sayı1 = random.randint(0, 99)
        bölenler = [2, 4, 5, 10]
        sayı2 = random.choice(bölenler)
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


# kelimeTahmini fonksiyonu kullanıcıdan kelimeyi tahmin etmesini istiyor. Eğer
# kullanıcı kelimeyi doğru bilirse +100 genel puan ekleniyor ve oyunu kazanıyor.
# Eğer yanlış cevap girerse -50 genel puan azalıyor ve oyunu kaybediyor.
def kelimeTahmini(kelime_secimi, gizli_kelime, puan):
    kelime_tahmini = input("UYARI: Kelime tahmini için tek hakkınız vardır!\nDoğru Cevap: +100 Genel Puan\nYanlış Cevap: -50 Genel Puan\nKelime Tahmini (ya da 'iptal'): ").strip()

    kelime_tahmini = kelime_tahmini.replace("İ", "i").lower()

    if kelime_tahmini == "iptal":
        print("İşleminiz İptal Edildi.\n")
        return gizli_kelime, puan, "iptal"

    if kelime_tahmini == kelime_secimi:
        for i in range(len(kelime_secimi)):
            gizli_kelime[i] = kelime_secimi[i]
        puan += 100
        print(f"\033[92mTebrikler! Kelimeyi bildiniz.\033[0m 🎉 | Genel puan: {puan}")
        print(f"\033[97mKelime: \033[95m{kelime_secimi}\033[0m")
        return gizli_kelime, puan, "bitti"
    else:
        puan -= 50
        gizli_kelime = ["_"] * len(kelime_secimi)
        print(f"\033[91mYanlış kelime tahmini! Kaybettiniz.\033[0m 😔 | Genel puan: {puan}")
        print(f"\033[97mKelime: \033[95m{kelime_secimi}\033[0m")
        return gizli_kelime, puan, "bitti"


# ipucu fonksiyonu eğer kullanıcının yeterli bonus puanı varsa kullanıcıya ipucu veriyor.
# 1 bonus puan kullanılırsa kelimenin kategorisini gösteriyor. 2 bonus puan kullanılırsa
# ise kelime ile ilgili detaylı bir ipucu veriliyor.
def ipucu(kelime_secimi, kategori_adı, bonus):
    while True:
        bonus_seçimi = input("""1) Kelimenin Kategorisi(1 bonus puan)\n2) Kelime İle İlgili Detaylı İpucu(2 bonus puan)\nya da 'iptal'\nSeçiminiz(1, 2): """).strip().replace("İ", "i").lower()

        if bonus_seçimi == "iptal":
            print("İpucu menüsünden çıkıldı.\n")
            break

        elif bonus_seçimi == "1":
            if bonus > 0:
                print(f"Kelimenin kategorisi: {kategori_adı}\n")
                bonus -= 1
                break
            else:
                print("⚠️ Yeterli bonus puanınız yok! Lütfen tekrar seçin.\n")

        elif bonus_seçimi == "2":
            if bonus > 1:
                tum_grup_ipuclari = {
                    "Hayvanlar": {
                        ("kedi", "köpek"): [
                            "İpucu: Bu canlı ev ortamına kolayca uyum sağlayabilen evcil bir hayvandır.",
                            "İpucu: İnsanlarla çok yakın ve sıcak ilişkiler kurabilen popüler dostlarımızdandır."
                        ],
                        ("inek", "koyun", "keçi"): [
                            "İpucu: Bu canlı bir çiftlik hayvanıdır ve tamamen otçul beslenir.",
                            "İpucu: İnsanların beslenmesi için hayati önem taşıyan süt üretiminde büyük rol oynar."
                        ],
                        ("aslan", "kaplan", "leopar"): [
                            "İpucu: Bu canlı vahşi doğada yaşayan, kürk desenleriyle büyüleyen yırtıcı bir kedigildir.",
                            "İpucu: Doğal ortamında besin zincirinin en tepesinde yer alan usta bir avcıdır."
                        ],
                        ("zürafa", "gergedan", "goril"): [
                            "İpucu: Bu canlı vahşi doğada, özellikle Afrika coğrafyasında doğal olarak yaşar.",
                            "İpucu: Oldukça büyük, ağır veya uzun yapılara sahip dikkat çekici bir yabani hayvandır."
                        ],
                        ("ayı",): [
                            "İpucu: Bu canlı genellikle ormanlık alanlarda yaşar ve kış uykusuna yatmasıyla bilinir.",
                            "İpucu: Hem et hem ot yiyebilen (omnivor), fiziksel olarak oldukça güçlü bir hayvandır."
                        ]
                    },
                    "Meyveler": {
                        ("elma", "armut", "erik", "kayısı"): [
                            "İpucu: Bu meyve ağaç dallarında yetişir ve genellikle kabuğuyla birlikte de tüketilebilir.",
                            "İpucu: Türkiye genelinde ılıman iklim bahçelerinde en çok yetiştirilen meyve türlerindendir."
                        ],
                        ("çilek", "karpuz", "kavun"): [
                            "İpucu: Bu meyve bir ağaçta değil, doğrudan toprak üzerinde veya sürüngen otsu bitkilerde büyür.",
                            "İpucu: İçeriğindeki yüksek su oranıyla özellikle sıcak yaz aylarında serinletici olarak çok tüketilir."
                        ],
                        ("kivi", "mandalina", "portakal", "limon"): [
                            "İpucu: Bu meyve, yüksek C vitamini oranıyla kış aylarında bağışıklığı desteklemek için sıkça tüketilir.",
                            "İpucu: Sulu, eksiye yakın tatlı veya ekşi aromaya sahip, tazeleyici bir narenciye/tropikal meyvedir."
                        ],
                        ("hindistancevizi", "ananas"): [
                            "İpucu: Bu meyve yalnızca sıcak ve bol yağışlı tropikal iklim bölgelerinde yetişir.",
                            "İpucu: Dış görünüşü oldukça sert, lifli veya dikenli yapılara sahip egzotik bir meyvedir."
                        ]
                    },
                    "Teknoloji": {
                        ("telefon", "tablet", "akıllısaat"): [
                            "İpucu: Bu cihaz tamamen taşınabilir mimariye sahiptir ve dahili şarj edilebilir batarya ile çalışır.",
                            "İpucu: Günlük hayatımızda mobil olarak yanımızda gezdirdiğimiz, dokunmatik ekrana sahip akıllı bir cihazdır."
                        ],
                        ("televizyon", "oyunkonsolu"): [
                            "İpucu: Bu cihaz doğrudan ev eğlencesi, oyun veya medya tüketimi amacıyla salon/oda ortamında kullanılır.",
                            "İpucu: Genellikle tek başına bir iletişim aracı değildir; görüntü paneline veya büyük bir ekrana ihtiyaç duyar."
                        ],
                        ("bilgisayar",): [
                            "İpucu: Bu cihaz profesyonel iş üretimi, yazılım, tasarım veya oyun için yüksek işlem gücüne sahiptir.",
                            "İpucu: Masaüstü veya dizüstü mimarisiyle donanım bileşenlerinin en organize çalıştığı ana istasyondur."
                        ],
                        ("kulaklık", "hoparlör"): [
                            "İpucu: Bu ses teknolojisi ürünü, bir cihazdan alınan dijital sinyalleri doğrudan işitilebilir ses dalgasına çevirir.",
                            "İpucu: Müzik dinlemek, video izlemek veya bir şeyler dinlemek için kullanılan temel ses çıkış birimidir."
                        ]
                    }
                }

                bulunan_ipucu = None
                if kategori_adı in tum_grup_ipuclari:
                    kategori_dict = tum_grup_ipuclari[kategori_adı]
                    for grup_ogeleri, ipuclari_listesi in kategori_dict.items():
                        if kelime_secimi in grup_ogeleri:
                            bulunan_ipucu = random.choice(ipuclari_listesi)
                            break

                if bulunan_ipucu:
                    print(f"{bulunan_ipucu}\n")
                else:
                    print(f"İpucu: Bu kelime {kategori_adı} kategorisindedir.\n")

                bonus -= 2
                break
            else:
                print("⚠️ Yeterli bonus puanınız yok! Lütfen tekrar seçin.\n")

        else:
            print("Geçersiz Giriş! Lütfen 1, 2 ya da 'iptal' yazın.\n")

    return bonus


# harfTahmini fonksiyonu kullanıcının harf tahmini seçeneğini seçtikten sonra rastgele
# seçilen kelimedeki harfleri tahmin etmeye çalışmasını sağlar. Eğer doğru tahmin ederse
# 10 genel puan kazanır. Yanlış tahmin ederse 5 genel puan kaybeder ve hata sayısı 1 artar.
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


# Oyunun genel kısımları AdamAsmaca fonksiyonunda yer alıyor. kategoriler sözlüğünden
# rastgele bir kategori seçiliyor ve kelime seçiminde de o kategoriler içinden rastgele
# bir kelime seçiliyor. Adam asmaca görselini çizdirmek için hata sayısı indeks olarak
# alınarak görsel değişkeninin içindeki görseller bastırılıyor. While döngüsü gizli
# kelime tamamlanana kadar veya hata sayısı dolana kadar devam ediyor. Kullanıcının
# girdiği harfler tahmin edilenler listesi içine eklenip yazdırılıyor. Kullanıcı 'k'
# girerse kelimeTahmini fonksiyonu,'h' girerse harfTahmini fonksiyonu, 's' girerse işlemÇöz
# fonksiyonu, 'i' girerse ipucu fonksiyonu çalışıyor ve 'ç' girerse program sonlandırılıyor.
def adamAsmaca():
    print("\033[97m=== Calc & Hang: İşlem Yap, Harfi Kurtar! ===\033[0m\n")
    kategoriler = {
        "Meyveler": ["elma", "armut", "erik", "kayısı", "çilek", "karpuz", "kavun", "kivi", "mandalina", "portakal",
                     "limon", "hindistancevizi", "ananas"],
        "Hayvanlar": ["kedi", "köpek", "inek", "koyun", "keçi", "kaplan", "aslan", "leopar", "zürafa", "gergedan",
                      "goril", "ayı"],
        "Teknoloji": ["telefon", "tablet", "akıllısaat", "televizyon", "oyunkonsolu", "bilgisayar", "kulaklık",
                      "hoparlör"]
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
        print(f"\033[97mKalan hata hakkı:\033[00m {maks_hata - hata_sayısı}")
        print(
            "\033[97mSeçenekler:\033[0m Kelime Tahmini\033[96m(k)\033[0m | Harf Tahmini\033[96m(h)\033[0m | Soru Çöz\033[96m(s)\033[0m |"
            " İpucu\033[96m(i)\033[0m | Çıkış\033[97m(ç)\033[0m")

        seçim = input("Seçiminiz: ").strip().lower()

        if seçim == "k":
            gizli_kelime, puan, durum = kelimeTahmini(kelime_secimi, gizli_kelime, puan)
            if durum == "bitti":
                return
            continue

        elif seçim == "ç":
            print("Program Sonlandırılıyor...👋")
            return

        elif seçim == "s":
            bonus, puan, gizli_kelime, hata_sayısı = işlemÇöz(bonus, kullanılmayan_işlemler, puan, kelime_secimi,
                                                              gizli_kelime, hata_sayısı)

        elif seçim == "i":
            bonus = ipucu(kelime_secimi, kategori_adı, bonus)

        elif seçim == "h":
            gizli_kelime, tahmin_edilenler, hata_sayısı, puan = harfTahmini(kelime_secimi, gizli_kelime,
                                                                            tahmin_edilenler, hata_sayısı, puan)

        else:
            print("Geçersiz Giriş!\n")

    if "_" not in gizli_kelime:
        pass
    else:
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