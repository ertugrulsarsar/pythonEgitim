# Kullanıcıdan bir cümle alınır, cümlenin her harfi büyük harfe çevrilerek tek tek ekrana basılır.

def string_manipulasyon():
    cumle = input("Bir cümle giriniz: ")
    for harf in cumle:
        print(harf.upper())

string_manipulasyon()
