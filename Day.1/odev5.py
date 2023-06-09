liststring = input("bir liste girin: ")
liste = []
for i in liststring.split(","):
    liste.append(int(i))
max = max(liste)
min = min(liste)
print(f"Max Number: {max}" )
print(f"min Number: {min}" )
print("toplam: ", max + min)
