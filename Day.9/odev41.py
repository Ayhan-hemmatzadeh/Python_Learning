# 1.liste almak
def ListeTekCiftBulma(liste):
    tek_list = []
    cift_list = []
    for number in liste:
        if number % 2 == 0:
            cift_list.append(number)
        else:
            tek_list.append(number)
    return tek_list, cift_list

numbers = input("bir liste girin (virgülle ayırınız): ").split(",")
number_list =  [int(num) for num in numbers]
print(ListeTekCiftBulma(number_list))