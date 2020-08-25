def inputformati(girdi):
    return f'\033[1m \033[94m{girdi}\033[0m'


def uyariformati(uyari):
    return f'\033[91m \033[1m{uyari}\033[0m'


def soruformati(soru):
    return f'\033[4m {soru}\033[0m'


def sakaformati(saka):
    return f'\033[96m \033[1m{saka}\033[0m'


def nadirsakaformati(nadirsaka):
    return f'\033[36m \033[1m{nadirsaka}\033[0m'


def sonucformati(sonuc):
    return f'\033[1m{sonuc}\033[0m'


def kgvmhesaplama(ay, gvm):
    kumulatifgvm = 0
    for i in range(ay):
        kumulatifgvm = kumulatifgvm + gvm
    return kumulatifgvm

def oncekiayhesaplama(ay,gvm):
    oncekiay = kgvmhesaplama(ay-1,gvm)
    return oncekiay

def gvhesaplama(kumulatif, oncekiay, gelirvermat):
    aylikgv = 0
    if kumulatif < 22000:
        gvorani = 0.15
        aylikgv = gelirvermat * gvorani
    elif 22000 < kumulatif < 46000:
        gvorani = 0.2
        if oncekiay <= 22000:
            aylikgv = ((22000 - oncekiay) * 0.15) + ((kumulatif - 22000) * gvorani)
        else:
            aylikgv = gelirvermat * gvorani
    elif 46000 < kumulatif < 120000:
        gvorani = 0.27
        if oncekiay <= 46000:
            aylikgv = ((46000 - oncekiay) * 0.2) + ((kumulatif - 46000) * gvorani)
        else:
            aylikgv = gelirvermat * gvorani
    elif 120000 < kumulatif < 600000:
        gvorani = 0.35
        if oncekiay <= 120000:
            aylikgv = ((120000 - oncekiay) * 0.27) + ((kumulatif - 120000) * gvorani)
        else:
            aylikgv = gelirvermat * gvorani
    elif 600000 < kumulatif:
        gvorani = 0.4
        if oncekiay < 600000:
            aylikgv = ((600000 - oncekiay) * 0.35) + ((kumulatif - 600000) * gvorani)
        else:
            aylikgv = gelirvermat * gvorani
    return aylikgv


def agihesaplama(medeni, cocuk, escalisma):
    agi=0
    if medeni == 0:
        if cocuk == 0:
            agi = 220.73
        if cocuk == 1:
            agi = 253.83
        if cocuk == 2:
            agi = 286.94
        if cocuk == 3:
            agi = 331.09
        if cocuk == 4:
            agi = 353.16
        if cocuk == 5:
            agi = 375.23
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
        Brut = input(f'{soruformati("Lütfen aylık brüt ücretinizi giriniz:")}')
        try:
            Brut = int(Brut)
        except:
            print(f'{uyariformati("Lütfen sayısal bir değer girin !")}')
            continue
        try:
            if Brut < 2943:
                print(f'{uyariformati("2020 yılı içerisinde brüt ücret 2.943 liradan az olamaz")}')
                continue
            elif 50000 > Brut > 15000:
                print(f'{sakaformati("Hey Maşallah, Allah daha çok versin")}')
            elif Brut > 50000:
                print(f'{nadirsakaformati("Hoşgelmişsin Ağam. Bütün marabaların yolunu bekliyirdi.")}')
            break
        except:
            continue
    return Brut


def useray():
    ay=0
    while True:
        try:
            ay = input(f'{soruformati("Kaçıncı ayı hesaplamak istiyorsunuz(1-12):")}')
            ay = int(ay)
        except:
            print(f'{uyariformati("Lütfen sayısal bir değer girin")}')
            continue
        if 0 < ay < 13:
            break
        else:
            print(f'{uyariformati("Bir yılda 12 ay bulunur")}')
            continue
    return ay

def usercocuk():
    cocuk=0
    while True:
        try:
            cocuk = input(f'{soruformati("Varsa çocuk sayısını belirtiniz, yoksa 0 yazınız :")}')
            cocuk = int(cocuk)
        except:
            print(f'{uyariformati("Lütfen çocuk sayısını sayısal olarak girin, çocuğunuz yoksa 0 girin")}')
            continue
        if 10 > cocuk > 5:
            print(f'{sakaformati("Hey Maşallah, Allah Bağışlasın")}')
            break
        elif cocuk > 10:
            print(f'{nadirsakaformati("Senin derdin bizi aşar kardeş")}')
            break
        else:
            print(f'{sakaformati("Allah bağışlasın")}')
            break
    return cocuk

