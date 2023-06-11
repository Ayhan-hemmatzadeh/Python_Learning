def teksayılarFunc(numbers):
    numbers_list = []
    for num in numbers:
        if num % 2 != 0:
            numbers_list.append(num)
    return numbers_list

numbers = input("Bir liste girin (sayılar arasında virgül bırakarak): ")
numberlist = [int(number) for number in  numbers.split(",")]

tek_sayilar = teksayılarFunc(numberlist)
print(tek_sayilar)
