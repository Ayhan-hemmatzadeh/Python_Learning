def kelimeTersCeviren(wordlist):
    wordlist.reverse()
    return wordlist

text = input("bir yazı giriniz: ")
print(kelimeTersCeviren(text.split()))
