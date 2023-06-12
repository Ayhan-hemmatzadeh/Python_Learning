def harfSayıHesaplama(text):
    harfSayilari = {}
    for harf in text:
        harf = harf.lower()
        if harf in harfSayilari:
            harfSayilari[harf] += 1
        else:
            harfSayilari[harf] = 1

    return harfSayilari


text = input("bir metin giriniz: ")
print(harfSayıHesaplama(text))