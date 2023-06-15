def basHarfiBuyutenFonksiyon(text):
    text_list = []
    for word in text.split():
        text_list.append(word.capitalize())
    return " ".join(text_list)





text_list = input("bir yazı giriniz: ")
print(basHarfiBuyutenFonksiyon(text_list))
