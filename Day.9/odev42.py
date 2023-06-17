def isPalindrom(text):
    treverse= text[::-1]

    if treverse.lower() == text.lower():
        return True
    else:
        return False


text = input("bir yazı giriniz: ")
result =  isPalindrom(text)
if  result :
    print("palindromdır")
else:
    print("palondrom değildir.")