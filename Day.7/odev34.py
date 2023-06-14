def sirala_liste(liste):
    liste = sorted(liste)
    return liste



numbers = input("Bir liste girin (sayılar arasında virgül bırakarak): ").split(",")
number_list = [int(number) for number in numbers]

print(sirala_liste(number_list))
