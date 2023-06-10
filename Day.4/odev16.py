numbers = []
for index in range(1, 6):
    number = int(input(f"{index}.sayı giriniz:  "))
    numbers.append(number)
print(f"En Büyük sayı {max(numbers)} ve En küçük sayı {min(numbers)}")