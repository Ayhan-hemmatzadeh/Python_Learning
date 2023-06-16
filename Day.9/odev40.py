def enUzunKelimeyi(text):
    uzunKelime = ""
    for word in text.split():
        if len(word) > len(uzunKelime):
            uzunKelime = word
    return uzunKelime

text = input("bir yazı giriniz: ")
print(enUzunKelimeyi(text))