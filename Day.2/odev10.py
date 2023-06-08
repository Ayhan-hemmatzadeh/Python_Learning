char = input("bir harf giriniz: ")
sesli_harf = ["a","e","ı","i","u","ü","o","ö"]
if char.lower() in  sesli_harf:
    print("Sesli harf.")
else:
    print("sesli harf değil.")