def userescalisma():
    while True:
        escalisma = input(f'{soruformati("Eşiniz çalışıyor mu?(E/H):")}')
        if escalisma == 'E' or escalisma == 'e':
            escalisma = 1
            print(f'Eşin Çalışma Durumu={inputformati("Çalışıyor")}')
            break
        elif escalisma == 'H' or escalisma == 'h':
            escalisma = 0
            print(f'Eşin Çalışma Durumu={inputformati("Çalışmıyor")}')
            break
        else:
            print(
                f'{uyariformati("Lütfen eşiniz çalışıyorsa E çalışmıyorsa H yazın, sizin gül hatrınız için küçük harfleri de kabul ediyoruz")}')
            continue
    return escalisma



def usermedeni():
    cocuk = 0
    escalisma = 0
    while True:
        medeni = input(f'{soruformati("Evli misiniz?(E/H):")}')
        if medeni == 'E' or medeni == 'e':
            medeni = 1
            print(f'Medeni Hali= {inputformati("Evli")}')
            cocuk = usercocuk()
            escalisma = userescalisma()
            break
        elif medeni == 'H' or medeni == 'h':
            medeni = 0
            escalisma = 0
            print(f'Medeni Hali={inputformati("Bekar")}')
            cocuk = usercocuk()
            break
        else:
            print(
                f'{uyariformati("Lütfen evliyseniz E bekarsanız H yazın, sizin gül hatrınız için küçük harfleri de kabul ediyoruz")}')
            continue
    return medeni, cocuk, escalisma


def sgkiscihesaplama(brut):
    sgkisci = brut * 0.14
    return sgkisci


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


def ayismi(ay):
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
        return aylar[ay]
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
    Ayismi = ayismi(Ay)
    Medeni, Cocuk, Escalisma = usermedeni()
    Sgkisci = sgkiscihesaplama(Brut)
    Issizlik = issiziscihesaplama(Brut)
    Gelirvermat = gvmathesaplama(Brut, Sgkisci, Issizlik)
    Oncekiaykgvm = oncekiayhesaplama(Ay, Gelirvermat)
    Damgavergisi = dvhesaplama(Brut)
    Sgkisveren = sgkisverenhesaplama(Brut)
    Issizlikisveren = issizlikisverenhesaplama(Brut)
    Kumulatif = kgvmhesaplama(Ay, Gelirvermat)
    Aylikgelirvergisi = gvhesaplama(Kumulatif, Oncekiaykgvm, Gelirvermat)
    Agi = agihesaplama(Medeni, Cocuk, Escalisma)
    Netmaas = netmaashesaplama(Brut, Sgkisci, Issizlik, Aylikgelirvergisi, Damgavergisi)
    Toplamelegecen = topelgecenhesaplama(Netmaas, Agi)
    Toplamisverenmaliyeti = topisvmalhesaplama(Brut, Sgkisveren, Issizlikisveren)

    print(f'Hesaplanacak Ay= {inputformati(Ayismi)}')
    print(f'Brut Maaş= {inputformati(Brut)}')
    print(f'Çocuk Sayısı= {inputformati(Cocuk)}')
    print(f'Kümülatif Vergi Matrahı= {sonucformati(Kumulatif)}')
    print(f'Sgk İşçi Payı= {sonucformati(Sgkisci)}')
    print(f'İşsizlik sigortası İşçi Payı= {sonucformati(Issizlik)}')
    print(f'Gelir Vergisi Matrahı= {sonucformati(Gelirvermat)}')
    print(f'Damga Vergisi= {sonucformati(Damgavergisi)}')
    print(f'İşsizlik Sigortası İşveren Payı= {sonucformati(Issizlikisveren)}')
    print(f'Sgk İşveren Payı= {sonucformati(Sgkisveren)}')
    print(f'Aylık Gelir Vergisi= {sonucformati(Aylikgelirvergisi)}')
    print(f'Asgari Geçim İndirimi= {sonucformati(Agi)}')
    print(f'Net Maaş= {sonucformati(Netmaas)}')
    print(f'Toplam Ele Geçen= {sonucformati(Toplamelegecen)}')
    print(f'İşveren Toplam Maliyeti= {sonucformati(Toplamisverenmaliyeti)}')


