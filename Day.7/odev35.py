def list_total(list):
    sum = 0
    for num in list:
        sum += num
    return sum

numbers = input("bir liste girin (virgülle ayırınız): ").split(",")
number_list =  [int(num) for num in numbers]
print(list_total(number_list))