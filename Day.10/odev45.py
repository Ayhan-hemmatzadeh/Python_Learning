def ortalam(list):
    total = 0
    for num in list:
        total += num
    return total / len(list)

numbers = input("bir liste girin (virgülle ayırınız): ").split(",")
number_list = [int(num) for num in numbers]
print(f"Ortalama: {ortalam(number_list)}")



