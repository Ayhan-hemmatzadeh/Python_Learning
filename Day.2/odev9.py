year = int(input("bir yıl giriniz: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("artık yıldır.")
else:
    print("artık yıl değil.")