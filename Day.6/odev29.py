def findLongWord(text):
    words = text.split()
    longText = ""

    for word in words:
        if len(word) > len(longText):
            longText = word
    return longText

text = input("bir cümle giriniz: ")
longWord =  findLongWord(text)
print(longWord)
