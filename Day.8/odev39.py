def listeHesaplama(list, islem):
    sonuc = 0 if islem != "*" else 1
    for num in list:
        if islem == "+":
            sonuc += num
        elif islem == "*":
            sonuc *= num
    return sonuc


numbers = input("bir liste girin (virgülle ayırınız): ").split(",")
islem = input("hangi işlem (*/+): ")
number_list = [int(num) for num in numbers]
print(listeHesaplama(number_list, islem))