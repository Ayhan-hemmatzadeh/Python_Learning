def ciftSayıları(number):
    list_cift = []
    for num in number:
        if num % 2 == 0:
            list_cift.append(num)
    return list_cift

list_number = input("bir liste giriniz (virgülle ayırınız): ").split(",")
int_list = [int(num) for num in list_number]
number = ciftSayıları(int_list)
print(number)