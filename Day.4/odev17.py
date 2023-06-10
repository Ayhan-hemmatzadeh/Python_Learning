text = input("bir metin girin: ")
list_text = []
for character in text:
    list_text.append(character.upper())
print("".join(list_text))
