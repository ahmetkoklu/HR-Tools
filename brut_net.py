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


def kgvmhesaplama(ay, gvm):
    kumulatifgvm = 0
    for i in range(ay):
        kumulatifgvm = kumulatifgvm + gvm
    return kumulatifgvm


def gvhesaplama(kumulatif, ay, gelirvermat):
    aylikgv = 0
    if kumulatif < 22000:
        gvorani = 0.15
        aylikgv = gelirvermat * gvorani
    elif 22000 < kumulatif < 46000:
        gvorani = 0.2
        if kgvmhesaplama(ay - 1, gelirvermat) <= 22000:
            aylikgv = ((22000 - kgvmhesaplama(ay - 1, gelirvermat)) * 0.15) + ((kumulatif - 22000) * gvorani)
        aylikgv = gelirvermat * gvorani
    elif 46000 < kumulatif < 120000:
        gvorani = 0.27
        if kgvmhesaplama(Ay - 1, gelirvermat) <= 46000:
            aylikgv = ((46000 - kgvmhesaplama(ay - 1, gelirvermat)) * 0.2) + ((kumulatif - 46000) * gvorani)
        aylikgv = gelirvermat * gvorani
    elif 120000 < kumulatif < 600000:
        gvorani = 0.35
        if kgvmhesaplama(Ay - 1, gelirvermat) <= 120000:
            aylikgv = ((120000 - kgvmhesaplama(ay - 1, gelirvermat)) * 0.27) + ((kumulatif - 120000) * gvorani)
        aylikgv = gelirvermat * gvorani
    elif 600000 < kumulatif:
        gvorani = 0.4
        if kgvmhesaplama(Ay - 1, gelirvermat) < 120000:
            aylikgv = (600000 - (kgvmhesaplama(ay - 1, gelirvermat)) * 0.35) + ((kumulatif - 600000) * gvorani)
        aylikgv = gelirvermat * gvorani
    return aylikgv


def agihesaplama(medeni, cocuk, escalisma):
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


def userbrut():
    while True:
        Brut = input(color.UNDERLINE + 'Lütfen aylık brüt ücretinizi giriniz:' + color.END)
        try:
            Brut = int(Brut)
        except:
            print(color.RED + color.BOLD + 'Lütfen sayısal bir değer girin !' + color.END)
            continue
        try:
            if Brut < 2943:
                print(color.RED + color.BOLD + '2020 yılı içerisinde brüt ücret 2.943 liradan az olamaz' + color.END)
                continue
            elif 50000 > Brut > 15000:
                print(color.BLUE + color.BOLD + 'Hey Maşallah, Allah daha çok versin' + color.END)
            elif Brut > 50000:
                print(color.GREEN + color.BOLD + 'Hoşgelmişsin Ağam. Bütün marabaların yolunu bekliyirdi.' + color.END)
            break
        except:
            continue
    return Brut


def useray():
    while True:
        try:
            Ay = input(color.UNDERLINE + 'Kaçıncı ayı hesaplamak istiyorsunuz(1-12):' + color.END)
            Ay = int(Ay)
        except:
            print(color.RED + color.BOLD + 'Lütfen sayısal bir değer girin' + color.END)
            continue
        if 0 < Ay < 13:
            break
        else:
            print(color.RED + color.BOLD + 'Bir yılda 12 ay bulunur' + color.END)
            continue
    return Ay


def usermedeni():
    while True:
        Medeni = input(color.UNDERLINE + 'Evli misiniz?(E/H):' + color.END)
        if Medeni == 'E' or Medeni == 'e':
            Medeni = 1
            print('Medeni Hali=\033[1m \033[92m Evli\033[0m')
            while True:
                try:
                    Cocuk = input(color.UNDERLINE + 'Varsa çocuk sayısını belirtiniz, yoksa 0 yazınız :' + color.END)
                    Cocuk = int(Cocuk)
                except:
                    print(
                        color.RED + color.BOLD + 'Lütfen çocuk sayısını sayısal olarak girin, çocuğunuz yoksa 0 girin' + color.END)
                    continue
                if 10 > Cocuk > 5:
                    print(color.BLUE + color.BOLD + 'Hey Maşallah, Allah Bağışlasın' + color.END)
                    break
                elif Cocuk > 10:
                    print(color.GREEN + color.BOLD + 'Senin derdin bizi aşar kardeş' + color.END)
                    break
                else:
                    print(color.BLUE + color.BOLD + 'Allah bağışlasın' + color.END)
                    break
            while True:
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
                    print(
                        color.RED + color.BOLD + 'Lütfen eşiniz çalışıyorsa E çalışmıyorsa H yazın, sizin gül hatrınız için küçük harfleri de kabul ediyoruz' + color.END)
                    continue
            break
        elif Medeni == 'H' or Medeni == 'h':
            Medeni = 0
            Cocuk = 0
            Escalisma = 0
            print('Medeni Hali=\033[1m \033[92mBekar\033[0m')
            break
        else:
            print(
                color.RED + color.BOLD + 'Lütfen evliyseniz E bekarsanız H yazın, sizin gül hatrınız için küçük harfleri de kabul ediyoruz' + color.END)
            continue
    return Medeni, Cocuk, Escalisma


