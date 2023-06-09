A = int(input("1. kenar ölçüsünü girin: "))
B = int(input("2. kenar ölçüsünü girin: "))
C = int(input("3. kenar ölçüsünü girin: "))

if A == B or A == C or C == B:
    print("bu bir üçgen oluşturur.")
else:
    print("bu bir üçgen oluşturmaz.")

