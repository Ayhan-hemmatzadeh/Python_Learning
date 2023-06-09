text = input("bir kelime girin: ")
text_len = len(text)
list = []
while text_len > 0:
    list.append(text[text_len -1])
    text_len -= 1
print("".join(list))