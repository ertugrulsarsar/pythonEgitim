# 1 ile 100 arasında rastgele bir sayı tutulur. Kullanıcı, doğru sayıyı bulana kadar tahmin eder.

import random

def tahmin_oyunu():
    hedef_sayi = random.randint(1, 100)
    tahmin = -1
    deneme_sayisi = 0
    
    print("1 ile 100 arasında bir sayı tahmin edin.")
    while tahmin != hedef_sayi:
        tahmin = int(input("Tahmininiz: "))
        deneme_sayisi += 1
        
        if tahmin < hedef_sayi:
            print("Daha yüksek bir sayı deneyin.")
        elif tahmin > hedef_sayi:
            print("Daha düşük bir sayı deneyin.")
        else:
            print(f"Tebrikler! {deneme_sayisi} denemede doğru tahmin ettiniz.")

tahmin_oyunu()
