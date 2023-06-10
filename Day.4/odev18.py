numbers = []
total = 0
for index in range(1, 11):
    number = int(input(f"{index}.sayı giriniz:  "))
    numbers.append(number)
    total += number
print(f"En Büyük sayı {max(numbers)} ")
print(f"En küçük sayı {min(numbers)}")
print(f"Sayı ların toplamı {total}")
print(f"Sayı ların ortalaması {total/10}")