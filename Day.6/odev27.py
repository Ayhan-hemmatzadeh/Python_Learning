def listNumber(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = input("Bir liste girin (sayılar arasında virgül bırakarak): ").split(",")
numList = [int(num) for num in numbers ]
total = listNumber(numList)
print(total)

