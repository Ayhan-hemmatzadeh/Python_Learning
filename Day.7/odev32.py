def seslHarfler(text):
    list_sesli_harfler = ["a","e","ı","i","u","ü","f","ö",]
    listChar = []

    for char in text.lower():
        if char in list_sesli_harfler and char not in listChar:
            listChar.append(char)
    return listChar

text = input("bir yazı giriniz: ")
sesli_list = seslHarfler(text)
print(sesli_list)