def maxNumber(numbers):
    return max(numbers)


text = input("sayıları virgüle ayırarak giriniz: ")
numberlist = text.split(",")
print(maxNumber(numberlist))