def asalSayi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

number = int(input("bir sayı giriniz: "))
if asalSayi(number):
    print(number, "bir asal sayıdır.")
else:
    print(number, "bir asal sayı değildir.")