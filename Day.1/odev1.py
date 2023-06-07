name = input("isminizi  girin: ")
age = int(input("yaşınızı girin: "))
height = float(input("boyunuzu girin :"))
hobby = input("hobilerinizi giriniz :")
hobby_list = []
for item in hobby.split(","):
    hobby_list.append(item)


print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Hobby: {'-'.join(hobby_list)}")