number =  int(input("bir sayı girin: "))
faktoriyel = 1
for num in range(1, number +1):
    faktoriyel *= num
print(f"{number}! => {faktoriyel}")