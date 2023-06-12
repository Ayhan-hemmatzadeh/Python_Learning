def Faktoriyel(number):
    result = 1
    for num in range(1, number +1):
        result *= num
    return result

number = int(input("bir sayı giriniz: "))
print(Faktoriyel(number))