def sgkiscihesaplama(brut):
    Sgkisci = brut * 0.14
    return Sgkisci


def issiziscihesaplama(brut):
    issizlik = brut * 0.01
    return issizlik


def gvmathesaplama(brut, sgkisci, issizlik):
    gelirvermat = brut - (sgkisci + issizlik)
    return gelirvermat


def dvhesaplama(brut):
    damgavergisi = brut * 0.00759
    return damgavergisi


def sgkisverenhesaplama(brut):
    sgkisveren = brut * 0.155
    return sgkisveren


def issizlikisverenhesaplama(brut):
    issizlikisveren = brut * 0.02
    return issizlikisveren


def ayadiprint(ay):
    aylar = {
        1: 'Ocak',
        2: 'Şubat',
        3: 'Mart',
        4: 'Nisan',
        5: 'Mayıs',
        6: 'Haziran',
        7: 'Temmuz',
        8: 'Ağustos',
        9: 'Eylül',
        10: 'Ekim',
        11: 'Kasım',
        12: 'Aralık'
    }

    if ay in aylar:
        print(f'Hesaplanacak Ay=\033[1m \033[92m{aylar[ay]}\033[0m')
    else:
        print(f'Geçersiz ay: {ay}')


def netmaashesaplama(brut, sgkisci, issizlik, aylikgelirvergisi, damgavergisi):
    netmaas = brut - sgkisci - issizlik - aylikgelirvergisi - damgavergisi
    return netmaas


def topelgecenhesaplama(netmaas, agi):
    toplamelegecen = netmaas + agi
    return toplamelegecen


def topisvmalhesaplama(brut, sgkisveren, issizlikisveren):
    toplamisverenmaliyeti = brut + sgkisveren + issizlikisveren
    return toplamisverenmaliyeti


if __name__ == '__main__':
    Brut = userbrut()
    Ay = useray()
    Medeni, Cocuk, Escalisma = usermedeni()
    Sgkisci = sgkiscihesaplama(Brut)
    Issizlik = issiziscihesaplama(Brut)
    Gelirvermat = gvmathesaplama(Brut, Sgkisci, Issizlik)
    Damgavergisi = dvhesaplama(Brut)
    Sgkisveren = sgkisverenhesaplama(Brut)
    Issizlikisveren = issizlikisverenhesaplama(Brut)
    Kumulatif = kgvmhesaplama(Ay, Gelirvermat)
    Aylikgelirvergisi = gvhesaplama(Kumulatif, Ay, Gelirvermat)
    Agi = agihesaplama(Medeni, Cocuk, Escalisma)
    Netmaas = netmaashesaplama(Brut, Sgkisci, Issizlik, Aylikgelirvergisi, Damgavergisi)
    Toplamelegecen = topelgecenhesaplama(Netmaas, Agi)
    Toplamisverenmaliyeti = topisvmalhesaplama(Brut, Sgkisveren, Issizlikisveren)

    ayadiprint(Ay)

    print(f'Brut Maaş=\033[1m \033[92m{Brut}\033[0m')
    print(f'Çocuk Sayısı=\033[1m \033[92m{Cocuk}\033[0m')
    print(f'Kümülatif Vergi Matrahı=\033[1m {Kumulatif}\033[0m')
    print(f'Sgk İşçi Payı=\033[1m {Sgkisci}\033[0m')
    print(f'İşsizlik sigortası İşçi Payı=\033[1m {Issizlik}\033[0m')
    print(f'Gelir Vergisi Matrahı=\033[1m {Gelirvermat}\033[0m')
    print(f'Damga Vergisi=\033[1m {Damgavergisi}\033[0m')
    print(f'İşsizlik Sigortası İşveren Payı=\033[1m {Issizlikisveren}\033[0m')
    print(f'Sgk İşveren Payı=\033[1m {Sgkisveren}\033[0m')
    print(f'Aylık Gelir Vergisi=\033[1m {Aylikgelirvergisi}\033[0m')
    print(f'Asgari Geçim İndirimi=\033[1m {Agi}\033[0m')
    print(f'Net Maaş=\033[1m {Netmaas}\033[0m')
    print(f'Toplam Ele Geçen=\033[1m {Toplamelegecen}\033[0m')
    print(f'İşveren Toplam Maliyeti=\033[1m {Toplamisverenmaliyeti}\033[0m')
