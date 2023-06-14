def enSikHarflar(text):
    harfler_dic = {}
    for char in text.lower():
        if char in harfler_dic:
            harfler_dic[char] += 1
        else:
            harfler_dic[char] = 1

    harf_listesi = []
    for harf,harfSayi in harfler_dic.items():
        if harfSayi > 1:
            harf_listesi.append(harf)


    return harf_listesi



text = input("bir yazı giriniz: ")
print(enSikHarflar(text))
