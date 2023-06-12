def worldCount(text):
    return text.split()
text = input("bir cümle giriniz: ")
words = worldCount(text)
print(len(words))