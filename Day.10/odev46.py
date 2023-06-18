def wordlenDic(text):
    word_dic  = {}
    for word in text.split():
        word_dic[word] = len(word)
    return word_dic

text = input("bir yazı giriniz: ")
print(wordlenDic(text))