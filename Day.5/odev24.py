def sesliHarflerSayisi(text):
    sesliHarfler = ["a", "e", "ı", "i", "u", "ü", "o", "ö"]
    harfSayısı = 0
    for character in text:
        if character.lower() in sesliHarfler:
            harfSayısı += 1

    return harfSayısı


text = input("bir metin girin: ")
sesliHarfSayisi = sesliHarflerSayisi(text)
print(f"sesli harf sayısı: {sesliHarfSayisi}")

