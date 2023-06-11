def reverseText(text):
     text.reverse()
     return text

text = input("bir kelime giriniz: ")
reversedText = reverseText(list(text))
print("".join(reversedText))