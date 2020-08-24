class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


while True:
    Brut = input(color.UNDERLINE + 'Lütfen aylık brüt ücretinizi giriniz:' + color.END)
    try:
        Brut = int(Brut)
    except:
        print(color.RED + color.BOLD + 'Lütfen sayısal bir değer girin !' + color.END)
    try:
        if Brut < 2943:
            print(color.RED + color.BOLD + '2020 yılı içerisinde brüt ücret 2.943 liradan az olamaz' + color.END)
            raise ValueError
        elif 50000 > Brut > 15000:
            print(color.BLUE + color.BOLD + 'Hey Maşallah, Allah daha çok versin' + color.END)
        elif Brut > 50000:
            print(color.GREEN + color.BOLD + 'Hoşgelmişsin Ağam. Bütün marabaların yolunu bekliyirdi.' + color.END)
        break
    except:
        continue

while True:
    try:
        Ay = input(color.UNDERLINE + 'Kaçıncı ayı hesaplamak istiyorsunuz(1-12):' + color.END)
        Ay = int(Ay)
    except:
        print(color.RED + color.BOLD + 'Lütfen sayısal bir değer girin' + color.END)
    try:
        if 0 < Ay < 13:
            break
        else:
            print(color.RED + color.BOLD + 'Bir yılda 12 ay bulunur' + color.END)
            raise ValueError

    except:
        continue

while True:
    Medeni = input(color.UNDERLINE + 'Evli misiniz?(E/H):' + color.END)
    try:
        if Medeni == 'E' or Medeni == 'e':
            Medeni = 1
            print('Medeni Hali=\033[1m \033[92m Evli\033[0m')
            while True:
                try:
                    Cocuk = input(color.UNDERLINE + 'Varsa çocuk sayısını belirtiniz, yoksa 0 yazınız :' + color.END)
                    Cocuk = int(Cocuk)
                    if 10 > Cocuk > 5:
                        print(color.BLUE + color.BOLD + 'Hey Maşallah, Allah Bağışlasın' + color.END)
                    elif Cocuk > 10:
                        print(color.GREEN + color.BOLD + 'Senin derdin bizi aşar kardeş' + color.END)
                    else:
                        print(color.BLUE + color.BOLD +'Allah bağışlasın' + color.END)
                    break
                except:
                    print(color.RED + color.BOLD + 'Lütfen çocuk sayısını sayısal olarak girin, çocuğunuz yoksa 0 girin' + color.END)
            while True:
                try:
                    Escalisma = input(color.UNDERLINE + 'Eşiniz çalışıyor mu?(E/H):' + color.END)
                    if Escalisma == 'E' or Escalisma == 'e':
                        Escalisma = 1
                        print('Eşin Çalışma Durumu=\033[1m \033[92mÇalışıyor\033[0m')
                        break
                    elif Escalisma == 'H' or Escalisma == 'h':
                        Escalisma = 0
                        print('Eşin Çalışma Durumu=\033[1m \033[92mÇalışmıyor\033[0m')
                        break
                    else:
                        raise ValueError
                except:
                    print(color.RED + color.BOLD + 'Lütfen eşiniz çalışıyorsa E çalışmıyorsa H yazın, sizin gül hatrınız için küçük harfleri de kabul ediyoruz' + color.END)
            break
        elif Medeni == 'H' or Medeni == 'h':
            Medeni = 0
            Cocuk = 0
            Escalisma = 0
            print('Medeni Hali=\033[1m \033[92mBekar\033[0m')
            break
        else:
            print(color.RED + color.BOLD + 'Lütfen evliyseniz E bekarsanız H yazın, sizin gül hatrınız için küçük harfleri de kabul ediyoruz' + color.END)
            raise ValueError
    except:
        continue

print(f'Brut Maaş=\033[1m {Brut}\033[0m')

if Ay == 1:
    print('Hesaplanacak Ay=\033[1m \033[92mOcak\033[0m')
elif Ay == 2:
    print('Hesaplanacak Ay=\033[1m \033[92mŞubat\033[0m')
elif Ay == 3:
    print('Hesaplanacak Ay=\033[1m \033[92mMart\033[0m')
elif Ay == 4:
    print('Hesaplanacak Ay=\033[1m \033[92mNisan\033[0m')
elif Ay == 5:
    print('Hesaplanacak Ay=\033[1m \033[92mMayıs\033[0m')
elif Ay == 6:
    print('Hesaplanacak Ay=\033[1m \033[92mHaziran\033[0m')
elif Ay == 7:
    print('Hesaplanacak Ay=\033[1m \033[92mTemmuz\033[0m')
elif Ay == 8:
    print('Hesaplanacak Ay=\033[1m \033[92mAğustos\033[0m')
elif Ay == 9:
    print('Hesaplanacak Ay=\033[1m \033[92mEylül\033[0m')
