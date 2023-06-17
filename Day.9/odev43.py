def armstrong(number):
    num_text= str(number)
    numLen = len(num_text)
    total = 0

    for num in num_text:
       total += (int(num) ** numLen)

    if number == total:
        return True
    else:
        return False

number = int(input("Bir sayı giriniz: "))

if armstrong(number):
    print("Armstrong sayıdır.")
else:
    print("Armstrongsayı değildir.")