elif Ay == 10:
    print('Hesaplanacak Ay=\033[1m \033[92mEkim\033[0m')
elif Ay == 11:
    print('Hesaplanacak Ay=\033[1m \033[92mKasım\033[0m')
elif Ay == 12:
    print('Hesaplanacak Ay=\033[1m \033[92mAralık\033[0m')

print(f'Çocuk Sayısı=\033[1m \033[92m{Cocuk}\033[0m')

Sgkisci = Brut * 0.14
Issizlik = Brut * 0.01
Gelirvermat = Brut - (Sgkisci + Issizlik)
Damgavergisi = Brut * 0.00759
Sgkisveren = Brut * 0.205
Issizlikisveren = Brut * 0.02


def kgvm(ay, gvm):
    kumulatifgvm = 0
    for i in range(ay):
        kumulatifgvm = kumulatifgvm + gvm
    return kumulatifgvm


Kumulatif = kgvm(Ay, Gelirvermat)

print(f'Kümülatif Vergi Matrahı=\033[1m {Kumulatif}\033[0m')
print(f'Sgk İşçi Payı=\033[1m {Sgkisci}\033[0m')
print(f'İşsizlik sigortası İşçi Payı=\033[1m {Issizlik}\033[0m')
print(f'Gelir Vergisi Matrahı=\033[1m {Gelirvermat}\033[0m')
print(f'Damga Vergisi=\033[1m {Damgavergisi}\033[0m')
print(f'İşsizlik Sigortası İşveren Payı=\033[1m {Issizlikisveren}\033[0m')
print(f'Sgk İşveren Payı=\033[1m {Sgkisveren}\033[0m')


def gelirvergisi(kumulatif, ay, gelirvermat):
    aylikgv = 0
    if kumulatif < 22000:
        gvorani = 0.15
        aylikgv = gelirvermat * gvorani
    elif 22000 < kumulatif < 46000:
        gvorani = 0.2
        if kgvm(ay - 1, gelirvermat) <= 22000:
            aylikgv = ((22000 - kgvm(ay - 1, gelirvermat)) * 0.15) + ((kumulatif - 22000) * gvorani)
        aylikgv = gelirvermat * gvorani
    elif 46000 < kumulatif < 120000:
        gvorani = 0.27
        if kgvm(Ay - 1, gelirvermat) <= 46000:
            aylikgv = ((46000 - kgvm(ay - 1, gelirvermat)) * 0.2) + ((kumulatif - 46000) * gvorani)
        aylikgv = gelirvermat * gvorani
    elif 120000 < kumulatif < 600000:
        gvorani = 0.35
        if kgvm(Ay - 1, gelirvermat) <= 120000:
            aylikgv = ((120000 - kgvm(ay - 1, gelirvermat)) * 0.27) + ((kumulatif - 120000) * gvorani)
        aylikgv = gelirvermat * gvorani
    elif 600000 < kumulatif:
        gvorani = 0.4
        if kgvm(Ay - 1, gelirvermat) < 120000:
            aylikgv = (600000 - (kgvm(ay - 1, gelirvermat)) * 0.35) + ((kumulatif - 600000) * gvorani)
        else:
            aylikgv = gelirvermat * gvorani
    return aylikgv


Aylikgelirvergisi = gelirvergisi(Kumulatif, Ay, Gelirvermat)

print(f'Aylık Gelir Vergisi=\033[1m {Aylikgelirvergisi}\033[0m')


def agi(medeni, cocuk, escalisma):
    if medeni == 0:
        agi = 220.73
    if medeni == 1:
        if escalisma == 0:
            if cocuk == 0:
                agi = 264.87
            elif cocuk == 1:
                agi = 297.98
            elif cocuk == 2:
                agi = 331.09
            elif cocuk >= 3:
                agi = 375.23
        if escalisma == 1:
            if cocuk == 0:
                agi = 220.73
            elif cocuk == 1:
                agi = 253.83
            elif cocuk == 2:
                agi = 286.94
            elif cocuk == 3:
                agi = 331.09
            elif cocuk == 4:
                agi = 353.16
            elif cocuk >= 5:
                agi = 375.23
    return agi


Agi = agi(Medeni, Cocuk, Escalisma)
Netmaas = Brut - Sgkisci - Issizlik - Aylikgelirvergisi - Damgavergisi
Toplamelegecen = Netmaas + Agi
Toplamisverenmaliyeti = Brut + Sgkisveren + Issizlikisveren

print(f'Asgari Geçim İndirimi=\033[1m {Agi}\033[0m')

print(f'Net Maaş=\033[1m {Netmaas}\033[0m')

print(f'Toplam Ele Geçen=\033[1m {Toplamelegecen}\033[0m')

print(f'İşveren Toplam Maliyeti=\033[1m {Toplamisverenmaliyeti}\033[0m')
